#Module chỉ đơn giản là những file Python thôi và dĩ nhiên việc tạo file Python không còn gì xa lạ và khó khăn với chúng ta nữa. Bạn không cần phải có một dòng code đặc biệt trong một file Python để biến nó thành một module, chỉ đơn giản là một file Python bình thường như mọi khi bạn vẫn tạo, thậm chí file Python đó chẳng ghi bất cứ chữ nào thì vẫn là một module.
#Bản thân khi muốn sử dụng module thì ta sẽ lưu module đó vào một biến, biến đó thuộc lớp Module. Mà đã là biến, thì phải tuân theo những quy tắc đặt tên biến, và chỉ vậy thôi!
#Module của Python có thể không nhất thiết phải là file Python mà có thể là những file được viết bởi những ngôn ngữ lập trình khác như C, C++,… Ví dụ như (Java – Jython). Những module như vậy được gọi là extension module, và thường được sử dụng cho việc lưu các external library. Tuy nhiên phạm vi bài viết này sẽ không đề cập đến extension module, cho nên bạn không cần lo lắng nếu không hiểu những ngôn ngữ lập trình vừa mới đề cập ở trên.
#ví dụ tạo một module có tên duymodule.py
import duymodule
duymodule.printslepp('đây là demo test imprort module')

print(duymodule.Chuvi(78,66688))