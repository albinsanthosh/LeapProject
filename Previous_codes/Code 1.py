import requests
import pandas as pd


f = open("token.txt","r")
token = f.read()
company_name = input('Enter company name:')


url = f"https://api.github.com/repos/{company_name}/contributors?access_token={token}"

response = requests.get(url)
data = response.json()
#print(data)
df = pd.DataFrame(columns=["Name", "Commits", "Organization"])
for item in data:
    name = item["login"]
    commits = item["contributions"]
    org_url = item["organizations_url"]
    org_url = org_url + "?access_token={}".format(token)
    #org_url = "".join([org_url, "?access_token={}".format(token)])
    #print(name, commits, org_url)
    org_response = requests.get(org_url).json()
    #print(org_response)
    for item1 in org_response:
        # if item1 == []:
        #     pass
        # else:
        #     org_name = item1["login"]
        #     print(org_name)
        if item1:
            org_name = item1["login"]
            #print(org_name)
            df = df.append({"Name": name,"Commits": commits,"Organization": org_name}, ignore_index=True)

print(df)
