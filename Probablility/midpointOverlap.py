import time
from random import random

val = input("Enter how many midpoint pairs you would like to generate: ")
totalOverlap=0
print("Calculating "+str(val)+" midpoint pairs...")
start_time = time.time()

for _ in range(int(val)):
    point1 = 6 + (random() * (22 - 6))
    point2 = 0 + (random() * (11 - 0))

    if(abs(point1-point2)<=2):
        # Uncomment this to debug (Can cause lag with numbers over 1,000,000)
        # print("Point 1: "+str(point1))
        # print("Point 2: "+str(point2))
        # print("Distance: "+str(abs(point1-point2)))
        totalOverlap=totalOverlap+1

print("Completed in: "+"--- %s seconds ---" % (time.time() - start_time))
print("Total Number of overlaping points found in "+str(val)+" midpoint pairs generated: "+str(totalOverlap))
overlapPercentage=100*(totalOverlap/int(val))
print("Overlap percentage: "+str(overlapPercentage)+"%")