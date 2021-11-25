#5 Губка Боб жарит котлеты. Всего у него К котлет, на одну сковородку помещается М котлет.
#Расчитать сколько сковородок "полных" надо пожарить и сколько котлет останется еще дожарить на последней.
from random import *
k=int(input("skolko vsego kotlet? "))
m=randint(2,8)
print("na skovorodku vlezaet",m,"kotlet")
if k<m:
    print("vse kotleti vlezaut na skovorodku")
else:
    k>=m 
    a=m/k
    if a<1 and a>0:
        print("kotleti ne vlezaut, ostatok budet zaritsa na drugoi skorovodke")
    else:
        print("vse kotleti vlezaut na skovorodku")




print()
print()
print()
#4 Одноклеточная амеба каждые 3 часа делится на 2 клетки. Определить, сколько клеток будет через 3, 6, 9, ..., 24 часа, если первоначально была одна амеба.
a=1  
b=0
for i in range (8):
    b=b+3
    a+=2
    print(b,"час =",a ,"клеток")
    print(end =" ")
    






print()
print()
print()
#3 Известны оценки по физике каждого из  учеников класса. Определить минимальную и максимальную оценки. (Оценки и количество учеников получаем случайным образом)
from random import*
k=randint(3,33)
print("ucenikov v klasse:")
print(k)
print("ocenki ucenikov:")
for i in range(1,k):
    i=randint(1,5)
    print(i)
m=max(i)
print("lutsii rezultat",m)
n=min(i)
print("hudsii rezultat",n)






print()
print()
print()
#2 Вывести степени натуральных чисел, не превосходящие данного числа n. Пользователь задает показатель степени и число n.
a=int(input("vvedite cislo "))
b=int(input("vvedite stepen "))
for i in range(1,a+1):
    print(i**b)



print()
print()
print()
#1 Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n зверьков. Между двумя соседними зверьками также имеется пустой (из пробелов) столбец. Разрешается вывести пустой столбец после последнего зверька. Для упрощения рисования скопируйте зверька из примера в среду разработки.
#  ^---^
# ( o o )
#  ! = !/)
n=int(input("skolko zverkov hotite? "))
while n>9 or n==0:
    print("eto cislo ne podhodit, poprobuite ese")
    n=int(input("skolko zverkov hotite? "))
a=["  ^---^   "]
b=[" ( o o )  "]
c=["  ! = !/) "]
for i in a+b+c:
    print(i*n)
