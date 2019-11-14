import time
import logging
from multiprocessing import Pool

logging.basicConfig(level=logging.DEBUG, filename='app_proc.log', filemode='w')
logger = logging.getLogger('logger')

COUNT = 50000000

def countdown(n):
    while n>0:
        n-=1

pool = Pool(processes=2)
logger.info('pool created')

start = time.time()
r1 = pool.apply_async(countdown,[COUNT//2])
logger.info('process 1 start')
r2 = pool.apply_async(countdown,[COUNT//2])
logger.info('process 2 start')
pool.close()
logger.info('pool closed')
pool.join()
logger.info('pool join')
end = time.time()

print('time - ', end-start)
logger.info('time - '+ str(end-start))