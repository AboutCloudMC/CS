import json

with open("questions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

points = dict(Gryffindor=0, Hufflepuff=0, Ravenclaw=0, Slytherin=0)

for question in data["questions"]:
    answer = input(question["question"] + "\n > ")
    if answer.lower() == "yes":
        for point in question["fittingHouse"]:
            points[point] += 1

highest = ""
if points["Gryffindor"] > points["Hufflepuff"]:
    highest = "Gryffindor"
else:
    highest = "Hufflepuff"
if points[highest] < points["Ravenclaw"]:
    highest = "Ravenclaw"
if points[highest] < points["Slytherin"]:
    highest = "Slytherin"

print("\n You belong to " + highest + "! \n")