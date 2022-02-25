
# import library
from bs4 import BeautifulSoup
import requests
import os
import time
from googlesearch import search

def getSongLink(url = None):
    if url is None:
        return ""
    try:
        req=requests.get(url)
        content=req.text
        soup=BeautifulSoup(content, features="html.parser")
        atag = soup.findAll('a')
        last = ""
        print("length of atag {}".format(len(atag)))
        for i in atag:
            if i["href"].endswith(".mp3"):
                last = i["href"]
        return last
    except Exception as e:
        print("Error", e)
        return ""

def downloadfromDirectUrl(url, downloadLocation):
    try:
        fname = url.split('/')[-1]
        print("Song Name",fname)
        start = time.time()
        print("DOWNLOAD STARTED....")
        r = requests.get(url, allow_redirects=True)
        print("DOWNLOAD ENDED....")
        print(f"TOTAL TIME TAKEN IS {int(time.time() - start)} seconds")
        open(f'{downloadLocation}/{fname}', 'wb').write(r.content)
        if fname in os.listdir():
            print("FILE SAVED SUCCESSFULLY")
            return True
        print("task failed successfully".upper())
        return False
    except Exception as e:
        print("Error", e)
        return False


def getGoogleResults(songName):
    for j in search(songName, tld="co.in", num=10, stop=10, pause=2):
        return j

def doEverything(song, downloadLocation):
    url = getGoogleResults(f"{song} pagalworld")
    print(url)
    downloadLink = getSongLink(url)
    if downloadLink != "":
        hasDownloaded = downloadfromDirectUrl(downloadLink, downloadLocation)
    else:
        print("invalid download link {}".format(downloadLink))


if __name__ == "__main__":
    downloadLocation = "specify_download_location"
    songsList = [
        # "tu tu hai wahi jonita gandhi",
        # "aise na mujhe tum dekho ash king",
        # "baahon ke darmiyan anwesha",
        # "kya leke aaya jagat mai",
        # "Tere liye sooryavanshi",
        "Matkar Maya Ko Ahankar"
        ]
    for songName in songsList:
        doEverything(songName, downloadLocation)

