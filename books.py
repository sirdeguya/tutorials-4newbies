import requests
import json

#
# Don't touch this
#
STATUS = 'Fail'
TEXT_TO_FIND = 'placeat quia et porro iste'
URLS = dict(
    posts='https://jsonplaceholder.typicode.com/posts',
    users='https://jsonplaceholder.typicode.com/users',
)
posts_response = json.loads(requests.get(URLS['posts']).content)
users_response = json.loads(requests.get(URLS['users']).content)
users = []


class User:
    def __init__(self, id, name, username, email, phone):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.phone = phone
        self.posts = []


#
# Work on this
#
for user in users_response:
    new_user = User(
        id=user['id'],
        name=user['name'],
        username=user['user_name'],
        email=user['email'],
        phone=user['phone'],
    )
    for post in posts_response:
        if post['user_id'] == new_user.id:
            new_user.post.append(post)
    users.append(new_user)


#
# Dont touch this
#
if users[8].posts[5]['title'] == TEXT_TO_FIND:
    STATUS = 'Success'
print(f'End result: {STATUS}')



