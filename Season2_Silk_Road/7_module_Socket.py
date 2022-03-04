# Python là một ngôn ngữ có khả năng cung cấp cho chúng ta
#  làm việc ở 2 cấp độ truy cập của dịch vụ mạng (network service). Ở tầng thấp thì chúng ta có thể cho phép các socket hỗ trợ cơ bản đến các hệ điều hành, từ đó bạn có thể triển khai các kết nối giữa client với server. Và bài này chúng ta sẽ cùng nhau nghiên cứu về lập trình mạng với module socket trong Python.


#1, Socket là gì?
# Socket là các endpoint của một kênh giao tiếp hai chiều. 
# Nó sử dụng để kết nối với một chương trình khác chạy trên một máy tính khác trên Internet.
#  Một chương trình mạng có thể sử dụng nhiều socket cùng một lúc, 
# nhờ đó nhiều chương trình có thể sử dụng Internet cùng một lúc

#Thường thì người ta sẽ chia socket ra làm hai loại chính là:

# Stream Socket: Dựa trên giao thức TCP việc truyền dữ liệu chỉ thực hiện giữa 2 quá trình đã thiết lập kết nối.
#  Giao thức này đảm bảo dữ liệu được truyền đến nơi nhận một cách đáng tin cậy, 
# đúng thứ tự nhờ vào cơ chế quản lý luồng lưu thông trên mạng và cơ chế chống tắc nghẽn.
 

# +Datagram Socket: Dựa trên giao thức UDP việc truyền dữ liệu không yêu cầu có sự thiết lập kết nối giữa 2 quá trình. 
# Ngược lại với giao thức TCP thì dữ liệu được truyền theo giao thức UDP không được tin cậy, có thế không đúng trình tự và lặp lại.
#  Tuy nhiên vì nó không yêu cầu thiết lập kết nối và không có những cơ chế phức tạp nên tốc độ nhanh…ứng dụng cho các ứng dụng truyền dữ liệu nhanh như các ứng dụng chat, game…


#2, Module socket trong Python.

#Module socket trong Python sẽ giúp chúng ta thực hiện các kết nối client server. 
# để giao tiếp giữa các máy với nhau. Và để có thể sử dụng được nó thì
#  đầu tiên chúng ta cần phải import module socket vào chương trình với cú pháp sau:
import socket

#Tiếp theo chúng ta sẽ khởi tao đối tượng socket trong module này với cú pháp như sau
# socket.socket(AddressFamily, socketType, Protocol)
#Trong đó:
#AddressFamily là cách chúng ta thiết lập địa chỉ kết nối. Trong Python thì hỗ trợ chúng ta 3 kiểu.
    # AF_INET kiểu này là thiết lập dưới dạng ipv4.
    # AF_INET6 kiểu này là thiết lập dưới dạng ipv6.
    # AF_UNIX
#SocketType là cách thiết lập giao thức cho socket. Thông thường thì sẽ là SOCK_STREAM (TCP) hoặc SOCK_DGRAM (UDP).

#Protocol tham số thiết lập loại giao thức, Tham số này có thể không cần thiết lập. Mặc định sẽ bằng 0.

#một số phương thức
# bind(address, port)	Phương thức này được dùng để lắng nghe đến địa chỉ address và port
# listen(backlog)	Phương thức này thiết lập mở kết nối trên server, với tham số truyền vào là số kết nối được phép (nhỏ nhất là 0 và lớn nhất là do cấu hình của server).
# accept()	Phương thức này thiết lập chấp nhận một kết nối, và nó sẽ trả về một tuple gồm 2 thông số (conn, address) để chúng ta có thể gửi ngược về client.
# connect(address)	Phương thức này thiết lập một kết nối từ client đến server.
# recv(bufsize, flag)	Phương thức này dùng để nhận dữ liệu qua giao thức TCP.
# send(byte,flag)	Phương thức này gửi dữ liệu thông qua giao thức TCP.
# recvfrom(bufsize, flag)	Phương thức này dùng để nhận dữ liệu qua giao thức UCP
# sendto(bytes, address)	Phương thức này dùng để gửi dữ liệu qua giao thức UCP.
# close()	Phương thức này dùng để đóng một kết nối.

# 3, Ví Dụ.

# Code server server.py: 
# HOST = 'localhost' # Thiết lập địa chỉ address
# PORT = 8000 # Thiết lập post lắng nghe
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # cấu hình kết nối
# s.bind((HOST, PORT)) # lắng nghe
# s.listen(1) # thiết lập tối ta 1 kết nối đồng thời
# conn, addr = s.accept() # chấp nhận kết nối và trả về thông số
# with conn:
#     try:
#         # in ra thông địa chỉ của client
#         print('Connected by', addr)
#         while True:
#             # Đọc nội dung client gửi đến
#             data = conn.recv(1024)
#             # In ra Nội dung 
#             print(data)
#             # Và gửi nội dung về máy khách
#             conn.sendall(b'Hello client')
#             if not data: # nếu không còn data thì dừng đọc
#                 break
#     finally:
#         s.close() # đóng socket

import socket
#client.py:
HOST = '103.28.172.12'    # Cấu hình address server
PORT = 1111             # Cấu hình Port sử dụng
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cấu hình socket
s.connect((HOST, PORT)) # tiến hành kết nối đến server
# s.sendall(b'Hello server!') # Gửi dữ liệu lên server 
data = s.recv(1024) # Đọc dữ liệu server trả về
print('Server Respone: ', repr(data))