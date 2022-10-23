class Solution:
    def intToRoman(self, num: int) -> str:
        units_dict = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9}
        dozens_dict = {"X": 10, "XX": 20, "XXX": 30, "XL": 40, "L": 50, "LX": 60, "LXX": 70, "LXXX": 80, "XC": 90}
        hundreds_dict = {"C": 100, "CC": 200, "CCC": 300, "CD": 400, "D": 500, "DC": 600, "DCC": 700, "DCCC": 800, "CM": 900}
        thousands_dict = {"M": 1000, "MM": 2000, "MMM": 3000}

        multiplier = 1
        str_number = str(num)[::-1]
        res = []

        for digit in str_number:
            if int(digit) == 0:
                print("0 !")
                multiplier *= 10
            else:
                if multiplier == 1:
                    for items in units_dict.items():
                        if items[1] == int(digit):
                            res.append(items[0])
                            multiplier *= 10
                elif multiplier == 10:
                    for items in dozens_dict.items():
                        if items[1] == int(digit) * multiplier:
                            res.append(items[0])
                            multiplier *= 10
                elif multiplier == 100:
                    for items in hundreds_dict.items():
                        if items[1] == int(digit) * multiplier:
                            res.append(items[0])
                            multiplier *= 10
                elif multiplier == 1000:
                    for items in thousands_dict.items():
                        if items[1] == int(digit) * multiplier:
                            res.append(items[0])
                            multiplier *= 10

        return "".join(res[::-1])