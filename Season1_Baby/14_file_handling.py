#khái quát : đọc file, viết file, con trỏ file,....

#Khái quát về file: là một thứ quen thuộc có thể là văn bản, hình ảnh, video,...
#trong python có 2 kiểu: text và bin

    #Text File: Được cấu trúc mỗi các dòng bao gồm cá kí tự 
    # các file text file được ngăn cách bởi 1 kí tự newline ( \n) mặc định trong Python

    #Binary File: các file này chỉ có thể được xử lí bởi 1 ứng dụng có thể hiểu cấu trúc file này
    # chúng ta ở test ở mức độ cơ bản là xử lí text

#Cách mở file
# files = open('14filehandling.txt', 'r') 
# hoặc với các file khác tìm hiểu thêm help(open)
f = open('14filehandling.txt')
print(f)

# thay đổi đằng sau opp bằng r, r+, w, w+, a, a+
    # r để đọc đây là mode mặc định
    # r+ để đọc và ghi
    # w để ghi trước đó, nó sẽ xóa hết nội dung file hiện có, nếu fule không tồn tại nó sẽ tạo file mới 
    # w+ giống w, nhưng thêm là để ghi và để đọc
    # a mở để ghi, nếu file không tồn tại tạo file mới ( sẽ không xóa nội dung file cũ nên dùng)
    # a+ tương tự a thêm đọc

#Phương thức

#read
data = f.read() # tham số truyền vào để đọc đến đâu, lúc này con trỏ nằm cuối file
#close đóng file lại , đọc xong nên đóng file
#readline đọc hết file, đọc toàn bộ dòng, đưa text vào list với từng dòng

data = list(f) #đưa về hết dạng list giống realfile

#write trả về số thứ tự mà ta ghi vào
# data2 = f.write("đẹp như ai")
# #để write ta phải đổi mode
# f = open('14filehandling.txt', mode='w')
# print(data2) #trả về số

#kiểm soát con trỏ file
dat3 = f.seek(5) #dịch chuẩn con trỏ vị trí index5 trong chuỗi 

#with dùng để thực hiện khối lệnh xong và đóng 