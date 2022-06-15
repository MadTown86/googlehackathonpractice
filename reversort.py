# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def reverse(L):
    tempr = L[:]
    print("TEMPR " + str(tempr))
    res = []
    print("RANGE " + str([x for x in range(len(tempr)-1, -1, -1)]))
    for x in range(len(tempr)-1, -1, -1):
        res.append(tempr[x])
    print("RES" + str(res))
    return res



def reversort(L):
    for i in range(len(L)-1):
        j = L.index(min(L[i:]))
        jval = L[j]
        ival = L[i]
        L[i] = jval
        L[j] = ival

def reversort_recurs(L):
    for i in range(len(L)-1):
        print("i " + str(i))
        print("L[i:] " + str(L[i:]))
        j = L.index(min(L[i:]))
        print("j " + str(j))
        print("L[i:j] " + str(L[i:j+1]))
        tempr = L[:]
        print("TEMPR " + str(tempr))
        res = []
        print("RANGE " + str([x for x in range(len(tempr) - 1, -1, -1)]))
        for x in range(len(tempr) - 1, -1, -1):
            res.append(tempr[x])
        L[i:j].reverse()
    return(L)


print(reversort_recurs([4, 2, 1, 3]))



