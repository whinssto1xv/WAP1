days=int(input("enter total no of days"))
present=int(input("enter no of present days"))
eligible=present*100/days
if eligible>75:
    print("eligible")
else:
     print("not eligible")

