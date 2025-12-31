print('=================')
print('Area Calculator 📐')
print('=================')

print('1) Triangle')
print('2) Rectangle')
print('3) Square')
print('4) Circle')
print('5) Quit')

response = int(input('Which shape: '))

if response == 1:
    base = int(input('Enter base: '))
    height = int(input('Enter height: '))
    area = (base * height) / 2
    print('The area is: ' + str(area))
if response == 2:
    length = int(input('Enter length: '))
    width = int(input('Enter width: '))
    area = (length * width)
    print('The area is: ' + str(area))
if response == 3:
    side = int(input('Enter length of side: '))
    area = side ** 2
    print('The area is: ' + str(area))
if response == 4:
    radius = int(input('Enter radius: '))
    area = 3.14 * (radius ** 2)
    print('The area is: ' + str(area))
if response == 5:
    print('Goodbye!')
