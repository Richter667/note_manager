
a = ["Выполнено", "Не выполнено", "Отложено"]

n = input("Введите текущий статус заметки  (1.выполнено, 2.не выполнено, 3.отложено): ")

if n == str (1):
    print("Статус заметки изменен на", a[0])

elif n == str(2):
      print("Статус заметки изменен на", a[1])

elif n == str(3):
    print("Статус заметки изменен на", a[2])

else:
    print("Введите статус заново")







# a = ["Выполнено", "Не выполнено", "Отложено"]
#
# n = str(input("Введите текущий статус заметки  (Выполнено, Не выполнено, Отложено): "))
# if n in a:
#         print("Статус заметки изменен на", n )
# else:
#     print("Введите статус заново")

