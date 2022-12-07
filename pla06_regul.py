import re

passport = "12 34 567890"

#is_valid = True

#if len(passport) != 12:
#    is_valid = False

#if passport[2] != " " or passport[5] !=" ":
#    is_valid = False

#for i in range(0, len(passport)):
 #   if i != 2 and i != 5:
  #      char = passport[i]
   #     if char < "0" and char > "9":
    #        is_valid = False

#print(is_valid)

#При помощи регулярных выражений
#\d - цифра, \D - Не цифра
# ^ - это начало текста $ - Конец текста. Ограничивает паттерн
# {2} - ровно 2 раза, {2, } - два и более раза
#pattern = "\d\d \d\d \d\d\d\d\d\d"
pattern = "^\d{2} \d{2} \d{6}$"
result = re.match(pattern, passport)
#print(result)

if result != None:
    print("Valid")
else:
    print("NOT VALID")

text ="""
Мама мыла раму. Ее паспорт номер 12 34 567890.
У папы пропуск 12345. У тети Даши документ 11 22 334455
"""
# Найти паспорта в тексте.
pattern = "\d{2} \d{2} \d{6}"
results = re.findall(pattern, text)
print(results)
