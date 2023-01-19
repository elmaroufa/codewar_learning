#New file add ohter exercic
def solution(number):
    listes = range(number)
    listes = [ int(x) for x in listes] 
    som = 0
    for x in listes:
        if ( x%3 == 0 or x%5 == 0):
            som = som + x
    return som
  
  
#-------------------------------OTHER SOLUTION -----------------------------------------------------------------------------------------------------------------------
def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
def solution(number):
    sum = 0
    for i in range(number):
        if (i % 3) == 0 or (i % 5) == 0:
            sum += i
    return sum
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------EXERCICE EXTRACT DOMAIN IN URL -----------------------------------------------------------------

import re
def domain_name(url):
    pattern = re.compile(r'(https?://|www\.)?(www\.)?([a-z0-9-]+)(\..+)?')
    subbed_url = pattern.sub(r'\3',url)
    return subbed_url
#--------------------------------------------------------------------------OTHER SOLUTION--------------------------------------------------------------------------
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

import re
def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')

# ------------------------------------------------EXERCICE PHONE NUMBER FORMAT --------------------------------------------------------------------------------
def create_phone_number(n):
    #your code here
    liste1 = '(' + ''.join([ str(x) for x in n[:3]]) + ')'
    liste2 = n[3:10]
    liste2.insert(3, '-')
    liste2 = ''.join([str(x) for x in liste2])
    liste = liste1 + ' ' +  liste2
    return liste



myliste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(create_phone_number(myliste))
#OUTPUT: (123) 456-7890

#---------------------------------OTHER SOLUTION ---------------------------------------------------------------------------------------------------------
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

def create_phone_number(n):
    n = ''.join(map(str,n))
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])





def zero(f = None): return 0 if not f else f(0)
def one(f = None): return 1 if not f else f(1)
def two(f = None): return 2 if not f else f(2)
def three(f = None): return 3 if not f else f(3)
def four(f = None): return 4 if not f else f(4)
def five(f = None): return 5 if not f else f(5)
def six(f = None): return 6 if not f else f(6)
def seven(f = None): return 7 if not f else f(7)
def eight(f = None): return 8 if not f else f(8)
def nine(f = None): return 9 if not f else f(9)

def plus(y): return lambda x: x+y
def minus(y): return lambda x: x-y
def times(y): return lambda  x: x*y
def divided_by(y): return lambda  x: x/y
#_____________---------------------------------------------------------------------------------------------------------------------------------------------------



def filter_list(l):
    'return a new list with the strings filtered out'
    final_liste = []
    #isinstance(myVar, int)
    for x in l:
        if isinstance(x, int):
            final_liste.append(x)
    
    return final_liste
    

liste = [1,2,'aasf','1','123',123]
print(filter_list(liste))
#-----------------------------------------------------other solution --------------------------------------------------------------------------------------------

def filter_list(l):
  'return a new list with the strings filtered out'
  return [i for i in l if not isinstance(i, str)]

def filter_list(l):
  'return a new list with the strings filtered out'
  return [x for x in l if type(x) is not str]

#_______________------------------------------------------------------------------------------------------------------------------------------------------------

def pig_it(text):
    #your code here
    def convert_string(text):
        if text == '!' or text == '?' :
            return text
        text = list(text)
        value = text[0]
        del text[0]
        text.append(value)
        return ''.join(text) + 'ay'
    return " ".join([convert_string(x) for x in text.split(' ')])

#---------------------------------------------------------------------------------------solutions for pro --------------------------------------------------------

def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

def pig_it(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())

#------------------------------------------------------------------------------exercice add text ------------------------------------------------------------------#

def text(liste):
    if len(liste) == 0:
        return  "no one likes this"
    elif len(liste) == 1:
        return ' '.join(liste) + ' likes this'
    else :
        lastindex = len(liste) - 1
        liste2 = liste[:lastindex]
        liste2 = ', '.join(liste2) + ' and ' + liste[lastindex] + ' likes this'
        return liste2

liste = ["Alex", "hamed","abbo", "saly", "kone"]
print(text(liste))

#--------------------------------------------------------------------------------------ALGO SEARCH SEQUENCIAL -----------------------------------------

def findValueListe(liste,value):
   return value in liste ,value
   
def otherMethods(liste, value):
    value_control = None
    i = 0
    for x in liste:
        if value == x :
            value_control = x
            i+=1
    return value_control,i
#------other funcion---------------------------------------------------------------------------------------------------------------------------------------------
@classmethod

def SequentialSearch(cls, arr, value):
    size = len(arr)
    i = 0
    while i < size:
        if value == arr[i]:
            return True
        i += 1
    return False

liste = [1,2,4,5,4,5,4,4,4,4,4,5]
value=5
print(otherMethods(liste, value))
#-------------------------------------------------------Binary Search in pyhton -------------------------------------------------------------------------
def binarySearch(arr, value):
    size = len(arr)
    low = 0
    high = size - 1
    while low <= high:
        mid = low + (high - low) / 2
        mid= int(mid)
        if arr[mid] == value:
            return True
        else:
            if arr[mid] < value:
                low = mid + 1
            else:
                high = mid - 1
    return False
    
arr= [1,2,3,4,5,6,7,8]
print(binarySearch(arr,8))
#------------------------------------------EXO INVERSE ARRAY ------------------------------------------------------------------------------------------
def inverseArray(array):
    index = len(array) - 1
    inverse_array = []
    while index >=0:
        inverse_array.append(array[index])
        index = index -1
        
    return inverse_array
    
array = ['a','b',5,5,'b','e','r','t','y']
print(inverseArray(array))
#------------------------------------------------------ALGO PERMUTATION ----------------------------------------------------------------------------------
def reverse(liste, iterateur, k):
    j = k
    i = iterateur 
    while i < j:
        liste[i],liste[j] = liste[j],liste[i]
        i+=1
        j-=1
    #return liste

def rotateLiss(liste, position):
    size = len(liste) 
    reverse(liste, 0, position-1)
    reverse(liste,position, size-1)
    reverse(liste,0,size-1)
    return liste
        
liste = [1,3,4,5,6,7,8]
size = len(liste) -1
k = 3
print(rotateLiss(liste, k))
#-------------------------------------------------------------------------------------------------------------------------------
# my solution
def generate_hashtag(s):
    #your code here
    if len(s) == 0 or s.isspace() :
        return False
    if len(s) == 140 or len(s) > 140:
        return False
    result = s.split()
    result = ''.join([x.capitalize() for x in result])
    return "#" + result
# Best solution:
def generate_hashtag(s):
    output = "#"
    
    for word in s.split():
        output += word.capitalize()
    
    return False if (len(s) == 0 or len(output) > 140) else output

#--------------------------------------------------------------------------------------------------------------------------------------------------

def fact(n):
    if n<=0 or n==1:
        return 1
    p=n
    while n>1:
        p=p*(n-1)
        n -= 1
    return p
    
val = fact(0)
print(val)
        
#----------------------------------------------------Binary Searcg----------------------------------------------------------------------------------
def binarySearch(value,liste):
    low = 0
    size = len(liste)
    hight = size -1
    while low <= hight:
        mid = int(low + ((hight - low)/2))
        print(mid)
        if liste[mid] == value:
            return True
        else:
            if liste[mid] < value:
                low = mid + 1
            else:
                hight = mid -1
    return False
 
liste = [1, 1, 3, 5, 7, 9, 10, 11, 19, 19]  
print(binarySearch(19,liste))
