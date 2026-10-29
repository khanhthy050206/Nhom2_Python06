from quan_ly_nha_hang import QuanLyNhaHang


def nhap_so_nguyen(thong_bao):
    while True:
        try:
            return int(input(thong_bao))
        except ValueError:
            print("Vui lòng nhập số nguyên.")


def main():
    ql = QuanLyNhaHang()
    for ma, suc_chua in [("A1", 2), ("A2", 4), ("B1", 6)]:
        ql.them_ban(ma, suc_chua)

    while True:
        print("\n===== QUẢN LÝ ĐẶT BÀN NHÀ HÀNG =====")
        print("1. Xem bàn | 2. Thêm bàn | 3. Đặt bàn")
        print("4. Xem đặt bàn | 5. Tìm theo SĐT | 6. Hủy đặt bàn")
        print("7. Thống kê | 0. Thoát")
        chon = input("Chọn: ").strip()
        try:
            if chon == "1":
                for ban in ql.ds_ban:
                    print(ban.hien_thi())
            elif chon == "2":
                ban = ql.them_ban(input("Mã bàn: "), nhap_so_nguyen("Sức chứa: "))
                print("Đã thêm:", ban)
            elif chon == "3":
                ten = input("Tên khách: ")
                sdt = input("Số điện thoại: ")
                ngay_gio = input("Ngày giờ (VD 2026-11-01 18:30): ")
                so_nguoi = nhap_so_nguyen("Số người: ")
                ma_ban = input("Mã bàn: ")
                print("Đặt bàn thành công:", ql.dat_ban(ten, sdt, ngay_gio, so_nguoi, ma_ban))
            elif chon == "4":
                for dat in ql.ds_dat_ban:
                    print(dat.hien_thi())
                if not ql.ds_dat_ban:
                    print("Chưa có lượt đặt bàn.")
            elif chon == "5":
                ket_qua = ql.tim_theo_sdt(input("Số điện thoại: "))
                for dat in ket_qua:
                    print(dat.hien_thi())
                if not ket_qua:
                    print("Không tìm thấy.")
            elif chon == "6":
                ma_dat = nhap_so_nguyen("Mã đặt bàn cần hủy: ")
                print("Đã hủy." if ql.huy_dat_ban(ma_dat) else "Không tìm thấy lượt đặt còn hiệu lực.")
            elif chon == "7":
                for ten, so in ql.thong_ke().items():
                    print(f"{ten}: {so}")
            elif chon == "0":
                print("Đã thoát chương trình.")
                break
            else:
                print("Lựa chọn không hợp lệ.")
        except ValueError as loi:
            print("Lỗi:", loi)


if __name__ == "__main__":
    main()
