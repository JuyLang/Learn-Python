#print 
# có nhiều param 
# các param

#object: hiểu nôm nam là gom các argument tạo thành tuple

from time import perf_counter, sleep


print("kDUy")
print("Duy", "dfdsfds")
# ta có thể in ra bất kì bao nhiều param

# print("đâsdas"+ 89) # sẽ k đc
print("đaadasd" + str(89)) #sẽ đc

print("đấuúy"+"đâsd") #sẽ không có khoảng trắng
print("đấuúy","đâsd") #sẽ  có khoảng trắng

#sep là một khoảng trắng mặc địch, ta có thể thay seep

print("fasfasf", "fasfasfas","sadsadas", sep="-----")

#end kết thúc với nội dung gì, ta không muốn xuống dòng ( mặc thêm kí tự newline \n )
print('line 1 ')
print('line 2 ')
print('line 3 ')

print("a line witout newlien ", end=" ")
print("a line witout newlien222")

#ví dụ nghịch
# from time import sleep
# print("start...")
# sleep(3)
# print("end...")
#ví dụ 2

# print("start...", end="")
# sleep(3)
# print("end...")

# hoặc Flush là là thấy giá trị thì sẽ in ra

content = "Anh yêu em nhiều lắm Hà Dung ơi"
for x in content:
    print(x, end='', flush=True)
    sleep(0.1)
