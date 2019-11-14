import requests
import time
import logging
from multiprocessing import Pool

logging.basicConfig(level=logging.DEBUG, filename='app_request.log', filemode='w')
logger = logging.getLogger('logger')

pool = Pool(processes=3)
logger.info('pool created')

resp1 = requests.get('http://api.dataatwork.org/v1/jobs/autocomplete?contains=%22software%22')
resp2 = requests.get('http://api.dataatwork.org/v1/jobs/autocomplete?begins_with=%22software%22')
resp3 = requests.get('http://api.dataatwork.org/v1/jobs/autocomplete?begins_with=%22engineer%22')

start = time.time()

r1 = pool.apply_async(resp1)
logger.info(resp1.content)
r2 = pool.apply_async(resp2)
logger.info(resp2.content)
r3 = pool.apply_async(resp3)
logger.info(resp3.content)

pool.close()
logger.info('pool closed')
pool.join()
logger.info('pool join')
end = time.time()

logger.info('time - '+ str(end - start))
print('time - '+ str(end - start))
