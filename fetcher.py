import requests

versions = requests.get("https://ddragon.leagueoflegends.com/api/versions.json").json()
data_in = requests.get(f"https://ddragon.leagueoflegends.com/cdn/{versions[0]}/data/en_US/champion.json").json()

print("Name")

for champ in data_in["data"].values():
    print(champ["name"])

