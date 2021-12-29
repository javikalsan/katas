import pytest
from expects import expect, equal

from enum import Enum


class Numerals(Enum):
    THOUSAND = {"arabic": 1000, "roman": "M"}
    NINEHUNDRED = {"arabic": 900, "roman": "CM"}
    FIVEHUNDRED = {"arabic": 500, "roman": "D"}
    FOURHUNDRED = {"arabic": 400, "roman": "CD"}
    HUNDRED = {"arabic": 100, "roman": "C"}
    NINETY = {"arabic": 90, "roman": "XC"}
    FIFTY = {"arabic": 50, "roman": "L"}
    FOURTY = {"arabic": 40, "roman": "XL"}
    TEN = {"arabic": 10, "roman": "X"}
    NINE = {"arabic": 9, "roman": "IX"}
    FIVE = {"arabic": 5, "roman": "V"}
    FOUR = {"arabic": 4, "roman": "IV"}
    ONE = {"arabic": 1, "roman": "I"}


class RomanNumeralsKata:
    def roman_numeral_for(self, number):
        roman = ""
        for numeral in Numerals:
            while number >= numeral.value["arabic"]:
                roman += numeral.value["roman"]
                number -= numeral.value["arabic"]
        return roman


@pytest.fixture(autouse=True)
def sut():
    return RomanNumeralsKata()

class TestRomanNumeralsKata:
    class TestGiven_a_positive_arabic_number:
        def test_it_returns_I_for_number_1(self, sut):
            expect(sut.roman_numeral_for(1)).to(equal("I"))

        def test_it_returns_II_for_number_2(self, sut):
            expect(sut.roman_numeral_for(2)).to(equal("II"))

        def test_it_returns_III_for_number_3(self, sut):
            expect(sut.roman_numeral_for(3)).to(equal("III"))

        def test_it_returns_IV_for_number_4(self, sut):
            expect(sut.roman_numeral_for(4)).to(equal("IV"))

        def test_it_returns_V_for_number_5(self, sut):
            expect(sut.roman_numeral_for(5)).to(equal("V"))

        def test_it_returns_VI_for_number_6(self, sut):
            expect(sut.roman_numeral_for(6)).to(equal("VI"))

        def test_it_returns_VII_for_number_7(self, sut):
            expect(sut.roman_numeral_for(7)).to(equal("VII"))

        def test_it_returns_VIII_for_number_8(self, sut):
            expect(sut.roman_numeral_for(8)).to(equal("VIII"))

        def test_it_returns_IX_for_number_9(self, sut):
            expect(sut.roman_numeral_for(9)).to(equal("IX"))

        def test_it_returns_X_for_number_10(self, sut):
            expect(sut.roman_numeral_for(10)).to(equal("X"))

        def test_it_returns_XXIX_for_number_29(self, sut):
            expect(sut.roman_numeral_for(29)).to(equal("XXIX"))

        def test_it_returns_XXX_for_number_30(self, sut):
            expect(sut.roman_numeral_for(30)).to(equal("XXX"))

        def test_it_returns_XL_for_number_40(self, sut):
            expect(sut.roman_numeral_for(40)).to(equal("XL"))

        def test_it_returns_L_for_number_50(self, sut):
            expect(sut.roman_numeral_for(50)).to(equal("L"))

        def test_it_returns_LX_for_number_60(self, sut):
            expect(sut.roman_numeral_for(60)).to(equal("LX"))

        def test_it_returns_LXX_for_number_70(self, sut):
            expect(sut.roman_numeral_for(70)).to(equal("LXX"))

        def test_it_returns_LXXX_for_number_80(self, sut):
            expect(sut.roman_numeral_for(80)).to(equal("LXXX"))

        def test_it_returns_XC_for_number_90(self, sut):
            expect(sut.roman_numeral_for(90)).to(equal("XC"))

        def test_it_returns_C_for_number_100(self, sut):
            expect(sut.roman_numeral_for(100)).to(equal("C"))

        def test_it_returns_CC_for_number_200(self, sut):
            expect(sut.roman_numeral_for(200)).to(equal("CC"))

        def test_it_returns_CCC_for_number_300(self, sut):
            expect(sut.roman_numeral_for(300)).to(equal("CCC"))

        def test_it_returns_CD_for_number_400(self, sut):
            expect(sut.roman_numeral_for(400)).to(equal("CD"))

        def test_it_returns_D_for_number_500(self, sut):
            expect(sut.roman_numeral_for(500)).to(equal("D"))

        def test_it_returns_DC_for_number_600(self, sut):
            expect(sut.roman_numeral_for(600)).to(equal("DC"))

        def test_it_returns_DCC_for_number_700(self, sut):
            expect(sut.roman_numeral_for(700)).to(equal("DCC"))

        def test_it_returns_DCCC_for_number_800(self, sut):
            expect(sut.roman_numeral_for(800)).to(equal("DCCC"))

        def test_it_returns_CM_for_number_900(self, sut):
            expect(sut.roman_numeral_for(900)).to(equal("CM"))

        def test_it_returns_M_for_number_1000(self, sut):
            expect(sut.roman_numeral_for(1000)).to(equal("M"))

        def test_it_returns_MMXXI_for_number_2021(self, sut):
            expect(sut.roman_numeral_for(2021)).to(equal("MMXXI"))
