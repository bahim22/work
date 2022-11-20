import random
import string
def getRandomString(length):
    letters = string.ascii_lowercase
    # concat strings; ex: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
    resultStr = ''.join(random.choice(letters) for i in range(length))

    print("random string wjjof length", length, "is: ", resultStr)

# ex. exe
getRandomString(8)
