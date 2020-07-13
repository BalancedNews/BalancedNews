class Agent:
    def _init_(self, name, url, partisanScore):
        self.name = name                    # type: str
        self.url = url                      # type: str
        self.partisanScore = partisanScore  # type: float

    def getName(self):
        # type: () ->str
        return self.name


    def getUrl(self):
        # type: () ->str
        return self.url

    def getPartisanScore(self):
        # type: () -> float
        return self.partisanScore



class AgentPool:
    def _init_(self):
        self._agentList = []  # type: List[Agent]

    def addAgent(self, agent):
        # type: (Agent) ->bool

        if(len(self._agentList) == 0):
            self._agentList = [agent];

        for i in range(len(self._agentList)):
            if agent.getPartisanScore()<self._agentList[i].getPartisanScore():
                self._agentList.insert(i,agent)
        else:
            self._agentList.append(agent)


    def findAgentWithName(self, name):
        # type: (str) ->[Agent, bool]

        for agent in self._agentList:
            if agent.getName() == name:
                return [agent, True]

        return [None, False]

    def findClosestAgentwithPartisanScore(self, partisanScore):
        # type: (int) ->[Agent, bool]

        if(len(self._agentList)==0):
            return None, False

        scoreList = [agent.getPartisanScore for agent in self._agentList]
        for i in range(len(scoreList)):
            pass


    def findOppositeAgentWithName(self, name):
        # type: (str) ->[Agent, bool]

        (agent,success) = self.findAgentWithName(name)
        if not success:
            return (None, False)

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   print("hi")