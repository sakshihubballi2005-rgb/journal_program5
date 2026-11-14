def simple_interest(principal, interest, time):
    return (principal*interest*time)/100

if_name_ =="_main_":
    p = int(input("Enter Principal Amount:"))
    r = int(input("Enter Rate of Interest:"))
    t = int(input("Enter Time:"))

    print("simple interest is:",simple_interest(p, i, t))