import requests

AGIFY_ENDPOINT = "https://api.agify.io?name="
GENDERIZE_ENDPOINT = "https://api.genderize.io/?name="
POSTS_URL = "https://api.npoint.io/c790b4d5cab58020d391"

# name = "fukurou"

# genderize_data = requests.get(f"{GENDERIZE_ENDPOINT}{name}").json()
# predicted_gender = genderize_data['gender']
# print(genderize_data)

all_posts = requests.get(POSTS_URL).json()
print(all_posts)