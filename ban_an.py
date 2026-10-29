class BanAn:
    """Lưu thông tin một bàn ăn."""

    def __init__(self, ma_ban, suc_chua):
        if not str(ma_ban).strip():
            raise ValueError("Mã bàn không được để trống.")
        if not isinstance(suc_chua, int) or suc_chua <= 0:
            raise ValueError("Sức chứa phải là số nguyên dương.")
        self.ma_ban = str(ma_ban).strip().upper()
        self.suc_chua = suc_chua
        self.trang_thai = "Trống"

    def hien_thi(self):
        return f"Bàn {self.ma_ban} | Sức chứa: {self.suc_chua} | Trạng thái: {self.trang_thai}"

    def __str__(self):
        return self.hien_thi()
