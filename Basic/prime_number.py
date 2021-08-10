for i in range(2,101):
    for j in range(2,int(i/2)+1):
        if i%j==0:
            print(i, " is not a prime number")
            break
    else:
        print(i, " is a prime number")