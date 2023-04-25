import pygame
import random
import pickle

pygame.init()


class Player:
    def __init__(self) -> None:
        self.balance = 0
        self.achievements = []
        self.buildings = {KeyBoard: 0, Laptop: 0, GamingPC: 0, Server: 0}
        self.BuildingUpgrades = {KeyBoard: [], Laptop: [], GamingPC: [], Server: []}


class KeyBoard:
    def __init__(self) -> None:
        self.price = 10
        self.amount = 0
        self.upgrades = []
        self.cps = 1 * self.amount * 1.01 ** len(self.upgrades)



class Laptop:
    def __init__(self) -> None:
        self.price = 100
        self.amount = 0
        self.upgrades = []
        self.cps = 12.5 * self.amount * 1.01 ** len(self.upgrades)


class GamingPC:
    def __init__(self) -> None:
        self.price = 1000
        self.amount = 0
        self.upgrades = []
        self.cps = 125 * self.amount * 1.01 ** len(self.upgrades)


class Server:
    def __init__(self) -> None:
        self.price = 10000
        self.amount = 0
        self.upgrades = []
        self.cps = 1500 * self.amount * 1.01 ** len(self.upgrades)


class BitCoinMiner:
    def __init__(self) -> None:
        self.player = Player()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 30)
        self.BuildingTypes = [KeyBoard, Laptop, GamingPC, Server]

    def BuyBuilding(self, building):
        if self.player.balance >= building().price:
            self.player.balance -= building().price
            building().price *= 1.15
            building().amount += 1
            self.player.buildings[building] += 1
        if building not in self.player.achievements:
            self.player.achievements.append(building)

    def SellBuilding(self, building):
        if building.amount > 0:
            building.amount -= 1
            self.player.balance += building.price / 2

    def click(self):
        self.player.balance += 1

    def CalcBPF(self):
        BPF = (sum([building().cps for building in self.player.achievements]) / 60) * 1.01 ** len(self.player.achievements)
        return BPF

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.font.render(
            f"Balance: {self.player.balance}", True, (255, 255, 255)), (0, 0))
        self.screen.blit(self.font.render(
            f"CPS: {self.CalcBPF()}", True, (255, 255, 255)), (0, 30))
        self.screen.blit(self.font.render(
            f"KeyBoards: {KeyBoard().amount}", True, (255, 255, 255)), (0, 60))
        self.screen.blit(self.font.render(
            f"Laptops: {Laptop().amount}", True, (255, 255, 255)), (0, 90))
        self.screen.blit(self.font.render(
            f"GamingPCs: {GamingPC().amount}", True, (255, 255, 255)), (0, 120))
        self.screen.blit(self.font.render(
            f"Servers: {Server().amount}", True, (255, 255, 255)), (0, 150))
        pygame.display.update()

    def save(self):
        with open("save.pkl", "wb") as f:
            pickle.dump(self.player, f)

    def load(self):
        try:
            with open("save.pkl", "rb") as f:
                self.player = pickle.load(f)
            KeyBoard.amount = self.player.buildings[KeyBoard]
            Laptop.amount = self.player.buildings[Laptop]
            GamingPC.amount = self.player.buildings[GamingPC]
            Server.amount = self.player.buildings[Server]
        except:
            pass
    def DeleteSave(self):
        self.player = Player()
        KeyBoard.amount = self.player.buildings[KeyBoard]
        Laptop.amount = self.player.buildings[Laptop]
        GamingPC.amount = self.player.buildings[GamingPC]
        Server.amount = self.player.buildings[Server]

    def run(self):
        self.load()
        while True:
            self.clock.tick(60)
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.save()
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                    self.click()
                if event.type == pygame.KEYUP and event.key == pygame.K_s:
                    self.save()
                if event.type == pygame.KEYUP and event.key == pygame.K_d:
                    self.DeleteSave()
                if event.type == pygame.KEYUP and event.key == pygame.K_1:
                    self.BuyBuilding(KeyBoard)
                if event.type == pygame.KEYUP and event.key == pygame.K_2:
                    self.BuyBuilding(Laptop)
                if event.type == pygame.KEYUP and event.key == pygame.K_3:
                    self.BuyBuilding(GamingPC)
                if event.type == pygame.KEYUP and event.key == pygame.K_4:
                    self.BuyBuilding(Server)


Game = BitCoinMiner()
Game.run()
