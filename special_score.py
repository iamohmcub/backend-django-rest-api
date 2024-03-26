"""
เขียนโปรแกรมอะไรก็ได้ที่อยาก present Python's skill set เจ๋ง ๆ ของตัวเอง
ข้อนี้ไม่ต้องทำก็ได้ ไม่มีผลลบกับการให้คะแนน แต่ถ้าทำมาเเล้วเจ๋งจริง ก็จะพิจารณาเป็นพิเศษ

"""
input = 1040320

# เป็นลอจิกเกี่ยวกับการถอนเงินที่ตู้ ATM 
# เหตุเกิดจากความสงสัยเวลาเราไปถอนเงิน 
# ตู้ ATM จะรู้ได้อย่างไรว่าต้องให้แบงค์อะไรบ้าง

def bankWithdraw(input):
    availableBank = [1000, 500, 100, 50, 20]
    result = {}
   
    for bank in availableBank:
        count = input // bank
        input %= bank
        result[f"แบงค์ {bank}"] = count
    return result

output = bankWithdraw(input)
print(output)