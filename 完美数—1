#判断一个数是否是完全数
#完全数是指一个数的各个因数之和等于这个数本身
#输入一个要判断的数
theNumber = input("请输入一个整数：")
theNumber = int(theNumber)
#初始化和为0
sum = 0
#枚举1到theNumber/2之间的数
#i=1是循环的起点
i = 1
#寻找theNumber的因数并求和
while i <= theNumber/2:
    if theNumber % i == 0:
        sum += i
    i = i + 1
#判断输入的数是否是完全数
if sum == theNumber:
    print(theNumber, "是完全数")
else:
    print(theNumber, "不是完全数")
