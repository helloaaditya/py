# program 6 Write a function cumulative sum to compute cumulative sum.

def cumulative_sum(data):
    c_sum=[]
    c_sum=[sum(data[0:x+1]) for x in range(0,len(data))]
    print ("the cumulative sum of {} is {}".format(data,c_sum))

d=[]
n=int(input("enter the number of elements in the list:"))
for x in range(0,n):
    element=int(input("enter the element:" + str(x+1) + ":"))
    d.append(element)
cumulative_sum(d)

