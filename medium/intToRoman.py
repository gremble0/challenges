class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        romanStr = ""

        while num > 0:
            match num:
                case _ if num >= 1000:
                   romanStr += "M"
                   num -= 1000
                case _ if num >= 900:
                    romanStr += "CM"
                    num -= 900
                case _ if num >= 500:
                    romanStr += "D"
                    num -= 500
                case _ if num >= 400:
                    romanStr += "CD"
                    num -= 400
                case _ if num >= 100:
                    romanStr += "C"
                    num -= 100
                case _ if num >= 90:
                    romanStr += "XC"
                    num -= 90
                case _ if num >= 50:
                    romanStr += "L"
                    num -= 50
                case _ if num >= 40:
                    romanStr += "XL"
                    num -= 40
                case _ if num >= 10:
                    romanStr += "X"
                    num -= 10
                case _ if num >= 9:
                    romanStr += "IX"
                    num -= 9
                case _ if num >= 5:
                    romanStr += "V"
                    num -= 5
                case _ if num >= 4:
                    romanStr += "IV"
                    num -= 4
                case _:
                    romanStr += "I"
                    num -= 1

        return romanStr
