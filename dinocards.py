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

# DINO_CARD_TRAIT_REQUIREMENTS_OLD = [
#     [0,0,1,0,0,2,0,1],
#     [0,2,1,0,0,0,0,0],
#     [0,2,0,0,1,0,0,0],
#     [2,1,1,0,0,0,0,0],
#     [0,0,0,0,1,2,0,0],
#     [0,0,0,0,1,0,0,2],
#     [1,0,1,0,0,0,0,2],
#     [0,1,0,0,1,1,1,0],
#     [0,0,0,0,1,1,0,1],
#     [0,1,0,2,0,1,1,0],
#     [0,1,0,1,0,2,0,0],
#     [1,0,0,1,0,0,1,1],
#     [0,1,1,0,1,0,0,0],
#     [0,0,1,0,1,0,0,0],
#     [1,0,1,0,0,0,1,1],
#     [1,2,1,0,0,0,0,0],
#     [0,0,1,1,0,0,0,0],
#     [0,2,0,1,0,1,0,0]
# ]

DINO_CARD_TRAIT_REQUIREMENTS = [
    [0,0,1,0,0,2,0,1],
    [0,2,1,0,0,0,0,0],
    [0,2,0,0,1,0,0,0],
    [2,1,1,0,0,0,0,0],
    [0,0,0,0,2,2,0,0],
    [1,0,0,0,1,0,0,2],
    [1,0,1,0,0,0,0,2],
    [0,1,0,0,1,1,1,0],
    [0,0,0,0,1,1,0,1],
    [0,1,0,2,0,1,1,0],
    [0,1,0,1,0,2,0,0],
    [1,0,0,1,0,0,2,1],
    [0,1,1,0,1,0,0,0],
    [0,0,1,0,1,0,0,0],
    [3,0,1,0,0,1,1,1],
    [1,2,1,0,0,0,0,0],
    [0,0,3,1,0,0,0,0],
    [0,2,0,2,0,2,0,0]
]

def cardsConflictCount(dinoCardIndex, habitatCardIndex):
    dinoCardTraits = DINO_CARD_TRAIT_REQUIREMENTS[dinoCardIndex]
    habitatCardTraits = CARDS[habitatCardIndex]["habitat"]
    conflictCount = 0
    for traitIndex in range (len(dinoCardTraits)):
        if dinoCardTraits[traitIndex] > 0 and habitatCardTraits[traitIndex] > 0:
            conflictCount = conflictCount + 1
    return conflictCount

dinoConflicts = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

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

NEW_HABITAT_DIRECTORIES = [
    "paleoart",
    "paleoart",
    "paleoart",
    "paleoart",
    "paleoart",
    "paleoart",
    "paleoart",
    "paleoart",
    "paleoart",
    "paleoart",
    "paleoart",
    "paleoart",
    "paleoart",
    "paleoart",
    "paleoart",
    "paleoart",
    "paleoart",
    "paleoart"
]

NEW_HABITAT_IMAGE_FILENAMES = [
    "island.png",
    "lagoon.png",
    "swamp.png",
    "flood_plain.png",
    "prarie.png",
    "river.png",
    "riparian_forest.png",
    "coniferous_forest.png",
    "marsh.png",
    "lake.png",
    "delta.png",
    "savanna.png",
    "coast.png",
    "mixed_forest.png",
    "deciduous_forest.png",
    "desert_plain.png",
    "scrublands.png",
    "wetlands.png"
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
    if len(currentSolutionIn) >= 5:
        return
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

import statistics
cardSolutions = []
cardSolutionUsageCounts = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
cardSolutionsMedianLength = []
cardSolutionsLengthCounts = []
for card in cardIndexes:
    solutions = []
    cardsAvailable = list(filter(lambda x: x != card, cardIndexes))
    currentSolution = []
    requirements = CARDS[card]["dino"]
    getCards(card, cardsAvailable, requirements, solutions, currentSolution)
    #print(solutions)
    cardSolutions.append(solutions)
    for solution in solutions:
        for solutionCard in solution:
            cardSolutionUsageCounts[solutionCard] += 1
    solutionLengths = [len(solution) for solution in solutions]
    solutionLengthsCounts = [solutionLengths.count(length) for length in range(2,6)]
    cardSolutionsLengthCounts.append(solutionLengthsCounts)
    cardSolutionsMedianLength.append(statistics.median(solutionLengths))

cardSolutionMeanUsage = statistics.mean(cardSolutionUsageCounts)

habitCardRelativeDemand = [usageCount / cardSolutionMeanUsage for usageCount in cardSolutionUsageCounts]

dinoAverageSolutionValues = []
#print(habitCardRelativeDemand)
for card in cardIndexes:
    solutionValuesTotal = 0
    for solution in cardSolutions[card]:
        for habitCardIndex in solution:
            solutionValuesTotal += habitCardRelativeDemand[habitatCardIndex]
    dinoAverageSolutionValues.append(solutionValuesTotal / len(cardSolutions[card]))

dinoAverageSolutionValueAverage = statistics.mean(dinoAverageSolutionValues)
dinoCardRelativeAverageSolutionValue = [averageSolutionValue / dinoAverageSolutionValueAverage for averageSolutionValue in dinoAverageSolutionValues]

print(dinoCardRelativeAverageSolutionValue)
totalSolutions = 0
cardSolutionsMinSolution = []
cardSolutionsNumberSolution = []
for i in range(len(cardSolutions)):
    card = cardSolutions[i]
    solutionCount = len(card)
    cardSolutionsNumberSolution.append(solutionCount / cardSolutionsMedianLength[i])
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
    print("    Median solution length = " + str(cardSolutionsMedianLength[i]))
    print("    Dino solution average value = " + str(dinoAverageSolutionValues[i]))
    print("    Solution use = " + str(cardSolutionUsageCounts[i]))
    totalSolutionsRatios.append(solutionCount/totalSolutions)
    totalSolutionsRatiosByMax.append(solutionCount/maxNumberSolutions)

totalCardsAverage = 0
for average in totalCardsAverages:
    totalCardsAverage = totalCardsAverage + average
totalCardsAverage = totalCardsAverage / 18
print(totalCardsAverages)
#print(totalSolutionsRatios)

bonusPercent = 30
cardValues = []
for i in range(len(totalCardsAverages)):
    solutionRatioScale = 1 + (bonusPercent * (1-totalSolutionsRatiosByMax[i])) / 100
    relativeAverageScale = (totalCardsAverages[i] / totalCardsAverage)
    #cardValue = round(totalCardsAverages[i] * relativeAverageScale * solutionRatioScale)
    #cardValue = round(cardSolutionsMinSolution[i] * solutionRatioScale * (1/dinoCardRelativeAverageSolutionValue[i]) * 5)
    amalgamatedExpectedCards = (cardSolutionsMinSolution[i] * 0.5 + cardSolutionsMedianLength[i] * 0.25 + totalCardsAverages[i] * 0.25)
    cardValue = round(amalgamatedExpectedCards * solutionRatioScale * (1/dinoCardRelativeAverageSolutionValue[i]) * 5)

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

HABITAT_POWERS = [
    "",
    "",
    "",
    "Discard: Refersh Draft Row. Then Take Draft Action.",
    "Discard: Refersh Draft Row. Then Take Draft Action.",
    "",
    "",
    "Discard: Take a card from the discard pile and add to your hand",
    "",
    "",
    "",
    "When Drafted: May take top dinosaur card on deck and place unpublished in tableau",
    "",
    "When Drafted: May take top dinosaur card on deck and place unpublished in tableau",
    "Discard: Take a card from the discard pile and add to your hand",
    "When Drafted: May take top dinosaur card on deck and place unpublished in tableau",
    "",
    ""
]

DINOSAUR_BONUS_POINTS = [
    "",
    "",
    "+2 bonus points for each other herbivore",
    "",
    "",
    "",
    "",
    "+3 bonus points if last dinosaur published",
    "+2 bonus points for each dinosaur that shares a trait with this card",
    "",
    "",
    "",
    "+4 bonus points if both other dinosaurs are carnivores or omnivores",
    "+3 bonus points if other dinosaurs are both worth 12 or less points",
    "",
    "",
    "",
    "+1 bonus point for each unique trait other dinosaurs don't share with this card"
]


manualCardValues = [12,14,10,18,14,12,16,10,11,17,14,12,10,12,13,23,19,11]
for cardIndex in range(len(CARDS)):
    card = CARDS[cardIndex]
    habitat = card["habitat"]
    # habitat name
    print(HABITAT_NAMES[cardIndex], end =",")

    # habitat image path
    print(NEW_HABITAT_DIRECTORIES[cardIndex] + "/" + NEW_HABITAT_IMAGE_FILENAMES[cardIndex], end = ",")

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
    print(manualCardValues[cardIndex], end = ",")

    print(HABITAT_POWERS[cardIndex], end = ",")
    
    print(DINOSAUR_BONUS_POINTS[cardIndex])
    
    

print("-------------------")

print("card Solution Usage Counts,habit Card Relative Demand,card Solutions Number Solution,card Solutions Min Solution,card Solutions Median Length,dino Average Solution Values,total Solutions Ratios,total Solutions Ratios By Max,total Cards Averages,dino Card Relative Average Solution Value,solution Ratio Scale,relative Average Scale,solutions 2,solutions 3,solutions 4,solutions 5,card Values")
for cardIndex in range(len(CARDS)):
    if False:
        print(round(cardSolutionUsageCounts[cardIndex],2), end =",")
        print(round(habitCardRelativeDemand[cardIndex],2), end =",")
        print(round(cardSolutionsNumberSolution[cardIndex],2), end =",")
        print(round(cardSolutionsMinSolution[cardIndex],2), end =",")
        print(round(cardSolutionsMedianLength[cardIndex],2), end =",")
        print(round(dinoAverageSolutionValues[cardIndex],2), end =",")
        print(round(totalSolutionsRatios[cardIndex],2), end =",")
        print(round(totalSolutionsRatiosByMax[cardIndex],2), end =",")
        print(round(totalCardsAverages[cardIndex],2), end =",")
        print(round(dinoCardRelativeAverageSolutionValue[cardIndex],2), end =",")
        print(round(1 + (bonusPercent * (1-totalSolutionsRatiosByMax[cardIndex])) / 100,2), end =",")
        print(round((totalCardsAverages[cardIndex] / totalCardsAverage),2), end =",")
        for lengthCount in cardSolutionsLengthCounts[cardIndex]:
            print(lengthCount, end = ",")
        # dinosaur point value
        print(manualCardValues[cardIndex]) #, end =",")
        #print(cardValues[cardIndex] - 10)

habitatCardsWithTraitCounts = [0,0,0,0,0,0,0,0]
dinosaurCardsWithTraitCounts = [0,0,0,0,0,0,0,0]

for card in CARDS:
    for habitatTraitIndex in range(len(card["habitat"])):
        if card["habitat"][habitatTraitIndex]:
            habitatCardsWithTraitCounts[habitatTraitIndex] += 1
    for dinoTraitIndex in range(len(card["dino"])):
        if card["dino"][dinoTraitIndex]:
            dinosaurCardsWithTraitCounts[dinoTraitIndex] += 1
print(habitatCardsWithTraitCounts)
print(dinosaurCardsWithTraitCounts)
