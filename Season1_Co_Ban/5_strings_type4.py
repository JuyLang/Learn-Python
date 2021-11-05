a = '13'
print(int(a))
print(type(a))

#method chuỗi
b = "duy"
b1 = b.capitalize() #viết hoa chữ cái đầu . Viết bằng cách chuyển sang ACSCI rồi trừ 62
print(b)
print(b1)
print(b.upper()) #viết hoa hết
print(b.lower()) #viết thường hết
print(b.swapcase()) # chữ viết thường thành hoa, hao thành thường

print(b.title())
print(b1.center(15, "+")) # dùng để trả về khoảng trắng hoặc kí tự. Chừa 30 ô
print(b1.rjust(10,"+")) # căn phải ,trái ngược lại

c = "duy"
d = c.encode(encoding='utf-8', errors='strict') #mã hóa 
print(c)
print(d)
e = "có gì hot"
f = e.encode() #ta có thể thay đổi, nếu để không thì ra 
print(f)
print(f.decode())

#join
g = c.join(["1", '8', "9"])
print(g)#cộng 1 danh sách vào chuỗi

#replace thay cái gì bằng cái gì
#strip cắt khoảng trắng 2 đầu, hoặc kí tự giống nhau 2 đầu
