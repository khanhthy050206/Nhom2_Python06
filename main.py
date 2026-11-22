from ban_an import BanAn
from dat_ban import DatBan
from quan_ly_nha_hang import QuanLyNhaHang


def nhap_ban(ql):
    ma_ban = input("Mã bàn: ").strip()
    ten_ban = input("Tên bàn: ").strip()
    khu_vuc = input("Khu vực: ").strip()
    suc_chua = int(input("Sức chứa: ").strip())
    ban = BanAn.from_dict({
        "ma_ban": ma_ban,
        "ten_ban": ten_ban,
        "khu_vuc": khu_vuc,
        "suc_chua": suc_chua,
        "trang_thai": "Trống",
    })
    ql.them_ban(ban)
    print("Đã thêm bàn.")


def dat_ban(ql):
    ma_dat = input("Mã đặt bàn: ").strip()
    ma_ban = input("Mã bàn: ").strip()
    so_dien_thoai = input("Số điện thoại khách: ").strip()
    so_nguoi = int(input("Số người: ").strip())
    ngay_gio = input("Ngày giờ (YYYY-MM-DD HH:MM): ").strip()
    dat = DatBan.from_dict({
        "ma_dat": ma_dat,
        "ma_ban": ma_ban,
        "so_dien_thoai": so_dien_thoai,
        "so_nguoi": so_nguoi,
        "ngay_gio": ngay_gio,
        "trang_thai": "Đã đặt",
    })
    ql.dat_ban(dat)
    print("Đặt bàn thành công.")


def tim_ban(ql):
    ma_ban = input("Mã bàn cần tìm: ").strip()
    ban = ql.lay_ban(ma_ban)
    if ban is None:
        print("Không tìm thấy bàn.")
    else:
        print(f"Bàn {ban.ma_ban} | {ban.ten_ban} | Khu vực: {ban.khu_vuc} "
              f"| Sức chứa: {ban.suc_chua} | Trạng thái: {ban.trang_thai}")


def tim_theo_sdt(ql):
    sdt = input("Số điện thoại cần tìm: ").strip()
    ket_qua = ql.tim_theo_sdt(sdt)
    if not ket_qua:
        print("Không có lượt đặt nào khớp.")
    for d in ket_qua:
        print(f"{d.ma_dat} | Bàn {d.ma_ban} | SĐT {d.so_dien_thoai} | "
              f"{d.so_nguoi} người | {d.ngay_gio} | {d.trang_thai}")


def huy_dat(ql):
    ma_dat = input("Mã đặt bàn cần hủy: ").strip()
    if ql.huy_dat_ban(ma_dat):
        print("Đã hủy đặt bàn.")
    else:
        print("Không tìm thấy mã đặt bàn.")


def menu():
    ql = QuanLyNhaHang("data")
    while True:
        print("\n===== QUẢN LÝ NHÀ HÀNG =====")
        print("1. Thêm bàn")
        print("2. Đặt bàn")
        print("3. Tìm bàn theo mã")
        print("4. Tìm đặt bàn theo số điện thoại")
        print("5. Hủy đặt bàn")
        print("6. Thống kê")
        print("0. Thoát")
        chon = input("Chọn chức năng: ").strip()
        try:
            if chon == "1":
                nhap_ban(ql)
            elif chon == "2":
                dat_ban(ql)
            elif chon == "3":
                tim_ban(ql)
            elif chon == "4":
                tim_theo_sdt(ql)
            elif chon == "5":
                huy_dat(ql)
            elif chon == "6":
                ql.in_thong_ke()
            elif chon == "0":
                print("Thoát chương trình.")
                break
            else:
                print("Lựa chọn không hợp lệ.")
        except ValueError as e:
            print(f"Lỗi: {e}")


if __name__ == "__main__":
    menu()
