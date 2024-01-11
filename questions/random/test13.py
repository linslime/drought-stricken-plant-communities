import random
import numpy as np
import csv

def ran1(n):
    list = []
    for i in range(n):
        list.append(random.uniform(0.1,1))
    return list

def ran2(n):
    list = [np.random.normal(loc = 0.25 , scale= 0.25,size = (n)).tolist() for i in range(n)]
    for i in range(n):
        list[i][i] = 1
    return list

def ran3(n):
    return np.random.normal(loc =100 , scale= 60.0,size = (n)).tolist()

def ran4(n):
    list = []
    for i in range(n):
        list.append(random.uniform(0,0.005))
    return list

if __name__ == "__main__":
    list = ran2(200)
    with open("D:\Desktop\\p0.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(list)

    print(list)

