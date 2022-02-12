def EggDrop():
    global Egg, SCORE
    while True:
        Egg = game.create_sprite(randint(0, 4), 0)
        for index in range(5):
            basic.pause(speed)
            Egg.change(LedSpriteProperty.Y, 1)
            basic.pause(speed)
        if Egg.is_touching(Basket):
            music.play_tone(523, music.beat(BeatFraction.HALF))
            Egg.delete()
            SCORE += 1
        else:
            music.start_melody(music.built_in_melody(Melodies.FUNK), MelodyOptions.ONCE)
            basic.show_string("" + (word[randint(0, len(word) + 1)]))
            game.set_score(SCORE)
# button input

def on_button_pressed_a():
    Basket.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    Basket.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

SCORE = 0
Egg: game.LedSprite = None
Basket: game.LedSprite = None
word: List[str] = []
speed = 0
speed = 300
word = ["GAME OVER", "WINNER"]
Basket = game.create_sprite(2, 4)
EggDrop()