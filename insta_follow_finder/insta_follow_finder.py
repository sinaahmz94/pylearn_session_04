import instaloader
import getpass


username = input("please enter your username: ")
password = getpass.getpass("please enter your password: ")

old_followers = []
f = open("followes2.txt", "r")
for line in f:
    old_followers.append(line)

l = instaloader.Instaloader()
l.login(username, password)
profile = instaloader.Profile.from_username(l.context, username)

new_followers = []
for follower in profile.get_followers():
    new_followers.append(follower)

for new_followers in new_followers:
    if new_followers not in old_followers:
        print(new_followers)
