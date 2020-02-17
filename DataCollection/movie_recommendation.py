dataset = {
    "action" : ["matrix","batman","superman","dabang","avengers","thor","hulk",
                "krrish","ironman","uri"],
    "comedy" : ["the mask","dhamaal","bala","housefull","golmaal","hera pheri",
                "golmaal 2","dhamaal 2","hera pheri 2","bhootnath"],
    "drama" : ["dabang","krrish","hera pheri","bala","kahani","batla house",
               "kgf","zero","sultan"],
    "thriller" : ["kahani","kgf","batla house","madras cafe","uri","raw",
                  "lucy","the ring","oculus"],
    "horror" : ["oculus","the ring","it","the ring 2","evil dead","conjuring",
                "conjuring 2","bhootnath","aatma"]
}

user = {"uri","kgf","dhamaal","golmaal","thor","hulk","batman","the mask","matrix"}
# j = a intersection b / a union b

scores = {}
for item in dataset:
    scores[item] = 0.0

for item in dataset:
    intersection = user.intersection(set(dataset[item]))
    union = user.union(set(dataset[item]))
    simScore = len(intersection) / len(union)
    scores[item] = round(simScore * 100,2)

print(scores)

max_score = max(scores.values())
for item in scores:
    if max_score == scores[item]:
        cat = item
        break

recommended = set(dataset[cat]) - user
print("Recommended Movies",recommended)


