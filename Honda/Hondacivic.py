from robot.libraries.BuiltIn import BuiltIn
from Vehicle import Vhbase
from collections import deque
import yaml
import numpy as np

class Hondacivic:
  def __init__(self,name):
      self.name=name

HC = Vhbase.car('4', 'car', 'red')
HC.start()

HC1= Vhbase.truck(4, 't', 't').start()

#binary search
def binaryseach(list,element):
    start=0
    end=len(list)-1
    while (start<=end):
        mid=start+end/2
        if element==list[mid]:
           return mid
        else:
            if element<list[mid]:
                end=mid-1
            else:
                start=mid+1
    return-1


def distinctelements(list):
    output=[]
    for element in list:
        if element not in output:
            output.append(element)
    return output.count()



def  loopf () :
    # type: () -> object
    for i in range(1,10):
        print i

def sum_of_numbers():
    numbers = [1,10,20,30,40,50]
    sum = 0
    for number in numbers:
       sum = sum + number
    print sum

def breaks():
    for i in range(1,10):
        if i == 3:
            break
    print i

def multiply(a,b):
    x=a*b
    print x

def whileloopex(f=0):
   # f=0
    while ( f <  10):
        f=f+1
        print f

def arrayfunc():
    arr=[8,-7,1,4,3,2]
    arr.sort()
    print 'after sort......'
    print   sorted(arr).index(8)
    print 'after sort again........'
    #arr.index(2)
    arr.append(6)
   # arr.sort()
    #print arr
    arr.pop()
    #print arr
    print arr[0]
    print len(arr)
    for x in arr:
        abs(x)
        print x

def smallest_not_in_list(list):
    list.sort()
    list1=np.array(list)

    present=True
    try:
     #k=list.index(0,len(list)
     h=list.index(1)
    except:
        #present=False
        print "1 not present"
        return 1

    if (present):
               i=1
               for k in xrange(h,len(list)):
                try:
                 if list.index(k):
                  print ("on to next number")
                except:
                    return k



def binarysearch(list,key):
    start=0
    end=len(list)-1
    #list.sort()
   # list1=np.array(list)
    while start<=end:
        mid=(start+end)/2
        if list[mid]==key:
            return mid
        else:
            if list[mid]<key:
                start=mid+1
            else:
                end=mid-1
    return -1

# insertion sort algorithm
def ins_sort(k):
    for i in range(1,len(k)):    #since we want to swap an item with previous one, we start from 1
        j = i                    #bcoz reducing i directly will mess our for loop, so we reduce its copy j instead
        temp = k[j]              #temp will be used for comparison with previous items, and sent to the place it belongs
        while j > 0 and temp < k[j-1]: #j>0 bcoz no point going till k[0] since there is no seat available on its left, for temp
            k[j] = k[j-1] #Move the bigger item 1 step right to make room for temp
            j=j-1 #take k[j] all the way left to the place where it has a smaller/no value to its left.
        k[j] = temp
    return k







#first in first out
def queueex():
     queue=deque(['terry','mike','paul'])
     queue.append("abdul")
     print queue
     queue.popleft()
     queue.appendleft('har')
     print queue

def readyaml():
 for key, value in yaml.load(open('../test.yaml'))['instance'].iteritems():
    print key, value
    if (key=="Id"):
        print value

def dict():
    rel={'naren':41,'harsha':40}
    for(k,v) in rel.items():
        if k=='naren':
            print v
#bubblesort
def bubbleSort(alist):

    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)




def solution(A):
    # write your code in Python 3.6
    output1=[]
    output2=[]
    for element in A:
        if element not in output1:
            output1.append(element)
        else:
            output2.append(element)

    for element1 in output1:
        if element1 not in output2:
            return element1

def solutionag(A):
    sum_left, sum_right = 0, sum(A)
    for index, value in enumerate(A):
        #print (index , value)
        sum_right -= value
        if sum_left == sum_right:
            return index

        sum_left += value
    return -1


def main():
    print "Hello World!"
    #loopf()
    #summation()
    breaks()
    whileloopex()
    arrayfunc()
    queueex()
    print ("...............................................")
    readyaml()
    dict()
    test=[-7,-5,0,1,3,5]
    print 'practise prb'
    print binarysearch(test,1)
    #print smallest_not_in_list(test)inc
    print  " distinct...."
    list={2,1,1,2,3,1}
    #print distinctelements(list)

    A1=[9,3,9,3,9,7,9]
    print solution(A1)



    A = [-7, 1, 5, 2, -4, 3, 0]
    solutionag(A)
    #print ins_sort(list)

if __name__=="__main__":
 main()
else:
    "somebody else running the prog"




