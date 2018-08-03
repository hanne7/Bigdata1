import re
f = open('national_code_selected.txt', 'r', encoding='utf-8')
lines = f.readlines()

nums = []
for i in lines:
    nums.append(re.findall('\d+', i)[0])

print(nums)
