import json
from pathlib import Path
from datetime import datetime

from ban_an import BanAn
from dat_ban import DatBan


class QuanLyNhaHang:
    """Lớp quản lý bàn ăn, đặt bàn và lưu trữ JSON."""

    def __init__(self, thu_muc_du_lieu="data"):
        self.thu_muc = Path(thu_muc_du_lieu)
        self.thu_muc.mkdir(parents=True, exist_ok=True)
        self.file_ban = self.thu_muc / "ban_an.json"
        self.file_dat = self.thu_muc / "dat_ban.json"
        self.ds_ban = [BanAn.from_dict(x) for x in self._doc_json(self.file_ban)]
        self.ds_dat = [DatBan.from_dict(x) for x in self._doc_json(self.file_dat)]

    @staticmethod
    def _doc_json(duong_dan):
        if not duong_dan.exists() or duong_dan.stat().st_size == 0:
            return []
        try:
            with open(duong_dan, "r", encoding="utf-8") as f:
                du_lieu = json.load(f)
            if not isinstance(du_lieu, list):
                raise ValueError(f"Dữ liệu trong {duong_dan.name} phải là danh sách.")
            return du_lieu
        except json.JSONDecodeError as exc:
            raise ValueError(f"Tệp {duong_dan.name} không đúng định dạng JSON.") from exc

    @staticmethod
    def _ghi_json(duong_dan, du_lieu):
        tam = duong_dan.with_suffix(".tmp")
        with open(tam, "w", encoding="utf-8") as f:
            json.dump(du_lieu, f, ensure_ascii=False, indent=4)
        tam.replace(duong_dan)

    def _luu_ban(self):
        self._ghi_json(self.file_ban, [x.to_dict() for x in self.ds_ban])

    def _luu_dat(self):
        self._ghi_json(self.file_dat, [x.to_dict() for x in self.ds_dat])

    def them_ban(self, ban):
        if any(x.ma_ban == ban.ma_ban for x in self.ds_ban):
            raise ValueError("Mã bàn đã tồn tại.")
        self.ds_ban.append(ban)
        self._luu_ban()

    def tim_ban(self, ma_ban):
        return next((x for x in self.ds_ban if x.ma_ban == str(ma_ban)), None)

    def xoa_ban(self, ma_ban):
        if any(x.ma_ban == str(ma_ban) and x.trang_thai != "Trống" for x in self.ds_ban):
            raise ValueError("Không thể xóa bàn đang được sử dụng.")
        ban = self.tim_ban(ma_ban)
        if ban is None:
            return False
        self.ds_ban.remove(ban)
        self._luu_ban()
        return True

    def tim_kiem_ban(self, tu_khoa):
        tu_khoa = str(tu_khoa).lower()
        return [b for b in self.ds_ban
                if tu_khoa in b.ma_ban.lower()
                or tu_khoa in b.ten_ban.lower()
                or tu_khoa in b.khu_vuc.lower()]

    def dat_ban(self, dat):
        ban = self.tim_ban(dat.ma_ban)
        if ban is None:
            raise ValueError("Bàn không tồn tại.")
        if dat.so_nguoi > ban.suc_chua:
            raise ValueError("Số người vượt quá sức chứa của bàn.")
        if any(x.ma_dat == dat.ma_dat for x in self.ds_dat):
            raise ValueError("Mã đặt bàn đã tồn tại.")
        thoi_diem_moi = datetime.strptime(dat.ngay_gio, "%Y-%m-%d %H:%M")
        for cu in self.ds_dat:
            if cu.ma_ban == dat.ma_ban and cu.trang_thai == "Đã đặt":
                thoi_diem_cu = datetime.strptime(cu.ngay_gio, "%Y-%m-%d %H:%M")
                if abs((thoi_diem_moi - thoi_diem_cu).total_seconds()) < 2 * 60 * 60:
                    raise ValueError("Bàn đã có lượt đặt trong khoảng thời gian gần đó.")
        self.ds_dat.append(dat)
        ban.cap_nhat_trang_thai("Đã có lịch")
        self._luu_dat()
        self._luu_ban()

    def huy_dat_ban(self, ma_dat):
        dat = next((x for x in self.ds_dat if x.ma_dat == str(ma_dat)), None)
        if dat is None:
            return False
        dat.trang_thai = "Đã hủy"
        ban = self.tim_ban(dat.ma_ban)
        if ban:
            ban.cap_nhat_trang_thai("Trống")
        self._luu_dat()
        self._luu_ban()
        return True

    def tim_kiem_dat_ban(self, so_dien_thoai="", ngay=""):
        ket_qua = self.ds_dat
        if so_dien_thoai:
            ket_qua = [x for x in ket_qua if so_dien_thoai in x.so_dien_thoai]
        if ngay:
            ket_qua = [x for x in ket_qua if x.ngay_gio.startswith(ngay)]
        return ket_qua
