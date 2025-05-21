#import flask

from flask import Flask


app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/info')
def intro():
    return '반갑습니다. 저는 Scott 입니다.'

if __name__=='__main__':
    app.run(debug=True)