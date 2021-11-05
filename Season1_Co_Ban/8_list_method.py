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
