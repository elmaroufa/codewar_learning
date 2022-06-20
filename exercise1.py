#Enter Python code here and hit the Run button.
def digit_pow(n,p):
  liste_number = [int(x) for x in str(n)]
  #liste_number = [pow(x,(p+=1)), for x in liste_number]
  final_liste = []
  for x in liste_number:
      final_liste.append(pow(x,p))
      p+=1
  total_liste = 0
  for x in final_liste:
      total_liste+=x
  number_k = total_liste / n
      
      
  return int(number_k)


liste = digit_pow(46288, 3)
print(liste)
#------------------------------------------------------------------
#other function:
def narcissistic( value ):
    # Code away
    number_list = [int(x) for x in str(value)]
    pow_number = len(number_list)
    number_list = [pow(x,pow_number) for x in number_list]
    total_list = 0
    for x in number_list:
        total_list+=x
    if total_list == value:
        return True
    else:
        return False
# Good solution:
def narcissistic(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))
  
#----------------------------------------------------------------------------------------------------------------------------------
#exercice 3: return total sum of the two lowest positive numbers given an array of minimum 4 positive integers
def special_liste(liste):
    total_num = len(liste)
    liste = [int(x) for x in liste]
    liste.sort()
    p=liste[:4]
    total = p[0] + p[1]
    return total
    
liste = [19, 5, 42, 2, 77]
print(special_liste(liste))
#-------------------------------------------------------------------------------------------------------------------------------------------------
# exercie 4: return string reverse total > 5
#-------------------------------------------------------------------------------------------------------------------------------------------------
def spin_words(sentence):
    def my_reverse(x):
        if len(x) >=5:
            return x[::-1]
        else:
            return x
    my_liste = list(sentence.split(" "))
    my_liste = [my_reverse(x) for x in my_liste]
    
    return ' '.join(my_liste)


liste = "saly est amoureux de sa femme"
print(spin_words(liste))
#---------------other solution : -------------------------------------------------
def spin_words(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
#------------------------------------------------------------------------------------------------------------------------------------------------
def str_to_list( str ) :
    my_str = list(str.strip())
    my_str = [my_str.remove(" ")  for x in my_str if x!=" " ]
   
    return my_str
 
modata = "string 1999977 ere dfdf fdf fdf"    
print(str_to_list(modata))
#--------------------------------------------------------------------------------------------------------------------------------------------------
def create_phone_number(liste):
    liste1 = liste[:3]
    liste1.append(")")
    liste1.insert(0,"(")
    liste1 = [str(x) for x in liste1]
    value1 = "".join(liste1)+" "
    liste2 = liste[3:6]
    liste2 = [str(x) for x in liste2]
    value2 = "".join(liste2)+"-"
    liste3 = liste[6:10]
    liste3 = [str(x) for x in liste3]
    value3 = value1 + value2 + "".join(liste3)
    return value3
    
    
    
phone = [1, 2, 3, 4, 5, 6, 7, 8, 9,3,4,5]

print(create_phone_number(phone))
#----------------------------------------------------------------------------------------
#exercice 4: return sum sere
def series_sum(n):
    # Happy Coding ^_^
    def result_sum(i):
        return str("{:.2f}".format(i))
    if n==0:
        return result_sum(n)
    if n==1:
        return result_sum(n)
    liste = [1]*(n-1)
    i = 4
    total_liste = 0
    for x in liste:
        total_liste = total_liste + (x/i)
        i=i+3
    total_liste = total_liste + 1
    return result_sum(total_liste)
#--------------------------others solution ---------------------------------
def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
  
def series_sum(n):
    sum = 0.0
    for i in range(0,n):
        sum += 1 / (1 + 3 * float(i))
    return '%.2f' % sum
