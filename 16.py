class SchoolMember:
    ''' 代表任何学校里的成员 '''
    def _init_(self, name, age):
        self.name = name
        self.age = age
        print('(Intialized SchoolMember: {}.format(self.name)')

    def tell(self):
        '''告诉我等等的细节'''
        print('Name:"{}" Age:"{}"'.format(self.name))

class Teacher(SchoolMember):
    '''代表一位老师'''
    def _init_(self, name, age, salary):
        SchoolMember._init_(self, name, age)
        self.salary = salary
        print('(iInitialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
    '''代表一位学生'''
    def _init_(self, name, age):
        self.marks = marks
        print('marks:"{:d}"'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('marks: "{:d}"'.format(self.marks))

t = Teacher('Mrs.Shividya',40,30000)
s = Student('Swaroop',25,75)

print()#打印一行空白行

members = [t, s]
for menber in members:
    #d对全体师生工作
    member.tell()




emp1.age = 7  # 添加一个 'age' 属性
emp1.age = 8  # 修改 'age' 属性
del emp1.age  # 删除 'age' 属性
#getattr(obj, name[, default]) : 访问对象的属性。
#hasattr(obj,name) : 检查是否存在一个属性。
#setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
#delattr(obj, name) : 删除属性。
hasattr(emp1, 'age')    # 如果存在 'age' 属性返回 True。
getattr(emp1, 'age')    # 返回 'age' 属性的值
setattr(emp1, 'age', 8) # 添加属性 'age' 值为 8
delattr(emp1, 'age')    # 删除属性 'age'
__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
__doc__ :类的文档字符串
__name__: 类名
__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）

class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print
        "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print
        "Name : ", self.name, ", Salary: ", self.salary


print
"Employee.__doc__:", Employee.__doc__
print
"Employee.__name__:", Employee.__name__
print
"Employee.__module__:", Employee.__module__
print
"Employee.__bases__:", Employee.__bases__
print
"Employee.__dict__:", Employee.__dict__


class Parent:  # 定义父类
    parentAttr = 100

    def __init__(self):
        print
        "调用父类构造函数"

    def parentMethod(self):
        print
        '调用父类方法'

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print
        "父类属性 :", Parent.parentAttr


class Child(Parent):  # 定义子类
    def __init__(self):
        print
        "调用子类构造方法"

    def childMethod(self):
        print
        '调用子类方法'


c = Child()  # 实例化子类
c.childMethod()  # 调用子类的方法
c.parentMethod()  # 调用父类方法
c.setAttr(200)  # 再次调用父类的方法 - 设置属性值
c.getAttr()  # 再次调用父类的方法 - 获取属性值



