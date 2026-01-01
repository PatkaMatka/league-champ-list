import requests
from PIL import Image
from io import BytesIO
import os
import shutil

new_folder = "icons"
if os.path.exists(new_folder):
    shutil.rmtree(new_folder)
os.makedirs(new_folder)

URL_IMG = f"https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champion-icons"
URL_ID = "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champion-summary.json"

id_in = requests.get(URL_ID).json()

for champion in id_in:
    print(f"Processing {champion["name"]}")
    img_in = requests.get(f"{URL_IMG}/{champion["id"]}.png")
    i = Image.open(BytesIO(img_in.content))
    rescaled_i = i.resize((50,50))
    rescaled_i.save(f"icons/{champion["name"]}.png")
