import PlayerActionList
from PlayerAction import PlayerAction


class Player:
    def __init__(self, name: str):
        self.name = name
        self.actions = []
        self.initAction()
    def initAction(self):
        self.actions.append(PlayerAction("visit", True, PlayerActionList.visitAction))
        self.actions.append(PlayerAction("execute", False, PlayerActionList.executeNPCAction))
        self.actions.append(PlayerAction("investigate role", False, PlayerActionList.roleInvestigationAction))

    #todo: refactor so that actions can be performed on dead NPCs as well as alive ones, depending on the action
    def takeDayActionDialogue(self, gameInfo):
        print("What do you want to do today? Possible actions are: ")
        possibleDayActions = [actions for actions in self.actions if not actions.isNightAction]
        possibleDayActionsNames = [actions.name for actions in possibleDayActions]
        for action in possibleDayActions:
            print("-- ", action.name)
        actionToTake = input()
        while actionToTake not in possibleDayActionsNames:
            print("Invalid input, try again")
            print("What do you want to do today?")
            for action in possibleDayActions:
                print(action.name)
            actionToTake = input()

            # npcNames = [npc.name for npc in gameInfo.npcList]
        aliveNpcNames = [npc.name for npc in gameInfo.npcList if npc.isAlive]
        for action in possibleDayActions:
            if action.name == actionToTake:
                print("Who do you want to " + action.name + "?")
                self.printAliveNpcNames(aliveNpcNames)
                targetNPCName = input()
                while targetNPCName not in aliveNpcNames:
                    print("Invalid input, try again")
                    print("Who do you want to " + action.name + "?")
                    self.printAliveNpcNames(aliveNpcNames)
                    targetNPCName = input()
                action.performAction(gameInfo, targetNPCName)

        # print("Who do you want to execute?")
        # aliveNpc = list(filter(lambda npc: npc.isAlive, self.gameInfo.npcList))
        # for npc in aliveNpc:
        #     print(npc.name)
        # npcToExecute = input()
        #
        # aliveNpcNameList = [npc.name for npc in aliveNpc]
        #
        # while npcToExecute not in aliveNpcNameList:
        #     if npcToExecute == "None":
        #         break
        #     print("Invalid input, try again")
        #     print("Who do you want to execute?")
        #     for npc in aliveNpc:
        #         print(npc.name)
        #     npcToExecute = input()
        #
        # if npcToExecute != "None":
        #     PlayerActionList.executeNPCAction(self.gameInfo, npcToExecute)

    def takeNightActionDialogue(self, gameInfo):
        print("What do you want to do tonight? Possible actions are: ")
        possibleNightActions = [actions for actions in self.actions if actions.isNightAction]
        possibleNightActionsNames = [actions.name for actions in possibleNightActions]
        for action in possibleNightActions:
            print("-- " + action.name)
        actionToTake = input()
        while actionToTake not in possibleNightActionsNames:
            print("Invalid input, try again")
            print("What do you want to do tonight?")
            for action in possibleNightActions:
                print(action.name)
            actionToTake = input()


        # npcNames = [npc.name for npc in gameInfo.npcList]
        aliveNpcNames = [npc.name for npc in gameInfo.npcList if npc.isAlive]
        for action in possibleNightActions:
            if action.name == actionToTake:
                print("Who do you want to " + action.name + "?")
                self.printAliveNpcNames(aliveNpcNames)
                targetNPCName = input()

                while targetNPCName not in aliveNpcNames:
                    print("Invalid input, try again")
                    print("Who do you want to " + action.name + "?")
                    self.printAliveNpcNames(aliveNpcNames)
                    targetNPCName = input()
                action.performAction(gameInfo, targetNPCName)

    def printAliveNpcNames(self, aliveNpcNames):
        for npcName in aliveNpcNames:
            print(npcName)