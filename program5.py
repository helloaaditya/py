# insertion sort
def insertionSort(L):
    for index in range(1,len(L)):
        currentvalue = L[index]
        position = index
        while position>0 and L[position-1]>currentvalue:
            L[position]=L[position-1]
            position = position-1
        L[position]=currentvalue

L = [54,26,93,17,77,31,44,55,20]
insertionSort(L)
print(L)

