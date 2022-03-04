#Các method 
a = [1,3,4,5,6,8,9,11,13]
# print(a)
# c = a.count(3) #giống như chuỗi, kiểm tra số lần suất hiện của 1
# print(c)

#index Như chuỗi,vị trí nằm trong list
#coppy trả về 1 list tương tự, lúc này sẽ k trỏ cùng 
c = a.copy()
c[0]  = 0 
print(c)
print(a)
#clear xóa hết list trở thành rỗng
#append thêm vào trong list một cục bị phân
#extend thêm phần tử mở rộng
#insert thêm phần tử x(index) trong list[x]
a1 = [1,2,3,4,5]
a1.insert(1,'duy')
print(a1)
#pop bỏ đi phần tử thứ y(index) và trả về
#sort đảo ngược
b = ["\x34\x77"
,"\x64\x7D","\x67\x7B","\x6A","\x7D","\x31\x67","\x77\x30","\x72","\x61\x6C","\x73","\x68\x37","\x61\x67\x7B","\x66\x6C","\x6D\x33\x74","\x76\x61\x6C\x75\x65","\x70\x77\x64","\x67\x65\x74\x45\x6C\x65\x6D\x65\x6E\x74\x42\x79\x49\x64","\x59\x65\x70\x2C\x20\x74\x68\x61\x74\x27\x73\x20\x74\x68\x65\x20\x66\x6C\x61\x67\x21","\x53\x6F\x72\x72\x79\x2C\x20\x74\x68\x61\x74\x27\x73\x20\x6E\x6F\x74\x20\x74\x68\x65\x20\x66\x6C\x61\x67\x21"]
​