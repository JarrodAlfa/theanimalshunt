import pygame


class GameMap:
    def __init__(self, screen_w, screen_h):
        self.w = screen_w
        self.h = screen_h

        self.tile_w = 190
        self.overlap = 8
        self.ground_push_down = 24

        # sky background
        self.sky_img = pygame.image.load("assets/sky.png").convert()
        self.sky_scale = 1.0
        self.sky_y_offset = -148
        self._update_sky()

        # ground + tree assets
        self.grass_img = pygame.image.load("assets/terreno_teste.png").convert_alpha()
        self.dirt_img = pygame.image.load("assets/tile_2.png").convert_alpha()
        self.tree_base_img = pygame.image.load("assets/arvore_teste_2.png").convert_alpha()

        # clouds
        self.cloud_imgs = [
            pygame.image.load("assets/Clouds.png.png").convert_alpha(),
            pygame.image.load("assets/Clouds_1.png.png").convert_alpha(),
            pygame.image.load("assets/Clouds_2.png.png").convert_alpha(),
        ]

        self.cloud_imgs = [
            pygame.transform.scale(img, (int(self.w * 0.35), int(self.h * 0.16)))
            for img in self.cloud_imgs
        ]

        self.clouds = [
            {"img": self.cloud_imgs[0], "x": int(self.w * 0.10), "y": int(self.h * 0.08), "speed": 0.4},
            {"img": self.cloud_imgs[1], "x": int(self.w * 0.45), "y": int(self.h * 0.05), "speed": 0.15},
            {"img": self.cloud_imgs[2], "x": int(self.w * 0.70), "y": int(self.h * 0.12), "speed": 0.1},
        ]

        # scale ground
        self.dirt_img = self._scale_by_width(self.dirt_img, self.tile_w)

        self.grass_front_img = self._scale_by_width(self.grass_img, self.tile_w)
        self.grass_front_img = self._scale_y(self.grass_front_img, 2.10)

        self.grass_back_img = self._scale_by_width(self.grass_img, self.tile_w)
        self.grass_back_img = self._scale_y(self.grass_back_img, 1.10)
        self.grass_back_img = self._darken(self.grass_back_img, 0.78)

        # trees
        self.tree_far_img = self._make_tree_variant(1.10, 1.60, 0.62)
        self.tree_mid_img = self._make_tree_variant(1.80, 2.10, 0.78)
        self.tree_near_img = self._make_tree_variant(2.50, 3.00, 1.00)

        self.dirt_w = self.dirt_img.get_width()
        self.dirt_h = self.dirt_img.get_height()
        self.grass_front_h = self.grass_front_img.get_height()
        self.grass_back_h = self.grass_back_img.get_height()

        step = self.dirt_w - self.overlap
        self.cols = (self.w + step - 1) // step + 6

        self.dirt_y = self.h - self.dirt_h + self.ground_push_down
        self.grass_front_y = self.dirt_y - self.grass_front_h + 27
        self.grass_back_y = self.grass_front_y - int(self.grass_back_h * 0.60)

        self.tree_far_anchor = 65
        self.tree_mid_anchor = 115
        self.tree_near_anchor = 135

        mid_ground_y = self.grass_front_y - int(self.grass_back_h * 0.55)

        self.trees_far = [
            (int(self.w * 0.10), self._tree_y_on(self.grass_back_y, self.tree_far_img, self.tree_far_anchor)),
            (int(self.w * 0.33), self._tree_y_on(self.grass_back_y, self.tree_far_img, self.tree_far_anchor)),
            (int(self.w * 0.62), self._tree_y_on(self.grass_back_y, self.tree_far_img, self.tree_far_anchor)),
            (int(self.w * 0.82), self._tree_y_on(self.grass_back_y, self.tree_far_img, self.tree_far_anchor)),
        ]

        self.trees_mid = [
            (int(self.w * 0.18), self._tree_y_on(mid_ground_y, self.tree_mid_img, self.tree_mid_anchor)),
            (int(self.w * 0.52), self._tree_y_on(mid_ground_y, self.tree_mid_img, self.tree_mid_anchor)),
            (int(self.w * 0.72), self._tree_y_on(mid_ground_y, self.tree_mid_img, self.tree_mid_anchor)),
        ]

        self.trees_near = [
            (int(self.w * 0.10) - self.tree_near_img.get_width() // 2,
             self._tree_y_on(self.grass_front_y, self.tree_near_img, self.tree_near_anchor)),
            (int(self.w * 0.58) - self.tree_near_img.get_width() // 2,
             self._tree_y_on(self.grass_front_y, self.tree_near_img, self.tree_near_anchor)),
            (int(self.w * 0.92) - self.tree_near_img.get_width() // 2,
             self._tree_y_on(self.grass_front_y, self.tree_near_img, self.tree_near_anchor)),
        ]

    def _update_sky(self):
        self.sky_scaled = pygame.transform.scale(
            self.sky_img,
            (int(self.w * self.sky_scale), int(self.h * self.sky_scale))
        )

    def update(self):
        for cloud in self.clouds:
            cloud["x"] += cloud["speed"]
            if cloud["x"] > self.w:
                cloud["x"] = -cloud["img"].get_width()

    def draw(self, screen):
        screen.blit(self.sky_scaled, (0, self.sky_y_offset))

        for cloud in self.clouds:
            screen.blit(cloud["img"], (cloud["x"], cloud["y"]))

        step = self.dirt_w - self.overlap
        shift = step // 2

        for col in range(self.cols):
            x = (col * step) - step
            screen.blit(self.dirt_img, (x, self.dirt_y))
            screen.blit(self.grass_front_img, (x, self.grass_front_y))
            screen.blit(self.grass_back_img, (x, self.grass_back_y))

            x2 = (col * step + shift) - step
            screen.blit(self.dirt_img, (x2, self.dirt_y - 2))
            screen.blit(self.grass_front_img, (x2, self.grass_front_y - 2))
            screen.blit(self.grass_back_img, (x2, self.grass_back_y - 2))

        for x, y in self.trees_far:
            screen.blit(self.tree_far_img, (x, y))
        for x, y in self.trees_mid:
            screen.blit(self.tree_mid_img, (x, y))
        for x, y in self.trees_near:
            screen.blit(self.tree_near_img, (x, y))

    def _scale_by_width(self, img, new_w):
        w, h = img.get_width(), img.get_height()
        new_h = int(h * (new_w / w))
        return pygame.transform.scale(img, (new_w, new_h))

    def _scale_y(self, img, factor):
        w, h = img.get_width(), img.get_height()
        return pygame.transform.scale(img, (w, int(h * factor)))

    def _darken(self, img, factor):
        out = img.copy()
        shade = int(255 * factor)
        out.fill((shade, shade, shade, 255), special_flags=pygame.BLEND_RGBA_MULT)
        return out

    def _make_tree_variant(self, scale_w, scale_h, darken):
        w = int(self.tile_w * scale_w)
        h = int(self.tile_w * scale_h)
        img = pygame.transform.scale(self.tree_base_img, (w, h))
        if darken < 1:
            img = self._darken(img, darken)
        return img

    def _tree_y_on(self, grass_y, tree_img, anchor_px):
        return grass_y - tree_img.get_height() + anchor_px