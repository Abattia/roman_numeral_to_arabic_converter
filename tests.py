# std lib imports
import unittest

# local imports
import roman_to_arabic as app

class ToArabicTestCase(unittest.TestCase):

    def test_MMMCMXCIV_goes_to_3994(self):
        a_roman = "MMMCMXCIV"

        result = app.to_arabic(a_roman)

        self.assertEqual(result, 3994)

    def test_CM_goes_to_900(self):
        a_roman = "CM"

        result = app.to_arabic(a_roman)

        self.assertEqual(result, 900)

    def test_CD_goes_to_400(self):
        a_roman = "CD"

        result = app.to_arabic(a_roman)

        self.assertEqual(result, 400)

    def test_XC_goes_to_90(self):
        a_roman = "XC"

        result = app.to_arabic(a_roman)

        self.assertEqual(result, 90)

    def test_XL_goes_to_40(self):
        a_roman = "XL"

        result = app.to_arabic(a_roman)

        self.assertEqual(result, 40)

    def test_IX_goes_to_9(self):
        a_roman = "IX"

        result = app.to_arabic(a_roman)

        self.assertEqual(result, 9)

    def test_IV_goes_to_4(self):
        a_roman = "IV"

        result = app.to_arabic(a_roman)

        self.assertEqual(result, 4)

    def test_D_goes_to_500(self):
        a_roman = "D"

        result = app.to_arabic(a_roman)

        self.assertEqual(result, 500)

    def test_L_goes_to_50(self):
        a_roman = "L"

        result = app.to_arabic(a_roman)

        self.assertEqual(result, 50)

    def test_V_goes_to_5(self):
        a_roman = "V"

        result = app.to_arabic(a_roman)

        self.assertEqual(result, 5)

    def test_M_goes_to_1000(self):
        a_roman = "M"

        result = app.to_arabic(a_roman)

        self.assertEqual(result, 1000)

    def test_CC_goes_to_200(self):
        a_roman = "CC"

        result = app.to_arabic(a_roman)

        self.assertEqual(result, 200)

    def test_XXX_goes_to_30(self):
        a_roman = "XXX"

        result = app.to_arabic(a_roman)

        self.assertEqual(result, 30)

    def test_X_goes_to_10(self):
        a_roman = "X"

        result = app.to_arabic(a_roman)

        self.assertEqual(result, 10)

    def test_III_goes_to_3(self):
        a_roman = "III"

        result = app.to_arabic(a_roman)

        self.assertEqual(result, 3)

    def test_II_goes_to_2(self):
        a_roman = "II"

        result = app.to_arabic(a_roman)

        self.assertEqual(result, 2)

    def test_I_goes_to_1(self):
        a_roman = "I"

        result = app.to_arabic(a_roman)

        self.assertEqual(result, 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)
