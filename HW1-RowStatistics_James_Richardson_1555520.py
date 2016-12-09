
inFile = open('data.txt', 'r')
outFile = open("RowStatistics.txt","w")
list = []

def createMatrix(file, list):
    for line in file:
        list.append(line)

def findMin(row):
    list = row.split(',')
    min = int(list[0])
    for num in list:
        if(num == '\n'):
            continue
        if int(num) < min:
            min = int(num)
    return min

def findMax(row):
    list = row.split(',')
    max = int(list[0])
    for num in list:
        if (num == '\n'):
            continue
        if int(num) > max:
            max = int(num)
    return max

def findAvg(row):
    list = row.split(',')
    sum = 0
    for num in list:
        if (num == '\n'):
            continue
        sum += int(num)
    return float(sum / len(list))

def findRange(row):
    return findMax(row) - findMin(row)

def findMedian(row):
    list = row.split(',')
    list.sort()
    return (list[2])

createMatrix(inFile, list)

for row in list:
    outFile.write(str(findMin(row)) + ',')
    outFile.write(str(findMax(row))  + ',')
    outFile.write(str(findAvg(row))  + ',')
    outFile.write(str(findRange(row))  + ',')
    outFile.write(str(findMedian(row)))
    outFile.write('\n')
inFile.close()
outFile.close()
