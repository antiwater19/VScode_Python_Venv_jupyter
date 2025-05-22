#import flask
#from flask import Flask

from flask import *


app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>루트페이지</h1>'

@app.route('/info')
def intro():
    return '<h2>TQQQ 뮤한 메슈~하면 다들 부자되게~?<br><br>ㅋㅋㅋㅋ 엌ㅋ 구라치지맠ㅋ<br>scott</h2>'

@app.route('/home/<name>') # /home/<name> => /home/홍길동
def home1(name):
    return 'hello~ ' + name

@app.route('/hello/<int:age>')
def hello(age):
    return str(age + 10)

def about():
    return '안녕하세요!!!'

app.add_url_rule('/about', 'about', about)
app.add_url_rule('/hi', 'about2', about)
app.add_url_rule('/bye', 'about3', about)

# /admin    /manger    /memeber
@app.route('/admin')
def admin():
    return '<h3>admin page</h3>'

@app.route('/manager')
def manager():
    return 'manager page'

@app.route('/member')
def member():
    return 'member page'

@app.route('/user/<name>')
def user(name): # /user/admin
    if name == 'admin':
        return redirect(url_for('admin'))
# 추가적인 조건을 추가할 수 있다.
    if name == 'manager':
        return redirect(url_for('manager'))

if __name__=='__main__': 
    app.run(debug=True)     