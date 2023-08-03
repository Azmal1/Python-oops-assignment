# 1) Write a python class to convert an integer into a roman numeral and viceversa
# class py_solution:
#     def int_to_Roman(self, num):
#         val = [
#             1000, 900, 500, 400,
#             100, 90, 50, 40,
#             10, 9, 5, 4,
#             1
#             ]
#         syb = [
#             "M", "CM", "D", "CD",
#             "C", "XC", "L", "XL",
#             "X", "IX", "V", "IV",
#             "I"
#             ]
#         roman_num = ''
#         i = 0
#         while  num > 0:
#             for j in range(num // val[i]):
#                 roman_num += syb[i]
#                 num -= val[i]
#             i += 1
#         return roman_num


# print(py_solution().int_to_Roman(40))
# print(py_solution().int_to_Roman(4000))







import roman
class romantoint:
    def romann(self,num):
       return roman.fromRoman(num)
    def romannn(self,num):
        return roman.toRoman(num)





convert=romantoint()

number="X"
res=convert.romann(number)
print(res)


number=40
res1=convert.romannn(number)
print(res1)