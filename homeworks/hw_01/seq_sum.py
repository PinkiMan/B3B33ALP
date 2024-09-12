# nums = list(map(int, input().split()))
nums = [4, -3, -2, -1, 6, 9, 1, 2, 8, 4, 1, 7]

last = 69

longest = []
array = []

for number in nums:
    IsPrime = True

    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                IsPrime = False
                break

    elif number == 1 or number == 0 or number == -1:
        IsPrime = False

    else:
        for i in range(2, abs(number)):
            if abs(number) % i == 0:
                IsPrime = False
                break

    if not IsPrime:
        if number < last or array == []:
            array.append(number)
        else:
            if len(array) > len(longest):
                longest = array
            elif len(array) == len(longest):
                if sum(array) > sum(longest):
                    longest = array
            array = [number]

    else:
        if len(array) > len(longest):
            longest = array
        elif len(array) == len(longest):
            if sum(array) > sum(longest):
                longest = array
        array = []

    last = number

if len(array) > len(longest):
    longest = array
elif len(array) == len(longest):
    if sum(array) > sum(longest):
        longest = array

print(len(longest))
print(sum(longest))
