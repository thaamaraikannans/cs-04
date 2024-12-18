# import requests

# response = requests.get("https://s05.hotshare.link/Mardini_2024_360p_Original_HD.mp4", stream=True)

# with open("F:\\IMS\\dog.mp4", "wb") as f:
#     for value in response.iter_content(1024):
#         f.write(value)

import os

os.chmod("award.txt", 0o777)
print(os.access("award.txt", os.R_OK))
print(os.access("award.txt", os.W_OK))