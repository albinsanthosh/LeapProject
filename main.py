import requests
import pandas as pd
personal_token = 'Your personal token'
org_dict = {'Misc':{'total_contributions': 0,'unique_contributors': 0, "id": []}}

# Getting all Commits data
since_date = '2021-01-25'
until_date = '2021-01-30'
repo_name = 'Hashicorp/consul'
df = pd.DataFrame()
n = 1
total_commits = 0
while True:
    info_url = f'https://api.github.com/repos/{repo_name}/commits?page={n}&per_page=100&access_token={personal_token}&since={since_date}&until={until_date}'
    commit_info = requests.get(info_url).json()
    if commit_info:
        no_of_items = len(commit_info)
        print(no_of_items)
        total_commits = total_commits + no_of_items
        print("Total commits ",total_commits)
        df = pd.concat([df, pd.DataFrame(commit_info)], ignore_index=True)
        n = n + 1
        print(df.shape)
    else:
        print("Completed")
        break

data = df

for commit in data['commit']:
    email = commit['author']['email']
    email_end = email.split('@')
    company_name = email_end[1].split('.')
    company = company_name[0]

    # If the organization is users.noreply.github.com e.x. mikemorris@users.noreply.github.com, johncowen@users.noreply.github.com
    # For Total contributions, increase the count
    # For unique contributors, if email-id is in list, we will skip his commit i.e. multiple commits

    if company == 'users':
        org_dict['Misc']['total_contributions'] = org_dict['Misc']['total_contributions'] + 1
        if email not in org_dict['Misc']['id']:
            org_dict['Misc']['id'].append(email)  # org id List
            org_dict['Misc']['unique_contributors'] = org_dict['Misc']['unique_contributors'] + 1
# If organization is not users.noreply.github.com, make a new key as company name.
    else:
        if company in org_dict.keys():
            org_dict[company]['total_contributions'] = org_dict[company]['total_contributions'] + 1
        else:
            org_dict[company] = {'total_contributions': 1, 'unique_contributors': 0, 'id': []}
        if email not in org_dict[company]['id']:
            org_dict[company]['id'].append(email)       # org id List
            org_dict[company]['unique_contributors'] = org_dict[company]['unique_contributors'] + 1


for organization in org_dict:
    org_dict[organization].pop('id')


print(org_dict)