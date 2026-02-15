Limit = 20
d = 2
prime = []
for number in range(2,Limit+1):
    ok=True
    for d in range(2,number):
        if number%d==0:
            break;
    else:
        prime.append(number)
print(prime[::2]) #print din doi in doi
