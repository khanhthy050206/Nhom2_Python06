# BẢNG PHÂN CÔNG NHIỆM VỤ NHÓM

**Đề tài:** HỆ THỐNG QUẢN LÝ ĐẶT BÀN NHÀ HÀNG

**Học phần:** Lập trình Python 

**Nhóm:** 2

**Thành viên 1:** Lê Khánh Thy

**MSSV:** 2044240353

**Thành viên 2:** Phan Thị Cẩm Nhung

**MSSV:** 2044240249

## I. MỤC TIÊU ĐỀ TÀI

Xây dựng chương trình quản lý đặt bàn nhà hàng bằng ngôn ngữ Python, áp dụng kiến thức lập trình cơ bản. Chương trình hỗ trợ quản lý thông tin bàn ăn, tiếp nhận yêu cầu đặt bàn, kiểm tra sức chứa, tìm kiếm và hủy đặt bàn, đồng thời thống kê thông tin cơ bản.

Đề tài hướng đến việc vận dụng các kiến thức về kiểu dữ liệu, câu lệnh điều kiện, vòng lặp, hàm, danh sách, lớp, đối tượng, thuộc tính và phương thức.

## II. PHÂN CÔNG NHIỆM VỤ CỤ THỂ

### 1. Thành viên 1: Xây dựng các lớp dữ liệu

**File phụ trách:** `ban_an.py`, `dat_ban.py`

**1.1. Phân tích và thiết kế dữ liệu**

- Xác định các thông tin cần quản lý của bàn ăn: mã bàn, sức chứa và trạng thái.
- Xác định các thông tin của lượt đặt bàn: mã đặt bàn, tên khách hàng, số điện thoại, ngày giờ đặt, số người, mã bàn và trạng thái đặt.
- Thống nhất tên thuộc tính và phương thức với Thành viên 2 để các file có thể kết nối với nhau.

**1.2. Lập trình file `ban_an.py`**

- Xây dựng lớp `BanAn` để lưu trữ thông tin bàn ăn.
- Xây dựng phương thức khởi tạo `__init__()` để gán mã bàn, sức chứa và trạng thái ban đầu.
- Kiểm tra mã bàn không được để trống.
- Kiểm tra sức chứa phải là số nguyên dương.
- Xây dựng phương thức `hien_thi()` để hiển thị thông tin bàn.
- Xây dựng phương thức `__str__()` để hỗ trợ in thông tin đối tượng dễ đọc.

**1.3. Lập trình file `dat_ban.py`**

- Xây dựng lớp `DatBan` để lưu thông tin đặt bàn.
- Xây dựng phương thức `__init__()` để khởi tạo các thuộc tính của lượt đặt bàn.
- Kiểm tra tên khách hàng, số điện thoại và ngày giờ đặt bàn không được để trống.
- Kiểm tra số người đặt bàn phải là số nguyên dương.
- Thiết lập trạng thái mặc định của lượt đặt bàn là “Đang đặt”.
- Xây dựng phương thức `hien_thi()` để hiển thị đầy đủ thông tin đặt bàn.
- Xây dựng phương thức `__str__()` để trình bày thông tin đối tượng.

**1.4. Kiểm thử và hoàn thiện**

- Kiểm tra trường hợp mã bàn bị bỏ trống.
- Kiểm tra sức chứa bằng 0 hoặc là số âm.
- Kiểm tra trường hợp thiếu thông tin khách hàng.
- Kiểm tra số người đặt bàn không hợp lệ.
- Đảm bảo hai lớp hoạt động đúng và có thể được sử dụng trong file quản lý nhà hàng.

**Sản phẩm bàn giao:** `ban_an.py` và `dat_ban.py`.

**Nội dung trình bày:** Giới thiệu lớp `BanAn`, lớp `DatBan`, thuộc tính, phương thức, hàm khởi tạo và cách kiểm tra dữ liệu đầu vào.

### 2. Thành viên 2: Xây dựng chức năng quản lý và chương trình chính

**File phụ trách:** `quan_ly_nha_hang.py`, `main.py`

**2.1. Phân tích quy trình hoạt động**

- Xác định các chức năng chính của chương trình.
- Thiết kế quy trình thêm bàn, đặt bàn, tìm kiếm, hủy đặt bàn và thống kê.
- Thống nhất cách sử dụng các lớp `BanAn` và `DatBan` với Thành viên 1.

**2.2. Lập trình file `quan_ly_nha_hang.py`**

- Xây dựng lớp `QuanLyNhaHang` để quản lý danh sách bàn ăn và danh sách đặt bàn.
- Xây dựng phương thức `them_ban()` để thêm bàn mới và kiểm tra mã bàn trùng lặp.
- Xây dựng phương thức `lay_ban()` để tìm bàn theo mã bàn.
- Xây dựng phương thức `dat_ban()` để tiếp nhận yêu cầu đặt bàn.
- Kiểm tra bàn có tồn tại hay không.
- Kiểm tra số người đặt không vượt quá sức chứa của bàn.
- Ngăn việc đặt trùng cùng một bàn vào cùng ngày và giờ khi lượt đặt trước vẫn còn hiệu lực.
- Xây dựng phương thức `huy_dat_ban()` để hủy lượt đặt bàn.
- Xây dựng phương thức `tim_theo_sdt()` để tìm lượt đặt theo số điện thoại.
- Xây dựng phương thức `thong_ke()` để thống kê tổng số bàn, tổng lượt đặt và số lượt đặt còn hiệu lực.

**2.3. Lập trình file `main.py`**

- Xây dựng menu để người dùng lựa chọn chức năng.
- Tạo hàm nhập số nguyên và xử lý trường hợp người dùng nhập sai định dạng.
- Khởi tạo một số bàn mẫu để thuận tiện cho việc chạy thử.
- Kết nối menu với các phương thức của lớp `QuanLyNhaHang`.
- Hiển thị kết quả và thông báo lỗi rõ ràng.
- Xử lý ngoại lệ để chương trình không bị dừng đột ngột khi xảy ra lỗi dữ liệu.
- Xây dựng chức năng thoát chương trình.

**2.4. Kiểm thử và hoàn thiện**

- Kiểm tra chức năng thêm bàn.
- Kiểm tra đặt bàn thành công.
- Kiểm tra trường hợp số người vượt quá sức chứa.
- Kiểm tra trường hợp đặt trùng bàn và thời gian.
- Kiểm tra chức năng tìm kiếm và hủy đặt bàn.
- Kiểm tra các chức năng thống kê và xử lý lỗi nhập liệu.
- Đảm bảo chương trình có thể chạy từ file `main.py`.

**Sản phẩm bàn giao:** `quan_ly_nha_hang.py` và `main.py`.

**Nội dung trình bày:** Giới thiệu lớp `QuanLyNhaHang`, quy trình xử lý đặt bàn, menu chương trình và cách các lớp phối hợp với nhau.

## III. NHIỆM VỤ CHUNG CỦA CẢ NHÓM

1. Thống nhất yêu cầu, chức năng và cấu trúc chương trình trước khi lập trình.
2. Phối hợp thiết kế sơ đồ lớp và luồng xử lý của hệ thống.
3. Tích hợp các file code, kiểm tra lỗi và đảm bảo các lớp hoạt động thống nhất.
4. Cùng kiểm thử các chức năng chính và xử lý những lỗi phát sinh.
5. Hoàn thiện file `README.md`, hướng dẫn cài đặt và chạy chương trình.
6. Chuẩn bị nội dung báo cáo, slide thuyết trình và phần minh họa chương trình.
7. Mỗi thành viên thực hiện commit các file được phân công lên GitHub.
8. Cùng rà soát sản phẩm cuối cùng và cập nhật đường dẫn repository công khai trong file `link.txt`.
9. Cả hai thành viên phải hiểu luồng hoạt động tổng thể và có khả năng giải thích phần code của mình khi giảng viên đặt câu hỏi.


## IV. KẾ HOẠCH THỰC HIỆN

| Giai đoạn | Nội dung công việc | Kết quả |
|---|---|---|
| Giai đoạn 1 | Phân tích yêu cầu, xác định chức năng và thiết kế lớp | Hoàn thiện phân công và sơ đồ lớp |
| Giai đoạn 2 | Thành viên 1 xây dựng các lớp dữ liệu; Thành viên 2 xây dựng lớp quản lý | Hoàn thiện các file lớp |
| Giai đoạn 3 | Xây dựng menu, tích hợp các file và hoàn thiện chức năng | Chương trình có thể chạy |
| Giai đoạn 4 | Kiểm thử, sửa lỗi, viết README và chuẩn bị thuyết trình | Hoàn thiện sản phẩm |
| Giai đoạn 5 | Upload lên GitHub và kiểm tra đường dẫn nộp bài | Repository công khai hoàn chỉnh |

