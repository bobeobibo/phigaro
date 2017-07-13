import sys
import math

with open(sys.argv[1]) as stringsfile:
    lines = stringsfile.read().split("\n")

def getListFromFile(filename):
    with open(filename) as file:
        return file.read().split("\n")
    
def countGrad(sequence, windowSize):
    #input: 'NPPPNNPNPN??NP'-like sequence converted to [0,1,1,1,0,0,1,0,1,0,0,0,0,1], list type
    grad = [] 
    ofset = math.floor(windowSize / 2)
    for i in range(0, len(sequence)):  # for all values
        grad.append(0)
        start = int(i - ofset)
        if start < 0:  # if start is negative
            start = 0
        end = int(i + ofset)
        if end > len(sequence) - 1:  # if end is out of range
            end = len(sequence) - 1
        grad[i] += sum(sequence[start:end + 1])  # count sum of elements in window
    return grad

# delete all elements from grad which do not have neighbors that > minVal
def countNormGrad(grad, windowSize, minVal):
    #input: grad from previous function, window size, number of phage sequences in a window threshold
    normGrad = list(grad)  # copy gradient
    ofset = math.floor(windowSize / 2)
    for i in range(0, len(normGrad)): #same as in previous function
        start = int(i - ofset)
        if start < 0:
            start = 0
        end = int(i + ofset)
        if end > len(grad) - 1:
            end = len(grad) - 1
        delete = True
        for j in range(start, end):  # check neighbors
            if normGrad[j] > minVal:  # if at least one is bigger than minVal
                delete = False
        if delete:
            normGrad[i] = 0
    return normGrad

def getPhages(sequence, normGrad):  # get coordinates of phages
    phages = []
    i = 0
    while i < len(normGrad):
        rangeFinish = False
        if normGrad[i] != 0:  # bump into not zero
            start = i
            if start < 0:
                start = 0
            end = findEndOfRange(normGrad, start)
            if start >= end:
                break
            phageStart = findPhageStart(sequence, start)
            phageEnd = findPhageEnd(sequence, end)
            if phageStart < 0:
                phageStart = 0
            phages.append({"start": phageStart, "end": phageEnd})
            i = end + 1
        else:
            i += 1
    return phages

def findEndOfRange(normGrad, iStart):  # find where the sequence stops (12345321*here*0000)
    #takes normGrad and putative end position
    i = iStart
    while normGrad[i] != 0 and i < (len(normGrad)-1):
        i += 1
    return i-1

def findPhageStart(sequence, iStart):  # find first phage protein in sequence
    i = iStart
    while sequence[i] == 0 and i < (len(sequence)-1):
        i += 1
    return i - 1

def findPhageEnd(sequence, iEnd):  # find last phage protein in sequence
    i = iEnd
    while sequence[i] == 0:
        i -= 1
    return i + 1

def findendofrange(iStart,nrmgr): 
    i = iStart
    while nrmgr[i] != 0 and i < len(nrmgr) - 1:
        i += 1
    return i-1

def findFageStart(iStart, lin):
    i = iStart
    while lin[i] == 0:
        i += 1
    return i - 1

def findFageEnd(iEnd, lin):
    i = iEnd
    while lin[i] == 0:
        i -= 1
    return i + 1

res = 0
Windowsize = 37 #optimize this
MinPhageInWindow = 14 #optimize this

scafoldy = [x.split(' ')[0] for x in lines if x]
npn = [x.split(' ')[1] for x in lines if x]

kkz = list()

phcontpos = []
countphage = 0
countarphage = 0

for i in range(len(npn)):
    kkz.append(list())
    count = 0
    arpositions = []
    for letter in npn[i]:
        if letter == 'P':
            kkz[i].append(1)
        elif letter == 'r':
            arpositions.append(count)
        else:
            kkz[i].append(0)
        count += 1
    grad = countGrad(kkz[i], Windowsize)
    normGrad = countNormGrad(grad, Windowsize, MinPhageInWindow)
    phages = getPhages(kkz[i], normGrad)

    if phages:
        countphage += 1
        if arpositions:
            pass
        for jj in phages:
            if arpositions:
                print(scafoldy[i], npn[i][jj['start']:jj['end']+1])
            if jj['end'] - jj['start'] > 0.8*len(kkz[i]):   #this is not nessesary
                print ("It is a phage")
            else:
                print("It is a prophage")
            arhere = False
            for zz in arpositions:
                if (zz >= (jj['start']-2)) and (zz <= (jj['end']+2)):
                    arhere = True
                    print("AR-gene inside")
            if arhere == True:
                countarphage += 1
print(countphage, countarphage)
