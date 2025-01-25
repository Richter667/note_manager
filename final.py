username = "Richter" # 1.
title = "Beginning" # 2.
content = "Beginning action" #3.
status = "In progress" #4.
created_date = "20-01-25" #5.
issue_date = "20-02-25" #6.

print ("Имя пользователя:", username)
print ("Заголовок заметки:", title)
print ("Описание заметки:", content)
print ("Статус заметки:", status)
print ("Дата создания заметки:", created_date [0:5])
print ("Дата истечения заметки:", issue_date [0:5])

username = input ("Введите имя пользователя: ")
title = input("Введите заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки: ")
created_date = input("Введите дату создания заметки: ")
issue_date = input("Введите дату истечения заметки: ")

zagolovok_1 = input("Основные темы: ")
zagolovok_2 = input("Персонажи: ")
zagolovok_3 = input("Рекомендации для чтения: ")

zametka_knigi = ["Основные темы: " + zagolovok_1, "Персонажи: " + zagolovok_2, "Рекомендации для чтения: " + zagolovok_3]

print("\n".join (zametka_knigi))

note = ["Имя пользователя:", username,
        "Заголовок заметки:", title,
        "Описание заметки:", content,
        "Статус заметки:", status,
        "Дата создания заметки:", created_date,
        "Дата истечения заметки:", issue_date, ["Основные темы: " + zagolovok_1, "Персонажи: " + zagolovok_2, "Рекомендации для чтения: " + zagolovok_3]]

print (note)