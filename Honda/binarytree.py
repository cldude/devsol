import os
#sort algorithm
def sort(l):
    p = 0
    while(p<len(l)-1):
        if(l[p]>l[p+1]):
            l[p],l[p+1] = l[p+1],l[p]
            if(not(p==0)):
                p = p-1
        else:
            p += 1
    return l

# simple binary tree
# in this implementation, a node is inserted between an existing node and the root


class BinaryTree():

    def __init__(self,rootid):
        self.left = None
        self.right = None
        self.rootid = rootid

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.rootid = value
    def getNodeValue(self):
        return self.rootid

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            self.left = tree
            tree.left = self.left


def printTree(tree):
    if tree != None:
        printTree(tree.getLeftChild())
        print(tree.getNodeValue())
        printTree(tree.getRightChild())



# test tree

def main():
    myTree = BinaryTree("Maud")
    myTree.insertLeft("Bob")
    myTree.insertRight("Tony")
    myTree.insertRight("Steven")
    printTree(myTree)
    A=[1,1,3,7,5,6]
   # print sorted(A)
    print A.sort()
    print A[1:3]
    print A[2:-1]
    print A[:4]
    print A[1:]
    print A[:]
    #return minimum in aray list
    print min(A)
    #return max in array list
    print max(A)
    #number of occurences of element in A
    print A.count(1)

    print "debugging sol test"
    A=[1,1,3,3,3,5,5,5,5]
    solutiontm(A,2)

    #tuple = (1, 2, 'hi')
    #print len(tuple)  ## 3
    #print tuple[2]    ## hi
   # tuple[2] = 'bye'  ## NO, tuples cannot be changed
   # tuple = (1, 2, 'bye')  ## this works

    #S=   "00:01:07,400-234-090"
    S='00:01:07,400-234-090\n00:06:07,701-080-080\n00:05:00,400-234-090'
    k= S.splitlines()
    sec=[]
    str2=[]
    d={}
    for element in k:
        #print element.split(",")
        k1=element.split(",")
        t1=seconds(k1[0])
        t2=phonenumerals(k1[1])
       # sec.append(seconds(k1[0]))
       # print get_sec(k1[0])
        #str2.append(k1[1])
        #dictionary= dict(zip(k1[1],sec))
       # grades['k'] = 'x'
#>>> grades['newinput'] = 'newval'
       # d[k1[1]]=str(seconds(k1[0]))

        if t2 in d:
           d[t2]=d.get(t2)+seconds(k1[0])
        else:
           d[t2]=seconds(k1[0])
       # temp=0

    keymax=maxvalkey(d)
    bill=0
    for key,value in d.iteritems():
        if key==keymax:
            print ("No bill due to promotion")
        else:
         if value<300:
            bill=bill+3*value
         if value>=300:
            if value%60 !=0:
               bill=bill+(value/60+value%60)*150
            else:
               bill=bill+(value/60)*150
    print bill

#A=[1,3,4,5]
#k=2
def solutiontm(A, K):
    n = len(A)
    best = 0
    count = 1
    for i in range(n - K - 1):
        if (A[i] == A[i + 1]):
            count = count + 1
        else:
            count = 0
        best = max(best, count)
    result = best + 1 + K

    return result



      # print sec
       #print str2
   # dictionary = dict(zip(sec, str2))
    #print dictionary
    #for key,value in dictionary.iteritems():
     #   print("i am there")
      #  print (key,value)




  #  str3=[]
    #for el in str2:
   # s2= [[1,2,3],[3,4,5]]

def maxvalkey(dict):
    val=list(dict.values())
    k=list(dict.keys())
    return k[val.index(max(val))]

def phonenumerals(ph):
    f,s,t=ph.split('-')
    z=(int(f)%100)/10+int(f)/100+(int(f)%100)%10
    q=(int(s)%100)/10+int(s)/100+(int(s)%100)%10
    m=(int(t)%100)/10+int(t)/100+(int(t)%100)%10
    #return int(f)*1+int(s)*1+int(t)*1
    return z+q+m


def seconds(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


## Example pulls filenames from a dir, prints their relative and absolute paths
def printdir(dir):
    filenames = os.listdir(dir)
    for filename in filenames:
        print filename  ## foo.txt
        print os.path.join(dir, filename) ## dir/foo.txt (relative to current dir)
        print os.path.abspath(os.path.join(dir, filename)) ## /home/nick/dir/foo.txt


def get_sec(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

#cyclic rotation of Array
def solution(A, K):
    A = A[-K:]+A[:-K]
    return A

if __name__=="__main__":
    main()
