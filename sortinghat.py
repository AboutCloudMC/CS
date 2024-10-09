import json

with open("questions.json", "r", encoding="utf-8") as f:
    data = json.load(f)

points = dict(G=0, H=0, R=0, S=0)

for question in data["questions"]:
    print(question)
    answer = input(question["question"] + "\n > ")
    if answer.lower() == "yes":
        for point in question["fittingHouse"]:
            print(point)
            points[point] += 1