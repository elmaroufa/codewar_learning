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
