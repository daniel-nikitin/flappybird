import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SCREEN_TITLE = 'flappybird'
GRAVITY = 3
JUMP = 20
CEILING = SCREEN_HEIGHT - 50
FLOOR = 50


class BIRD(arcade.Sprite):
    def __init__(self):
        super().__init__(filename="bird/yellowbird-midflap.png", scale=1)
        self.center_y = 250
        self.center_x = 250
        self.wingsound = arcade.load_sound("audio/wing.wav")

    def update(self):
        self.center_y += self.change_y
        self.change_y -= GRAVITY

        if self.bottom < FLOOR:
            self.bottom = FLOOR

        if self.top > CEILING:
            self.top = CEILING

    def jump(self):
        self.change_y = JUMP
        arcade.play_sound(self.wingsound)


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.backrnd = arcade.load_texture("bg.png")
        self.pause_image = arcade.load_texture("PAUSE.png")
        self.bird = BIRD()
        self.pause = False

    def on_key_press(self, symbol: int, modifiers: int):

        if symbol == arcade.key.ESCAPE:
            self.pause = not self.pause
        if self.pause == True:
            return
        if symbol == arcade.key.SPACE:
            self.bird.jump()

    def on_key_release(self, symbol: int, modifiers: int):
        pass

    def update(self, delta_time: float):
        if self.pause == True:
            return
        self.bird.update()

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.backrnd)
        self.bird.draw()
        if self.pause == True:
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                          self.pause_image)


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()
