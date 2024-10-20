n=input("Введите строку на русском ")
print("Длина строки ",len(n))
gl=0
sg=0
for i in n:
    if i=="а" or i=="о" or i=="у" or i=="ы" or i=="э" or i=="е" or i=="ё" or i=="ю"  or i=="я" or i=="и":
        gl+=1
    elif i!=" ":
        sg+=1
print("Количество гласных", gl)
print("Количество согласных",sg )
 

