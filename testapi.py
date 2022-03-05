import requests
import json

try:
    fetchapi = "https://programming-quotes-api.herokuapp.com/Quotes/random"
    response = requests.get(fetchapi)
    thoughtJSON = json.loads(response.text)

    quote = thoughtJSON['en']
    author = thoughtJSON['author']

    print(f"{quote} \n by {author} ")
except:
    print("problem with fetching thought api")


#There's only one trick in software, and that is using a piece of software that's already been written. 
 #by Bill Gates 