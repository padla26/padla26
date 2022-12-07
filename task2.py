import  os
import re

cmd = f"ipconfig"
result = os.popen(cmd).read().encode("windows-1251").decode("866")

print(result)
# \. - это просто точка, она экранирована
#[\.\s] - в паттерне это или точка или пробельный символ, + это в любом количестве
#pattern = "IPv4-адрес[\.\s]+ : \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

# сКОБКИ МАРКИРУЮТ ТОЛЬКО ТУ ГРУППУ, которую ты хочешь видеть
pattern = "IPv4-адрес[\.\s]+ : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
results = re.findall(pattern, result)
print(results)

#result = results[0]
#pattern = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
#results = re.findall(pattern, result)
#print(results[0])

# Получить маску подсети
pattern = "Маска подсети[\.\s]+ : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
results = re.findall(pattern, result)
print(results)