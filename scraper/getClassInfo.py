import re
import json
f = open("CsClassesPage1.html", "r")
classList=f.read()
f.close()
from bs4 import BeautifulSoup
import requests

scheduleSoup = BeautifulSoup(classList, 'html.parser')
#print(soup.prettify())
classes=scheduleSoup.find_all(class_="row-fluid data_row primary-row class-info class-not-checked")
#Set up output
output = {}
output["all_classes"] = []
output["all_profs"] = []
output["required_classes"] = ["COM SCI 1", "COM SCI 31", "COM SCI 32", "COM SCI 35L", "COM SCI M51A", "COM SCI 111", "COM SCI 118", 
    "COM SCI 131", "COM SCI M151B", "COM SCI M152A", "COM SCI 180", "COM SCI 181", "COM SCI 130"]
output["class_prerequisites"] = {}
classDict = {}
howmany = 0
weekdays = {"M":"Monday", "T":"Tuesday", "W": "Wednesday", "R": "Thursday", "F":"Friday"}
dept_codes = {"Mathematics": "MATH", "Computer Engineering": "ECE", "Computing": "COMPTNG", 
                "Environmental Engineering": "C&EE", "Statistics":"STATS", "Life Sciences": "LIFESCI",
                "COM SCI":"COM SCI"}

descriptionsFile = open("CsCourseDescriptions.html")
descriptionsHtml = descriptionsFile.read()
descriptionsFile.close()
descriptionSoup = BeautifulSoup(descriptionsHtml, "html.parser")
#print(descriptionSoup.prettify())

bad_classes = []
    
#Get info from schedule of classes
for i in classes:
    #print(i.get("id"))
    #print(i.contents)
    #print(i)
    classId = i.get("id")
    idNumber = classId.split("COMSCI")[1].lstrip("0")
    readableId = ""
    if "CC" in idNumber:
        readableId = readableId + "C"
        idNumber = idNumber.replace("CC","C")
    elif "CM" in idNumber:
        readableId = readableId + "CM"
        idNumber = idNumber.replace("CM","")
    elif "M" in idNumber:
        readableId = readableId + "M"
        idNumber = idNumber.replace("M","")
    readableId = "COM SCI " + readableId + idNumber
    if "COM SCI 59" in readableId or "COM SCI 375" in readableId or "COM SCI 298" in readableId or readableId in bad_classes:
        continue

    #print(readableId)
    if(readableId not in classDict.keys()):
        classDict[readableId]={}
        classDict[readableId]["lecture_sections"] = {}
    classDict[readableId]["lecture_sections"][classId] = {}
    classDict[readableId]["lecture_sections"][classId] = {}
    classDict[readableId]["lecture_sections"][classId]["discussion_sections"] = {}
    timeCol = i.find_all(class_="timeColumn")
    for j in timeCol:
        cid = j.find("div").get("id").split("-")[0]
        if(len(cid.split("_")) > 2):
            classDict[readableId]["lecture_sections"][classId]["discussion_sections"][cid] = {}
        #print(classDict[readableId]["lecture_sections"][classId]["discussion_sections"])
        day = j.find_all("p")[0].string
        timeList = j.find_all("p")[1].contents
        if len(cid.split("_")) == 2:
            classDict[readableId]["lecture_sections"][classId]["lecture_timing"] = []
            for dayLetter in day:
                try:
                    classDict[readableId]["lecture_sections"][classId]["lecture_timing"].append([weekdays[dayLetter], str(timeList[0]), str(timeList[2][1:])])
                except:
                    classDict[readableId]["lecture_sections"][classId]["lecture_timing"].append(["Monday", "10am", "11:50am"])
                    break
        else:
            for dayLetter in day:
                classDict[readableId]["lecture_sections"][classId]["discussion_sections"][cid]["discussion_timing"] = [weekdays[dayLetter], str(timeList[0]), str(timeList[2][1:])]
    className = i.find_all("label")
    if readableId in bad_classes:
        continue
    for j in className:
        longId = j.get("for").split("-")[0]
        longIdList = longId.split("_")
        #print(longIdList)
        className = j.string
        #print(className)
        className = className.replace("Select ", "")
        if len(longIdList) == 2:
            classDict[readableId]["lecture_sections"][longId]["lecture_names"] = className
        else:
            classDict[readableId]["lecture_sections"][longIdList[1]+"_"+longIdList[2]]["discussion_sections"][longId]["sectionName"] = className
    instructorCol = i.find_all(class_="instructorColumn hide-small")
    #print(instructorCol)
    classDict[readableId]["lecture_sections"][classId]["instructor"] = []
    classDict[readableId]["units"] = []
    for j in instructorCol:
        if not classDict[readableId]["lecture_sections"][classId]["instructor"]:
            classDict[readableId]["lecture_sections"][classId]["instructor"] = j.string #TODO: Fix multiple instructor classes
        if j.string not in ["TA", "none", None] + output["all_profs"]:
            output["all_profs"].append(j.string)
    unitCol = i.find_all(class_="unitsColumn")
    for j in unitCol:
        if not classDict[readableId]["units"]:
            classDict[readableId]["units"] = int(j.string.split(".")[0])
output["class_info"] = classDict


#Stuff from course description webpage
descriptionTags = descriptionSoup.find_all(class_="course-record")
for i in descriptionTags:
    #print(i)
    title = i.find("h3").string.split(". ")
    #print(title)
    textTitle = "COM SCI " + title[0]
    output["all_classes"].append(textTitle)
    output["class_prerequisites"][textTitle] = []
    description = i.find_all("p")[1].string
    if description and ("requisite" in description.lower()):
        reqBreak = description.split("equisit")
        reqString = reqBreak[1].split(".")[0]
       # print(textTitle + " " + reqString+"\n")
        currentDept = ""
        last_word = ""
        for word in reqString.split(" "):
            #print(word) #TODO: Make it work with OR statements somehow
            if word == "course" or word == "courses":
                currentDept = "COM SCI"
            #elif word in dept_codes.keys():
                #print(output["class_prerequisites"])
             #   currentDept = dept_codes[word]
            #if last_word + " " + word in dept_codes.keys():
             #   currentDept = dept_codes[last_word + " " + word]
            elif re.match("[cmCM]*[0-9]{1,3}[:alpha:]*", word) and currentDept:
                #print(word)
                output["class_prerequisites"][textTitle].append(currentDept + " " + word.replace(",",""))
            last_word = word

default_rating = {}
default_rating["Overall"] = -1.0
default_rating["Easiness"] = -1.0
default_rating["Clarity"] = -1.0
default_rating["Workload"] = -1.0
default_rating["Helpfulness"] = -1.0


rating_arr = []
for course in output["class_info"]:
	if course is None:
		continue
	temp_key = (list((output["class_info"][course]["lecture_sections"]).keys())[0])
	#print(output["class_info"][course]["lecture_info"][temp_key])
	#print(temp_key)
	instructor = output["class_info"][course]["lecture_sections"][temp_key]["instructor"]
	if instructor is None:
		instructor = "badname"
	urlcourse = course.replace(" ", "-")
	URL = "https://bruinwalk.com/classes/" + urlcourse.lower() + "/"
	page = requests.get(URL)
	soup = BeautifulSoup(page.text, 'html.parser')
	profs = soup.find_all(class_="title-container")
	overall_rating = soup.find_all(class_="overall-rating-container")
	ratings = soup.find_all(class_="rating")
	runner = 0
	prof_runner = 0;
	prof_last_name = "null"
	added = False
	for elm in overall_rating:
		rating_group = {}
		z = re.findall("(\">.*<\/a)", str(profs[prof_runner]))
		prof_name = z[0].strip("\"></a")
		prof_last_name = (re.findall("([A-Za-z-\.]*)$", prof_name))[0]
		if prof_last_name is None:
			print("NOOOOOO\n")
		#rating_group["prof"]= prof_name
		overall = (re.findall("([0-9]\.[0-9]|N\/A)", str(elm)))[0]
		if overall == "N/A":
			overall = "-1.0"
		rating_group["Overall"] = float(overall)
		easiness = (re.findall("([0-9]\.[0-9]|N\/A)", str(ratings[runner+0])))[0]
		if easiness == "N/A":
			easiness = "-1.0"
		rating_group["Easiness"] = float(easiness)
		clarity = (re.findall("([0-9]\.[0-9]|N\/A)", str(ratings[runner+1])))[0]
		if clarity == "N/A":
			clarity = "-1.0"
		rating_group["Clarity"] = float(clarity)
		workload = (re.findall("([0-9]\.[0-9]|N\/A)", str(ratings[runner+2])))[0]
		if workload == "N/A":
			workload = "-1.0"
		rating_group["Workload"] = float(workload)
		helpfulness = (re.findall("([0-9]\.[0-9]|N\/A)", str(ratings[runner+3])))[0]
		if helpfulness == "N/A":
			helpfulness = "-1.0"
		rating_group["Helpfulness"] = float(helpfulness)
		rating_arr.append(rating_group)
		added = True
		runner+=4
		prof_runner+=1
	#print(instructor)
	#print(prof_last_name)
	if prof_last_name is None:
		output["class_info"][course]["lecture_sections"][temp_key]["rating"] = default_rating
	if instructor is None:
		output["class_info"][course]["lecture_sections"][temp_key]["rating"] = default_rating
	if prof_last_name in instructor:
		if added:
			output["class_info"][course]["lecture_sections"][temp_key]["rating"] = rating_arr[-1]
		else:
			output["class_info"][course]["lecture_sections"][temp_key]["rating"] = default_rating
	added = False



f=open("output.json", "w")
f.write(json.dumps(output, indent=4))
f.close()
print(json.dumps(output, indent=4))


