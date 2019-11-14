import logging

logging.basicConfig(level=logging.DEBUG, filename='app.log')

a = 1
b = 1
print(a==b)
print(a is b)
print(id(a), ' ', id(b))


import time

COUNT = 50000000

def countdown(n):
    while n>0:
        n-=1

start = time.time()
countdown(COUNT)
end = time.time()

print('time - ', end-start)