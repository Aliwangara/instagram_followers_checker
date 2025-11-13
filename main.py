import json

followers = 'utils/followers_1.json'
following = "utils/following.json"

followers_list  = []
following_list = []
not_following_back = []

def get_followers():

 with open(followers,'r') as f:
  load = json.load(f)
#   print(load)
  for load_item in load:
   get_follower = load_item.get('string_list_data')
   for follower_info in get_follower:
    follower_name = follower_info.get("value")
    name_method = follower_name.strip().lower()
    followers_list.append(name_method)
get_followers()

# print(f"Follower List: {followers_list}") 

def get_following():
 
 with open(following,'r') as f:
  load_following = json.load(f)
#   print(load_following)
  get_following_info = load_following.get('relationships_following')
  for user_name in get_following_info:
   get_user_name = user_name.get('title')
   user_name_method = get_user_name.strip().lower()
   following_list.append(user_name_method)

get_following()

# print(f"Following List: {following_list}")


def check_following():
    not_following_back = []
    for user in following_list:
        if user not in followers_list:
            not_following_back.append(user)
    return not_following_back

result = check_following()
print(f"Not following: {result}")