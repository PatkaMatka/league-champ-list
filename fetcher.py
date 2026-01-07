import requests

versions = requests.get("https://ddragon.leagueoflegends.com/api/versions.json").json()
data_in = requests.get(f"https://ddragon.leagueoflegends.com/cdn/{versions[0]}/data/en_US/champion.json").json()


open("names.csv", "w").close()

with open("names.csv", "a") as file:
    file.write("Name\n")
    for champ in data_in["data"].values():
        file.write(f"\"{champ["name"]}\"\n")
        print(f"Added {champ["name"]}\n")
