import unittest
from app import app

class TestAgeCalculator(unittest.TestCase):
    """Unit tests for age calculation app"""

    def setUp(self):
        """Set up the test client for the Flask app"""
        self.app = app.test_client()
        self.app.testing = True

    def test_valid_birth_year_lower_bound(self):
        """
        Test case 1: Năm sinh biên dưới (1950).
        Kết quả mong đợi: Tuổi được tính chính xác, không có lỗi.
        """
        response = self.app.post("/", data={"birth_year": "1950"})
        self.assertIn(b"Tuoi cua ban la 75", response.data)  # Assuming current_year = 2025
        self.assertNotIn(b"error", response.data)

    def test_valid_birth_year_upper_bound(self):
        """
        Test case 2: Năm sinh biên trên (2025).
        Kết quả mong đợi: Tuổi được tính chính xác, không có lỗi.
        """
        response = self.app.post("/", data={"birth_year": "2025"})
        self.assertIn(b"Tuoi cua ban la 0", response.data)  # Assuming current_year = 2025
        self.assertNotIn(b"error", response.data)

    def test_valid_birth_year_in_range(self):
        """
        Test case 3: Năm sinh trong khoảng hợp lệ (1990).
        Kết quả mong đợi: Tuổi được tính chính xác, không có lỗi.
        """
        response = self.app.post("/", data={"birth_year": "1990"})
        self.assertIn(b"Tuoi cua ban la 35", response.data)  # Assuming current_year = 2025
        self.assertNotIn(b"error", response.data)
    
    def test_birth_year_below_lower_bound(self):
        """
        Test case 4: Năm sinh dưới giá trị biên dưới (1949).
        Kết quả mong đợi: Thông báo lỗi 'Năm sinh phải từ 1950 đến 2025'.
        """
        response = self.app.post("/", data={"birth_year": "1949"})
        self.assertIn(b"Nam sinh phai tu 1950 den 2025", response.data)

    def test_birth_year_above_upper_bound(self):
        """
        Test case 5: Năm sinh trên giá trị biên trên (2026).
        Kết quả mong đợi: Thông báo lỗi 'Năm sinh phải từ 1950 đến 2025'.
        """
        response = self.app.post("/", data={"birth_year": "2026"})
        self.assertIn(b"Nam sinh phai tu 1950 den 2025", response.data)

    def test_non_numeric_birth_year(self):
        """
        Test case 6: Năm sinh không phải là số ('abc').
        Kết quả mong đợi: Thông báo lỗi 'Năm sinh phải là số'.
        """
        response = self.app.post("/", data={"birth_year": "abc"})
        self.assertIn(b"Nam sinh phai la so", response.data)

    def test_empty_birth_year(self):
        """
        Test case 7: Dữ liệu rỗng.
        Kết quả mong đợi: Thông báo lỗi 'Năm sinh phải là số'.
        """
        response = self.app.post("/", data={"birth_year": ""})
        self.assertIn(b"Nam sinh phai la so", response.data)

    def test_decimal_birth_year(self):
        """
        Test case 8: Số thập phân ('1960.5').
        Kết quả mong đợi: Thông báo lỗi 'Năm sinh phải là số'.
        """
        response = self.app.post("/", data={"birth_year": "1960.5"})
        self.assertIn(b"Nam sinh phai la so", response.data)

    def test_alphanumeric_birth_year(self):
        """
        Test case 9: Ký tự kết hợp chữ và số ('2000abc').
        Kết quả mong đợi: Thông báo lỗi 'Năm sinh phải là số'.
        """
        response = self.app.post("/", data={"birth_year": "2000abc"})
        self.assertIn(b"Nam sinh phai la so", response.data)

    def test_whitespace_birth_year(self):
        """
        Test case 12: Dữ liệu hợp lệ nhưng có khoảng trắng (' 1980 ').
        Kết quả mong đợi: Tuổi được tính chính xác, không có lỗi.
        """
        response = self.app.post("/", data={"birth_year": " 1980 "})
        self.assertIn(b"Tuoi cua ban la 45", response.data)  # Assuming current_year = 2025
        self.assertNotIn(b"error", response.data)

# Entry point for the test runner
if __name__ == "__main__":
    unittest.main()
