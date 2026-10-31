class BanAn:
    """Lớp mô tả một bàn ăn trong nhà hàng."""

    def __init__(self, ma_ban, ten_ban, suc_chua, khu_vuc="Tầng 1", trang_thai="Trống"):
        self.ma_ban = str(ma_ban).strip()
        self.ten_ban = str(ten_ban).strip()
        self.suc_chua = int(suc_chua)
        self.khu_vuc = str(khu_vuc).strip()
        self.trang_thai = str(trang_thai).strip()

        if not self.ma_ban or not self.ten_ban:
            raise ValueError("Mã bàn và tên bàn không được để trống.")
        if self.suc_chua <= 0:
            raise ValueError("Sức chứa phải lớn hơn 0.")

    def cap_nhat_trang_thai(self, trang_thai):
        self.trang_thai = trang_thai

    def to_dict(self):
        return {
            "ma_ban": self.ma_ban,
            "ten_ban": self.ten_ban,
            "suc_chua": self.suc_chua,
            "khu_vuc": self.khu_vuc,
            "trang_thai": self.trang_thai
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["ma_ban"], data["ten_ban"], data["suc_chua"],
            data.get("khu_vuc", "Tầng 1"), data.get("trang_thai", "Trống")
        )

    def __str__(self):
        return f"{self.ma_ban} - {self.ten_ban} ({self.suc_chua} chỗ) - {self.trang_thai}"
