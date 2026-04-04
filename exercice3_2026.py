# i,j = 1 , 1
# for i in range(1,10):
#     for j in range(1,10):
#         print(f" {i}x{j}={i*j}")
#         j+=1
#     print("-----------------------------------------------------------------")
#     i+=1

# def find_number(values, listes):
#     return True if values in listes else False

# listes = [1,2,3,4,5,6,7,8,8,9,0]
# print(find_number(22, listes))

# def find_numeber(value, arr):
#     hight = len(arr) -1
#     low = 0
#     while low <= hight:
#         mid = low + int(hight-low/2)
#         if arr[mid] == value:
#             return True
#         else:
#             if arr[mid] > value:
#                 hight = mid -1
#             else :
#                 low = mid + 1
#     return False


# def reverse_liste(liste):
#     i, j = 0, len(liste) - 1
#     while i < j:
#         liste[i], liste[j] = liste[j], liste[i]
#         i+=1
#         j-=1
#     return liste

# def permutes(k, liste):
#     a = reverse_liste(liste[:k])
#     b = reverse_liste(liste[k:])
#     liste = reverse_liste(a+b)
#     return liste


# liste = [0,1,2,3,4,5,6,7,8,9]
# print(permutes(5,liste))

# def maxSubArraySum(arr):
#     size = len(arr)
#     maxSoFar = 0
#     maxEndingHere = 0
#     i = 0

#     while i < size:
#         maxEndingHere = maxEndingHere + arr[i]

#         if maxEndingHere < 0:
#             maxEndingHere = 0

#         if maxSoFar < maxEndingHere:
#             maxSoFar = maxEndingHere

#         i += 1

#     return maxSoFar


# arr = [1, -2, 3, 4, -4, 6, -4, 8, 2]
# print(maxSubArraySum(arr))

def kadane(arr):
    if not arr:
        return 0, []

    max_global  = arr[0]
    max_current = arr[0]

    start = end = 0        # indices du meilleur sous-tableau
    temp_start = 0         # début potentiel

    for i in range(1, len(arr)):
        # Vaut-il mieux recommencer ou continuer ?
        if arr[i] > max_current + arr[i]:
            max_current = arr[i]
            temp_start  = i          # nouveau départ
        else:
            max_current += arr[i]

        # Nouveau maximum global ?
        if max_current > max_global:
            max_global = max_current
            start      = temp_start
            end        = i

    return max_global, arr[start:end+1]


# --- Test ---
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
somme, sous_tableau = kadane(arr)
print(f"Somme max       : {somme}")           # 6
print(f"Sous-tableau    : {sous_tableau}")     # [4, -1, 2, 1]