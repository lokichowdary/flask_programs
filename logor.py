from flask import Flask
from operators1 import Cal_Cu
from exce import ValueToLarge, ValueToSmall, ZeroNotDivisible
import logging

logging.basicConfig(filename="loki.log", format='%(asctime)s %(message)s', filemode='w')
LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)
LOGGER.setLevel(logging.DEBUG)
LOGGER.setLevel(logging.ERROR)


app = Flask(__name__)

@app.route('/<name>/<int:a>/<int:b>')
def user_choice(name,a,b):
    obj1=Cal_Cu(a,b)

    if name == 'add':
        LOGGER.info('entered into the add')
        try:
            if a>=11 or b>=11:
                
                raise ValueToLarge("num should be less than 11")
            else:
                return str(obj1.add())
        except ValueToLarge as e:
            LOGGER.error(f'greater number error {a} and {b}',f'error is {e}')
            return str(e)

    
    if name == 'sub':
        try:
            if a<b:
                raise ValueToSmall("a value less than b")
            else:
                return str(obj1.sub())
        except ValueToSmall as s:
            return str(s)
        

    if name == 'mul':
        return str(obj1.mul())


    if name == 'div':
        try:
            if a==0 or b==0:
                raise ZeroNotDivisible('divisible by zero not possible')
            else:
                return str(obj1.div())
        except ZeroNotDivisible as d:
            return str(d)
                
           
    if name == 'mod':
        return str(obj1.mod())

if __name__ == '__main__':
    app.run(debug=True,port=5009)
