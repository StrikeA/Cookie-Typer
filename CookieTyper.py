# Importing all of the systems.
import pygame
import random
import pickle
import os
import subprocess
import sys

# Creating the window and initiating pygame
pygame.init()
pygame.display.set_caption("Cookie Typer")

# Creating the class for player
class Player:
    def __init__(self) -> None:
# Key variables
        self.balance = 0
        self.achievements = []


# The first building class, one of 9
class KeyBoard:
    def __init__(self) -> None:
# More key variables that are included in every building class
        self.price = 10
        self.amount = 0
        self.next_achievement = 1
        self.upgrades = 0
        self.next_upgrade_achievement = 1
        self.next_upgrade = 1
        self.upgrade_price = 100

# A function within the class to specify the bps given by the building
    def bps(self):
        return 0.1 * self.amount * 2 ** self.upgrades


# The second building class
class Laptop:
    def __init__(self) -> None:
# More key variables that are included in every building class
        self.price = 100
        self.amount = 0
        self.next_achievement = 1
        self.upgrades = 0
        self.next_upgrade_achievement = 1
        self.next_upgrade = 1
        self.upgrade_price = 1000

# A function within the class to specify the bps given by the building
    def bps(self):
        return 1 * self.amount * 2 ** self.upgrades


# The third building class
class GamingPC:
    def __init__(self) -> None:
# More key variables that are included in every building class
        self.price = 1000
        self.amount = 0
        self.next_achievement = 1
        self.upgrades = 0
        self.next_upgrade_achievement = 1
        self.next_upgrade = 1
        self.upgrade_price = 10000

# A function within the class to specify the bps given by the building
    def bps(self):
        return 10 * self.amount * 2 ** self.upgrades


# The fourth building class
class Server:
    def __init__(self) -> None:
# More key variables that are included in every building class
        self.price = 10000
        self.amount = 0
        self.next_achievement = 1
        self.upgrades = 0
        self.next_upgrade_achievement = 1
        self.next_upgrade = 1
        self.upgrade_price = 100000

# A function within the class to specify the bps given by the building
    def bps(self):
        return 100 * self.amount * 2 ** self.upgrades


# The fifth building class
class SuperComputer:
    def __init__(self) -> None:
# More key variables that are included in every building class
        self.price = 100000
        self.amount = 0
        self.next_achievement = 1
        self.upgrades = 0
        self.next_upgrade_achievement = 1
        self.next_upgrade = 1
        self.upgrade_price = 1000000

# A function within the class to specify the bps given by the building
    def bps(self):
        return 1000 * self.amount * 2 ** self.upgrades


# The sixth building class
class QuantumComputer:
    def __init__(self) -> None:
# More key variables that are included in every building class
        self.price = 1000000
        self.amount = 0
        self.upgrades = 0
        self.next_upgrade_achievement = 1
        self.next_upgrade = 1
        self.upgrade_price = 10000000

# A function within the class to specify the bps given by the building
    def bps(self):
      return 10000 * self.amount * 2 ** self.upgrades


# The seventh building class
class AI:
    def __init__(self) -> None:
# More key variables that are included in every building class
        self.price = 10000000
        self.amount = 0
        self.next_achievement = 1
        self.upgrades = 0
        self.next_upgrade_achievement = 1
        self.next_upgrade = 1
        self.upgrade_price = 100000000

# A function within the class to specify the bps given by the building
    def bps(self):
      return 1000000 * self.amount * 2 ** self.upgrades


# The eighth building class
class QuantumAI:
    def __init__(self) -> None:
# More key variables that are included in every building class
        self.price = 100000000
        self.amount = 0
        self.next_achievement = 1
        self.upgrades = 0
        self.next_upgrade_achievement = 1
        self.next_upgrade = 1
        self.upgrade_price = 1000000000

# A function within the class to specify the bps given by the building
    def bps(self):
      return 10000000 * self.amount * 2 ** self.upgrades


# The final building class
class DysonSphere:
    def __init__(self) -> None:
# More key variables that are included in every building class
        self.price = 1000000000
        self.amount = 0
        self.next_achievement = 1
        self.upgrades = 0
        self.next_upgrade_achievement = 1
        self.next_upgrade = 1
        self.upgrade_price = 10000000000

# A function within the class to specify the bps given by the building
    def bps(self):
      return 100000000 * self.amount * 2 ** self.upgrades


# The main game class
class BitCoinMiner:
    def __init__(self) -> None:
# The Attributes that tell the game window how to display
        self.display_info = pygame.display.Info()
        self.hight = self.display_info.current_h
# Bringing player class into the main class
        self.player = Player()
# The main attributes
        self.total_earned = 0
# More Display attributes
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 30)
# Bringing the building types into a list
        self.BuildingTypes = [KeyBoard(), Laptop(), GamingPC(), Server(), SuperComputer(), QuantumComputer(), AI(), QuantumAI(), DysonSphere()]
# Miscellaneous
        self.bpf_achievment = 10000
        self.total_achievment = 10000
        self.click_upgrades = 1
        self.click_upgrades_price = 100

# The function that is used to purchase buildings and regulate the price of buildings
    def BuyBuilding(self, building):
# Checking if the player has enough balance
        if self.player.balance >= building.price:
            self.player.balance -= building.price
            building.price *= 1.15
            building.amount += 1

# The function that is used to sell buildings
    def SellBuilding(self, building):
# Checking if the player has enough buildings to sell, and decreasing the building price
        if building.amount > 0:
            building.price /= 1.15
            self.player.balance += building.price / 2
            building.amount -= 1
# Checking if the player has the achievement for said building, and giving it to them if they do not
            if building.__class__ not in self.player.achievements:
                self.player.achievements.append(building.__class__)

# The function that allows for purchasing upgrades
    def BuyUpgrade(self, building):
# Making sure the purchase requirments are met
        if self.player.balance >= building.upgrade_price and building.amount >= building.next_upgrade:
            self.player.balance -= building.upgrade_price
            building.upgrade_price *= 10
            building.upgrades += 1

# The function that allows for clicking 
    def click(self):
# multiplying gain by upgrades
        self.player.balance += 1 * self.click_upgrades

# The function that regulates your actual earnings per second
    def CalcBPF(self):
# Giving building bps per second, times 0.01 per achievment.
        BPF = (sum([building.bps() for building in self.BuildingTypes]) / 60) * 1.01 ** len(self.player.achievements)
        return BPF

# def CalcBPF(self):
    def draw(self):
# set background color
        self.screen.fill((110, 64, 21))
# draw balance to screen
        self.screen.blit(self.font.render(
            f"Balance: {round(self.player.balance, 2)}", True, (0, 0, 0)), (10, 10))
# draw BPF to screen
        self.screen.blit(self.font.render(
            f"BPS: {round(self.CalcBPF() * 60, 2)}", True, (0, 0, 0)), (10, 40))
# draw achievements to screen
        self.screen.blit(self.font.render(
            f"Achievements: {len(self.player.achievements)}", True, (0, 0, 0)), (10, self.hight - 60))
# set y position for building info
        y_pos = 70
# set a for loop to drwa buildings
        for building in self.BuildingTypes:
# draw building amount
            self.screen.blit(self.font.render(
                f"{building.__class__.__name__}: {building.amount}", True, (0, 0, 0)), (10, y_pos))
# draw building price
            self.screen.blit(self.font.render(
                f"Price: {round(building.price, 2)}", True, (0, 0, 0)), (10, y_pos + 30))
# draw building upgrades
            self.screen.blit(self.font.render(
                f"{building.__class__.__name__} upgrades: {building.upgrades}", True, (0, 0, 0)), (400, y_pos))
# draw upgrade price
            self.screen.blit(self.font.render(
                f"Price: {round(building.upgrade_price, 2)}", True, (0, 0, 0)), (400, y_pos + 30))
# increment y position
            y_pos += 60
# draw click upgrades
        self.screen.blit(self.font.render(
            f"Click upgrades: {self.click_upgrades - 1}", True, (0, 0, 0)), (10, 610))
# draw click upgrade price
        self.screen.blit(self.font.render(
            f"Click upgrade price: {self.click_upgrades_price}", True, (0, 0, 0)), (400, 610))
# update display
        pygame.display.update()
# def achievements(self):


    def achievements(self):
# set a for loop to check if achievements are met
        for building in self.BuildingTypes:
# check if building amount is greater than or equal to next achievement
            if building.amount >= building.next_achievement:
# add achievement to player achievements
                self.player.achievements.append(building.__class__)
# multiply next achievement by 10
                building.next_achievement *= 10
# check if building upgrades is greater than or equal to next upgrade achievement
            if building.upgrades >= building.next_upgrade_achievement:
# add achievement to player achievements
                self.player.achievements.append(building.__class__)
# multiply next upgrade achievement by 10
                building.next_upgrade_achievement *= 10
# check if click upgrades is greater than or equal to next click upgrade achievement
            if (self.CalcBPF() * 60) >= self.bpf_achievment:
# add achievement to player achievements
                self.player.achievements.append("bps_achievment")
# multiply next click upgrade achievement by 10
                self.bpf_achievment *= 10
# check if total earned is greater than or equal to next total achievement
            if self.player.balance >= self.total_achievment:
# add achievement to player achievements
                self.player.achievements.append("total_achievment")
# multiply next total achievement by 10
                self.total_achievment *= 10
# check if total earned is greater than or equal to 1
            if self.total_earned == 1:
# add achievement to player achievements
                self.player.achievements.append("You've done it!")
# def save(self):


    def save(self):
# open save.pickle in write binary mode
        with open("save.pickle", "wb") as f:
# dump player and BuildingTypes to save.pickle
            pickle.dump([self.player, self.BuildingTypes], f)
# def load(self):


    def load(self):
# try to open save.pickle in read binary mode
        try:
# open save.pickle in read binary mode
            with open("save.pickle", "rb") as f:
# load player and BuildingTypes from save.pickle
                self.player, self.BuildingTypes = pickle.load(f)
# if save.pickle does not exist
        except:
# pass
            pass


    def restart(self):
# remove save.pickle
        try:
# remove save.pickle
            os.remove("save.pickle")
# if save.pickle does not exist
        except:
# pass
            pass
# open a new instance of the game
        subprocess.Popen([sys.executable] + sys.argv)
# kill current instance of the game
        os.kill(os.getpid(), 9)


# The function that is actually running the code
    def run(self):
# Loading the save if you have one
        self.load()
# Game loop
        while True:
# Frames per second
            self.clock.tick(60)
# Increasing your balance every second
            self.player.balance += self.CalcBPF()
# The total earned
            self.total_earned += self.CalcBPF()
# Creating the window
            self.draw()
# If you quit the game, it saves
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.save()
                    pygame.quit()
                    quit()

# Creating keybinds for every task
                keys = pygame.key.get_pressed()
# Saving the game
                if event.type == pygame.KEYUP and event.key == pygame.K_s:
                    if keys[pygame.K_LSHIFT]:
                        self.restart()
                    else:
                        self.save()
# The click method
                if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                    if keys[pygame.K_LSHIFT]:
                        if self.player.balance >= self.click_upgrades_price:
                            self.click_upgrades += 1
                            self.player.balance -= self.click_upgrades_price
                            self.click_upgrades_price *= 10
                    else:
                        self.click()
# Buying and regulating keyboards
                if event.type == pygame.KEYUP and event.key == pygame.K_1:
                    if keys[pygame.K_LSHIFT]:
                        self.SellBuilding(self.BuildingTypes[0])
                    elif keys[pygame.K_LCTRL]:
                        self.BuyUpgrade(self.BuildingTypes[0])
                    else:
                        self.BuyBuilding(self.BuildingTypes[0])
# Buying and regulating Laptops
                if event.type == pygame.KEYUP and event.key == pygame.K_2:
                    if keys[pygame.K_LSHIFT]:
                        self.SellBuilding(self.BuildingTypes[1])
                    elif keys[pygame.K_LCTRL]:
                        self.BuyUpgrade(self.BuildingTypes[1])
                    else:
                        self.BuyBuilding(self.BuildingTypes[1])
# Buying and regulating GamingPCs
                if event.type == pygame.KEYUP and event.key == pygame.K_3:
                    if keys[pygame.K_LSHIFT]:
                        self.SellBuilding(self.BuildingTypes[2])
                    elif keys[pygame.K_LCTRL]:
                        self.BuyUpgrade(self.BuildingTypes[2])
                    else:
                        self.BuyBuilding(self.BuildingTypes[2])
# Buying and regulating servers
                if event.type == pygame.KEYUP and event.key == pygame.K_4:
                    if keys[pygame.K_LSHIFT]:
                        self.SellBuilding(self.BuildingTypes[3])
                    elif keys[pygame.K_LCTRL]:
                        self.BuyUpgrade(self.BuildingTypes[3])
                    else:
                        self.BuyBuilding(self.BuildingTypes[3])
# Buying and regulating Super computers
                if event.type == pygame.KEYUP and event.key == pygame.K_5:
                    if keys[pygame.K_LSHIFT]:
                        self.SellBuilding(self.BuildingTypes[4])
                    elif keys[pygame.K_LCTRL]:
                        self.BuyUpgrade(self.BuildingTypes[4])
                    else:
                        self.BuyBuilding(self.BuildingTypes[4])
# Buying and regulating Quantum computers
                if event.type == pygame.KEYUP and event.key == pygame.K_6:
                    if keys[pygame.K_LSHIFT]:
                        self.SellBuilding(self.BuildingTypes[5])
                    elif keys[pygame.K_LCTRL]:
                        self.BuyUpgrade(self.BuildingTypes[5])
                    else:
                        self.BuyBuilding(self.BuildingTypes[5])
# Buying and regulating AIs
                if event.type == pygame.KEYUP and event.key == pygame.K_7:
                    if keys[pygame.K_LSHIFT]:
                        self.SellBuilding(self.BuildingTypes[6])
                    elif keys[pygame.K_LCTRL]:
                        self.BuyUpgrade(self.BuildingTypes[6])
                    else:
                        self.BuyBuilding(self.BuildingTypes[6])
# Buying and regulating Quantum AIs
                if event.type == pygame.KEYUP and event.key == pygame.K_8:
                    if keys[pygame.K_LSHIFT]:
                        self.SellBuilding(self.BuildingTypes[7])
                    elif keys[pygame.K_LCTRL]:
                        self.BuyUpgrade(self.BuildingTypes[7])
                    else:
                        self.BuyBuilding(self.BuildingTypes[7])
# Buying and regulating Dyson spheres
                if event.type == pygame.KEYUP and event.key == pygame.K_9:
                    if keys[pygame.K_LSHIFT]:
                        self.SellBuilding(self.BuildingTypes[8])
                    elif keys[pygame.K_LCTRL]:
                        self.BuyUpgrade(self.BuildingTypes[8])
                    else:
                        self.BuyBuilding(self.BuildingTypes[8])


# Running the actual game
Game = BitCoinMiner()
Game.run()
