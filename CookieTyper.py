import pygame
import random
import pickle

pygame.init()


class Player:
    def __init__(self) -> None:
        self.balance = 0
        self.achievements = []


class KeyBoard:
    def __init__(self) -> None:
        self.price = 10
        self.amount = 0
        self.upgrades = []

    def cps(self):
        return 1 * self.amount * 1.01 ** len(self.upgrades)

class Laptop:
    def __init__(self) -> None:
        self.price = 100
        self.amount = 0
        self.upgrades = []

    def cps(self):
        return 12.5 * self.amount * 1.01 ** len(self.upgrades)

class GamingPC:
    def __init__(self) -> None:
        self.price = 1000
        self.amount = 0
        self.upgrades = []

    def cps(self):
        return 125 * self.amount * 1.01 ** len(self.upgrades)

class Server:
    def __init__(self) -> None:
        self.price = 10000
        self.amount = 0
        self.upgrades = []

    def cps(self):
        return 1500 * self.amount * 1.01 ** len(self.upgrades)
    
class BitCoinMiner:
    def __init__(self) -> None:
        self.player = Player()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 30)
        self.BuildingTypes = [KeyBoard(), Laptop(), GamingPC(), Server()]

    def BuyBuilding(self, building):
        if self.player.balance >= building.price:
            self.player.balance -= building.price
            building.price *= 1.15
            building.amount += 1
        if building.__class__ not in self.player.achievements:
            self.player.achievements.append(building.__class__)

    def SellBuilding(self, building):
        if building.amount > 0:
            building.price /= 1.15
            self.player.balance += building.price / 2
            building.amount -= 1
            

    def click(self):
        self.player.balance += 1

    def CalcBPF(self):
        BPF = sum([building.cps() for building in self.BuildingTypes]) / 60
        return BPF

    def draw(self):
        self.screen.fill((110, 64, 21))
        self.screen.blit(self.font.render(f"Balance: {round(self.player.balance, 2)}", True, (0, 0, 0)), (10, 10))
        self.screen.blit(self.font.render(f"BPS: {round(self.CalcBPF() * 60, 2)}", True, (0, 0, 0)), (10, 40))
        self.screen.blit(self.font.render(f"Keyboards: {self.BuildingTypes[0].amount}", True, (0, 0, 0)), (10, 70))
        self.screen.blit(self.font.render(f"Price: {round(self.BuildingTypes[0].price, 2)}", True, (0, 0, 0)), (10, 100))
        self.screen.blit(self.font.render(f"Laptops: {self.BuildingTypes[1].amount}", True, (0, 0, 0)), (10, 130))
        self.screen.blit(self.font.render(f"Price: {round(self.BuildingTypes[1].price, 2)}", True, (0, 0, 0)), (10, 160))
        self.screen.blit(self.font.render(f"GamingPCs: {self.BuildingTypes[2].amount}", True, (0, 0, 0)), (10, 190))
        self.screen.blit(self.font.render(f"Price: {round(self.BuildingTypes[2].price, 2)}", True, (0, 0, 0)), (10, 220))
        self.screen.blit(self.font.render(f"Servers: {self.BuildingTypes[3].amount}", True, (0, 0, 0)), (10, 250))
        self.screen.blit(self.font.render(f"Price: {round(self.BuildingTypes[3].price, 2)}", True, (0, 0, 0)), (10, 280))
        pygame.display.update()


    def run(self):
        while True:
            self.clock.tick(60)
            self.player.balance += self.CalcBPF()
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                keys = pygame.key.get_pressed()
                if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                    self.click()
                if event.type == pygame.KEYUP and event.key == pygame.K_1:
                    if keys[pygame.K_LSHIFT]:
                        self.SellBuilding(self.BuildingTypes[0])
                    else:
                        self.BuyBuilding(self.BuildingTypes[0])
                if event.type == pygame.KEYUP and event.key == pygame.K_2:
                    if keys[pygame.K_LSHIFT]:
                        self.SellBuilding(self.BuildingTypes[1])
                    else:
                        self.BuyBuilding(self.BuildingTypes[1])
                if event.type == pygame.KEYUP and event.key == pygame.K_3:
                    if keys[pygame.K_LSHIFT]:
                        self.SellBuilding(self.BuildingTypes[2])
                    else:
                        self.BuyBuilding(self.BuildingTypes[2])
                if event.type == pygame.KEYUP and event.key == pygame.K_4:
                    if keys[pygame.K_LSHIFT]:
                        self.SellBuilding(self.BuildingTypes[3])
                    else:
                        self.BuyBuilding(self.BuildingTypes[3])

Game = BitCoinMiner()
Game.run()