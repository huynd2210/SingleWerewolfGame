from main.GameEngine.GameInfo import GameInfo


class NightInfo:
    def __init__(self):
        self.nightCasualties = []

    def resolveNightConclusion(self, gameInfo: GameInfo):
        self.resolveNPCSBeingKilled(gameInfo)

    def resolveNPCSBeingKilled(self, gameInfo: GameInfo):
        for npc in gameInfo.npcList:
            if npc.isBeingKilled:
                self.nightCasualties.append(npc)
                npc.isAlive = False
                npc.isBeingKilled = False

    def reset(self):
        self.nightCasualties = []

