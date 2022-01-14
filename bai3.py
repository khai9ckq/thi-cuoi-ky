
ho = input("Nhập họ: ")
ten dem = input("Nhập tên đệm: ")
ten = input("Nhập tên: ")
print(len(ho),len(tendem),len(ten))
n = int(input("Nhap so trên n = "));
def thuanNghich(n):
    str1 = str(n);
    str2 = str1[::-1]
    if (str1 == str2):
        return True;
    else:
        return False;
print(thuanNghich(n));



