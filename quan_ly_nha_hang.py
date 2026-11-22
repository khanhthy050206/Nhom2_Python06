import json
from pathlib import Path

from ban_an import BanAn
from dat_ban import DatBan


class QuanLyNhaHang:
    """Quản lý danh sách bàn ăn và danh sách đặt bàn, lưu trữ dữ liệu JSON."""

    def __init__(self, thu_muc_du_lieu="data"):
        self.thu_muc = Path(thu_muc_du_lieu)
        self.thu_muc.mkdir(parents=True, exist_ok=True)
        self.file_ban = self.thu_muc / "ban_an.json"
        self.file_dat = self.thu_muc / "dat_ban.json"
        self.ds_ban = [BanAn.from_dict(x) for x in self._doc_json(self.file_ban)]
        self.ds_dat = [DatBan.from_dict(x) for x in self._doc_json(self.file_dat)]

    # ------------------------------------------------------------------
    # Đọc / ghi dữ liệu JSON
    # ------------------------------------------------------------------
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

    # ------------------------------------------------------------------
    # 2.2 Quản lý bàn ăn
    # ------------------------------------------------------------------
    def them_ban(self, ban):
        """Thêm bàn mới; kiểm tra trùng mã bàn bằng vòng lặp."""
        for b in self.ds_ban:
            if b.ma_ban == ban.ma_ban:
                raise ValueError("Mã bàn đã tồn tại.")
        self.ds_ban.append(ban)
        self._luu_ban()

    def lay_ban(self, ma_ban):
        """Tìm bàn theo mã bàn; trả về None nếu không có."""
        ma_ban = str(ma_ban)
        for ban in self.ds_ban:
            if str(ban.ma_ban) == ma_ban:
                return ban
        return None

    # Giữ tên cũ để tương thích các đoạn code đang dùng tim_ban()
    def tim_ban(self, ma_ban):
        return self.lay_ban(ma_ban)

    def xoa_ban(self, ma_ban):
        """Xóa bàn trống; không xóa bàn đang có lịch sử dụng."""
        for b in self.ds_ban:
            if str(b.ma_ban) == str(ma_ban) and b.trang_thai != "Trống":
                raise ValueError("Không thể xóa bàn đang được sử dụng.")
        ban = self.lay_ban(ma_ban)
        if ban is None:
            return False
        self.ds_ban.remove(ban)
        self._luu_ban()
        return True

    def tim_kiem_ban(self, tu_khoa):
        """Tìm bàn theo mã, tên hoặc khu vực."""
        tu_khoa = str(tu_khoa).lower()
        return [b for b in self.ds_ban
                if tu_khoa in str(b.ma_ban).lower()
                or tu_khoa in str(b.ten_ban).lower()
                or tu_khoa in str(b.khu_vuc).lower()]

    # ------------------------------------------------------------------
    # 2.2 Quản lý đặt bàn
    # ------------------------------------------------------------------
    def dat_ban(self, dat):
        """Tiếp nhận yêu cầu đặt bàn.

        Kiểm tra:
        1. Bàn có tồn tại hay không.
        2. Số người đặt không vượt sức chứa của bàn.
        3. Mã đặt bàn không trùng.
        4. Không trùng cùng ngày và giờ với một lượt đặt còn hiệu lực
           (trạng thái "Đã đặt") của chính bàn đó.
        """
        ban = self.lay_ban(dat.ma_ban)
        if ban is None:
            raise ValueError("Bàn không tồn tại.")

        if dat.so_nguoi > ban.suc_chua:
            raise ValueError("Số người vượt quá sức chứa của bàn.")

        for cu in self.ds_dat:
            if cu.ma_dat == dat.ma_dat:
                raise ValueError("Mã đặt bàn đã tồn tại.")

        for cu in self.ds_dat:
            if (cu.ma_ban == dat.ma_ban
                    and cu.trang_thai == "Đã đặt"
                    and cu.ngay_gio == dat.ngay_gio):
                raise ValueError("Bàn đã được đặt vào ngày và giờ này (lượt đặt trước vẫn còn hiệu lực).")

        self.ds_dat.append(dat)
        ban.cap_nhat_trang_thai("Đã có lịch")
        self._luu_dat()
        self._luu_ban()

    def huy_dat_ban(self, ma_dat):
        """Hủy một lượt đặt bàn theo mã đặt bàn."""
        dat = next((x for x in self.ds_dat if str(x.ma_dat) == str(ma_dat)), None)
        if dat is None:
            return False

        dat.trang_thai = "Đã hủy"
        con_lai = any(x.ma_ban == dat.ma_ban and x.trang_thai == "Đã đặt"
                      for x in self.ds_dat)
        ban = self.lay_ban(dat.ma_ban)
        if ban:
            ban.cap_nhat_trang_thai("Đã có lịch" if con_lai else "Trống")

        self._luu_dat()
        self._luu_ban()
        return True

    def tim_theo_sdt(self, so_dien_thoai):
        """Tìm các lượt đặt bàn theo số điện thoại."""
        so_dien_thoai = str(so_dien_thoai)
        return [x for x in self.ds_dat if so_dien_thoai in str(x.so_dien_thoai)]

    def tim_kiem_dat_ban(self, so_dien_thoai="", ngay=""):
        """Tìm đặt bàn theo số điện thoại và/hoặc ngày (định dạng YYYY-MM-DD)."""
        ket_qua = self.tim_theo_sdt(so_dien_thoai) if so_dien_thoai else list(self.ds_dat)
        if ngay:
            ket_qua = [x for x in ket_qua if str(x.ngay_gio).startswith(ngay)]
        return ket_qua

    # ------------------------------------------------------------------
    # 2.2 Thống kê
    # ------------------------------------------------------------------
    def thong_ke(self):
        """Thống kê tổng số bàn, tổng lượt đặt và số lượt đặt còn hiệu lực."""
        tong_so_ban = len(self.ds_ban)
        tong_luot_dat = len(self.ds_dat)
        luot_dat_con_hieu_luc = sum(
            1 for x in self.ds_dat if x.trang_thai == "Đã đặt"
        )
        luot_dat_da_huy = sum(
            1 for x in self.ds_dat if x.trang_thai == "Đã hủy"
        )
        so_ban_trong = sum(1 for b in self.ds_ban if b.trang_thai == "Trống")
        so_ban_da_co_lich = tong_so_ban - so_ban_trong

        return {
            "tong_so_ban": tong_so_ban,
            "tong_luot_dat": tong_luot_dat,
            "luot_dat_con_hieu_luc": luot_dat_con_hieu_luc,
            "luot_dat_da_huy": luot_dat_da_huy,
            "so_ban_trong": so_ban_trong,
            "so_ban_da_co_lich": so_ban_da_co_lich,
        }

    def in_thong_ke(self):
        """In báo cáo thống kê ra màn hình."""
        tk = self.thong_ke()
        print("===== THỐNG KÊ NHÀ HÀNG =====")
        print(f"Tổng số bàn: {tk['tong_so_ban']}")
        print(f"Tổng lượt đặt: {tk['tong_luot_dat']}")
        print(f"Số lượt đặt còn hiệu lực: {tk['luot_dat_con_hieu_luc']}")
        print(f"Số lượt đặt đã hủy: {tk['luot_dat_da_huy']}")
        print(f"Bàn trống: {tk['so_ban_trong']} | Bàn đã có lịch: {tk['so_ban_da_co_lich']}")
        return tk
