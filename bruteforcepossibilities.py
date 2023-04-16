a = int(input())
str1 = "2"
str2 = "4"
liste = list(str1)
liste.append(str2)
i = 0
while True:
    liste.append(liste[i] + "2")
    liste.append(liste[i] + "4")
    i += 1
    if int(liste[i]) >= a:
        break
for j in liste:
    if a % int(j) == 0:
        print(j)
# from inheritance
