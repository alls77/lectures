import requests
import time
import logging
from threading import Thread

def resp(string):
    return requests.get(string).content


logging.basicConfig(level=logging.DEBUG, filename='app_request_threads.log', filemode='w')
logger = logging.getLogger('logger')


t1 = Thread(target=resp, args=('http://api.dataatwork.org/v1/jobs/autocomplete?contains=%22software%22',))
t2 = Thread(target=resp, args=('http://api.dataatwork.org/v1/jobs/autocomplete?begins_with=%22software%22',)) 
t3 = Thread(target=resp, args=('http://api.dataatwork.org/v1/jobs/autocomplete?begins_with=%22engineer%22',)) 
logger.info('threads created')

start = time.time()

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()

end = time.time()

logger.info('time - '+ str(end - start))
print('time - '+ str(end - start))