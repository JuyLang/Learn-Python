#định dạng chuỗi 
a = 'My name is %s'
print(a)
#ta có thể dùng như C,C++,Java để thêm giá trị vào, cú pháp

b = "Tôi là %s" %("Duy")
print(b)
c = 'Đây là ví dụ 2 hehe tôi yêu %s rất nhiều' %('hà')
print(c)
d = "đây là ví dụ 3 truyền vào nhiều : số 1 %s và số 2 %s"  %("Duy", "Gà")
print(d)

# %s giá trị của phương thức strings
# %r giá trị của phương thức repr
# %d giá trị số nguyên
# %f giá trị số thực


#
print(f'a\tb')

# nhưng nếu 
kteam = "keateam"
result = f"{kteam}- free education" #f là tìm kiếm biến tên kteam thay vào

print(result)

# rất tiện lợi, giống js là dấu %$

name = "duy"
old = '20'
girl_friend = "hà"

content = f"Ở đây có một bạn tên {name} năm nay {old} tuổi, có bạn gái tên {girl_friend}"
print(content)


#nêu muốn thêm dấu {} trong strings thì dùng 2 dấu {{}} hay dùng để clean code
content = f"Ở đây có một bạn tên {{name}} năm nay {old} tuổi, có bạn gái tên {girl_friend}"
print(content)

#định dạng bằng phương thức Format
formatt = 'a:{}, b:{}'.format(11,55)
print(formatt) #kiểu số cũng cho vào được

formatt2 = 'a:{0}, b:{2}, c:{1}'.format(11,55,398)
print(formatt2) #có thể thêm số để sắp xếp

#căn lề
    #CĂN TRÁI {:(c)<n}
    #CĂN Phải {:(c)>n}
    #CĂN Giữa {:(c)^n}
    #c chính là kí tự muốn để thay 
betwe = " {:?^50}".format("kteammm")
print(betwe)

light = '{:-<10}'.format(" lề trái")
print(light)
right = "{:*>10}".format("lề phải")
print(right)