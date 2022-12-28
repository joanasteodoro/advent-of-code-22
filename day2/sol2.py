#rock, paper, scissors
#a, b, c
#x, y, z



#perder, empate, ganhar
#a -> z
#b -> y
#c -> x

input = open('input2.txt', 'r')
lines = input.readlines()

#part 1
def readInput():
    finalSum = 0
    for line in lines:
        match line[0]:
            case 'A':
                match line[2]:
                    case 'X':
                        finalSum += 4
                    case 'Y':
                        finalSum += 8
                    case 'Z':
                        finalSum += 3
            case 'B':
                match line[2]:
                    case 'X':
                        finalSum += 1
                    case 'Y':
                        finalSum += 5
                    case 'Z':
                        finalSum += 9
            case 'C':
                match line[2]:
                    case 'X':
                        finalSum += 7
                    case 'Y':
                        finalSum += 2
                    case 'Z':
                        finalSum += 6
    return finalSum

#part 2
def calculateFinalSum():
    finalSum = 0
    for line in lines:
        match line[0]:
            case 'A':
                match line[2]:
                    case 'X':
                        finalSum += 3
                    case 'Y':
                        finalSum += 4
                    case 'Z':
                        finalSum += 8
            case 'B':
                match line[2]:
                    case 'X':
                        finalSum += 1
                    case 'Y':
                        finalSum += 5
                    case 'Z':
                        finalSum += 9
            case 'C':
                match line[2]:
                    case 'X':
                        finalSum += 2
                    case 'Y':
                        finalSum += 6
                    case 'Z':
                        finalSum += 7
    return finalSum

print(calculateFinalSum())