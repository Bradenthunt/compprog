#Fizzbuzz
def fizz_buzz(end_point):
    for i in range(end_point):
        if i % 15 == 0:
            print('FIZZBUZZ')
        elif i % 5 == 0: 
            print('Buzz')
        elif i % 3 == 0:
            print('Fizz')
        else:
            print(i)
fizz_buzz(100)

#API stuff
# import requests, json, webbrowser

# def doggie():
#     f = r"https://random.dog/woof.json"
#     page = requests.get(f)
#     data = json.loads(page.text)
#     webbrowser.open(data["url"])
# doggie()