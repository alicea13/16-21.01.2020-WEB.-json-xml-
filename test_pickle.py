from pickle import loads, dumps


s = {"Юля": 15, "Ваня": 11}
d = dumps(s)
print(d)

print(loads(d))