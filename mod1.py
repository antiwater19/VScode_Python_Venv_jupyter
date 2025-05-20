# 더하기함수, 빼기 함수

print('모듈이름 :', __name__)

def add(n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

PI = 3.14

class Cal:
    def pow(self, a, b):
        return a**b
    
# 테스트
if __name__ == '__main__':
    print(add(10, 30))
    print(add(100, 30))
