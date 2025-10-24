import requests
import tkinter as tk
import re

root = tk.Tk()
root.configure()

root.geometry("1600x900")
url = "https://store.steampowered.com/api/appdetails?appids=1687950"
response = requests.get(url)
# "header_image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1687950/header.jpg"
# "capsule_image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1687950/capsule_184x69.jpg"
# "background": "https://cdn.cloudflare.steamstatic.com/steam/apps/1687950/page_bg_generated.jpg"

def clean_html(raw_html):
    # Remove video/image tags entirely
    cleaned = re.sub(r'<video.*?</video>', ' ', raw_html, flags=re.DOTALL)
    # Remove all other HTML tags
    cleaned = re.sub(r'<.*?>', ' ', cleaned)
    # Remove URLs
    cleaned = re.sub(r'http\S+', ' ', cleaned)
    return cleaned.strip()


if response.status_code == 200:
    data = response.json()

    app_data = data["1687950"]["data"]
    # print(app_data["name"])
    # print(app_data["release_date"]["date"])
    # print(app_data["developers"])
    # print(app_data["publishers"])
    # print(app_data["price_overview"]["final_formatted"])
    # print(app_data["short_description"])
    # minimum_specs = clean_html(app_data["pc_requirements"]["minimum"])
    # recc_specs = clean_html(app_data["pc_requirements"]["recommended"])
    # print(minimum_specs)
    # print(recc_specs)
    # print(app_data["website"])
    # for a in app_data["genres"]:
    #     print(a["description"])
    # clean_data_game = clean_html(app_data["about_the_game"])
    print(data)




