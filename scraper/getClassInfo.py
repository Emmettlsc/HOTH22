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
output["required_classes"] = []
output["class_prerequisites"] = []
classDict = {}
howmany = 0
weekdays = {"M":"Monday", "T":"Tuesday", "W": "Wednesday", "R": "Thursday", "F":"Friday"}

descriptionsFile = open("CsCourseDescriptions.html")
descriptionsHtml = descriptionsFile.read()
descriptionsFile.close()
descriptionSoup = BeautifulSoup(descriptionsHtml, "html.parser")
#print(descriptionSoup.prettify())
descriptionTags = descriptionSoup.find_all(class_="course-record")
for i in descriptionTags:
    #print(i)
    title = i.find("h3").string.split(". ")
    print(title[0])
    output["all_classes"].append("COM SCI " + title[0])
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
    if "COM SCI 59" in readableId or "COM SCI 375" in readableId or "COM SCI 298" in readableId:
        continue
    #print(readableId)
    if(readableId not in classDict.keys()):
        classDict[readableId]={}
    classDict[readableId][classId] = {}
    classDict[readableId][classId]["discussion_timing"] = {}
    timeCol = i.find_all(class_="timeColumn")
    for j in timeCol:
        cid = j.find("div").get("id").split("-")[0]
        day = j.find_all("p")[0].string
        timeList = j.find_all("p")[1].contents
        if len(cid.split("_")) == 2:
            classDict[readableId][classId]["lecture_timing"] = []
            for dayLetter in day:
                try:
                    classDict[readableId][classId]["lecture_timing"].append([weekdays[dayLetter], str(timeList[0]), str(timeList[2][1:])])
                except:
                    classDict[readableId][classId]["lecture_timing"].append([day, "N/A", "N/A"])
                    continue
        else:
            classDict[readableId][classId]["discussion_timing"][cid] = []
            for dayLetter in day:
                classDict[readableId][classId]["discussion_timing"][cid].append([weekdays[dayLetter], str(timeList[0]), str(timeList[2][1:])])
    className = i.find_all("label")
    for j in className:
        longId = j.get("for").split("-")[0]
        longIdList = longId.split("_")
        #print(longIdList)
        className = j.string
        #print(className)
        if len(longIdList) == 2:
            classDict[readableId][longId]["lecName"] = className
        #else:
        #    classDict[readableId][longIdList[1]+"_"+longIdList[2]][longId]["name"] = className
    instructorCol = i.find_all(class_="instructorColumn hide-small")
    classDict[readableId]["instructor"] = []
    classDict[readableId]["units"] = []
    for j in instructorCol:
        if not classDict[readableId]["instructor"]:
            classDict[readableId]["instructor"] = j.string
    unitCol = i.find_all(class_="unitsColumn")
    for j in unitCol:
        if not classDict[readableId]["units"]:
            classDict[readableId]["units"] = j.string
    howmany = howmany + 1


output["class_info"] = classDict
f=open("output", "w")
f.write(str(output))
f.close()
print(output)