from quan_ly_nha_hang import QuanLyNhaHang
from ban_an import BanAn
from dat_ban import DatBan


def nhap_du_lieu():
    """Chạy thử nghiệp vụ qua menu Terminal."""
    ql = QuanLyNhaHang()

    while True:
        print("\n===== QUẢN LÝ ĐẶT BÀN NHÀ HÀNG =====")
        print("1. Thêm bàn")
        print("2. Xem danh sách bàn")
        print("3. Đặt bàn")
        print("4. Xem danh sách đặt bàn")
        print("5. Tìm kiếm đặt bàn")
        print("6. Hủy đặt bàn")
        print("0. Thoát")

        chon = input("Chọn chức năng: ").strip()
        try:
            if chon == "1":
                ban = BanAn(
                    input("Mã bàn: "), input("Tên bàn: "),
                    int(input("Sức chứa: ")), input("Khu vực: ") or "Tầng 1"
                )
                ql.them_ban(ban)
                print("Đã thêm bàn.")
            elif chon == "2":
                for ban in ql.ds_ban:
                    print(ban)
                if not ql.ds_ban:
                    print("Chưa có bàn.")
            elif chon == "3":
                dat = DatBan(
                    input("Mã đặt: "), input("Mã bàn: "), input("Tên khách: "),
                    input("Số điện thoại: "), input("Ngày giờ (YYYY-MM-DD HH:MM): "),
                    int(input("Số người: ")), input("Ghi chú: ")
                )
                ql.dat_ban(dat)
                print("Đặt bàn thành công.")
            elif chon == "4":
                for dat in ql.ds_dat:
                    print(dat)
                if not ql.ds_dat:
                    print("Chưa có lượt đặt.")
            elif chon == "5":
                sdt = input("Nhập số điện thoại (bỏ trống nếu không lọc): ")
                ngay = input("Nhập ngày YYYY-MM-DD (bỏ trống nếu không lọc): ")
                for dat in ql.tim_kiem_dat_ban(sdt, ngay):
                    print(dat)
            elif chon == "6":
                if ql.huy_dat_ban(input("Mã đặt cần hủy: ")):
                    print("Đã hủy đặt bàn.")
                else:
                    print("Không tìm thấy mã đặt.")
            elif chon == "0":
                print("Kết thúc chương trình.")
                break
            else:
                print("Lựa chọn không hợp lệ.")
        except (ValueError, TypeError) as e:
            print("Lỗi:", e)


if __name__ == "__main__":
    nhap_du_lieu()
