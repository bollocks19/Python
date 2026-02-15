numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]
even_numbers = []
odd_numbers=[]
for number in numbers:
    if(number%2==0):
        even_numbers.append(number)
    else: odd_numbers.append(number)
print(even_numbers)
print(odd_numbers)
