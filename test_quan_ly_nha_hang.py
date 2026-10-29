import unittest
from quan_ly_nha_hang import QuanLyNhaHang


class TestQuanLyNhaHang(unittest.TestCase):
    def setUp(self):
        self.ql = QuanLyNhaHang()
        self.ql.them_ban("A1", 4)

    def test_them_ban(self):
        self.assertEqual(self.ql.lay_ban("A1").suc_chua, 4)

    def test_trung_ma_ban(self):
        with self.assertRaises(ValueError):
            self.ql.them_ban("A1", 2)

    def test_dat_ban(self):
        dat = self.ql.dat_ban("An", "0900000000", "2026-11-01 18:30", 3, "A1")
        self.assertEqual(dat.ma_ban, "A1")

    def test_vuot_suc_chua(self):
        with self.assertRaises(ValueError):
            self.ql.dat_ban("An", "0900000000", "2026-11-01 18:30", 5, "A1")

    def test_trung_gio(self):
        self.ql.dat_ban("An", "0900000000", "2026-11-01 18:30", 2, "A1")
        with self.assertRaises(ValueError):
            self.ql.dat_ban("Binh", "0911111111", "2026-11-01 18:30", 2, "A1")

    def test_huy_dat_ban(self):
        dat = self.ql.dat_ban("An", "0900000000", "2026-11-01 18:30", 2, "A1")
        self.assertTrue(self.ql.huy_dat_ban(dat.ma_dat))


if __name__ == "__main__":
    unittest.main()
