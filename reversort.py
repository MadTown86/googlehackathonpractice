# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def reversort(L):
    for i in range(len(L)-1):
        j = L.index(min(L[i:]))
        jval = L[j]
        ival = L[i]
        L[i] = jval
        L[j] = ival

def reversort2(L):
    for i in range(len(L)-1):
        j = L.index(min(L[i:]))
        rslice = L[i:j+1]
        rslice.reverse()
        L[i:j+1] = rslice
        print(L)
    return(L)


print(reversort2([4, 2, 1, 3]))
print(reversort2([5, 2, 7, 6, 3, 8, 9]))



