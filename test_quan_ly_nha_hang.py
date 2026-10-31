import tempfile
import unittest

from ban_an import BanAn
from dat_ban import DatBan
from quan_ly_nha_hang import QuanLyNhaHang


class TestQuanLyNhaHang(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.ql = QuanLyNhaHang(self.temp.name)
        self.ql.them_ban(BanAn("B01", "Bàn 1", 4))

    def tearDown(self):
        self.temp.cleanup()

    def tao_dat(self, ma="D01", gio="2026-11-01 18:00", sdt="0901234567"):
        return DatBan(ma, "B01", "Nguyen Van A", sdt, gio, 2)

    def test_them_ban_thanh_cong(self):
        self.assertEqual(len(self.ql.ds_ban), 1)

    def test_trung_ma_ban(self):
        with self.assertRaises(ValueError):
            self.ql.them_ban(BanAn("B01", "Bàn trùng", 4))

    def test_suc_chua_khong_hop_le(self):
        with self.assertRaises(ValueError):
            BanAn("B02", "Bàn 2", 0)

    def test_dat_ban_thanh_cong(self):
        self.ql.dat_ban(self.tao_dat())
        self.assertEqual(len(self.ql.ds_dat), 1)

    def test_trung_thoi_gian(self):
        self.ql.dat_ban(self.tao_dat())
        with self.assertRaises(ValueError):
            self.ql.dat_ban(self.tao_dat("D02", "2026-11-01 19:00"))

    def test_vuot_suc_chua(self):
        with self.assertRaises(ValueError):
            self.ql.dat_ban(DatBan("D02", "B01", "Khach", "0901234567",
                                   "2026-11-01 21:00", 8))

    def test_huy_dat_ban(self):
        self.ql.dat_ban(self.tao_dat())
        self.assertTrue(self.ql.huy_dat_ban("D01"))
        self.assertEqual(self.ql.ds_dat[0].trang_thai, "Đã hủy")

    def test_tim_kiem_theo_sdt(self):
        self.ql.dat_ban(self.tao_dat())
        self.assertEqual(len(self.ql.tim_kiem_dat_ban(so_dien_thoai="0901")), 1)

    def test_tim_kiem_theo_ngay(self):
        self.ql.dat_ban(self.tao_dat())
        self.assertEqual(len(self.ql.tim_kiem_dat_ban(ngay="2026-11-01")), 1)

    def test_xoa_ban_khong_ton_tai(self):
        self.assertFalse(self.ql.xoa_ban("B99"))


if __name__ == "__main__":
    unittest.main()
