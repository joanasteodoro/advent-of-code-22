import re
input = open('input4.txt', 'r')
lines = input.readlines()

def processLine(line):
    pairs = line.strip()
    pairs = re.split(',|-|\+', pairs)
    for i in range(len(pairs)):
        pairs[i] = int(pairs[i]) 
    return pairs

def part1():
    finalSum = 0
    for line in lines:
        pairs = processLine(line)
        if pairs[0] <= pairs[2] and pairs[1] >= pairs[3]:
            finalSum += 1
        elif pairs[2] <= pairs[0] and pairs[3] >= pairs[1]:
            finalSum += 1
    return finalSum


print(part1())