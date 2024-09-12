

input=str(input())
date_number='28.6.2540'
if input[0].isdigit():
    date_number=input
    if input.count('.') != 2:
        print('ERROR')
        exit()
#print(date_number)

try:
    day_number=date_number.split('.')[0]
    month_number=date_number.split('.')[1]
    year_number=date_number.split('.')[2]
except:
    print('ERROR')
    exit()

if int(month_number)>12 or int(month_number)<1 :
    print('ERROR')
    exit()

if int(year_number)>9999 or int(year_number)<1:
    print('ERROR')
    exit()

leng=[31,29,31,30,31,30,31,31,30,31,30,31]

if int(day_number)<1 or int(day_number)>31:
    print('ERROR')
    exit()

if int(day_number)>leng[int(month_number)-1]:
    print('ERROR')
    exit()


Day_P=['first', 'second', 'third', 'fourth', 'fifth','sixth','seventh','eighth', 'ninth','tenth','eleventh','twelveth','thirteenth','fourteenth','fifteenth','sixteenth','seventeenth','eighteenth','nineteenth','twentieth']
Day_L=['twenty','thirty']
year_2=['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
Months=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
year_1=['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
year_3=['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine','ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']

string=''

if int(day_number)>=20:
    if int(day_number)<30 and int(day_number)!=20:
        string+='the '+Day_L[0]+'-'+Day_P[int(day_number)-21]

    elif int(day_number)==31:
        string +='the thirty-first'
    elif int(day_number)==20:
        string +='the twentieth'
    elif int(day_number)==30:
        string +='the thirtieth'
else:
    string +='the ' + Day_P[int(day_number)-1]

string+=' of '+Months[int(month_number)-1]

if len(year_number)==4:
    if int(list(year_number)[0]) != 0:
        string +=' '+year_1[int(list(year_number)[0])-1]+'thousand'
        year_number=year_number[-3:]
else:
    string+=' '

if len(year_number)>=3:
    if int(list(year_number)[0])!=0:
        string +=year_1[int(list(year_number)[0])-1]+'hundred'
        year_number = year_number[-2:]

if len(year_number)>=2:
    if int(year_number)==0:
        string +=''
    elif int(year_number)<=20:
        string +=year_3[int(year_number)-1]

    else:
        if int(year_number[-2:][0]) in [0,1,2]:
            if int(year_number[-2:][0])==2 and int(year_number[-2:][1])==0:
                string +='twenty'
            elif int(year_number[-2:][0])==2:
                string +='twenty'+year_1[int(year_number[-2:][1])-1]

        else:
            xd=int(year_number[-2:][1])
            xd1=int(year_number[-2:][0])
            yl=(['']+year_2)
            yt=(['']+year_1)
            xa=yl[int(year_number[-2:][0])-1]
            xb=yt[int(year_number[-2:][1])]
            string+= yl[int(year_number[-2:][0])-1]+yt[int(year_number[-2:][1])]
#print('\n'+string)
"""--------------------------------------------------------"""



if not input[0].isdigit():
    date_lett=input

else:
    date_lett='the thirty-first of December threethousandtwohundrednineteen'


if not 'the' in date_lett or not 'of' in date_lett:
    print('ERROR')
    exit()


date_scrap=date_lett.replace('the ','').replace('of ','')

try:
    day_lett=date_scrap.split(' ')[0]
    month_lett=date_scrap.split(' ')[1]
    year_lett=date_scrap.split(' ')[2]
except:
    print('ERROR')
    exit()


if month_lett not in Months:
    print('ERROR')
    exit()


leng=[31,29,31,30,31,30,31,31,30,31,30,31]



month_lett_num=str(Months.index(month_lett)+1)


if '-' in day_lett:
    if day_lett=='thirty-first':
        day_lett_num=str(31)

    elif day_lett.split('-')[0]=='twenty':
        day_lett_num=str(21+int(Day_P.index(day_lett.split('-')[1])))

    else:
        print('ERROR')
        exit()

else:
    if day_lett=='thirtieth':
        day_lett_num=str(30)
    elif day_lett=='twentieth':
        day_lett_num=str(20)
    else:
        if day_lett in Day_P:
            day_lett_num=str(Day_P.index(day_lett)+1)
        else:
            print('ERROR')
            exit()



year_lett_num=0
for item in year_1:
    if year_lett.startswith(item) and ('thousand' in year_lett or 'hundred' in year_lett) :
        year_lett_num=year_1.index(item)+1
        if year_lett.replace(item,'').startswith('thousand'):
            year_lett_num*=1000

            year_lett= str(year_lett.split('thousand')[1].replace('thousand', ''))

            if 'hundred' in year_lett:
                for item2 in year_1:
                    if year_lett.startswith(item2):
                        year_lett_num += 100 * (year_1.index(item2)+1)
                        year_lett = str(year_lett.split('hundred')[1].replace('hundred', ''))

                        break

        elif year_lett.replace(item,'').startswith('hundred'):
            year_lett_num*=100
            year_lett = str(year_lett.split('hundred')[1].replace('hundred', ''))
        break

if year_lett in year_3:
    year_lett_num+=year_3.index(year_lett)+1
else:
    for mont in year_2:
        if year_lett.startswith(mont):
            year_lett_num+=(year_2.index(mont)+2)*10
            year_lett=year_lett.replace(mont,'')

            for da in year_1:
                if year_lett.startswith(da):
                    year_lett_num += (year_1.index(da)+1)



#print('\n'+year_lett)

if int(day_lett_num)>leng[int(month_lett_num)-1]:
    print('ERROR')
    exit()

if input[0].isdigit():
    print(string)
else:
    print(day_lett_num+'.'+month_lett_num+'.'+str(year_lett_num))


