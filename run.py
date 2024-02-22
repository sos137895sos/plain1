from flask import Flask,request

app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/a', methods=['*'])
def add():
    data = request.form.get('data')

if __name__ == '__main__':
    app.run(port=5001,host='0.0.0.0')

