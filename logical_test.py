# """
# Convert Number to Thai Text.
# เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
# โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

# *** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
# ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

# """

input = 911

def convertArabicToThai(input):
    if input not in range(0, 10000000): return "out of range"
    
    thaiWords = ["ศูนย์", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
    thaiUnits = ["", "สิบ", "ร้อย", "พัน","หมื่น","แสน","ล้าน"]

    inputString = str(input)
    inputLength = len(inputString)

    if inputLength == 1: return thaiWords[input]

    result = ""
    for index in range(inputLength):
        indexNumber = int(index)
        inputNumber = int(inputString[indexNumber])

        word = thaiWords[inputNumber]
        unit = thaiUnits[inputLength - indexNumber - 1]

        if word == "ศูนย์": continue

        word = checkLastIndex(inputLength, word, index)
        word = checkSecondLastIndex(inputLength, word, index)

        result += word + unit

    return result

def checkLastIndex(inputLength, word , index):
    if index == inputLength-1 and word == "หนึ่ง": 
        word = "เอ็ด"
    return word

def checkSecondLastIndex(inputLength,word, index):
    if index == inputLength-2:
        if word == "หนึ่ง": word = ""
        if word == "สอง": word = "ยี่"
    return word

output = convertArabicToThai(input)
print(output)
