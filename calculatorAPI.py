from flask import Flask, request
app = Flask(__name__)
@app.route('/')
def index():
    return 'Welcome to my calculator'
def add2num(x, y):
    return (x + y)

def mult2num(x, y):
    return x * y

def sub2num(x, y):
    return x - y

def div2num(x, y):
    return x / y


@app.route('/add')
def add():
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))
    return str(add2num(x,y))


@app.route('/subtract')
def sub():
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))
    return str(sub2num(x,y))


@app.route('/division')
def div():
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))
    return str(div2num(x,y))


@app.route('/multiplication')
def mult():
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))
    return str(mult2num(x,y))

@app.route('/math')
def math():
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))
    num1 = add2num(x,y)
    num2 = mult2num(x,num1)
    num3 = sub2num(num2,y)
    num4 = div2num(num3,x)
    return str(num4)








app.run(host='0.0.0.0', port=93)