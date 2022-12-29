import string

input = open('input3.txt', 'r')
rucksacks = input.readlines()
processedRucksacks = {}
alphabet = list(string.ascii_letters)

#part 1
def splitCompartments(rucksack):
    rucksackLength = len(rucksack)
    rucksack = rucksack.strip()
    firstCompartment, secondCompartment = '', ''
    if rucksackLength % 2 == 0:
        firstCompartment = rucksack[0:rucksackLength//2]
        secondCompartment = rucksack[rucksackLength//2:]
    else:
        firstCompartment = rucksack[0:rucksackLength//2]
        secondCompartment = rucksack[rucksackLength//2:]
    return [firstCompartment, secondCompartment]


def populateProcessedRucksacks():
    for rucksack in rucksacks:
        dividedRucksack = splitCompartments(rucksack)
        print(dividedRucksack)
        processedRucksacks[rucksack] = dividedRucksack
    return processedRucksacks

def verifyCommonItems():
    processedRucksacks = populateProcessedRucksacks()
    commonItems = []
    for rucksack in processedRucksacks:
        firstCompartment = processedRucksacks[rucksack][0]
        secondCompartment = processedRucksacks[rucksack][1]
        intersection = ''.join(set(firstCompartment).intersection(secondCompartment))
        if len(intersection):
            commonItems.append(intersection)
    commonItems = ''.join(commonItems)
    return commonItems


def computePrioritySum():
    commonItems = verifyCommonItems()
    sum = 0

    for item in commonItems:
        sum += alphabet.index(item) + 1 

    return sum


sum = computePrioritySum()
print(sum)
