from datetime import datetime


class DatBan:
    """Lớp lưu thông tin một lượt đặt bàn."""

    def __init__(self, ma_dat, ma_ban, ten_khach, so_dien_thoai,
                 ngay_gio, so_nguoi, ghi_chu="", trang_thai="Đã đặt"):
        self.ma_dat = str(ma_dat).strip()
        self.ma_ban = str(ma_ban).strip()
        self.ten_khach = str(ten_khach).strip()
        self.so_dien_thoai = str(so_dien_thoai).strip()
        self.ngay_gio = str(ngay_gio).strip()
        self.so_nguoi = int(so_nguoi)
        self.ghi_chu = str(ghi_chu).strip()
        self.trang_thai = str(trang_thai).strip()

        if not all([self.ma_dat, self.ma_ban, self.ten_khach, self.so_dien_thoai]):
            raise ValueError("Vui lòng nhập đầy đủ thông tin bắt buộc.")
        if self.so_nguoi <= 0:
            raise ValueError("Số người phải lớn hơn 0.")
        try:
            datetime.strptime(self.ngay_gio, "%Y-%m-%d %H:%M")
        except ValueError as exc:
            raise ValueError("Ngày giờ phải có dạng YYYY-MM-DD HH:MM.") from exc

    def to_dict(self):
        return {
            "ma_dat": self.ma_dat,
            "ma_ban": self.ma_ban,
            "ten_khach": self.ten_khach,
            "so_dien_thoai": self.so_dien_thoai,
            "ngay_gio": self.ngay_gio,
            "so_nguoi": self.so_nguoi,
            "ghi_chu": self.ghi_chu,
            "trang_thai": self.trang_thai
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def __str__(self):
        return (f"{self.ma_dat} | Bàn {self.ma_ban} | {self.ten_khach} | "
                f"{self.ngay_gio} | {self.so_nguoi} người | {self.trang_thai}")
