import argparse
import requests
from bs4 import BeautifulSoup
import os
import re

# argument parsing

parser=argparse.ArgumentParser(description="Extract biographies of scientists from Wikipedia")

parser.add_argument("name",type=str,help="Name of scientist")
parser.add_argument("--output",type=str,help="Output file name (without extension)")

args=parser.parse_args()

# fetch web page

scientist_name=args.name.replace(" ","_")
url="https://en.m.wikipedia.org/wiki/"+scientist_name
headers={
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; Mobile)",
    "Accept-Language": "en-US,en;q=0.9"
}

response=requests.get(url,headers=headers,timeout=10)

print("Final URL:", response.url)
print("Status code:", response.status_code)


if response.status_code!=200:
    print("Wikipedia page not found")
    exit()

# parse html using beautiful soup

soup=BeautifulSoup(response.text,"lxml")

title=soup.find("h1").text

content=soup.find("div",class_="mw-parser-output")
paragraphs=[]
for p in content.find_all("p",recursive=False):
    if p.text.strip():
        text = re.sub(r'\[.*?\]', '', p.text).strip()
        paragraphs.append(text)
    if len(paragraphs) == 2:
        break
biography="\n".join(paragraphs)

infobox=soup.find("table",class_="infobox")
infobox_data={}
if infobox:
    for row in infobox.find_all("tr"):
        if row.th and row.td:
            key = re.sub(r'\[.*?\]', '', row.th.text).strip()
            value = re.sub(r'\[.*?\]', '', row.td.text).strip()
            infobox_data[key] = value

# output file

os.makedirs("output",exist_ok=True)
file_path=f"output/{args.output}.txt"

with open(file_path,"w",encoding='utf-8') as f:
    f.write(f"Name: {title}\n\n")
    f.write("Biography: \n")
    f.write(biography+"\n\n")
    f.write("Infobox details: \n")
    for key,value in infobox_data.items():
        f.write(f"{key} : {value}\n")

print(f"Biography saved to {file_path}")
