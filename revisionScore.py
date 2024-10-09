from datetime import datetime
import math

topics = ["System architecture", "Memory and Storage", "Programming Fundementals"]
topicsTodo = []
numberOfTopics = len(topics)
revisionScore = 0

for topic in topics:
    revised = input("Did you complete your revision about " + topic + "? (Yes or No) \n > ")
    if revised.lower() == "yes":
        revisionScore += 1
    else:
        topicsTodo.append(topic)

percentage = str(math.floor((revisionScore / numberOfTopics) * 100))

print("Your Revision Score: " + percentage + "%")

f = open("RevisionScore.txt", "at")
currentDate = datetime.today().strftime("%d.%m.%Y %H:%M")

topicsTodoStr = ""
if percentage != "100":
    topicsTodoStr = "(Please revise "
    for topic in topicsTodo:
        if topicsTodo[0] == topic:
            topicsTodoStr += topic
        elif topicsTodo[len(topicsTodo)-1] != topic:
            topicsTodoStr += (", " + topic)
        else:
            topicsTodoStr += (" and " + topic)
    topicsTodoStr += ")"
f.write(currentDate + ": " + percentage + "% " + topicsTodoStr + "\n")