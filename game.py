import random
import time 
import threading

weapons_ascii = '''
    1.:
                           ______
        |\_______________ (_____\\______________
HH======#H###############H#######################
        ' ~""""""""""""""`##(_))#H\"""""Y########
                          ))    \#H\       `"Y###
                          "      }#H)
    2.:
,______________________________________       
|_________________,----------._ [____]  ""-,__  __....-----=====
               (_(||||||||||||)___________/   ""                |
                  `----------' Krogg98[ ))"-,                   |
                                       ""    `,  _,--....___    |
                                               `/           """"


    3.:
 +--^----------,--------,-----,--------^-,
 | |||||||||   `--------'     |          O
 `+---------------------------^----------| 
   `\_,---------,---------,--------------'
     / XXXXXX /'|       /'
    / XXXXXX /  `\    /'
   / XXXXXX /`-------'
  / XXXXXX /
 / XXXXXX /
(________(                
 `------'
'''
key_ascii = '''
1:
      __
     /o \\_____
    \\__/-="="="
       ||
       ||
       ||
       ||

2:
   ___
  /   \\
 |  O  |
 |     |
 |_____|  
   ||

3:
     ____
    |    |
    |____|
    |    |
    |____|
'''
villian_ascii = '''
                            ,-.
       ___,---.__          /'|`\\          __,---,___
    ,-'    \\`    `-.____,-'  |  `-.____,-'    //    `-.
  ,'        |           ~'\\     /`~           |        `.
 /      ___//              `. ,'          ,  , \\___      \\
|    ,-'   `-.__   _         |        ,    __,-'   `-.    |
|   /          /\\_  `   .    |    ,      _/\\          \\   |
\\  |           \\ \\`-.___ \\   |   //'   _,' |           |  /
 \\  \\           | `._   `\\\\  |  //'   _,' |           /  /
  `-\\.         /'  _ `---'' , . ``---' _  `\\         /,-'
     ``       /     \\    ,='/ \\`=.    /     \\       ''
             |__   /|\\_,--.,-.--,--._/|\\   __|
             /  `./  \\\\`\\ |  |  | /,//' \\,'  \\
            /   /     ||--+--|--+-/-|     \\   \\
           |   |     /'\\_\\_\\ | /_/_/`\\     |   |
            \\   \\__, \\_     `~'     _/ .__/   /
             `-._,-'   `-._______,-'   `-._,-'
'''

class Game():
    print("Welcome to the game! There will be 2 levels to get the prize.")
    time.sleep(1)
    def __init__(self):
        self.level = 1
        self.lives = 3
        self.right_weapon = 2
        self.right_key = 3

    def check_key(self, key):
        return self.right_key == key
    
    def check_weapon(self, weapon):
        return self.right_weapon == weapon

weapon = 0
key = 0
game=Game()

class Riddle():
    def __init__(self, question, answer, options):
        self.question = question
        self.answer = answer
        self.options = options

    def check_ans(self, user_ans):
        return self.answer.lower() == user_ans.strip().lower()

riddles = [
    Riddle("I'm tall when I'm young, and I'm short when I'm old. What am I?", "Candle", ["Candle", "Tree", "Mountain", "River"]),
    Riddle("What has keys but can't open locks?", "Piano", ["Keyboard", "Piano", "Map", "Book"]),
    Riddle("What has a heart that doesn't beat?", "Artichoke", ["Clock", "Robot", "Artichoke", "Statue"]),
    Riddle("I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?", "Echo", ["Wind", "Echo", "Shadow", "Whistle"]),
    Riddle("The more you take, the more you leave behind. What am I?", "Footsteps", ["Time", "Money", "Footsteps", "Mist"]),
    Riddle("I'm light as a feather, yet the strongest person can't hold me for five minutes. What am I?", "Breath", ["Happiness", "Breath", "Hope", "Paper"]),
    Riddle("What can travel around the world while staying in the same spot?", "Stamp", ["Sun", "Stamp", "Shadow", "Clock"]),
    Riddle("I'm not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?", "Fire", ["Plant", "Fire", "Wind", "Cloud"]),
    Riddle("What has to be broken before you can use it?", "Egg", ["Glass", "Egg", "Code", "Lock"]),
    Riddle("I have branches, but no fruit, trunk, or leaves. What am I?", "Bank", ["River", "Bank", "Library", "Forest"])
]

class TimeUpError(Exception):
    pass

def input_with_timeout(prompt, timeout):
    timer = threading.Timer(timeout, lambda: print("\nTime's up!"))
    timer.start()  # Start the timer
    
    try:
        user_input = input(prompt)
        return user_input
    finally:
        timer.cancel()


def play_random_riddle():
    random_riddle = random.choice(riddles)
    print("\nRiddle Time!\n")  
    time.sleep(1)
    print(random_riddle.question)
    for idx, option in enumerate(random_riddle.options, start=1):
        print(f"{idx}. {option}")
    try:
        user_answer = input_with_timeout("Enter your answer (30 seconds): ", 30)
    except TimeUpError:
        return False
    
    return random_riddle.check_ans(user_answer)
    

def choose_weapon():
    time.sleep(1)
    print("\nChoose Your Weapon!\n")
    time.sleep(1)
    print(weapons_ascii)
    while True:
        try:
            weapon = int(input("Please pick a weapon (1, 2, 3): "))
            if weapon in [1, 2, 3]:
                return weapon
            else:
                print("Invalid choice! Please pick a number between 1 and 3.")
        except ValueError:
            print("Invalid input! Please enter a number (1, 2, or 3).")


def choose_key():
    time.sleep(1)
    print("\nChoose Your Key! TO OPEN THE DOOR AND FINISH THIS LEVEL \n")
    time.sleep(2)
    print(key_ascii)
    while True:
        try:
            key = int(input("Please pick a key (1, 2, 3): "))
            if key in [1, 2, 3]:
                return key
            else:
                print("Invalid choice! Please pick a number between 1 and 3.")
        except ValueError:
            print("Invalid input! Please enter a number (1, 2, or 3).")


def mid_level1():
    global weapon
    weapon = choose_weapon()
    check_key = False

    while check_key == False:
        key=choose_key()
        check_key = game.check_key(key)
        if check_key == True:
            print("\nCongrats! You Are Welcome to the level 2.\n")
            time.sleep(1)
            level2()
        else:
            print("the chosen key is wrong DOOR CANNOT BE OPENED")
            time.sleep(1)


def level2():
    if game.lives < 3:
        game.lives += 1
        time.sleep(1)
        print("Your life is increased by 1 and now it is ", game.lives)
    time.sleep(1)
    print('Fight with the villain using your weapon!\n')
    time.sleep(1)
    print(villian_ascii)
    if weapon == game.right_weapon:
        time.sleep(5)
        print("\nYou have defeated the villain!\n")
        time.sleep(1)
        completed_riddle = False
        while game.lives > 0 and completed_riddle == False:
            completed_riddle = play_random_riddle()
            if not completed_riddle:
                print("wrong ans next one")
        else:
            time.sleep(1)
            print("\n" + "="*200)
            print("🎉🎉🎉  CONGRATULATIONS, YOU ARE THE WINNER OF THIS GAME!  🎉🎉🎉")
            print("="*200 + "\n")
    else:
        time.sleep(5)
        print("You are dead! So are send to level 1 select New weapon")
        time.sleep(5)
        mid_level1()

def main():
    game = Game()
    completed_riddle = False
    while game.lives > 0 and completed_riddle == False:
        completed_riddle = play_random_riddle()
        if not completed_riddle:
            game.lives -= 1
            print(f"Incorrect answer. You have {game.lives} lives left.\n")
            time.sleep(1)
        else:
            print("Congratulations, you have completed the riddle!\n\nNow pick up the Weapon ")
            time.sleep(2.5)
    if game.lives <= 0:
        print("Game Over! You have run out of lives.")
    if completed_riddle:
        mid_level1()



main()