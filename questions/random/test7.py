import random

def ran1(n):
    list = []
    for i in range(n):
        list.append(random.uniform(0,1))
    return list

def ran2(n):
    list = []
    for i in range(n):
        li = []
        for j in range(n):
            li.append(random.uniform(-0.25,0.7))
        li[i] = 1
        list.append(li)
    return list

def ran3(n):
    list = []
    for i in range(n):
        list.append(random.randint(50, 150))
    return list
def ran4(n):
    list = []
    for i in range(n):
        list.append(random.uniform(0,0.005))
    return list

if __name__ == "__main__":
    list = ran2(50)
    print(list)