'''
Application Programming Interfaces (APIs) connect 
many different types of devices that access the internet. 
An API specifies how software components should interact, 
and an understanding of this type of program is essential 
for development of web applications. You will look at how 
information is exchanged on the internet through API endpoints 
on a server that stores data.
'''

# TODO 1 - run, you may need to pip install requests
import json, requests

print("\n--- part 1: agify, a dictionary ---")
url = 'https://api.agify.io/?name=' + 'TODO'
# getting the response, figuring out what we get

print("type of data:")
print("response:")
# get specific information
print("just the predicted age:")



# displaying useful info
print("\nthe best info:")



# TODO - look at the documentation https://agify.io/documentation






print("\n\n--- part 2: nationalize, a dictionary with lists of dictionaries ---")
url = 'https://api.nationalize.io?name=' + 'TODO'

# getting the response, figuring out what we get

print("type of data:", )
print("response:")


# get specific information, dig deep!!




# displaying useful info
print("\nthe best info:")




# TODO look at the documentation https://nationalize.io/documentation





# TODO look at the documentation https://icanhazdadjoke.com/api 

print("\n\n--- part 3: dad joke, a dictionary ---")
url = 'https://icanhazdadjoke.com/'
heads = {'Accept': 'application/json'} # required on this one

# get the response, figure out what we get
print("data type:")
print("the response")

# get specific information
print("the id:")
print("the joke:")






print("\n\n--- part 4: multiple requests ---")
# make a list of 10 requests



# create a list of jokes with 'dog' in the description
dog_jokes = []


print("\nhere are the dog jokes:", dog_jokes)








