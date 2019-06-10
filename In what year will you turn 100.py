import datetime

name = input('Enter your name ' )
age = int(input('Enter your age ' ))
now = datetime.datetime.now()
diff = 100 - age
print('Hi '+name+ ' you will complete 100 years in',(now.year+diff))