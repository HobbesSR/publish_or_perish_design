CARDS = [
    {"habitat":[0,1,0,1,0,1,1,0], "dino":[0,0,1,0,0,1,0,1]},
    {"habitat":[0,0,0,1,0,1,1,0], "dino":[0,1,1,0,0,0,0,0]},
    {"habitat":[1,0,1,0,0,1,0,1], "dino":[0,1,0,0,1,0,0,0]},
    {"habitat":[0,1,0,0,1,0,0,1], "dino":[1,1,1,0,0,0,0,0]},
    {"habitat":[0,1,0,0,1,0,0,1], "dino":[0,0,0,0,1,1,0,0]},
    {"habitat":[1,1,0,0,0,1,1,1], "dino":[0,0,0,0,1,0,0,1]},
    {"habitat":[1,1,1,0,0,1,0,1], "dino":[1,0,1,0,0,0,0,1]},
    {"habitat":[0,0,1,0,0,1,0,1], "dino":[0,1,0,0,1,1,1,0]},
    {"habitat":[1,1,0,0,0,1,0,0], "dino":[0,0,0,0,1,1,0,1]},
    {"habitat":[1,0,0,0,0,0,1,1], "dino":[0,1,0,1,0,1,1,0]},
    {"habitat":[1,0,0,1,0,1,1,0], "dino":[0,1,0,1,0,1,0,0]},
    {"habitat":[0,1,0,0,1,0,0,1], "dino":[1,0,0,1,0,0,1,1]},
    {"habitat":[0,1,0,1,0,1,1,0], "dino":[0,1,1,0,1,0,0,0]},
    {"habitat":[0,0,1,0,0,1,0,1], "dino":[0,0,1,0,1,0,0,0]},
    {"habitat":[0,0,1,0,0,1,0,1], "dino":[1,0,1,0,0,0,1,1]},
    {"habitat":[0,1,0,0,1,0,0,1], "dino":[1,1,1,0,0,0,0,0]},
    {"habitat":[0,1,0,0,1,1,0,0], "dino":[0,0,1,1,0,0,0,0]},
    {"habitat":[1,0,1,0,0,0,0,0], "dino":[0,1,0,1,0,1,0,0]}
]


def applyCardToRequirements(cardIndex, requirementsIn):
    card = CARDS[cardIndex]["habitat"]
    for i in range(8):
        requirementsIn[i] = requirementsIn[i] - card[i]

def requirementsSolved(requirementsIn):
    for i in range(8):
        if requirementsIn[i] > 0:
            return False
    return True

def addressesRequirement(cardIndex, requirementsIn):
    for i in range(8):
        if requirementsIn[i] > 0 and CARDS[cardIndex]["habitat"][i] > 0:
            return True
    return False

def getCards(cardIndex, cardsAvailableIn, requirementsIn, solutions, currentSolutionIn):
    cardsAvailable = list(filter(lambda x: addressesRequirement(x, requirementsIn), cardsAvailableIn))

    while len(cardsAvailable) > 0:
        requirements = list(requirementsIn)
        cardIndex = cardsAvailable.pop()
        applyCardToRequirements(cardIndex, requirements)
        newSolution = list(currentSolutionIn)
        newSolution.append(cardIndex)
        #print("New solution")
        #print(newSolution)
        #print("\n")
        if requirementsSolved(requirements):
            solutions.append(newSolution)
        else:
            getCards(cardIndex, cardsAvailable, requirements, solutions, newSolution)

cardIndexes = list(range(0,18))

cardSolutions = []

for card in cardIndexes:
    print(card)
    solutions = []
    cardsAvailable = list(filter(lambda x: x != card, cardIndexes))
    currentSolution = []
    requirements = CARDS[card]["dino"]
    getCards(card, cardsAvailable, requirements, solutions, currentSolution)
    cardSolutions.append(solutions)

totalSolutions = 0
for i in range(len(cardSolutions)):
    card = cardSolutions[i]
    solutionCount = len(card)
    totalSolutions = totalSolutions + solutionCount

totalCardsAverages = []
totalSolutionsRatios = []
totalSolutionsRatiosByMax = []
for i in range(len(cardSolutions)):
    card = cardSolutions[i]
    solutionCount = len(card)
    totalCards = 0
    for solution in card:
        totalCards = totalCards + len(solution)
    print("For card : " + str(i) + " - " + str(totalCards / solutionCount) + " - " + str(solutionCount))
    totalCardsAverages.append(totalCards/solutionCount)
    print(solutionCount/totalSolutions)
    totalSolutionsRatios.append(solutionCount/totalSolutions)
    totalSolutionsRatiosByMax.append(1-solutionCount/527)

totalCardsAverage = 0
for average in totalCardsAverages:
    totalCardsAverage = totalCardsAverage + average
totalCardsAverage = totalCardsAverage / 18
print(totalCardsAverages)
print(totalSolutionsRatios)
for i in range(len(totalCardsAverages)):
    solutionRatioScale = 1 + (totalSolutionsRatiosByMax[i]**2)
    print(round((totalCardsAverages[i] / totalCardsAverage) * totalCardsAverages[i] * solutionRatioScale))

resource_A = 0
resource_B = 1
resource_T = 2
resource_C = 3
resource_P = 4
resource_S = 5
resource_F = 6
resource_L = 7
resourceLetters = {
    resource_A:'A',
    resource_B:'B',
    resource_T:'T',
    resource_C:'C',
    resource_P:'P',
    resource_S:'S',
    resource_F:'F',
    resource_L:'L'
}

for cardIndex in range(len(CARDS)):
    card = CARDS[cardIndex]
    habitat = card["habitat"]
    print("Habitat" + str(cardIndex+1), end =",")
    for traitIndex in range(5):
    	for i in range(habitat[traitIndex]):
    	   print(resourceLetters[traitIndex], end = "")
    print(",", end = "")
    for traitIndex in range(5,8):
    	for i in range(habitat[traitIndex]):
    	   print(resourceLetters[traitIndex], end = "")
    print(",", end = "")
    dino = card["dino"]
    print("Dino" + str(cardIndex+1), end =",")
    for traitIndex in range(5):
    	for i in range(dino[traitIndex]):
    	   print(resourceLetters[traitIndex], end = "")
    print(",", end = "")
    for traitIndex in range(5,8):
    	for i in range(dino[traitIndex]):
    	   print(resourceLetters[traitIndex], end = "")
    print(",", end = "")
    solutionRatioScale = 1 + (totalSolutionsRatiosByMax[i]**2)
    print(round((totalCardsAverages[cardIndex] / totalCardsAverage) * totalCardsAverages[cardIndex] * solutionRatioScale))

