import requests


# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:javascript&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
# Store API response in a variable.
response_dict = r.json()

# Process results.
print(response_dict.keys())
print(f"Total repositories: {response_dict['total_count']:,.2f}")

# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")


print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']:,.2f} - \U00002B50")
    print(f"Size: {repo_dict['size']/1000:,.1f} MB - \U0001F4BE")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}\n")
    # print(f"\nKeys: {len(repo_dict)}")
    # for key in sorted(repo_dict.keys()):
    #     print(key)
