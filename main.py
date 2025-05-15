from datetime import *
count = 0
data = datetime(year=2015, month=1, day=1)
for i in range (1,13):
    data = data.replace(month = i)
    print(data)
    a = datetime.weekday(data)
    if a == 0:
        count += 1    
data = data.replace(year=2016, month= 1)
for i in range (1,13):
    data = data.replace(month = i)
    print(data)
    a = datetime.weekday(data)
    if a == 0:
        count += 1    
print(count)