import json
import itertools
import more_itertools
import os
import sys
import argparse
from datetime import datetime

priority_rewards = {
	"LOW": 1,
	"HIGH": 2,
	"MUST": 0
}
priority_costs = {
	"LOW": -1,
	"HIGH": -2,
	"MUST": float('-inf')
}

# log info to stdout
def log(str, log_type="INFO"):
	print("[" + log_type + "]", str)

# determine required classes whose prerequisites have been taken
# precondition: prerequisite for any required class is also a required class
def gen_potential_classes(class_info, classes_taken):
	potential_classes = set()
	for class_ in class_info["required_classes"]:
		if set(class_info["class_prerequisites"][class_]).issubset(classes_taken) and class_ in class_info["class_info"].keys():
			potential_classes.add(class_)
	return potential_classes-classes_taken

def str_to_datetime(str):
	if ":" in str:
		return datetime.strptime(str, '%I:%M%p')
	else:
		return datetime.strptime(str, '%I%p')
	#return datetime.strptime(str, '%H:%M')

def add_interval(time_list, time_intervals):
	day, s_time_str, e_time_str = time_list[0], time_list[1], time_list[2]

	s_time = str_to_datetime(s_time_str)
	e_time = str_to_datetime(e_time_str)

	time_intervals[day].append([s_time, e_time])

def overlap(time_intervals):
	if len(time_intervals) <= 1:
		return False
	elif len(time_intervals) == 2:
		[[s1, e1], [s2, e2]] = time_intervals
		not_overlapping = e1 <= s2 or e2 <= s1
		#overlapping = e1 > s2 and e2 > s1
		return not not_overlapping
	else:
		if overlap(time_intervals[1:]):
			return True
		else:
			for each_time_interval in time_intervals[1:]:
				if (overlap([time_intervals[0], each_time_interval])):
					return True
			return False

def combination_contains_overlap(class_info, combination):
	time_intervals = {"Monday":[], "Tuesday":[], "Wednesday":[], "Thursday":[], "Friday":[]}
	for [class_, lecture_section, discussion_section] in combination:
		for lecture_time_list in class_info["class_info"][class_]["lecture_sections"][lecture_section]["lecture_timing"]:
			add_interval(lecture_time_list, time_intervals)
		for discussion_time_list in class_info["class_info"][class_]["lecture_sections"][lecture_section]["discussion_sections"][discussion_section]["discussion_timing"]:
			add_interval(discussion_time_list, time_intervals)

	for day_time_intervals in time_intervals.values():
		if overlap(day_time_intervals):
			return True

	return False

def units_in_combination(class_info, combination):
	units = 0
	for [class_, lecture_section, discussion_section] in combination:
		units += class_info["class_info"][class_]["units"]

	return units

def time_condition(class_info, combination, time_condition_args):
	#log("time_condition called")
	time_condition_args_words = time_condition_args.split(" ")
	day, s_time_str, e_time_str = time_condition_args_words[0], time_condition_args_words[1], time_condition_args_words[2]
	
	s_time = str_to_datetime(s_time_str)
	e_time = str_to_datetime(e_time_str)

	time_intervals = {"Monday":[], "Tuesday":[], "Wednesday":[], "Thursday":[], "Friday":[]}
	for [class_, lecture_section, discussion_section] in combination:
		for lecture_time_list in class_info["class_info"][class_]["lecture_sections"][lecture_section]["lecture_timing"]:
			add_interval(lecture_time_list, time_intervals)
		for discussion_time_list in class_info["class_info"][class_]["lecture_sections"][lecture_section]["discussion_sections"][discussion_section]["discussion_timing"]:
			add_interval(discussion_time_list, time_intervals)
	day_time_intervals = time_intervals[day.lower().capitalize()]

	for day_time_interval in day_time_intervals:
		if overlap([(s_time, e_time), day_time_interval]):
			return True
	
	return False

def instructor_condition(class_info, combination, instructor_condition_args):
	#log("instructor_condition called")
	return False

def class_combo_condition(class_info, combination, class_combo_condition_args):
	#log("class_combo_condition called")
	classes = [elem[0] for elem in combination]
	class_combo = class_combo_condition_args.split("(")[1].split(")")[0].split(", ")
	is_class_combo = set(class_combo).issubset(set(classes))
	#log(str(is_class_combo) + " " + str(class_combo) + " is " + ("" if is_class_combo else "not ") + "subset of " + str(classes))
	return is_class_combo

def rating_condition(class_info, combination, rating_condition_args):
	#log("rating_condition called")

	return False

def total_units_condition(class_info, combination, total_units_condition_args):
	#log("total_units_condition called")
	total_condition_args_words = total_units_condition_args.split(" ")
	total_units = units_in_combination(class_info, combination)

	comparator = total_condition_args_words[0]
	rhs = int(total_condition_args_words[1])
	if comparator == "LESS_THAN":
		return total_units < rhs
	if comparator == "MORE_THAN":
		return total_units > rhs
	else: #unexpected; we failed to prove condition true
		return -1

# True/False -> condition determined to be True/False, -1 -> condition indeterminate
filter_condition_handler = {
	"TIME": time_condition,
	"INSTRUCTOR": instructor_condition,
	"CLASS_COMBO": class_combo_condition,
	"RATING": rating_condition,
	"TOTAL_UNITS": total_units_condition,
}

def check_filter_condition(class_info, filter_condition, combination):
	filter_condition_words = filter_condition.split(" ")
	condition_type = filter_condition_words[0]
	condition_args = " ".join(filter_condition_words[1:])
	return filter_condition_handler[condition_type](class_info, combination, condition_args)

def score_filter(class_info, filter, combination):
	filter_score = 0
	filter_words = filter.split(" ")
	priority = filter_words[0]
	action = filter_words[1]
	filter_condition = " ".join(filter_words[2:])
	filter_condition_eval = check_filter_condition(class_info, filter_condition, combination)
	
	if (filter_condition_eval==-1):
		return 0
	if (filter_condition_eval==True and action=="PREFER") or (filter_condition_eval==False and action=="AVOID"):
		return priority_rewards[priority]
	else:
		return priority_costs[priority]

# assign a score to each class combination based on filters in query
def score_combination(class_info, query, combination):
	score = 0
	filter_scores = []
	for filter_ in query["filters"]:
		filter_score = score_filter(class_info, filter_, combination)
		if filter_score == float('-inf'):
			return float('-inf'), None
		else:
			score += filter_score
			filter_scores.append(filter_score)

	return score, filter_scores

# determine all possible non-overlapping schedule configurations of potential_classes
# then remove configurations with -inf score, sort remaining in ascending order and return
def gen_sorted_configurations(class_info, query, potential_classes):
	all_class_sections = []
	for class_ in potential_classes:
		class_sections = []
		for lecture_section in class_info["class_info"][class_]["lecture_sections"].keys():
			for discussion_section in class_info["class_info"][class_]["lecture_sections"][lecture_section]["discussion_sections"].keys():
				class_sections.append([class_, lecture_section, discussion_section])
		all_class_sections.append(class_sections)


	combinations_with_overlap = []
	for all_class_sections_subset in more_itertools.powerset(all_class_sections):
		combinations_with_overlap += list([list(elem) for elem in itertools.product(*all_class_sections_subset)])
	combinations_without_overlap = list(filter((lambda combination : not combination_contains_overlap(class_info, combination)), combinations_with_overlap))
	
	scored_configurations = []
	for combination in combinations_without_overlap:
		score, filter_scores = score_combination(class_info, query, combination)
		if score == float('-inf'):
			continue
		total_units = units_in_combination(class_info, combination)

		configuration = {
			"filter_scores": filter_scores,
			"classes": combination,
			"total_units": total_units
		}
		scored_configurations.append([score, configuration])

	scored_configurations.sort(key=lambda x : x[0])
	configurations_list = [scored_configuration[1] for scored_configuration in scored_configurations]
	configurations = {}
	for i in range(len(configurations_list)):
		configurations["config" + str(i+1)] = configurations_list[i]

	return configurations

def main(args):
	#Ensure class info and query files exist
	assert os.path.exists(args.class_info_file), "specified class_info_file invalid"
	assert os.path.exists(args.query_file), "specified query_file invalid"

	with open(args.class_info_file, "r") as f:
		class_info = json.load(f)
	with open(args.query_file, "r") as f:
		query = json.load(f)

	potential_classes = gen_potential_classes(class_info, set(query["classes_taken"]))
	sorted_configurations = gen_sorted_configurations(class_info, query, potential_classes)
	
	query_response = {}
	query_response["query_id"] = query["query_id"]
	query_response["sorted_configurations"] = sorted_configurations

	#Write to args.output_file
	with open(args.output_file, "w") as f:
		f.write(json.dumps(query_response, indent=4))
	print(json.dumps(query_response, indent=4))
	log("Finished")

# parse user supplied arguments
def parse_arguments(argv):
	parser = argparse.ArgumentParser()
	parser.add_argument("--class_info_file", type=str, help="class info json file", default="./class_info.json")
	parser.add_argument("--query_file", type=str, help="class info json file", default="./sample_query.json")
	parser.add_argument("--output_file", type=str, help="class info json file", default="./query_response.json")
	return parser.parse_args(argv)

if __name__ == '__main__':
	main(parse_arguments(sys.argv[1:]))