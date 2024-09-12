import random


def Convert_2_Ternary(Number, lenght):
    if Number == 0:
        return '0' * lenght
    nums = []
    while Number:
        Number, r = divmod(int(Number), 3)
        nums.append(str(r))
    numa = list(reversed(nums))

    for i in range(lenght - len(numa)):
        numa.insert(0, '0')

    return numa


numbers = "1122334455667788"
sum = 60

numbers = input()
sum = int(input())

Input_Array = list(str(numbers))

Number_Of_Digits = len(Input_Array) - 1

Rnd_Arr = []

if Number_Of_Digits > 9:
    while len(Rnd_Arr) < 5000:
        Byte_Map = []
        for i in range(Number_Of_Digits):
            Byte_Map.append(str(random.choices(['+', '*'], weights=(70, 30), k=1)[0]))
        num = ''.join(Byte_Map)
        if num not in Rnd_Arr:
            Rnd_Arr.append(num)
            Arr = []

            for index, item in enumerate(Input_Array):
                Arr.append(item)
                if index < len(Byte_Map):
                    if Byte_Map[index] != ' ':
                        Arr.append(' ')
                        Arr.append(Byte_Map[index])
                        Arr.append(' ')

            xd = ' '.join(str(int(x)) if x.isdigit() else x for x in ''.join(Arr).split())
            if eval(xd) == sum:
                print(xd.replace(' ', ''))
                exit()

    print('NO_SOLUTION')

else:
    Byte_Map = Convert_2_Ternary(0, Number_Of_Digits)

    for i in range(3 ** (Number_Of_Digits)):
        Byte_Map = Convert_2_Ternary(i, Number_Of_Digits)
        arr = []
        for index, item in enumerate(Byte_Map):
            if item == '0':
                arr.append('')
            elif item == '1':
                arr.append('+')
            elif item == '2':
                arr.append('*')

        arr3 = []
        for id, number in enumerate(Input_Array):
            arr3.append(number)
            if len(arr) > id:
                arr3.append(arr[id])

        Eq_String = ''.join(arr3)

        xd = True
        List = []
        for Sum in Eq_String.split('+'):
            List2 = []
            for Seq in Sum.split('*'):
                if Seq[0] == '0' and int(Seq) != 0:
                    List2.append(Seq.lstrip('0'))
                    xd = False
                else:
                    List2.append(Seq)
            List.append('*'.join(List2))

        # print(xdd)
        Edit_String = '+'.join(List)
        if sum == int(eval(Edit_String)) and xd:
            print(Eq_String)
            exit()

    print('NO_SOLUTION')