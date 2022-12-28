def readInput():
    input = open('input1.txt', 'r')
    sums = [0]
    i = 0

    lines = input.readlines()

    for line in lines:
        if line.strip():
            sums[i] += int(line)    
        else:
            sums.append(0)
            i+=1
    return sums

def removeMaxSum():
    sums.remove(max(sums))
    threeMax.append(max(sums))


sums = readInput()
threeMax = [max(sums)]
removeMaxSum()
removeMaxSum()

print(sum(threeMax))
