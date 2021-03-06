# Python HW 4 Cycles

# Циклы While
# Создать переменную count со значением 0
# Создать переменную range_count со значением 10
# Создать переменную for_count со значением 0
# Создать переменную run  со значением True

count = 0
range_count = 10
for_count = 0
run = True

# Сделать цикл while который будет работать пока run
# Тело цикла:
#     5.1 Выводить в консоль “Hello Cycle”.

while run:
    one = input("Hello Cycle")
    
/Hello Cycle

# Сделать цикл while который будет работать пока run
# Тело цикла:
#     6.1 Выводить в консоль (“Step =”, count)
#     6.2 Переменной count прибавлять 1 с присвоением.

while run:
    print("Step =", count)
    count += 1
    
/Step = 1
Step = 2...

# Сделать цикл while который будет работать пока count < range_count
# Тело цикла:
#     7.1 Выводить в консоль (“Step =”, count)
#     7.2 Переменной count прибавлять 1 с присвоением.

while run:
     if count < range_count:
         count += 1
         print("Step =", count)
         continue
    
/Step = 1
Step = 2
Step = 3
Step = 4
Step = 5
Step = 6
Step = 7
Step = 8
Step = 9
Step = 10

# Сделать цикл while который будет работать пока count < range_count
# Тело цикла:
#     8.1 Выводить в консоль (“Step =”, count)
#     8.2 Переменной count прибавлять 1 с присвоением.
#     8.3 Сделать if с условием, если count равен 3 то выводить в консоль (“Step =”, count, ‘If body’)

while run:
    if count < range_count:
        print("Step =", count)
        count += 1
        if count == 3:
            print("Step =", count, "if body")


/Step = 0
Step = 1
Step = 2
Step = 3 if body
Step = 3
Step = 4
Step = 5
Step = 6
Step = 7
Step = 8
Step = 9

# Сделать цикл while который будет работать пока run
# Тело цикла:
#     9.1 Выводить в консоль (“Step =”, count)
#     9.2 Переменной count прибавлять 1 с присвоением.
#     9.2 Сделать if с условием, если count равен range_count то цикл остановится.
#     9.3 В теле if вывести в консоль (“STOP”, count)

while count < 20:
    print("Step =", count)
    count += 1
    if count == range_count:
        print("STOP", count)
        break
        
/Step = 0
Step = 1
Step = 2
Step = 3
Step = 4
Step = 5
Step = 6
Step = 7
Step = 8
Step = 9
STOP 10

# Циклы For
# Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от for_count  до range_count
# Тело цикла:
# 10.1 Вывести в консоль (‘Step =’, item)

item = 0
for item in range(for_count , range_count):
print("Step =", item)

# Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от 0 до 30
# Тело цикла:
# 11.1 Вывести в консоль (‘Step =’, item)
# 11.2 Сделать if с условием, если item равен  5, то вывести в консоль (‘Item =’, item).
# 11.3 Сделать if с условием, если item равен  10, то вывести в консоль (‘Item =’, item).
# 11.4 Сделать if с условием, если item меньше 4, то вывести в консоль (‘Item <’, item).
# 11.5 Сделать if с условием, если item больше или равно 27, то вывести в консоль (‘Item >=’, item).

for item in range(0, 30):
    print("Step =", item)
    if item == 5:
        print("Item =", item)
    if item == 10:
        print("Item =", item)
    if item < 4:
        print("Item <", item)
        continue
    if item >= 27:
        print("Item >=", item)

/Step = 0
Item < 0
Step = 1
Item < 1
Step = 2
Item < 2
Step = 3
Item < 3
Step = 4
Step = 5
Item = 5
Step = 6
Step = 7
Step = 8
Step = 9
Step = 10
Item = 10
Step = 11
Step = 12
Step = 13
Step = 14
Step = 15
Step = 16
Step = 17
Step = 18
Step = 19
Step = 20
Step = 21
Step = 22
Step = 23
Step = 24
Step = 25
Step = 26
Step = 27
Item >= 27
Step = 28
Item >= 28
Step = 29
Item >= 29


# Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от 0 до range_count +1
# Тело цикла:
# 12.1 Вывести в консоль (‘Step =’, item)
# 12.2 Сделать if с условием, если item равен  7.
#      - В теле if создать переменную inner_count равную 0
#      - В теле if вывести в консоль (‘-- inner_count =’, inner_count)
#      - В теле if сделать ещё одни цикл for с переменной inner_item который будет работать пока счётчик range досчитает от 0 до item.
#     Тело внутреннего цикла For:
#         -- Вывести в консоль (‘-------- Inner_Step =’, inner_item)
#         -- Сделать if если inner_item равен 5, то в inner_count присвоить inner_item.
#     - За пределами тела предыдущего цикла вывести в консоль (‘-- inner_count =’, inner_count)

for item in range(0, range_count+1):
    print("Step =", item)
    if item == 7:
        inner_count = 0
        print("--inner_count =", inner_count)
        inner_item = 0
        for inner_item in range(0, item):
            print("-------- Inner_Step =", inner_item)
            if inner_item == 5:
                inner_count = inner_item
        print("--inner_count =", inner_count)
        
/Step = 0
Step = 1
Step = 2
Step = 3
Step = 4
Step = 5
Step = 6
Step = 7
--inner_count = 0
-------- Inner_Step = 0
-------- Inner_Step = 1
-------- Inner_Step = 2
-------- Inner_Step = 3
-------- Inner_Step = 4
-------- Inner_Step = 5
-------- Inner_Step = 6
--inner_count = 5
Step = 8
Step = 9
Step = 10

# Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от 0 до 20
# Тело цикла:
# 13.1 Вывести в консоль (‘Step =’, item)
# 13.2 Сделать if с условием, если item больше  7 и item меньше 12.
#     - В теле if вывести (‘If_item =’, item)
#     - В теле if поставить continue
# 13.3 Выйти з if. Вывести в консоль (‘End_iteration =’, item)

items_list = []
for item in range(0, 20):
    print("Step =", item)
    if 7 < item < 12:
        print("If_item =", item)
        continue
        print("End_iteration =", item)
        
/Step = 0
End_iteration = 0
Step = 1
End_iteration = 1
Step = 2
End_iteration = 2
Step = 3
End_iteration = 3
Step = 4
End_iteration = 4
Step = 5
End_iteration = 5
Step = 6
End_iteration = 6
Step = 7
End_iteration = 7
Step = 8
If_item = 8
Step = 9
If_item = 9
Step = 10
If_item = 10
Step = 11
If_item = 11
Step = 12
End_iteration = 12
Step = 13
End_iteration = 13
Step = 14
End_iteration = 14
Step = 15
End_iteration = 15
Step = 16
End_iteration = 16
Step = 17
End_iteration = 17
Step = 18
End_iteration = 18
Step = 19
End_iteration = 19
