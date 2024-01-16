import  pygame
class SpriteSheet:
    def __init__(self, image_path):
        self.sprite_sheet = pygame.image.load(image_path).convert()

    def get_image(self, frame, width, height, scale):
        image = pygame.Surface((width, height)).convert()
        image.blit(self.sprite_sheet, (0, 0), (frame * width, 0, width, height))
        image.set_colorkey((0, 0, 0))  # Supposer que le noir est la couleur transparente
        image = pygame.transform.scale(image, (width * scale, height * scale))
        return image
