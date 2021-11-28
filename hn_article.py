import requests
import json


# Make an API call, and store the response.
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore the structure of the data.
response_dict = r.json()
readable_file = 'data/readable_hn_data.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)

# Process results.
# print(f"{response_dict}")
# print(f'\n')
for a, b in response_dict.items():
    print(f"{a}: {b}")
# print(f'\n')
# for i in response_dict.keys():
#     print(f"{i}: {response_dict[i]}")
# print(f'\n')
# print(f"The len of the key kids is: {len(response_dict['kids'])} IDs.")
