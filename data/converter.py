import csv, json
from googlesearch import search

def readCSV(fileName):
    mediaList = []
    with open(fileName, newline='') as csvfile:
        mediaTable = csv.reader(csvfile, delimiter=',')
        for media in mediaTable:
            mediaList.append(media)
    return mediaList


def getMediaDomain(mediaList):
    updated_list = []
    for  media in mediaList:
        query = media[0]
        urls = []
        for url in search(query, tld="com", num=3, stop=3, pause=2):
            domain = _extractDomain(url)
            urls.append(domain)
        media.append(urls)
        updated_list.append(media)
        print(query+":"+str(urls))
    return updated_list

def reviewDomains(mediaList):
    updated_list = []
    for media in mediaList:
        name = media[0]
        domains = media[2]
        print("\n"+name+": "+"1)" +domains[0]
                       +"2)" +domains[1]
                       +"3)" +domains[2])
        choice = int(input("Choose (1-3): "))
        media[2] = domains[(choice-1)]
        updated_list.append(media)
    return  updated_list

def _extractDomain(url):
    # type: (str) -> str
    url = url.replace("https://","")
    url = url.replace("http://","")
    url = url[:url.index("/")]
    return url
    

if __name__ == '__main__':
    mediaList = readCSV("source_data/us_media.csv")
    mediaList = getMediaDomain(mediaList)
    mediaList = reviewDomains(mediaList)

    with open("media_list.json", "w") as output:
        json.dump(mediaList,output, indent=4)