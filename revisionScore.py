from datetime import datetime
import math

topics = ["System architecture", "Memory and Storage", ""]
numberOfTopics = len(topics)
revisionScore = 0

for topic in topics:
    revised = input("Did you complete your revision about " + topic + "? (Yes or No) \n > ")
    if revised.lower() == "yes":
        revisionScore += 1

percentage = str(math.floor((revisionScore / numberOfTopics) * 100))



print("Your Revision Score: " + percentage + "%")

f = open("RevisionScore.txt", "at")


currentDate = datetime.today().strftime("%d.%m.%Y")
f.write(currentDate + ": " + percentage + "\n")