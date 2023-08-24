from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.basketball-reference.com/leaders/ast_career.html')
soup = BeautifulSoup(response.text, 'html.parser')

list = soup.find_all('td')

newList = list[0:250]

def every_nth(nums, nth):
  return nums[nth - 1::nth]

assists = every_nth(newList, 3)

print(f'The total number of players on the list is {str(len(newList))}.')

# get average of assists
totalAssists = 0
for item in assists:
    totalAssists += int(item.text)

print(f'The total number of assists is {totalAssists}.')
print(f'The average is {"%.2f" % (totalAssists / len(assists))} assists.')

print(f'The lowest number of assists is {assists[-1].text}.')
print(f'The highest number of assists is {assists[0].text}.')

# get the first quartile of assists
firstQuartile = assists[0:62]
totalFirstQuartile = 0
for item in firstQuartile:
    totalFirstQuartile += int(item.text)

print(f'The first quartile of assists is {"%.2f" % (totalFirstQuartile / len(firstQuartile))}.')

# get the second quartile of assists
secondQuartile = assists[62:125]
totalSecondQuartile = 0
for item in secondQuartile:
    totalSecondQuartile += int(item.text)

print(f'The second quartile of assists is {"%.2f" % (totalSecondQuartile / len(secondQuartile))}.')

# get the third quartile of assists
thirdQuartile = assists[125:187]
totalThirdQuartile = 0
for item in thirdQuartile:
    totalThirdQuartile += int(item.text)

print(f'The third quartile of assists is {"%.2f" % (totalThirdQuartile / len(thirdQuartile))}.')

# get the fourth quartile of assists
fourthQuartile = assists[187:250]
totalFourthQuartile = 0
for item in fourthQuartile:
    totalFourthQuartile += int(item.text)

print(f'The fourth quartile of assists is {"%.2f" % (totalFourthQuartile / len(fourthQuartile))}.')

# get the median of assists
median = assists[125].text
print(f'The median of assists is {median}.')
