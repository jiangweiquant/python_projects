class Human:

    def __new__(cls,sex):##重载object内部自带的__new__,cls接收当前类
        # print(cls)
        if sex == '女':
            #生成对象并返回
            return object.__new__(cls)#上帝之手##供娱乐cls = 其他类狸猫换太子
        else:
            #不生成对象
            pass
    def __init__(self,name):
        print('初始化方法运行')
        self.name = name
    def eat(self):
        print('吃饭方法')
    def run(self):
        print('跑步方法')
    def sleep(self):
        print('睡觉方法')


one = Human('男') #实例化对象【1、创建一个对象（new） 2、为对象init操作（初始化对象）】
print(one)
# print(one.__dict__)