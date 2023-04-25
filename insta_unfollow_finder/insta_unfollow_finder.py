import instaloader
import getpass
username = input("please enter your username: ")
password = getpass.getpass("please enter your password: ")
f = open("followers.txt", "r")
old_followers = []
for line in f:
    old_followers.append(line)
f.close

L = instaloader.Instaloader()
L.login(username, password)
profile = instaloader.Profile.from_username(L.context, username)

new_followers = []
for follower in profile.get_followers():
    new_followers.append(follower)

for old_followers in old_followers:
    if old_followers not in new_followers:
        print(old_followers)

f = open("followers.txt", "w")
for follower in new_followers:
    f.write(follower + "\n")