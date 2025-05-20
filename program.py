# import mod1
# from mod1 import add, sub
from mod1 import *

# print(mod1.add(10, 3)) # import mod1
# print(mod1.sub(10, 3))

print(add(10, 3)) # from mod1 import add, sub
print(sub(10, 3))

print(PI)

c = Cal()
print(c.pow(2,3))

print('모듈이름 :', __name__)

if __name__ == '__main__':
    pass

# .py를 우리는 모듈이라 칭한다.
# 모듈 => 코드들을 파일단위로 관리하기 위한것
# 모듈을 사용하기 위해서는 import를 사용한다.
# 외부에서 부를 때는 mod1가 되고 내부에서 부를때는 __main__이  된다.

# 외부 모듈과 내부 모듈이 있다.
# 외부 모듈은 import를 통해서 사용하고
# 내부 모듈은 from을 통해서 사용한다.