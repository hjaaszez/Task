import random

def v1():
    x = random.randint(0,3) #0:上 1:右 2:下 3:左
    if x==0:
        y = 0
    elif x == 1:
        y = v2()
    elif x==2:
        y = v4()
    elif x==3:
        y = 0
    return y

def v2():
    x = random.randint(0,3) #0:上 1:右 2:下 3:左
    if x==0:
        y = 0
    elif x==1:
        y = v3()
    elif x==2:
        y = v5()
    elif x==3:
        y = v1()
    return y

def v3():
    x = random.randint(0,2) #0:上 1:下 2:左
    if x==0:
        y = 0
    elif x==1:
        y = v6()
    elif x==2:
        y = v2()
    return y

def v4():
    x = random.randint(0,3) #0:上 1:右 2:下 3:左
    if x==0:
        y = v1()
    elif x==1:
        y = v5()
    elif x==2:
        y = 1
    elif x==3:
        y = 0
    return y

def v5():
    x = random.randint(0,3) #0:上 1:右 2:下 3:左
    if x==0:
        y = v2()
    elif x==1:
        y = v6()
    elif x==2:
        y = 1
    elif x==3:
        y = v4()
    return y

def v6():
    x = random.randint(0,1) #0:上 1:左
    if x==0:
        y = v3()
    elif x==1:
        y = v5()
    return y

if __name__=="__main__":
    roop = 100000
    for i in range(6):
        count = [0]*2
        for j in range(roop):
            if i == 0:
                walk = v1()
            elif i == 1:
                walk = v2()
            elif i == 2:
                walk = v3()
            elif i == 3:
                walk = v4()
            elif i == 4:
                walk = v5()
            else:
                walk = v6()

            count[walk] += 1
        print(f"{i + 1}の確率=", count[1]/roop)

