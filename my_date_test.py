import unittest
import my_date

class MyDateTest(unittest.TestCase):

    def test_is_leap_year1(self):
        self.assertTrue(my_date.is_leap_year(1984))

    def test_is_leap_year2(self):
        self.assertFalse(my_date.is_leap_year(1985))
        
    def ordnal_date(self):
        self.assertEqual(2,my_date.ordinal_date(2023,1,2))
        
    def days_elapsed(self):
        self.assertEqual(58,my_date.days_elapsed(2023,9,19,2023,11,16))
        
    def day_of_week(self):
        self.assertEqual('Saturday',my_date.day_of_week(2023,9,29))
        
    def to_str(self):
        self.assertEqual('Saturday, 29 September 2023',my_date.to_str(2023,9,29))
        
        
if __name__ == '__main__':
    unittest.main()