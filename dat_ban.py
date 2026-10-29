class DatBan:
    """Lưu thông tin một lượt đặt bàn."""

    def __init__(self, ma_dat, ten_khach, so_dien_thoai, ngay_gio, so_nguoi, ma_ban):
        if not str(ten_khach).strip():
            raise ValueError("Tên khách không được để trống.")
        if not str(so_dien_thoai).strip():
            raise ValueError("Số điện thoại không được để trống.")
        if not str(ngay_gio).strip():
            raise ValueError("Ngày giờ không được để trống.")
        if not isinstance(so_nguoi, int) or so_nguoi <= 0:
            raise ValueError("Số người phải là số nguyên dương.")
        self.ma_dat = ma_dat
        self.ten_khach = str(ten_khach).strip()
        self.so_dien_thoai = str(so_dien_thoai).strip()
        self.ngay_gio = str(ngay_gio).strip()
        self.so_nguoi = so_nguoi
        self.ma_ban = str(ma_ban).strip().upper()
        self.trang_thai = "Đang đặt"

    def hien_thi(self):
        return (f"Mã đặt: {self.ma_dat} | Khách: {self.ten_khach} | SĐT: {self.so_dien_thoai} "
                f"| Thời gian: {self.ngay_gio} | Số người: {self.so_nguoi} "
                f"| Bàn: {self.ma_ban} | Trạng thái: {self.trang_thai}")

    def __str__(self):
        return self.hien_thi()
