#Part1
#1


def make_power(number,pow):
    """function that receive number and power and return the number in the power"""
    def dispatch(x):
        if(x==0):
            return number
        elif(x==1):
            return pow
    return dispatch
        
def base(x):
    """return base of number in power"""
    return x(0)
    
def power(x):
    """return the power of number in power"""   
    return x(1)

def print_power(x):
    """function print the number^power"""
    if(type(x)!=int):
        if(power(x)==1 or power(x)==0):
            print(calc_power(x))
        else:
            print("{0}^{1}".format(base(x),power(x)))
    else:
        print(x)
        
def calc_power(x):
    """Calculate the power"""
    return base(x)**power(x)

def mul_power(a,b):
    """function multiply between 2 numbers"""
    if (base(a)==base(b)):
        return make_power(base(a), power(a)+power(b))
    else:
        return calc_power(a)*calc_power(b)
    
def div_power(a,b):
    """function multiply between 2 numbers"""
    if (base(a)==base(b)):
        return make_power(base(a), power(a)-power(b))
    else:
        return calc_power(a)*calc_power(b)

def improve_power(x):
    """Function check if b^p=a^(n*p) and return the new number"""
    for i in range(2,base(x)//2+1):
        if(base(x)%i==0):
            temp=base(x)
            n=0
            flag=True
            while(temp>1):
                if(temp%i!=0):
                    flag=False
                    break
                else:
                    temp=temp/i
                    n=n+1
            if (flag):
                return(make_power(i,n*power(x)))
    return (make_power(x(0), x(1)))
        
#2

def make_tree(v,l,r):
    """function that receive number and power and return the number in the power"""
    def dispatch(t):
        if(t==0):
            return v
        elif(t==1):
            return l
        elif (t==2):
            return r
    return dispatch

def value(t):
    """function return value of root in binary tree"""
    return t(0)

def left(t):
    """function return left son of root in binary tree"""
    return t(1)

def right(t):
    """function return right son of root in binary tree"""
    return t(2)

def print_tree(t):
    """Function print tree nodes by inorder method"""
    if (t==None):
        return 
    else:
        print_tree(left(t))
        print(value(t),end=" ")
        print_tree(right(t))

def count_value(tree,val):
    """Function receive tree and value and return number of appearances of the value in the tree"""
    if (tree==None):
        return 0
    elif(value(tree)==val):
        return 1+count_value(left(tree), val)+count_value(right(tree), val)
    else:
        return count_value(left(tree), val)+count_value(right(tree), val)


 
def tree_BST(tree):
    """Function check if tree is BST and return true/false"""  
    if(tree==None):
        return True
    elif (left(tree)!=None):
        if(value(left(tree))>value(tree)):
            return False
    elif (right(tree)!=None):
        if(value(right(tree))<value(tree)):
            return False
    return tree_BST(left(tree))
    return tree_BST(right(tree))
   
def tree_depth(tree):
    """Function return tree depth"""
    if(tree==None):
        return 0
    elif(left(tree)!=None):
        return 1+tree_depth(left(tree))
    elif(right(tree)!=None):
        return 1+tree_depth(right(tree))
    else:
        return 0
    
def tree_balanced(tree):
    """Function check if difference between 2 sub-trees of every root in the the
    tree is 1 or 0"""
    if(tree==None):
        return True
    if ((right(tree)!=None and left(tree)==None) and (tree_depth(right(tree))>=1)):
        return False
    if ((right(tree)==None and left(tree)!=None) and (tree_depth(left(tree))>=1)):
        return False
    if(right(tree)!=None and left(tree)!=None):
        result=tree_depth(right(tree))-tree_depth(left(tree))
        if(result>1 or result<-1):
            return False
    return (tree_balanced(left(tree)) and tree_balanced(right(tree)))
    
#Part2
#3
   
def get_prices(name,products,sales):
    """Function receive name of market,list of products and their cost and list of markets
    and their sales. Function return list of groceries of the market name it received"""
    return tuple((products[0],products[1]*((1-tuple(filter(lambda x: x[0]==name, sales))[0][1]))) for products in products)


products = (('p1',1000),('p2',2000),('p3',5000),('p4',100))
sales = (('s1',0.2),('s2',0.3),('s3',0.1))
    

def get_prices_dict(name,products,sales):
    """Function receive name of market,dictionary of products and their cost and dictionary of markets
    and their sales. Function return dictionary of groceries of the market name it received"""
    return {x:(1-sales[name])*products[x] for x in products}
        
        
prod_dict = dict(products)
sales_dict = dict(sales)


def get_prices_by_type(name,products,sales,types):
    """Function receive name of market,dictionary of products and their cost,dictionary of markets
    and their sales and dictionary of lists of products by their types.
    Function return dictionary of groceries of the market name it received"""
    return {x:products[x]*(lambda y:1-sales[name][y])(tuple(types)[0] if x==tuple(types.values())[0][1] or x==tuple(types.values())[0][0] else tuple(types)[1]) for x in products}
    
sales = {'s1':{'t1':0.2, 't2':0.1}, 's2':{'t1':0.1, 't2':0.2},'s3':{'t1':0.3, 't2':0.5}}
types = {'t1':('p2', 'p4'), 't2':('p1', 'p3')}   

from _operator import add
from _functools import reduce

def accumulate_prices(name,products,sales,types,add):
    """Function receive name of market,dictionary of products and their cost,dictionary of markets
    and their sales and dictionary of lists of products by their types.
    Function return accumulation of groceries of the market name it received"""
    return reduce(add,[get_prices_by_type(name,products,sales,types)[i] for i in get_prices_by_type(name,products,sales,types)])

#part3
#4

import random

def coding():
    """Function encrypt words and decode text with words that separate by one space between them"""
    
    key={'reverse_word': False, 'reverse_string': False, 'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g', 'h': 'h',
    'i': 'i', 'j': 'j', 'k': 'j', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'u': 'u',
    'v': 'v', 'w': 'w', 'x':'x', 'y': 'y', 'z': 'z'}
    x=0 #determine the sliding of the letters
    
    def isKeyEmpty(k):
        """Utility Function that checks if key is empty"""
        if k=={'reverse_word': False, 'reverse_string': False, 'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g', 'h': 'h',
                  'i': 'i', 'j': 'j', 'k': 'j', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'u': 'u',
                  'v': 'v', 'w': 'w', 'x':'x', 'y': 'y', 'z': 'z'}:
            return True
        return False
    
    def set_key(vars): #vars=[0]num,[1]rWord,[2]rString
        """Function that set the new key"""
        nonlocal key
        nonlocal x
        x=vars[0]
        if (vars[1]=='yes'):
            key['reverse_word']=True
        if (vars[2]=='yes'):
            key['reverse_string']=True
        if (x<-26 or x>26):
            x=x%26 #makes x to be in range
        if (x==0):
            x=random.randrange(-26,26) #random number
        for i in range (97,123): #26 ABC letters, ASCII value of 'a' is 97 97+26=123
            if(i+x>122):
                key[chr(i)]=chr(i-25+x)
            elif (i+x<97):
                key[chr(i)]=chr(i+26+x)
            else:
                key[chr(i)]=chr(i+x)
        print("done")
        
    def empty_key():
        """Function makes current key empty"""
        nonlocal key
        nonlocal x
        x=0
        key={'reverse_word': False, 'reverse_string': False, 'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g', 'h': 'h',
        'i': 'i', 'j': 'j', 'k': 'j', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'u': 'u',
        'v': 'v', 'w': 'w', 'x':'x', 'y': 'y', 'z': 'z'}
        print("done")
        
    def export_key():
        """Function export key"""
        if(isKeyEmpty(key)):
            print("key empty")
        else:
            return key
    
    def import_key(key2):
        """Function import key"""
        nonlocal key
        if(isKeyEmpty(key2)):
            print("key is empty")
        else:
            key=key2
            print("done")
        
    def encoding(sentence):
        """function encoding given string with the key"""
        sentence=list(sentence)
        for i in range(len(sentence)):
            if (sentence[i]!=' '):
                sentence[i]=key[sentence[i]]
        sentence=''.join(sentence)
        if(key['reverse_word']==True):
            splitT=tuple(sentence.split(' '))
            splitT=map(lambda x:x[::-1],splitT)
            sentence=' '.join(splitT)
        if(key['reverse_string']==True):
            splitList=sentence.split(' ')
            splitList=splitList[-1::-1]
            sentence=' '.join(splitList)
        return sentence
    
    def decoding(sentence):
        """function decoding given string with the key"""
        if(isKeyEmpty(key)):
            return "key empty"
        helpKey=dict((y,x) for x,y in key.items())
        if(key['reverse_word']==True):
            splitT=tuple(sentence.split(' '))
            splitT=map(lambda x:x[::-1],splitT)
            sentence=' '.join(splitT)
        if(key['reverse_string']==True):
            splitList=sentence.split(' ')
            splitList=splitList[-1::-1]
            sentence=' '.join(splitList)
        sentence=list(sentence)
        for i in range(len(sentence)):
            if(sentence[i]!=' '):
                sentence[i]=helpKey[sentence[i]]
        sentence=''.join(sentence)
        return sentence

    def dispatch(message,var=None):
        """dispatch with message passing"""
        if message=='set_key':
            set_key(var)
        elif message=='empty_key':
            empty_key()
        elif message=='export_key':
            return export_key()
        elif message=='import_key':
            import_key(var)
        elif message=='encoding':
            return encoding(var)
        elif message=='decoding':
            return decoding(var)
        else:
            print("Unknown message")   
    return dispatch

#5

def parking(payment,regular,priority,vip):
    """Function implement type named parking to manage parking lots"""
    regCount=0
    priCount=0
    vipCount=0
    #Those variables count the busy places in each parking lot
    carsSeq=()
    #cars sequence keep data of all cars that parking in the lots
    
    def print_list():
        carList=list(carsSeq)
        count=0
        def next():
            nonlocal count
            print("car: {}, parking type: {}, parking time: {}".format(carList[count][0],carList[count][1],carList[count][2]))
            count+=1
        def end():
            nonlocal count
            if count==regCount+priCount+vipCount: #if count is equal to the sum of whole counters
                count=0 #for next iteration if exist
                return True  
            else:
                return False
        return {'next':next,'end':end}
    def print_parking(type):
        """Function print data of cars in specific parking lot"""
        if (type=='Regular' or type=='Priority' or type=='VIP'):
            tempList=[]
            for i in carsSeq:
                if i[1]==type:
                    tempList.append(i)
            for i in range(len(tempList)):
                if i==len(tempList)-1:
                    print("car: {0}, parking time: {1}".format(tempList[i][0],tempList[i][2])) 
        else:
            print("Unknown parking lot type")

    def next_time():
        nonlocal carsSeq
        """Advance hours of parking for cars"""
        for i in range(len(carsSeq)):
            carsSeq[i][2]+=1
            
    def start_parking(carNumber,type):
        """Add new car to carsSeq"""
        nonlocal carsSeq
        nonlocal regCount
        nonlocal priCount
        nonlocal vipCount
        if(type=='Regular' and regCount==regular) or (type=='Priority' and priCount==priority) or (type=='VIP' and vipCount==vip):
            print(type+" parking is full")
            return
        if type=='Regular':
            regCount+=1
        elif type=='VIP':
            vipCount+=1
        elif type=='Priority':
            priCount+=1
        else:
            print("Illegal type entered")
            return
        temp=list(carsSeq)
        temp.append([carNumber,type,1])
        carsSeq=tuple(temp)   
        
    def end_parking(carNumber):
        """End car parking and delete it from carSeq"""
        nonlocal carsSeq
        flag=False
        for i in range(len(carsSeq)):
            if carsSeq[i][0]==carNumber:
                flag=True
                temp=carsSeq[i]
        if(flag):
            total=temp[2]*payment
            if temp[0]=='Priority':
                total*=2
            elif temp[0]=='VIP':
                total*=3
            tempList=list(carsSeq)
            tempList.remove(temp)
            carsSeq=tuple(tempList)
            return "car: {}, parking type: {}, parking time: {}\npayment: {}".format(temp[0],temp[1],temp[2],total)
        else:
            return "Car not found!" 
    
    return {'print_list':print_list,'print_parking':print_parking,'next_time':next_time,'start_parking':start_parking,
            'end_parking':end_parking}