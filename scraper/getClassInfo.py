import re
f = open("CsClassesPage1.html", "r")
classList=f.read()
f.close()
from bs4 import BeautifulSoup
scheduleSoup = BeautifulSoup(classList, 'html.parser')
#print(soup.prettify())
classes=scheduleSoup.find_all(class_="row-fluid data_row primary-row class-info class-not-checked")
#Set up output
output = {}
output["all_classes"] = []
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
        classDict[readableId]["lecture_info"] = {}
    classDict[readableId]["lecture_info"][classId] = {}
    classDict[readableId]["lecture_info"][classId] = {}
    classDict[readableId]["lecture_info"][classId]["discussion_timing"] = {}
    timeCol = i.find_all(class_="timeColumn")
    for j in timeCol:
        cid = j.find("div").get("id").split("-")[0]
        day = j.find_all("p")[0].string
        timeList = j.find_all("p")[1].contents
        if len(cid.split("_")) == 2:
            classDict[readableId]["lecture_info"][classId]["lecture_timing"] = []
            for dayLetter in day:
                try:
                    classDict[readableId]["lecture_info"][classId]["lecture_timing"].append([weekdays[dayLetter], str(timeList[0]), str(timeList[2][1:])])
                except:
                    bad_classes.append(readableId)
                    classDict[readableId] = None
                    break
        else:
            classDict[readableId]["lecture_info"][classId]["discussion_timing"][cid] = []
            for dayLetter in day:
                classDict[readableId]["lecture_info"][classId]["discussion_timing"][cid].append([weekdays[dayLetter], str(timeList[0]), str(timeList[2][1:])])
    className = i.find_all("label")
    if readableId in bad_classes:
        continue
    for j in className:
        longId = j.get("for").split("-")[0]
        longIdList = longId.split("_")
        #print(longIdList)
        className = j.string
        #print(className)
        if len(longIdList) == 2:
            classDict[readableId]["lecture_info"][longId]["lecture_names"] = className.replace("Select ", "")
        #else:
        #    classDict[readableId][longIdList[1]+"_"+longIdList[2]][longId]["name"] = className
    instructorCol = i.find_all(class_="instructorColumn hide-small")
    #print(instructorCol)
    classDict[readableId]["lecture_info"]["instructor"] = []
    classDict[readableId]["units"] = []
    for j in instructorCol:
        if not classDict[readableId]["lecture_info"]["instructor"]:
            classDict[readableId]["lecture_info"]["instructor"] = j.string #TODO: Fix multiple instructor classes
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
f=open("output", "w")
f.write(str(output))
f.close()
print(output)