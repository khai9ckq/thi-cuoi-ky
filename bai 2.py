
middlename = input("Nhập tên đệm :")
print(middlename)
name=str(input("Nhập tên : "));
n=str(len(middlename))+str(len(name));
n_len=len(n)
sum=0
for i in range(n_len):
    n_val=n[i]
    sum=sum+int(n_val)
print("Tổng các ký tự là: ",sum)