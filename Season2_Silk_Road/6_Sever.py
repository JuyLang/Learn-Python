#Đầu tiên để có thể khởi tạo được một con server thì bạn cần 
# import module htttp.server của Python vào trong chương trình:
from http.server import BaseHTTPRequestHandler

#Và ở đây chúng ta cần sử dụng đến 2 object BaseHTTPRequestHandler, HTTPServer trong module http.server.
#Tiếp đó chúng ta sẽ khai báo một class kế thừa từ class BaseHTTPRequestHandler của Python. 
# Và khai báo thêm một phương thức do_GET() để xử lý khi có get Request gửi lên.
from http.server import BaseHTTPRequestHandler, HTTPServer
 
# HTTPRequestHandler class
class SimpleHTTP(BaseHTTPRequestHandler):
 
  # Nhận GET request gửi lên.
  def do_GET(self):
        # SET http status trả về
        self.send_response(200)
 
        # Thiết lập header trả về
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Data
        message = "Xin chao"
        # Write data dưới dạng utf8
        self.wfile.write(bytes(message, "utf8"))
        return
# Ngoài ra thì trong lớp BaseHTTPRequestHandler còn hỗ trợ chúng ta một số các thuộc tính và phương thức như sau:
# server_version	Trả về version của server.
# do_HEAD()	Phương thức này cấu hình thông số head trả về.
# do_GET()	Phương thức xử lý khi có GET request gửi lên.
# do_POST()	Phương thức xử lý khi có POST request gửi lên.
# client_address	Thuộc tính này trả về tuple chứa host và port của server đang chạy.
# command	Thuộc tính này trả về kiểu của request gửi lên.
# path	Thuộc tính này trả về path của request gửi lên.
# request_version	Thuộc tính này trả về version của request hiện tại.
# headers	Thuộc tính này trả về tất tất cả những gì mà request gửi lên.

#Sau khi đã cấu hình xong thông số và các hành động xử lý. Giờ chúng ta sẽ sử dụng đến đối tượng HTTPServer để khởi chạy server.
# cấu hình host và cổng port cho server
server_address = ('127.0.0.1', 8000)

# Khởi tạo server với thông số cấu hình ở trên.
httpd = HTTPServer(server_address, SimpleHTTP)

# Tiến hành chạy server
httpd.serve_forever()



