# Project-1-Handwritten-digit-recognition
Nhận diện số viết tay (chữ nếu có thể), ứng dụng vào bài toán nhận diện điểm số của bài kiểm tra

Project hoạt động trên python 3.7.0 và opencv 3.4.3
+ Cài đặt python: https://www.python.org/downloads/
+ Cài dặt opencv cho python: python -m pip install opencv-python (xem chi tiết https://www.scivision.co/install-opencv-python-windows/)
+ Cài numpy cho python: pip install numpy

Bản beta: Đã giải quyết xong việc tự động tìm và cắt khung điểm để chuẩn bị cho việc nhận dạng
HƯỚNG DẪN SỬ DỤNG BẢN BETA:
+ clone repository về máy (đã cài đặt python và các thư viện nêu trên)
+ mở cmd or terminal, di chuyển vào trong thư mục chứa repository vừa clone về và nhập lệnh: 
    python main.py -q <tên ảnh đầu vào cần lấy khung điểm (nếu không cùng thư mục với project thì phải thêm đường dẫn)>
    VD: python main.py -q test.jpg
+ Khung điểm sẽ được cắt ra và trả về trong cùng thư mục
