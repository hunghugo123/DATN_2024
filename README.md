•	Thư mục cho giao diện frontend "datn-ailungx-frontend" bao gồm toàn bộ chương trình hệ thống Frontend của đề tài. Để chạy thử nghiệm chương trình Frontend, cần thực hiện các bước sau:
–	Cài đặt npm.
–	Gõ lệnh "npm install" để npm tiến hành cài đặt các gói thư viện cần thiết.
–	Chạy ứng dụng dưới chế độ phát triển bằng cách nhập "npm start" trên CMD.
–	Truy cập vào link "http://localhost:3000/" để sử dụng.
•	Thư mục cho máy chủ backend "datn-ailungx-backend": Chứa toàn bộ chương trình Backend của đề tài. Để chạy thử nghiệm chương trình Backend, cần thực hiện các bước sau:
–	Cài đặt npm.
–	Nhập lệnh "npm install" trên CMD để npm tiến hành cài đặt các gói thư viện cần
thiết.
–	Thêm tệp môi trường (.env) chứa các thông tin sau:
*	MONGODB_URL = Đường dẫn truy cập đến dự án MongoDB của bạn.
*	JWT_SKEY = Phần Signature của mã JWT được dùng để tạo Access Token (Nhập theo mong muốn).
*	JWT_REFRESH_KEY = Phần Signature của mã JWT được dùng để tạo Re-
fresh Token (Nhập theo mong muốn).
*	JWT_FP_KEY = Phần Signature của mã JWT được dùng để tạo đường dẫn xác thực cho việc đặt lại mật khẩu (Nhập theo mong muốn).
*	JWT_CR_KEY = Phần Signature của mã JWT được dùng để tạo đường dẫn
xác thực đăng ký tài khoản (Nhập theo mong muốn).
–	Thiết lập port trong tệp "index.js" và chạy ứng dụng bằng cách gõ lệnh trên CMD: "npm start".
–	Thực hiện các yêu cầu bằng việc gọi API từ link "http://localhost:port/".
•	Thư mục "datn-xray-model-api": Chứa toàn bộ chương trình Model API và mô hình dự đoán của đề tài. Để chạy thử nghiệm chương trình Model API, cần thực hiện các bước
sau:
–	Cài đặt python.
–	Cài đặt các thư viện.
–	Thiết lập port trong tệp "main.py" và chạy ứng dụng bằng cách nhập "python3 main.py" trên CMD.
–	Thực hiện các yêu cầu chẩn đoán bằng việc gọi API từ link "http://localhost:port/predict"
