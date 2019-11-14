import time
import logging
from threading import Thread


logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w')
logger = logging.getLogger('logger')

COUNT = 50000000

def countdown(n):
    while n>0:
        n-=1

t1 = Thread(target=countdown, args=(COUNT//2,)) 
t2 = Thread(target=countdown, args=(COUNT//2,)) 
logger.info('threads created')

start = time.time()

t1.start()
logger.info('thread 1 start')
t2.start()
logger.info('thread 2 start')
t1.join()
logger.info('thread 1 join')
t2.join()
logger.info('thread 2 join')
end = time.time()

print('time - ', end-start)
logger.info('time - '+ str(end-start))