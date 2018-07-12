# 我是注释：我是把数字拼接进字符串
x = "There aer %d types of people." % 10
# 赋值
binary = "binary"
# 赋值
do_not = "don't"
# 我是注释：我是把赋值拼接进字符串
y = "Those who know %s and those who %s."%(binary, do_not)

print(x)
print(y)
# 我是注释：字符串拼接字符串
print("i said: %r ." %x)
print("i also said: '%s'." %y)
# 字符串拼接字符串
hilarious = False
joke_evaluation = "isn't that joke so funny?! %r"

print(joke_evaluation % hilarious)
# 字符串拼接字符串
w = "66666"
e = "这是个毛啊"

print(w+e)