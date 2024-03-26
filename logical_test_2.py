
"""
Convert Arabic Number to Roman Number.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).
"""

input = 999
def converArabicToRoman(input):
    if input not in range(1, 1001): return "out of range"
    
    specialNumber = [
        1000, 900, 
        500, 400, 
        100, 90, 
        50, 40, 
        10, 9, 
        5, 4,
        1
    ]
    specialRoman = [
        "M", "CM", 
        "D", "CD", 
        "C", "XC", 
        "L", "XL", 
        "X", "IX", 
        "V", "IV", 
        "I"
    ]
    result = ""
    while input > 0:
        for index in range(len(specialNumber)):
            indexNumber = int(index)
            if input - specialNumber[indexNumber] >= 0: 
                result += specialRoman[indexNumber]
                input -= int(specialNumber[indexNumber])
                break
    return result

output = converArabicToRoman(input)
print(output)