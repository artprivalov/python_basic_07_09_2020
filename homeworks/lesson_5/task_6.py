import os

db = os.path.join(os.path.dirname(__file__), 'task_6.txt')
db_dict = {}

with open(db, 'r') as file:
    for line in file:
        tmp = line.split(' ')
        name = tmp[0].split(':')[0]
        db_dict[name] = tmp[1:]
result = {}
for key, value in db_dict.items():
    result[key] = sum([int(itm.split('(')[0]) for itm in value if itm.split('(')[0].isdigit()])
print(result)
