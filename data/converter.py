import csv, json

def readCSV(fileName):
    newsAgentsEntriesList = []
    with open(fileName, newline='') as csvfile:
        newsAgentEntries = csv.reader(csvfile, delimiter=',')
        for newsAgentEntry in newsAgentEntries:
            newsAgentsEntriesList.append(newsAgentEntry)
    return newsAgentsEntriesList





if __name__ == '__main__':
    newsAgentsEntriesList = readCSV("us_news_channel_partisan_score.csv")
    print(newsAgentsEntriesList)
    with open("news_agent_list.json", "w") as output:
        json.dump(newsAgentsEntriesList,output, indent=4)