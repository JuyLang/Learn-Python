# tạo ra 1 biến có nhiều giá trị
# đây chính là array trong các lập trình khác
# giới hạn bởi cặp ngoặc vuông
# các thành phần của list đc cách nhau bởi dấu phẩy 
# List có khả năng chứa mọi giá trị đối tượng của python và chinhh nó

a = [1,8.878,'duy',True,]
print(type(a))
print(a)
#có thể chứa chính nó

v = [ [88, [2, [1,9],2], 'Duy'], 'Duy1', [[1,6,8],7] ]
print(v)
#list rỗng
rong = [] #rỗng không phải null
#list
f = [i for i in range(30)] #list comperhandsion
#hoặc f = [i for i in range(1,30,1)] 
print(f)
f1 = [ [n*1,n*2] for n in range(15)]
print(f1)

#Constructor list
c = list([1,2,3]) # iterrable gồm chuỗi là list
print(c)
c1 = list('LăngDuy') #sẽ chuyển chuỗi thành mảng
print(c1)

#một số toán tử list
# cộng +
k = [5,6]
k = k + ['one', 'six']
print(k)
    # list cộng list thì đc, chuỗi cộng list k đc
    # cùng kiểu dữ liệu mới dùng đc
# Không thể nhân 2 list với nhau, nhưng có thể nhân đê tăng
# in
lt1 = [1,5,5]
lt2 = 5 in lt1
print(lt2)