# Requests module là một thư viện hỗ trợ chúng ta có thể gửi bất kỳ một loại request HTTP
#  nào một cách đơn giản nhất. 
# Và tác giả của module này chính là Kenneth Reitz tác giả của các module đơn giản mà 
# rất thần thánh trong giới Python :D.

#Mặc định thì thư viện này không được install kèm python nên các bạn muốn dùng thì cần phải tải nó. 
# Để install nó thì các bạn chỉ cần chạy lệnh. pip install requests

#Đầu tiên để có thể sử dụng được module này thì bạn cần phải import nó vào đầu chương trình.
import requests
# Tạo request.

# requests.method(url, params, data, json, headers, cookies, files, auth, timeout, allow_redirects, proxies, verify, stream, cert)
# # hoặc
# requests.Request(method, url, params, data, json, headers, cookies, files, auth, timeout, allow_redirects, proxies, verify, stream, cert)

# Trong đó:
# method sẽ là phương thức HTTP request mà bạn muốn tạo, các phương thức này có thể là: GET, POST,  PUT, PATCH, DELETE và OPTIONS.
# url là String chứa URL của trang web mà bạn muốn gửi request đến.
# data là một Dictionary hoặc list of tuples hoặc bytes và bạn muốn gửi kèm trong body của request. Tham số này có thể bỏ trống.
# json tương tự như data, nhưng kiểu dữ liệu là JSON serializable Python object. Tham số này có thể bỏ trống.
# headers là một Dictionary chứa các HTTP header mà bạn muốn gửi kèm request. Tham số này có thể bỏ trống.
# cookies là một Dictionary hoặc CookieJar Object chứa các cookie mà bạn muốn gửi kèm request. Tham số này có thể bỏ trống.
# files là một Dictionary chứa các files object (file object là result của hàm open()) mà bạn muốn gửi kèm request. Tham số này có thể bỏ trống.
# auth là một tuple chứa username, password của trang web mà bạn muốn gửi request đến nếu như trang web đó được bảo mật bởi Basic/Digest/Custom authentic. Tham số này có thể bỏ trống.
# timeout là một float hoặc tubple đơn vị tính bằng giây thiết lập request có thể chờ tối đa là bao nhiêu giây. Tham số này có thể bỏ trống.
# allow_redirects là một bool thiết lập xem request này có cho phép redirect không, mặc định thì giá trị này bằng True có nghĩa là cho phép. Tham số này có thể bỏ trống.
# proxies là một Dictionary chứa các protocol để ánh xạ đến proxy của URL. Tham số này có thể bỏ trống.
# verify  là một bool cấu hình xem có cho phép xác thực TLS hay không, mặc định là True. Tham số này có thể bỏ trống.
# stream là một bool cấu hình xem dữ liệu trả về có Stream hay không. Tham số này có thể bỏ trống.
# cert là một String chứa đường dẫn đến ssl client file (.pem). Tham số này có thể bỏ trống.
#  Phương thức này sẽ trả về một Response Object.


# VD:

# Gửi một get request đến Toidicode.com:
import requests

requests.get("https://toidicode.com/")

# https://toidicode.com/

#Gửi một GET request kèm param:

requests.get("https://toidicode.com/", params= {"post_id": 135})
# hoặc
requests.get("https://toidicode.com/?post_id=135")

#Gửi một POST data request kèm se timeout là 3s:

requests.post("https://toidicode.com/", data={"post_id": 135}, timeout=3)

#Tạo một POST request upload file lên server:

requests.post("https://toidicode.com/", files={'image': open('images/logo.png')})

#Dữ liệu trả về - Response
    # apparent_encoding	Thuộc tính	String	 Trả về kiểu mã hóa của dữ liệu trả về
    # close()	Phương thức	None	Đóng connection
    # content	Thuộc tính	String	Dữ liệu server trả về
    # cookies	Thuộc tính	CookieJar hoặc None	Cookies của request server trả về
    # elapsed	Thuộc tính	None hoặc timedelta	Thời gian thực thi request
    # encoding	Thuộc tính	None hoặc String	Kiểu mã hóa dữ liệu khi truy cập thuộc tính text
    # headers	Thuộc tính	None hoặc Dictionary	Header server trả về
    # history	Thuộc tính	None hoặc list	Các request đã thực thi khi thực thi request.
    # is_permanent_redirect	Thuộc tính	bool	Trả về True nếu request có redirect
    # is_redirect	Thuộc tính	bool	Trả về True nếu request có redirect bằng HTTP code
    # iter_content(chunk_size=1, decode_unicode=False)	Phương thức	Object	Lặp lại dữ liệu trả về khi Request set strame=True
    # iter_lines(chunk_size=512, decode_unicode=None, delimiter=None)	Phương thức	Object	Tương tự phương thức iter_content() nhưng sẽ lặp lại theo dòng
    # json(**kwargs)	Phương thức	Json	Chuyển đổi dữ liệu trả về thành Json, nếu có
    # links	Phương thức	Dictionary	Trả về list Header links của response đã được xử lý
    # next	Thuộc tính	PreparedRequest	Trả về PreparedRequest cho request tiếp theo
    # ok	Thuộc tính	bool	Trả về True nếu HTTP STATUS trả về là nhỏ hơn 400 ngược lại là False
    # raise_for_status()	Phương thức	None hoặc HTTPError	Raises HTTPError nếu có 1 điều đó xảy ra
    # reason	Thuộc tính	None hoặc String	Trả về lí do HTTP trạng thái được trả về.
    # request	Thuộc tính	None hoặc PreparedRequest	Xem chi tiết tại đây
    # status_code	Thuộc tính	None hoặc String	HTTP Status mà server trả về
    # text	Thuộc tính	String	Nội dung của request trả về.
    # url	Thuộc tính	None hoặc String	URL cuối cùng sau khi thực thi request.


#vd:

r = requests.get("http://ip-api.com/json")

#request: https://toidicode.com/?post_id=135

print(r.apparent_encoding)
# print(r.content)
print(r.encoding)
print(r.cookies)
print(r.elapsed)
print(r.encoding)
print(r.headers)
print(r.history)
print(r.is_permanent_redirect)
print(r.iter_content())
print(r.links)
print(r.raise_for_status())
print(r.json())