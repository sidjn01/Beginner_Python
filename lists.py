# ipAddress = input("PLease enter an IP address:")
# print(ipAddress.count("."))

parrot_list = ["non pinin", "no more", "a stiff", "bereft of live"]

for state in parrot_list:
    print("This parrot is " + state)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
numbers_in_order = sorted(numbers)

if numbers == numbers_in_order:
    print("Lists are equal")
else:
    print("Lists are not equal")

