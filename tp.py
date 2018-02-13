def map(value, leftMin, leftMax, rightMin, rightMax):

    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)

m=int(input())
m=map(m,int(-1),int(1),int(0),int(255))
print(m)
