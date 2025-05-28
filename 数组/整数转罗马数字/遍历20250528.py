# 由题可以知道1<=num<=3999，因此可以将num拆分为千分位、百分位、十位数和个位数
# 1. 千位从1到3依次为M, MM, MMM
# 2. 百位从1到9依次为C, CC, CCC, CD, D, DC, DCC, DCCC, CM
# 3. 十位从1到9依次为X, XX, XXX, XL, L, LX, LXX, LXXX, XC
# 4. 个位从1到9依次为I, II, III, IV, V, VI, VII, VIII, IX
# 将num拆分各个数位的公式为：
# 1. 千位为num//1000
# 2. 百位为num//100 mod 10
# 3. 十位为num//10 mod 10
# 4. 个位为num mod 10
class Solution:
    def intToRoman(self, num: int) -> str:
        R=(
            ("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"), # 个位
            ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"), # 十位
            ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"), # 百位
            ("", "M", "MM", "MMM") # 千位
        )

        return R[3][num//1000]+R[2][num//100%10]+R[1][num//10%10]+R[0][num%10]