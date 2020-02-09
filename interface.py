from various import *
from sprites import *
from sprite import Sprite
from group import Group
from sounds import *
import pygame


class Interface(Group):
    def __init__(self, player):
        super().__init__()
        interface_content.append(self)
        self.player = player
        self.tag = "health"
        self.health = player.health
        self.healths = []
        self.ammo_numbers = []
        self.bandolier_numbers = []
        self.bandolier = 0
        self.ammo_in_magazine = 0
        self.full_ammo = 0
        self.dividing_line = None
        self.set_interface()

    def set_interface(self):
        self.dividing_line = Sprite(self)
        self.dividing_line.image = PLAYER["dividing_line"]
        self.dividing_line.rect_f = list(self.dividing_line.image.get_rect())
        self.dividing_line.rect_f[X], self.dividing_line.rect_f[Y] = width - 90, height - 150
        self.dividing_line.rect = pygame.Rect(self.dividing_line.rect_f)
        self.display_hp()
        self.display_ammo()
        self.display_bandolier()

    def display_hp(self):
        for i in self.healths:
            i.kill()
        for i in range(int(self.health) - 1, -1, -1):
            sprite = Sprite(self, self.healths)
            sprite.image = PLAYER["health_point"]
            sprite.rect_f = list(sprite.image.get_rect())
            sprite.rect_f[X], sprite.rect_f[Y] = 20 + i * 75, 30
            sprite.rect = pygame.Rect(sprite.rect_f)

    def display_ammo(self):
        for i in range(len(self.ammo_numbers)):
            self.ammo_numbers[0].kill()
        for i in range(len(str(self.ammo_in_magazine))):
            filled = Sprite(self, self.ammo_numbers)
            filled.image = PLAYER[str(self.ammo_in_magazine)[i]]
            filled.rect_f = list(self.dividing_line.image.get_rect())
            filled.rect_f[X], filled.rect_f[Y] = width - 85 + i * 20, height - 130
            filled.rect = pygame.Rect(filled.rect_f)

    def display_bandolier(self):
        for i in range(len(self.bandolier_numbers)):
            self.bandolier_numbers[0].kill()
        for i in range(len(str(self.bandolier))):
            reserve = Sprite(self, self.bandolier_numbers)
            reserve.image = PLAYER[str(self.bandolier)[i]]
            reserve.rect_f = list(self.dividing_line.image.get_rect())
            reserve.rect_f[X], reserve.rect_f[Y] = width - 85 + i * 20, height - 60
            reserve.rect = pygame.Rect(reserve.rect_f)

    def change_hp(self):
        self.health = int(self.player.health)
        self.display_hp()

    def set_ammo(self):
        self.ammo_in_magazine = self.player.weapon.ammo_in_magazine
        self.bandolier = self.player.weapon.bandolier
        self.full_ammo = self.player.weapon.full_ammo
        self.display_ammo()
        self.display_bandolier()
