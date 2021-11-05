# được giới hạn bởi cặp ngoặc ()
# các thành phần của tuple 
# phân cách nhau bởi dấu ,
# tuple chứa khả năng chứa mọi giá trị
 # tốc độ truy xuất nhanh hơn list
 # dung lượng chiếm trong bộ nhớ nhỏ hơn
# bảo vệ dữ liệu của bạn khoogn bị thay đổi
# có thể dùng làm key của dictionary

tup = (1,2.8787,-3,"duy","hai",(8,6),78,5)
print(tup)
tup1 = (1) # sẽ trở thành biến int bình thường
print(type(tup1))
#không thể tạo như arr
# tup2 = (i for i in range(30))
# print(tup2) 

tup3 = tuple()
print(tup3)