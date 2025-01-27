y = ["Заголовки заметок: "] #создается список

n = str #переменная для записи данных

while True:

    n = str(input ("Введите заголовок заметки: "))
    y.append(n)
    if n == "stop":
        print(y); break

    print (y)










