###################################
#	         Made by e303			      #
#  use for ethical purposes only  #
#								                  #
#you may share/redistribute this  #
#while giving credit to the owner #
#i am not responsible for anything#
###################################
import os
import requests

subreddits = ["boykisser3", "boykisser4", "sillycat"] #add/change subs if you want
image_limit = 30  # images per subreddit
save_folder = "images"
os.makedirs(save_folder, exist_ok=True)

headers = {
    "User-Agent": "Mozilla/5.0"
}

count = 0
for subreddit in subreddits:
    print(f"getting from r/{subreddit}...")
    url = f"https://www.reddit.com/r/{subreddit}/top/.json?limit={image_limit}&t=all"
    res = requests.get(url, headers=headers)
    items = res.json()["data"]["children"]

    for item in items:
        img = item["data"].get("url_overridden_by_dest", "")
        if img.endswith((".jpg", ".png", ".jpeg")):
            try:
                content = requests.get(img, headers=headers).content
                with open(os.path.join(save_folder, f"{subreddit}_img_{count}.jpg"), "wb") as f:
                    f.write(content)
                count += 1
            except:
                pass

print(f"Downloaded {count} images from {', '.join(subreddits)}")
