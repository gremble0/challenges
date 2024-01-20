class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        romanStr = ""

        while num > 0:
            if num >= 1000:
                romanStr += "M"
                num = num - 1000
            elif num >= 900:
                romanStr += "CM"
                num = num - 900
            elif num >= 500:
                romanStr += "D"
                num = num - 500
            elif num >= 400:
                romanStr += "CD"
                num = num - 400
            elif num >= 100:
                romanStr += "C"
                num = num - 100
            elif num >= 90:
                romanStr += "XC"
                num = num - 90
            elif num >= 50:
                romanStr += "L"
                num = num - 50
            elif num >= 40:
                romanStr += "XL"
                num = num - 40
            elif num >= 10:
                romanStr += "X"
                num = num - 10
            elif num >= 9:
                romanStr += "IX"
                num = num - 9
            elif num >= 5:
                romanStr += "V"
                num = num - 5
            elif num >= 4:
                romanStr += "IV"
                num = num - 4
            else:
                romanStr += "I"
                num = num - 1

        return romanStr
