import requests
import pandas as pd
personal_token = 'Enter token'
org_dict = {'Misc':{'total_contributions': 0,'unique_contributors': 0, "id": []}}

# Getting all Commits data
since_date = '2021-01-15'
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

#df.to_excel(f'check_commits.xlsx', sheet_name='Test')


# Data processing
#data = pd.read_excel('check_commits.xlsx')
data = df
# To get the users organization api url of the commits

for author_info in data['author']:
    #author_info = eval(author_info)
    org_url = author_info['organizations_url']
    usr_org_info = requests.get(org_url+f"?access_token={personal_token}").json()
    co = pd.DataFrame(usr_org_info)
    # if the organization is empty
    if not usr_org_info:
        org_dict['Misc']['total_contributions'] = org_dict['Misc']['total_contributions'] + 1
        if author_info['id'] not in org_dict['Misc']['id']:
            org_dict['Misc']['id'].append(author_info['id'])  # org id List
            org_dict['Misc']['unique_contributors'] = org_dict['Misc']['unique_contributors'] + 1  # Addition of unique id to unique contributions

    else:
        for items in co['login']:
            if items in org_dict.keys():
                org_dict[items]['total_contributions'] = org_dict[items]['total_contributions'] + 1
            else:
                org_dict[items] = {'total_contributions': 1, 'unique_contributors': 0, 'id': []}
            if author_info['id'] not in org_dict[items]['id']:
                org_dict[items]['id'].append(author_info['id'])       # org id List
                org_dict[items]['unique_contributors'] = org_dict[items]['unique_contributors'] + 1 # Addition of unique id to unique contributions



for organization in org_dict:
    org_dict[organization].pop('id')

print("\n")
print(org_dict)
