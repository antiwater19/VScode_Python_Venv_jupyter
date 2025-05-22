from flask import *

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    uname = request.form['uname']
    pw = request.form['pass']
    # 회원디비 => id, pw 조건 검색하고 회원이 있다면 로그인, 없다면 에러
    if uname == 'king' and pw == '1111':
        return '환영합니다.'
    else:
        return '아이디혹은 비밀번호를 확인하세요.'
    
if __name__=='__main__':
    app.run(debug=True)