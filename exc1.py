import logging

logging.basicConfig(filename="file1.log", format='%(asctime)s %(message)s', filemode='w')
LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)

def fact(n):
    
    total = 1
    LOGGER.debug(f'total={total}')
    for i in range(1,n+1):
        LOGGER.debug(f'i={i}')
        total*=i
        LOGGER.debug(f'total={total}')
    return total
print(fact(5))