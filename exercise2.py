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

