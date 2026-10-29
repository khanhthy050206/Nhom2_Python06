from ban_an import BanAn
from dat_ban import DatBan


class QuanLyNhaHang:
    """Quản lý danh sách bàn ăn và đặt bàn."""

    def __init__(self):
        self.ds_ban = []
        self.ds_dat_ban = []
        self.ma_dat_tiep_theo = 1

    def them_ban(self, ma_ban, suc_chua):
        ma_ban = str(ma_ban).strip().upper()
        if any(b.ma_ban == ma_ban for b in self.ds_ban):
            raise ValueError("Mã bàn đã tồn tại.")
        ban = BanAn(ma_ban, suc_chua)
        self.ds_ban.append(ban)
        return ban

    def lay_ban(self, ma_ban):
        ma_ban = str(ma_ban).strip().upper()
        for ban in self.ds_ban:
            if ban.ma_ban == ma_ban:
                return ban
        return None

    def dat_ban(self, ten_khach, so_dien_thoai, ngay_gio, so_nguoi, ma_ban):
        ban = self.lay_ban(ma_ban)
        if ban is None:
            raise ValueError("Không tìm thấy bàn.")
        if so_nguoi > ban.suc_chua:
            raise ValueError("Số người vượt quá sức chứa của bàn.")
        ngay_gio = str(ngay_gio).strip()
        for dat in self.ds_dat_ban:
            if dat.ma_ban == ban.ma_ban and dat.ngay_gio == ngay_gio and dat.trang_thai == "Đang đặt":
                raise ValueError("Bàn đã được đặt vào thời gian này.")
        dat = DatBan(self.ma_dat_tiep_theo, ten_khach, so_dien_thoai, ngay_gio, so_nguoi, ban.ma_ban)
        self.ma_dat_tiep_theo += 1
        self.ds_dat_ban.append(dat)
        return dat

    def huy_dat_ban(self, ma_dat):
        for dat in self.ds_dat_ban:
            if dat.ma_dat == ma_dat and dat.trang_thai == "Đang đặt":
                dat.trang_thai = "Đã hủy"
                return True
        return False

    def tim_theo_sdt(self, so_dien_thoai):
        sdt = str(so_dien_thoai).strip()
        return [dat for dat in self.ds_dat_ban if dat.so_dien_thoai == sdt]

    def thong_ke(self):
        return {
            "Tổng số bàn": len(self.ds_ban),
            "Tổng lượt đặt": len(self.ds_dat_ban),
            "Lượt đặt còn hiệu lực": sum(dat.trang_thai == "Đang đặt" for dat in self.ds_dat_ban),
        }
