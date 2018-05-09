import sys

args = sys.argv[1:]
usernames = []
for i in args:
    usernames.append(i)

def greet_users(name):
    for i in name:
        print("Hello, " + i[0].upper() + i[1:] + "!")

greet_users(usernames)