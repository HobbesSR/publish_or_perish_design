CARDS = [
    {"habitat":[0,1,0,1,0,1,1,0]},
    {"habitat":[0,0,0,1,0,1,1,0]},
    {"habitat":[1,0,1,0,0,1,0,1]},
    {"habitat":[0,1,0,0,1,0,0,1]},
    {"habitat":[0,1,0,0,1,0,0,1]},
    {"habitat":[1,1,0,0,0,1,1,1]},
    {"habitat":[1,1,1,0,0,1,0,1]},
    {"habitat":[0,0,1,0,0,1,0,1]},
    {"habitat":[1,1,0,0,0,1,0,0]},
    {"habitat":[1,0,0,0,0,0,1,1]},
    {"habitat":[1,0,0,1,0,1,1,0]},
    {"habitat":[0,1,0,0,1,0,0,1]},
    {"habitat":[0,1,0,1,0,1,1,0]},
    {"habitat":[0,0,1,0,0,1,0,1]},
    {"habitat":[0,0,1,0,0,1,0,1]},
    {"habitat":[0,1,0,0,1,0,0,1]},
    {"habitat":[0,1,0,0,1,1,0,0]},
    {"habitat":[1,0,1,0,0,1,0,1]}
]

DINO_CARD_TRAIT_REQUIREMENTS = [
    [0,0,1,0,0,2,0,1],
    [0,2,1,0,0,0,0,0],
    [0,2,0,0,1,0,0,0],
    [2,1,1,0,0,0,0,0],
    [0,0,0,0,1,2,0,0],
    [0,0,0,0,1,0,0,2],
    [1,0,1,0,0,0,0,2],
    [0,1,0,0,1,1,1,0],
    [0,0,0,0,1,1,0,1],
    [0,1,0,2,0,1,1,0],
    [0,1,0,1,0,2,0,0],
    [1,0,0,1,0,0,1,1],
    [0,1,1,0,1,0,0,0],
    [0,0,1,0,1,0,0,0],
    [1,0,1,0,0,0,1,1],
    [1,2,1,0,0,0,0,0],
    [0,0,1,1,0,0,0,0],
    [0,2,0,1,0,1,0,0]
]

def cardsConflictCount(dinoCardIndex, habitatCardIndex):
    dinoCardTraits = DINO_CARD_TRAIT_REQUIREMENTS[dinoCardIndex]
    habitatCardTraits = CARDS[habitatCardIndex]["habitat"]
    conflictCount = 0
    for traitIndex in range (len(dinoCardTraits)):
        if dinoCardTraits[traitIndex] > 0 and habitatCardTraits[traitIndex] > 0:
            conflictCount = conflictCount + 1
    return conflictCount

dinoConflicts = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0
]

DINO_NAMES = [
    "Herrerasaurus",
    "Plateosaurus",
    "Stegosaurus",
    "Corythosaurus",
    "Gallimimus",
    "Allosaurus",
    "Tyrannosaurus",
    "Oviraptor",
    "Velociraptor",
    "Archaeopteryx",
    "Compsognathus",
    "Baryonyx",
    "Triceratops",
    "Brachiosaurus",
    "Ceratosaurus",
    "Apatosaurus",
    "Iguanodon",
    "Thecodontosaurus"
]

# for each card, find the list of available cards that have no conflicts
# find the cards with the fewest set of conflict free cards
# from the cards among those, find the card with the most conflicts
# assign to the first card that has no conflict with that card out of the cards with the fewest conflict free cards
for habitatCardIndex in range(len(CARDS)):
    print(habitatCardIndex, end = " - ")
    for dinoCardIndex in range(len(DINO_CARD_TRAIT_REQUIREMENTS)):
        if not cardsConflictCount(dinoCardIndex, habitatCardIndex):
            print(dinoCardIndex, end = ",")
        else:
            dinoConflicts[dinoCardIndex] += 1
    print("", end = "|")
    for dinoCardIndex in range(len(DINO_CARD_TRAIT_REQUIREMENTS)):
        if cardsConflictCount(dinoCardIndex, habitatCardIndex) == 1:
            print(dinoCardIndex, end = ",")
    print()

for i in range(len(dinoConflicts)):
    print("Conflicts for Dino " + str(i) + " - " + str(dinoConflicts[i]))

HABITAT_DINO_INDEXES = [6,3,2,4,15,13,9,10,5,17,1,0,8,11,12,16,14,7]
#[5,2,1,3,14,12,8,9,4,17,1,16,7,10,11,15,13,6]

for cardIndex in range(len(CARDS)):
    CARDS[cardIndex]["dino"] = DINO_CARD_TRAIT_REQUIREMENTS[HABITAT_DINO_INDEXES[cardIndex]]

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
    solutions = []
    cardsAvailable = list(filter(lambda x: x != card, cardIndexes))
    currentSolution = []
    requirements = CARDS[card]["dino"]
    getCards(card, cardsAvailable, requirements, solutions, currentSolution)
    cardSolutions.append(solutions)

totalSolutions = 0
cardSolutionsMinSolution = []
cardSolutionsNumberSolution = []
for i in range(len(cardSolutions)):
    card = cardSolutions[i]
    solutionCount = len(card)
    cardSolutionsNumberSolution.append(solutionCount)
    cardSolutionsMinSolution.append(len(min(card, key=len)))
    totalSolutions = totalSolutions + solutionCount

maxNumberSolutions = max(cardSolutionsNumberSolution)

totalCardsAverages = [] # average number of cards across all solutions for each card
totalSolutionsRatios = [] # percentage of solutions each card uses out of all solutions for all cards
totalSolutionsRatiosByMax = [] # The percentage relative to the max size set of solutions for each cards set of solutions
for i in range(len(cardSolutions)):
    card = cardSolutions[i]
    solutionCount = cardSolutionsNumberSolution[i]
    totalCards = 0
    for solution in card:
        totalCards = totalCards + len(solution)
    print("For card : " + str(i) + " - " + str(totalCards / solutionCount) + " - " + str(solutionCount))
    totalCardsAverages.append(totalCards/solutionCount)
    #print(solutionCount/totalSolutions)
    print("    Min solution = " + str(cardSolutionsMinSolution[i]))
    totalSolutionsRatios.append(solutionCount/totalSolutions)
    totalSolutionsRatiosByMax.append(solutionCount/maxNumberSolutions)

totalCardsAverage = 0
for average in totalCardsAverages:
    totalCardsAverage = totalCardsAverage + average
totalCardsAverage = totalCardsAverage / 18
print(totalCardsAverages)
#print(totalSolutionsRatios)

bonusPercent = 50
cardValues = []
for i in range(len(totalCardsAverages)):
    solutionRatioScale = 1 + (bonusPercent * (1-totalSolutionsRatiosByMax[i])) / 100
    relativeAverageScale = (totalCardsAverages[i] / totalCardsAverage)
    cardValue = round(totalCardsAverages[i] * relativeAverageScale * solutionRatioScale)
    cardValues.append(cardValue)
    print(str(cardValue) + " - " + str(totalCardsAverages[i]))

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
    #print("Dino" + str(cardIndex+1), end =",")
    print(DINO_NAMES[HABITAT_DINO_INDEXES[cardIndex]], end = ",")

    # dinosaur environment trait requirements
    dino = card["dino"]
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
    print(cardValues[cardIndex])

