import pygame
import random
import pickle

pygame.init()


class Player:
    def __init__(self) -> None:
        self.balance = 0
        self.achievements = []
<<<<<<< HEAD
=======
        self.buildings = {KeyBoard: 0, Laptop: 0, GamingPC: 0, Server: 0}
        self.BuildingUpgrades = {KeyBoard: [],
                                 Laptop: [], GamingPC: [], Server: []}
>>>>>>> 36fea1f15123329aafe5a5724c675a0c21e1dcb9


class KeyBoard:
    def __init__(self) -> None:
        self.price = 10
        self.amount = 0
<<<<<<< HEAD
        self.upgrades = []

    def cps(self):
        return 1 * self.amount * 1.01 ** len(self.upgrades)
=======
        self.cps = 1 * self.amount * 1.01 ** len(self.upgrades)
        self.upgrades = []

>>>>>>> 36fea1f15123329aafe5a5724c675a0c21e1dcb9

class Laptop:
    def __init__(self) -> None:
        self.price = 100
        self.amount = 0
<<<<<<< HEAD
        self.upgrades = []

    def cps(self):
        return 12.5 * self.amount * 1.01 ** len(self.upgrades)
=======
        self.cps = 12.5 * self.amount * 1.01 ** len(self.upgrades)
        self.upgrades = []

>>>>>>> 36fea1f15123329aafe5a5724c675a0c21e1dcb9

class GamingPC:
    def __init__(self) -> None:
        self.price = 1000
        self.amount = 0
<<<<<<< HEAD
        self.upgrades = []

    def cps(self):
        return 125 * self.amount * 1.01 ** len(self.upgrades)
=======
        self.cps = 125 * self.amount * 1.01 ** len(self.upgrades)
        self.upgrades = []

>>>>>>> 36fea1f15123329aafe5a5724c675a0c21e1dcb9

class Server:
    def __init__(self) -> None:
        self.price = 10000
        self.amount = 0
<<<<<<< HEAD
        self.upgrades = []

    def cps(self):
        return 1500 * self.amount * 1.01 ** len(self.upgrades)

        

=======
        self.cps = 1500 * self.amount * 1.01 ** len(self.upgrades)
        self.upgrades = []

>>>>>>> 36fea1f15123329aafe5a5724c675a0c21e1dcb9

class BitCoinMiner:
    def __init__(self) -> None:
        self.player = Player()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 30)
<<<<<<< HEAD
        self.BuildingTypes = [KeyBoard(), Laptop(), GamingPC(), Server()]
=======
        self.BuildingTypes = [KeyBoard, Laptop, GamingPC, Server]
>>>>>>> 36fea1f15123329aafe5a5724c675a0c21e1dcb9

    def BuyBuilding(self, building):
        if self.player.balance >= building.price:
            self.player.balance -= building.price
            building.price *= 1.15
            building.amount += 1
<<<<<<< HEAD
        if building.__class__ not in self.player.achievements:
            self.player.achievements.append(building.__class__)
        if self.player.achievements == 4:
            self.player.achievements.append("All buildings")
=======
            self.player.buildings[building] += 1
        if building not in self.player.achievements:
            self.player.achievements.append(building)
>>>>>>> 36fea1f15123329aafe5a5724c675a0c21e1dcb9

    def SellBuilding(self, building):
        if building.amount > 0:
            building.amount -= 1
            self.player.balance += building.price / 2

    def click(self):
        self.player.balance += 1

    def CalcBPF(self):
<<<<<<< HEAD
        BPF = sum([building.cps() for building in self.BuildingTypes]) / 60
=======
        BPF = sum([building.cps for building in self.player.achievements]) / 60
>>>>>>> 36fea1f15123329aafe5a5724c675a0c21e1dcb9
        return BPF

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.font.render(
            f"Balance: {self.player.balance}", True, (255, 255, 255)), (0, 0))
        self.screen.blit(self.font.render(
<<<<<<< HEAD
            f"BPS: {self.CalcBPF() * 60}", True, (255, 255, 255)), (0, 30))
        self.screen.blit(self.font.render(
            f"KeyBoards: {self.BuildingTypes[0].amount}", True, (255, 255, 255)), (0, 60))
        self.screen.blit(self.font.render(
            f"Laptops: {self.BuildingTypes[1].amount}", True, (255, 255, 255)), (0, 90))
        self.screen.blit(self.font.render(
            f"GamingPCs: {self.BuildingTypes[2].amount}", True, (255, 255, 255)), (0, 120))
        self.screen.blit(self.font.render(
            f"Servers: {self.BuildingTypes[3].amount}", True, (255, 255, 255)), (0, 150))
        self.screen.blit(self.font.render(
            f"Achievments: {self.player.achievements}", True, (255, 255, 255)), (0, 180))
        pygame.display.update()


    def run(self):
        while True:
            self.clock.tick(60)
            self.player.balance += self.CalcBPF()
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
=======
            f"CPS: {self.CalcBPF()}", True, (255, 255, 255)), (0, 30))
        self.screen.blit(self.font.render(
            f"KeyBoards: {KeyBoard.amount}", True, (255, 255, 255)), (0, 60))
        self.screen.blit(self.font.render(
            f"Laptops: {Laptop.amount}", True, (255, 255, 255)), (0, 90))
        self.screen.blit(self.font.render(
            f"GamingPCs: {GamingPC.amount}", True, (255, 255, 255)), (0, 120))
        self.screen.blit(self.font.render(
            f"Servers: {Server.amount}", True, (255, 255, 255)), (0, 150))
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

    def run(self):
        self.load()
        while True:
            self.clock.tick(60)
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.save()
>>>>>>> 36fea1f15123329aafe5a5724c675a0c21e1dcb9
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                    self.click()
<<<<<<< HEAD
                if event.type == pygame.KEYUP and event.key == pygame.K_1:
                    self.BuyBuilding(self.BuildingTypes[0])
                if event.type == pygame.KEYUP and event.key == pygame.K_2:
                    self.BuyBuilding(self.BuildingTypes[1])
                if event.type == pygame.KEYUP and event.key == pygame.K_3:
                    self.BuyBuilding(self.BuildingTypes[2])
                if event.type == pygame.KEYUP and event.key == pygame.K_4:
                    self.BuyBuilding(self.BuildingTypes[3])
=======
                if event.type == pygame.KEYUP and event.key == pygame.K_s:
                    self.save()
                if event.type == pygame.KEYUP and event.key == pygame.K_1:
                    self.BuyBuilding(KeyBoard)
                if event.type == pygame.KEYUP and event.key == pygame.K_2:
                    self.BuyBuilding(Laptop)
                if event.type == pygame.KEYUP and event.key == pygame.K_3:
                    self.BuyBuilding(GamingPC)
                if event.type == pygame.KEYUP and event.key == pygame.K_4:
                    self.BuyBuilding(Server)
>>>>>>> 36fea1f15123329aafe5a5724c675a0c21e1dcb9


Game = BitCoinMiner()
Game.run()
