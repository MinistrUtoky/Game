from all_various import *
from collider import Collider
from door import Door
from sprite import Sprite


class Wall(pygame.sprite.Group):
    def __init__(self, owner, way, images, x, y, length, coord_of_doors):
        super().__init__()
        self.way = way
        self.height = owner.height
        self.width = owner.width
        self.length = length
        self.owner = owner
        self.tag = "wall"
        self.colliders = []
        self.doors = []
        coord_of_doors2 = []
        for i in coord_of_doors:
            for j in i[1:]:
                coord_of_doors2.append(j)
        coord_of_doors = coord_of_doors2
        if way == "up" or way == "down":
            self.rect_f = [x + owner.rect_f[0], y + owner.rect_f[1],
                           length * METR + self.width * 2,
                           self.height]
            if way == "up":
                corner_image = images["corner_up"]
            else:
                corner_image = images["corner_down"]
            for i in range(2):
                corner = Sprite(self, middle)
                if i == 0:
                    corner.image = corner_image
                else:
                    corner.image = pygame.transform.flip(corner_image, True, False)
                corner.rect = list(corner.image.get_rect())
                corner.rect[0], corner.rect[1] = self.rect_f[0] + i * (self.rect_f[2] - corner.rect[2]), self.rect_f[1]
            for i in range(length):
                if i + 1 in coord_of_doors:
                    self.doors.append(Door(self, "horisontal", images, i * METR + self.width, 0))
                elif i not in coord_of_doors:
                    wall_surface = Sprite(self, middle)
                    wall_surface.image = images["wall_block_hor"]
                    wall_surface.rect = list(wall_surface.image.get_rect())
                    wall_surface.rect[0], wall_surface.rect[1] = self.rect_f[0] + i * METR + self.width, self.rect_f[
                        1]
                    self.colliders.append(
                        Collider(self, i * METR + self.width, self.height * (1 - WIDTH_WALL_COLLIDER), METR,
                                 self.height * WIDTH_WALL_COLLIDER))
            if way == "up":
                self.colliders.append(Collider(self, 0, self.height * (1 - WIDTH_WALL_COLLIDER), self.width,
                                               self.height * WIDTH_WALL_COLLIDER))
                self.colliders.append(
                    Collider(self, self.rect_f[2] - self.width, self.height * (1 - WIDTH_WALL_COLLIDER), self.width,
                             self.height * WIDTH_WALL_COLLIDER))
            else:
                self.colliders.append(Collider(self, 0, 0, self.width, self.height))
                self.colliders.append(Collider(self, self.rect_f[2] - self.width, 0, self.width, self.height))

        else:
            self.rect_f = [x + owner.rect_f[0], y + owner.rect_f[1], self.width,
                           length * METR]
            for i in range(length):
                if i + 1 in coord_of_doors:
                    self.doors.append(Door(self, "vertical", images, 0, i * METR))
                    print(self.rect_f)
                else:
                    wall_surface = Sprite(self, middle)
                    wall_surface.image = images["wall_block_ver"]
                    wall_surface.rect = list(wall_surface.image.get_rect())
                    wall_surface.rect[0], wall_surface.rect[1] = self.rect_f[0], self.rect_f[1] + i * METR
                    self.colliders.append(Collider(self, 0, METR * i, self.rect_f[2], METR))

    def move_camera(self, x, y):
        self.rect_f[0] -= x
        self.rect_f[1] -= y
        for i in self:
            i.rect[0] -= x
            i.rect[1] -= y
        for i in self.doors:
            i.move_camera(x, y)
        for i in self.colliders:
            i.move_camera(x, y)

    def draw(self, screen):
        super().draw(screen)
        for i in self.doors:
            i.draw(screen)
