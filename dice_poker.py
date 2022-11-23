import random

def maxPair(t):
    r = {}
    for i in range(1, 7):
        r[i] = 0
    for num in t:
        r[num] += 1
    return r

def isPair(mp):
    for i in range(1, 7):
        if mp[i] >= 2:
            return True
    return False 

def isTrip(mp):
    for i in range(1, 7):
        if mp[i] >= 3:
            return True
    return False 

def isQuad(mp):
    for i in range(1, 7):
        if mp[i] >= 4:
            return True
    return False 

def isQuint(mp):
    for i in range(1, 7):
        if mp[i] >= 5:
            return True
    return False 
    
def isTwoPair(mp):
    pair1 = 0
    for i in range(1, 7):
        if mp[i] >= 2:
            pair1 = i
    if pair1 == 0:
        return False
    for i in range(1, 7):
        if i == pair1:
            continue
        if mp[i] >= 2:
            return True
    return False


def isFullHouse(mp):
    trip = 0
    for i in range(1, 7):
        if mp[i] >= 3:
            trip = i
    if trip == 0:
        return False
    for i in range(1, 7):
        if i == trip:
            continue
        if mp[i] >= 2:
            return True
    return False

def isStraight(mp):
    for i in range (0, 2):
        straight = True
        for j in range(1, 6):
            if mp[i + j] == 0:
                straight = False
        if straight:
            return True
    return False


def toss():
    return [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]

result = {
    "pair": 0,
    "twopair": 0,
    "triplet": 0,
    "quad": 0,
    "quint": 0,
    "straight": 0,
    "full house": 0
}

def simulate():
    t = toss()
    mp = maxPair(t)
    result["pair"] += 1 if isPair(mp) else 0
    result["twopair"] += 1 if isTwoPair(mp) else 0
    result["triplet"] += 1 if isTrip(mp) else 0
    result["quad"] += 1 if isQuad(mp) else 0
    result["quint"] += 1 if isQuint(mp) else 0
    result["straight"] += 1 if isStraight(mp) else 0
    result["full house"] += 1 if isFullHouse(mp) else 0
    return t

reps = 1000000

for i in range(reps):
    simulate()

print("pair: ", result["pair"], result["pair"] / reps * 100)
print("twopair: ", result["twopair"], result["twopair"] / reps * 100)
print("triplet: ", result["triplet"], result["triplet"] / reps * 100)
print("full house: ", result["full house"], result["full house"] / reps * 100)
print("straight: ", result["straight"], result["straight"] / reps * 100)
print("quad: ", result["quad"], result["quad"] / reps * 100)
print("quint: ", result["quint"], result["quint"] / reps * 100)

print (result)
