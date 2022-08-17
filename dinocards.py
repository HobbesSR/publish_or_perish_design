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
    {"habitat":[1,0,1,0,0,1,0,1], "dino":[0,1,0,1,0,1,0,0]}
]

HABITAT_NAMES = [
    "Island",
    "Lagoon",
    "Swamp",
    "Floodplain",
    "Prarie",
    "River",
    "Riparian Forest",
    "Coniferous Forest",
    "Marsh",
    "Lake",
    "Delta",
    "Savanna",
    "Coast",
    "Mixed Forest",
    "Deciduous Forest",
    "Desert Plain",
    "Scrubland",
    "Wetland"
]

HABITAT_DIRECTORIES = [
    "island",
    "lagoon",
    "swamp",
    "floodplain",
    "prarie",
    "river",
    "riparian_forest",
    "coniferous_forest",
    "marshland",
    "lake",
    "delta",
    "savanna",
    "coast",
    "mixed_forest",
    "deciduous_forest",
    "desert_plain",
    "scrubland",
    "wetlands"
]

HABITAT_IMAGE_FILENAMES = [
    "dinos(4)_1.png",
    "dinos(6)_7.png",
    "dinos(7)_7.png",
    "dinos(8)_6.png",
    "dinos(9)_1.png",
    "dinos(10)_4.png",
    "dinos(2)_4.png",
    "dinos(11)_6.png",
    "dinos(12)_3.png",
    "dinos(14)_9.png",
    "dinos(16)_6.png",
    "dinos(17)_7.png",
    "dinos(18)_1.png",
    "dinos(24)_6.png",
    "dinos(25)_15.png",
    "dinos(26)_2.png",
    "dinos(27)_3.png",
    "dinos(28)_1.png"
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
    # habitat name
    print(HABITAT_NAMES[cardIndex], end =",")

    # habitat image path
    print(HABITAT_DIRECTORIES[cardIndex] + "/" + HABITAT_IMAGE_FILENAMES[cardIndex], end = ",")

    # habitat environment traits
    for traitIndex in range(5):
    	for i in range(habitat[traitIndex]):
    	   print(resourceLetters[traitIndex], end = "")
    print(",", end = "")

    # habitat prey traits
    for traitIndex in range(5,8):
    	for i in range(habitat[traitIndex]):
    	   print(resourceLetters[traitIndex], end = "")
    print(",", end = "")

    # dinosaur name
    dino = card["dino"]
    print("Dino" + str(cardIndex+1), end =",")

    # dinosaur environment trait requirements
    for traitIndex in range(5):
    	for i in range(dino[traitIndex]):
    	   print(resourceLetters[traitIndex], end = "")
    print(",", end = "")

    # dinosaur prey trait requirements
    for traitIndex in range(5,8):
    	for i in range(dino[traitIndex]):
    	   print(resourceLetters[traitIndex], end = "")
    print(",", end = "")

    # dinosaur point value
    solutionRatioScale = 1 + (totalSolutionsRatiosByMax[i]**2)
    print(round((totalCardsAverages[cardIndex] / totalCardsAverage) * totalCardsAverages[cardIndex] * solutionRatioScale))

