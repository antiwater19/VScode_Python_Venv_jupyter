from flask import *
from deptdb import *

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)