#question2.py
#divisibility tests in the range of 1 and 100
  #by: amon

list1 = []
list2 = []
list3 = []
list4 = []
list5 = []

for i in range(1, 100):
    if i % 7 == 0 and i % 3 == 0:
        list1.append(i)
    if i % 7 == 0 and i % 3 != 0:
        list2.append(i)
        if i % 2 != 0:
            list3.append(i)
    sum_digits = sum(int(digit) for digit in str(i))
    if i % sum_digits == 0:
        list4.append(i)
    if (pow(sum_digits, 2)) == i:
        list5.append(i)

print("Numbers divisible by 7 and 3 are:", list1)
print("Numbers divisble by 7 and not 3 are: ", list2)
print("Odd numbers divisible by 7 and not 3 are: ", list3)
print("Numbers divisible by sum of its digits are: ", list4)
print("Numbers that are equal to the square sum of its digits are: ", list5)
