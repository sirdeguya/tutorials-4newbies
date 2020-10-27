import requests
import random

response = requests.get('https://jsonplaceholder.typicode.com/todos')
#print(response.status_code)
#print(dir(response))

## Read the documentaion: https://requests.readthedocs.io/en/master/api/#requests.Response

#print(response.json)
#print(type(response.json))
#print(type(response.json()))
#print(response.json())
#print(len(response.json()))


# def print_numbers():
#     for i in range(20):
#         print(f'i is: {i}')
#         x = random.randint(0,100)
#         print(i*x)
#
#
# print_numbers()