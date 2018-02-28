#如果一个字符串包含很多需要转义的字符，对每一个字符都进行转义会很麻烦。为了避免这种情况，我们可以在字符串前面加个前缀 r ，表示这是一个 raw 字符串
print(r'\(~_~)/ \(~_~)/')
#\(~_~)/ \(~_~)/

#但是r'...'表示法不能表示多行字符串，也不能表示包含'和 "的字符串
#如果要表示多行字符串，可以用'''...'''表示：
print('''Line 1
Line 2
Line 3''')
#Line 1
#Line 2
#Line 3

print('Line 1\nLine 2\nLine 3')
#Line 1
#Line 2
#Line 3

#还可以在多行字符串前面添加 r ，把这个多行字符串也变成一个raw字符串：
print(r'''Python is created by "Guido".
It is free and easy to learn.
Let's start learn Python in imooc!'''
)
#Python is created by "Guido".
#It is free and easy to learn.
#Let's start learn Python in imooc!

#以下两段效果一样
print('\"To be, or not to be\": that is the question.\nWhether it\'s nobler in the mind to suffer.')
print()
print(r'''"To be, or not to be": that is the question.
Whether it's nobler in the mind to suffer.''')
#"To be, or not to be": that is the question.
#Whether it's nobler in the mind to suffer.
#
#"To be, or not to be": that is the question.
#Whether it's nobler in the mind to suffer.
