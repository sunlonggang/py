tmp = input("猜写一个数\n");
guess = int(tmp)
while guess != 8:
    print("猜错了");
    tmp = input("请继续\n")
    guess = int(tmp)
print("你很厉害了")