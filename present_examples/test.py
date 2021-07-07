import time
from data import RESPONSES as responses

def single_function(name, delay):
    time.sleep(delay)

for item in responses:
    single_function(item[0], item[1])
    
