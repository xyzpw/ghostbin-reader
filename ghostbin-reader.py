#!/usr/bin/env python3

import requests, re

replace_list = {"&nbsp;": " ", "&amp;": "&", "&lt;": "<", "&gt;": ">", "&quot;": "\"", "&apos;": "'", "&cent;": "¢", "&pound;": "£", "&yen;": "¥", "&euro;": "€", "&copy;": "©", "&reg;": "®"}
start_text_match = "<textarea id=\"editor\" name=\"content\">"
end_text_match = "</textarea>"
url = input("https://ghostbin.me/")

packet = requests.get(f"https://ghostbin.me/{url}")
if (start_text_match not in packet.text) or (end_text_match not in packet.text):
    exit("url is broken or non-existent - exiting")

start = packet.text.find(start_text_match) + len(start_text_match)
end = packet.text.find(end_text_match)

content = packet.text[start:end]
for key in replace_list:
    content = re.sub(key, replace_list[key], content)

print("\n" + content + "\n")
