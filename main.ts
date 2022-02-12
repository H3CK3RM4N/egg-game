function EggDrop () {
    while (true) {
        Egg = game.createSprite(randint(0, 4), 0)
        for (let index = 0; index <= 4; index++) {
            basic.pause(speed)
            Egg.change(LedSpriteProperty.Y, 1)
            basic.pause(speed)
        }
        if (Egg.isTouching(Basket)) {
            music.playTone(523, music.beat(BeatFraction.Half))
            Egg.delete()
            SCORE += 1
        } else {
            music.startMelody(music.builtInMelody(Melodies.Funk), MelodyOptions.Once)
            basic.showString("" + (word[randint(0, word.length + 1)]))
            game.setScore(SCORE)
        }
    }
}
// button input
input.onButtonPressed(Button.A, function () {
    Basket.change(LedSpriteProperty.X, -1)
})
input.onButtonPressed(Button.B, function () {
    Basket.change(LedSpriteProperty.X, 1)
})
let SCORE = 0
let Egg: game.LedSprite = null
let Basket: game.LedSprite = null
let word: string[] = []
let speed = 0
speed = 300
word = ["GAME OVER", "WINNER"]
Basket = game.createSprite(2, 4)
EggDrop()
