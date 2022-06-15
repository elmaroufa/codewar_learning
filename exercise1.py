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
