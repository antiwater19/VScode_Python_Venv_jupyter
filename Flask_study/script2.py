from flask import *
from deptdb import *

app = Flask(__name__)
# session 사용시에 필수 변수 이거 없으면 에러가 무조건 발생함.
app.secret_key='admin'

depts = DeptDAO()

students = [
    {'name': '손흥민', 'age':30},
    {'name': '김민재', 'age':25},
    {'name': '이강인', 'age':20}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome/<name>')
def welcome(name):
    return render_template('welcome.html', uname=name)

@app.route('/students')
def s_list():
    return render_template('student.html', data=students)

@app.route('/depts')
def dept_list():
    depts = DeptDAO().get_depts()
    return render_template('depts.html', dept_list=depts)

@app.route('/cookie') # 쿠키를 설정하는 페이지
def cookie():
    res = make_response('<h1>Cookie Set</h1> <a href=\"/cookie/view\">cookie view</a>')
    res.set_cookie('uid', 'cool')
    return res

@app.route('/cookie/view') # 쿠키를 읽어오는 페이지
def cookie_view():
    cookie_data = request.cookies.get('uid')
    return cookie_data

# get /login => 로그인 폼
# post /login => 로그인 처리  
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login/login_form.html') # /templates/login/login_form.html
    elif request.method == 'POST':
        # session 이용 사용자 데이터 저장
        session['login_info']=request.form['email']
        return redirect(url_for('profile'))
    else:
        return redirect(url_for('home'))
    
@app.route('/profile')
def profile():
    # 로그인 상태 체크
    if 'login_info' in session:
        # 로그인 상태
        email = session['login_info']
        return render_template('login/profile.html', name=email)
    else:
        return '로그인이 필요한 페이지 입니다.'

if __name__ == '__main__':
    app.run(debug=True)