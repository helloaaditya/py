#  write a program to implement selection sort.

def selection_sort(L):
    n=len(L)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if L[j]<L[min]:
                min=j
        L[i],L[min]=L[min],L[i]
    return 1
L1=[5,-5,1,2,0]
print("THE LIST BEFORE SORTING IS:",L1)
selection_sort(L1)
print("THE LIST AFTER SORTING IS:",L1)

