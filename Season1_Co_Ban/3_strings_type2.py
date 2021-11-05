#Chuỗi trần 
print("Haizzz, \neu một này nào đó")

# ví dụ khi ra sử dụng để mở file có dạng \\ nhiều
# khi đó ta sinh ra chuỗi trần, lúc này sẽ không bị Escape Sequenc
print(r"Haizzz, \neu một này nào đó") #thường xuyên khi ta hay sử dụng 
print("\n8") #
 
#toán tử trong strings

# Toán tử +
str1 = "Xin Chào"
str2 = "Khương Duy"
str3 = str1 +str2
print(str3)

#toán tử * : dùng để nhân số chuỗi lên
str4 = "Duy LK"
str5 = str4 * 5
print(str5)

#toán tử in : Chỉ có thể 1 trong 2 : true hoặc flase. Kiểm tra xem 1 chuỗi có nằm trong chuỗi khác không
str6 = "xin chào Duy"
str7 = "D"
str9 = str7 in str6 #kiểm tra 6 có nằm trong 7 không. Đúng in true
print(str9)

str8 = "helocp"
#đánh số từ 0 = h, 1 = e. dấu trừ đề đi ngược
print(str8[5])
print(str8[-1])
print(str8[len(str8)-1]) #len là lấy ra độ dài chuỗi

#cắt chuỗi
str10 = str8[1:len(str8)] #cắt từ vị trí số 1 đi
print(str10)
str11 = str8[None:len(str8)] # cắt từ đầu, coi như coppy
print(str11)
str12 = str8[None:None]
print(str12)

# cắt từ trái quá phải rồi, giờ ta căt từ phải sang trái
str13 = str8[None:3:-1] #cắt từ cuỗi đi, với bước nhảy là -1, đến 3
print(str13)

#cách đổi từ chuỗi sang số, và ngược lại
# str15 = '69'+5 #sẽ không được
str15 = int('69') +5
print(str15)

str16 = float("68898.5") + 8.878
print(str16)

#từ số thành chuỗi
int17 = 7 + 99
print(int17) # Sẽ in ra số
str17 = str(7) + '99'
print(str17)

#Python không đc viết
str18 = "xinchaoduy"
# muốn thay đổi chữ o thành số 0
# str18[1] = '0' # sẽ không được

str18 = str18[None:5]+'0'+str18[6:None]
print(str18)
#vì chuỗi là 1 hash có thể băm ra
print(hash(str17)) #sẽ thay đổi khi ta tạo ra(chạy)
