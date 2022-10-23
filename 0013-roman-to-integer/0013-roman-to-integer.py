class Solution:
    def romanToInt(self, s: str) -> int:
        value_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        special_value = {"CM": 900, "XC": 90, "IV": 4, "IX": 9, "XL": 40, "CD": 400}
        res = 0
        for items in special_value.items():
            if s.count(items[0]) > 0:
                for i in range(s.count(items[0])):
                    res += items[1]
                s = s.replace(items[0], "")
        for i in s:
            res += value_dict[i]
        return res