import re
f = open("CsClassesPage1.html", "r")
classList=f.read()
f.close()
from bs4 import BeautifulSoup
soup = BeautifulSoup(classList, 'html.parser')
#print(soup.prettify())
classes=soup.find_all(class_="row-fluid data_row primary-row class-info class-not-checked")
classDict = {}
for i in classes:
    #print(i.get("id"))
    #print(i.contents)
    #print(i)
    classId = i.get("id")
    classDict[classId]={}
    timeCol = i.find_all(class_="timeColumn")
    for j in timeCol:
        cid = j.find("div").get("id").split("-")[0]
        day = j.find_all("p")[0].string
        timeList = j.find_all("p")[1].contents
        try:
            time = str(timeList[0]) + str(timeList[2])
        except:
            classDict[classId]["lecTime"] = None
            classDict[classId]["lecDate"] = None
            continue
        if len(cid.split("_")) == 2:
            classDict[classId]["lecTime"] = time
            classDict[classId]["lecDate"] = day
        else:
            classDict[classId][cid] = {}
            classDict[classId][cid]["time"] = time
            classDict[classId][cid]["day"] = day
    className = i.find_all("label")
    for j in className:
        longId = j.get("for").split("-")[0]
        longIdList = longId.split("_")
        print(longIdList)
        className = j.string
        print(className)
        if len(longIdList) == 2:
            classDict[longId]["lecName"] = className
        else:
            classDict[longIdList[1]+"_"+longIdList[2]][longId]["name"] = className
        #classDict[]
    #for j in i.contents:
    #x    print(j.contents)
    #for j in i.contents[1].find_all(class_="timeColumn"):
    #    print(j)
    #for j in i.contents:
    #    print(j)

print(classDict)