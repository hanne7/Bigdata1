i = 1
while True:
    name = input("안녕하세요. 이름을 입력하세요. : ")
    if i == 1:
        print("Hi %s!! You are %dst person come here!" %(name, i))
    elif i == 2:
        print("Hi %s!! You are %dnd person come here!" % (name, i))
    elif i == 3:
        print("Hi %s!! You are %drd person come here!" % (name, i))
    elif i <= 10:
        print("Hi %s!! You are %dth person come here!" % (name, i))
    elif i > 10:
        print("Sorry %s. The event is closed because You are %dth person come here!" % (name, i))
    i = i + 1
