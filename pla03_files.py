# Прочитать из файла - не проблема
f = open("data/amounts.txt","r")
text = f.read()
#print(text)
f.close()

#Пример записи в файл
#f = open("data/results.txt", "w")
#f.write("Hello world!\nGood bye, world!")
#f.close()
#Далее текст надо разобрать для дальнейшей обработки
amounts = text.split("\n")
print(amounts)

#Обрабатываем разобранные данные.
#В данном случае находим числа от 10 до 100


f = open("data/results.txt", "w")

for x in amounts:
     #print(f"число {x}")
     amount = int(x) #Конверсия типа из строки в число
     if amount >= 10 and amount < 100:
         print(f"нормальное число {amount}")
         f.write(str(amount) + "; ")
f.close()