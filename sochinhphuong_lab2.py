def isSquareNumber(num):
    if number <= 0:
        return False
    else:
        isSquareNum = False
        for i in range(1, number + 1):
            if i * i == number:
                isSquareNum = True
                break
        
        if isSquareNum == True:
            return True
        else:
            return False
number = int (input("Nhap vao mot so nguyen:"))

result = isSquareNumber(number)

if result == True:
    print( number, " la so chinh phuong")
else:

    print(number, " khong phai la so chinh phuong")
