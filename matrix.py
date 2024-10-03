import random
matrix = [[random.randint(1,10)for i in range(3)] for j in range(3)]
for row in matrix:
    for element in row:
        print(element, end='\t')#Ставит в конце таб
    print()#перенос строки
print()
print()
count = 1# сброс счётчика
for row in matrix:
    if count != 2:
        row.reverse()#разворачивание строк кроме второй
    for element in row:
        print(element, end='\t')#Ставит в конце таб
    print()#перенос строки
    count += 1#счётчик