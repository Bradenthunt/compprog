car_color = "Blue"
car_make = "Tesla"

if car_color == "Blue":
    if car_make == "Tesla":
        print("My car is a Blue Tesla")
    else: 
        print("My car is blue")
elif car_color == "Red":
    print('My car is a ferrari')
else:
    print("I just have a bike")

# for loop
for i in range(1, 10):
    print(i)

sports = ['soccer', 'basketball', 'hockey', 'football']
print(sports)

for item in sports:
    print(item)

i = 1
while i < 6:
  print("I'm still going")
  i += 1

for i in range(50):
    if i > 24:
        break
    else:
        print(i)