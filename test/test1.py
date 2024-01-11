def fun1(list):
    print("f")
def fun2(list):
    print("s")
def fun3(list):
    print("t")
list = [fun1,fun2,fun3]
for i in list:
    i("asdf")