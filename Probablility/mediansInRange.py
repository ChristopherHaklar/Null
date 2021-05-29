import time
from random import random

val = input("Enter how many sets of 5 points you would like to generate: ")
print("Generating "+str(val)+" sets of 5 points...")
start_time = time.time()
totalValidMedians=0

for _ in range(int(val)):
    points=[]
    for x in range(5):
        points.append(random())
    points.sort()
    median=((points[2]+points[3])/2)
    if median > .25 and median < .75:
        totalValidMedians+=1
print("Completed in: "+"--- %s seconds ---" % (time.time() - start_time))
print("Total medians within range '1/4' to '3/4': "+str(totalValidMedians))
print("Percentage of medians valid: "+str((totalValidMedians/int(val)*100))+"%")