import json, math
from pprint import pprint


class Media:
    def __init__(self, name, url, partisanScore):
        self.name = name                    # type: str
        self.url = url                      # type: str
        self.partisanScore = float(partisanScore)  # type: float

    def getName(self):
        # type: () ->str
        return self.name

    def getUrl(self):
        # type: () ->str
        return self.url

    def getPartisanScore(self):
        # type: () -> float
        return self.partisanScore

    def __str__(self):
        return "{0}:(media = {1}, domain = {2})".format(
            self.partisanScore if self.partisanScore<0 else " " +str(self.partisanScore),
        self.name, self.url)

    def __lt__(self,other):
        return self.partisanScore>other.partisanScore

    def __ge__(self, other):
        return self.partisanScore>=other.partisanScore

class MediaPool:

    def __init__(self):
        self._mediaList = []  # type: List[Media]
    def __str__(self):
        s = "Media Pool length = "+str(len(self._mediaList)) +"\n"
        for media in self._mediaList:
            s += "    "+ str(media) + "\n"
        return s

    def addMedia(self, media):
        # type: (Media) -> ()

        if(len(self._mediaList) == 0):
            self._mediaList = [media];
            return

        for i in range(len(self._mediaList)):
            if media<=self._mediaList[i]:
                self._mediaList.insert(i, media)
                return

        self._mediaList.append(media)

    def findMediaWithName(self, name):
        # type: (str) ->[Media, bool]

        for Media in self._mediaList:
            if Media.getName() == name:
                return [Media, True]

        return [None, False]

    def findMediaWithUrl(self, url):
        # type: (str) ->[Media, bool]

        for Media in self._mediaList:
            if Media.getUrl() == url:
                return [Media, True]

        return [None, False]

    def findClosestMediawithPartisanScore(self, score):
        # type: (int) ->[Media, bool]

        if(len(self._mediaList)==0):
            return None, False

        scoreList = [Media.getPartisanScore() for Media in self._mediaList]
        index = self._findClosestValueIndex(scoreList, 0, len(scoreList), score)
        return self._mediaList[index]


    def _findClosestValueIndex(self, lis, low, high, value):
        comparison = value - lis[math.floor((low + high) / 2)]

        if(comparison == 0):
            return lis[math.floor((low + high) / 2)]
        else:
            if (low == high or low == high - 1):
                return low if abs(lis[low]-value) <= abs(lis[high]-value) else high
            else:
                if(comparison > 0):
                    return self._findClosestValueIndex(lis, math.floor((low + high)/2), high, value)
                else:
                    return self._findClosestValueIndex(lis, low, math.floor((low + high)/2), value)




def _buildAgentPool():
    with open("media_data.json", "r") as f:
        mediaList = json.load(f)

    # Testing stage comment
    print("Loading {0} media from {1}:".format(len(mediaList), "media_data.json"))

    mediaPool = MediaPool()
    i = 1
    for each in mediaList:
        i+=1
        media = Media(name = each[0], url = each[2], partisanScore = each[1])
        mediaPool.addMedia(media)

    print("Media Pool has been built.")
    return (mediaPool)


mediaPool = _buildAgentPool()

if __name__ == "__main__":
   # mediaPool = _buildAgentPool()
    pass