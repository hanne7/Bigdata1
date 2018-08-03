f = open('learning_python.txt', 'r', encoding='UTF-8')
lines = f.readlines()
for line in lines:
    print(line,end='')
print()
for line in lines:
    print(line.replace('python', 'C'), end='')
a = open('learn_python_copyed.txt', "w", encoding='UTF-8')
for line in lines:
    data = line.replace('python', "C")
    a.write(data)
a.close()
f.close()