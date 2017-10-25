import requests
from bs4 import BeautifulSoup
import urllib.request
from argparse import ArgumentParser

print("\n\nNymph Image Scrapper\n\n")

parser = ArgumentParser(prog="hungry")
parser.add_argument('-m', '--muse', type=str)

args = parser.parse_args()

muse = str(args.muse).replace(' ','+')

url = "https://www.google.ro/search?q={muse}&tbm=isch".format(muse=muse)

nymph_r = requests.get(url)
nymph_s = BeautifulSoup(nymph_r.text, 'html.parser')

imgs = nymph_s.findAll('img')

i = 0

for img in imgs[1:]:
    print("[*] Getting ",muse+str(i), " from ",img.attrs["src"])
    urllib.request.urlretrieve(img.attrs["src"], "loot/"+muse+str(i))
    i += 1
