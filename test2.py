
# #import cmath
# import math
# if 1!=2 : print("One equals one")
# else : print("One equals two")
# print(pow(2,3))
# #print(cmath.sqrt(-1))
# print((2+1j)*(9+4j))
# name = input ("what's your na12313me")
# print("hello "+name+"!")
#文件操作 先打开 然后写 再关闭
#如果不给详细路径 默认与py代码同一路径下 要是不是需要给详细路径
#详情见https://blog.csdn.net/weixin_52788247/article/details/119296570

# fpname = 'D:\\xinxin.txt'
# fp = open(fpname,'a')
# fp.write('i love xinxin')
# print('hello world'+fpname)
# print('hello world',fpname)
# fp.close

# name = 'Eric'
# print("Hello "+name+" , would you like to learn some Python today")
# print('Albert Einstein once said,"A person who never made a mistake never tried anything new."')
# name ='\nAlbert Einstein                '
# saying = '"A person who never made a mistake never tried anything new."'
# print(name + 'onces said, '+saying)
# print(name.lstrip() + 'onces said, '+saying)
# print(name.rstrip() + 'onces said, '+saying)
# print(name.strip() + 'onces said, '+saying)

name = []
test = ['eric','siri','maria','hello']
name.append("siri")
test.append('hery')
test.insert(2,'mike')
del test[1]
print(name,test)