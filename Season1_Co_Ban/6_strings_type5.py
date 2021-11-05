#method
a = "Lang Khuong Duy ,yeu Ha Dung"
b = a.split(" ") # chia các phần tử bằng kí tự
# có thể thêm max with
c = a.split(" ", 3) # cắt bao nhiêu lần
#rsplit cắt từ bên phải qua
print(a)
print(b)
print(c)

d = a.partition('Duy') # trả về 3 phần từ, chuỗi trước chữ Duy
print(d)
cout = a.count('a') # đếm chữ a trong chuỗi
print(cout)
# có thể tìm trong khoảng
cou1 =  a.count('a',0,7)
print(cou1)

#startswith kiểm tra xem có bắt đầu bằng chữ h, hoặc kết thuc
f = a.startswith('h') 
print(f)
h = a.startswith(a[len(a)-2])
print(h)

#find tìm kiếm trong chuỗi và cho ra số
k = a.find('y')
 #nếu không ra thì ra -1
print(k)
#index tương tự, nhưng có ra lỗi

#islowser kiểm tra có phải chữ thường hay k
#isupper ngược lại
#isdigit kiểm tra có phải số hay không

l = '88a'
l1 = l.isdigit() # l = '88' True, 
                 # l1 = "88s" Flase
print(l)
print(l1)