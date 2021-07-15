import random
import time

class Stickman:
    face = "         --------        \n   	| /     |       \n   	|       |       \n  	|     ෴෴෴    \n   	|    (͡❛ ͜ʖ ❛)    \n   	|      ┏皿┛     \n   	|      / \      \n	|               \n                    "
    body = "         --------        \n   	| /     |       \n   	|       |       \n  	|     ෴෴෴    \n   	|     (   )    \n   	|      ┏皿┛     \n   	|      / \      \n	|               \n                    "
    head = "         --------        \n   	| /     |       \n   	|       |       \n  	|     ෴෴෴    \n   	|     (   )    \n   	|               \n   	|               \n	|               \n                    "
    choobe = "         --------        \n   	| /     |       \n   	|       |       \n  	|               \n   	|              \n   	|               \n   	|               \n	|               \n                    "
    dead = "         --------        \n   	| /     |       \n   	|       |       \n  	|     ෴෴෴    \n   	|     (*﹏*)    \n   	|      ┏皿┛     \n   	|      / \      \n	|               \n                    "
    levels = {0: "", 1: choobe, 2: head, 3: body, 4: face, 5: dead}

    def print(self,level):
        print(self.levels[level])

    def max_level(self):
        level_nums=self.levels.keys()
        return max(level_nums)

class Message:

    def banner():
        messages=[
            """\n :::    :::     :::     ::::    :::  ::::::::  ::::    ::::      :::     ::::    ::: \n :+:    :+:   :+: :+:   :+:+:   :+: :+:    :+: +:+:+: :+:+:+   :+: :+:   :+:+:   :+: \n +:+    +:+  +:+   +:+  :+:+:+  +:+ +:+        +:+ +:+:+ +:+  +:+   +:+  :+:+:+  +:+ \n +#++:++#++ +#++:++#++: +#+ +:+ +#+ :#:        +#+  +:+  +#+ +#++:++#++: +#+ +:+ +#+ \n +#+    +#+ +#+     +#+ +#+  +#+#+# +#+   +#+# +#+       +#+ +#+     +#+ +#+  +#+#+# \n #+#    #+# #+#     #+# #+#   #+#+# #+#    #+# #+#       #+# #+#     #+# #+#   #+#+# \n ###    ### ###     ### ###    ####  ########  ###       ### ###     ### ###    #### \n
        """,
            """\n    ┬ ┬┬┌┬┐┬ ┬  ╔╦╗╔═╗╔═╗╔═╗╦    ┬ ┬┌─┐┬─┐┌┬┐┌─┐ \n    ││││ │ ├─┤   ║ ║ ║║╣ ╠╣ ║    ││││ │├┬┘ ││└─┐ \n    └┴┘┴ ┴ ┴ ┴   ╩ ╚═╝╚═╝╚  ╩═╝  └┴┘└─┘┴└──┴┘└─┘ \n
        """
        ]
        for line in messages:
            print(line)

    def intro():
        messages = """Hi! Ready to play some Hangman?
        If yes, type '1' to begin. 
        If no, type '0' to end the program. \n"""
        print(messages)

    def first_guess():
        messages = "\n Here we go! Guess a letter: \n"
        print(messages)

    def next_guess():
        messages = [
            "Guess another:", "Got another?", "You've got this! Try again:"
        ]
        random_choice = random.choices(messages)
        print(*random_choice)

    def correct():
        messages=[
            'Correct!',
            'Awesome!',
            'Yess!',
            'Woohoo!',
            'You got it!'
        ]
        random_choice = random.choices(messages)
        print(*random_choice)

    def wrong():
        messages=[
            'oops!',
            'nope :(',
            "don't lose your head!"
            ]
        random_choice = random.choices(messages)
        print(*random_choice)

    def win():
        messages = [
            "You did it! Congrats!",
            "Well done!",
            "🎊🥳🎊",
            "Wooho!",
            "Now that's what I'm talking about! well done!"
            ]
        random_choice = random.choices(messages)
        print(*random_choice)

    def lose(word):
        messages= [
            """\noops :(""",
            """\nSorry :(""",
            """\n😿😿""",
            """\nOh well :(""",
            """\nwell, you tried..."""
            ]

        random_choice = random.choices(messages)
        print(*random_choice)
        time.sleep(1)
        next_msg="""the word was '{}'. You'll get it next time!"""
        print(next_msg.format(word))
    
    def replay():
        messages="""type 1 to play again, or type 0 to exit: \n"""

        print(messages)

    def exit():
        messages = [
            'See you later!',
            'Bye!',
            'Come back soon!'
            ]
        random_choice = random.choices(messages)
        print(*random_choice)

class Hangman:

    #Functions

    def __init__(self,words,wrong_limit):
        """chooses random word and initiats all lists. also gets a wrong_limit that is 5 by default. 
        and also a word list that is our words by default
        """
        self.word: list = list(random.choice(words).lower())
        self.word_length: int = len(self.word)
        self.corrects: list = list('_' for i in range(self.word_length))
        self.wrongs: list = list()
        self.wrong_limit: int = wrong_limit
        self.stickman_level: int = 0

    def input_is_valid(self,answer,) -> bool:
        """validates user's answer and prints corresponding error. 
        return False if there was an error and True if there wasn't.
        """

        errors={
        'Duplicate': "You already entered that. Guess a new letter.",
        'Nonletter': "That's not a letter. Please enter only letters.",
        'OnlyOne' : "Please enter only one letter."
        }

        if answer in self.wrongs or answer in self.corrects:
            print(errors['Duplicate'])
            return False
        if not answer.isalpha():
            print(errors['Nonletter'])
            return False
        if len(answer)>1:
            print(errors['OnlyOne'])
            return False

        return True


    def replace_blanks(self,letter) -> bool:
        """replaces the letter given in corrects'proper indexes if the letter
        is in the word.
        if it did replace anything, returns True. else returns False, showing wrong answer
        """
        replaced=0

        for i in range (self.word_length):
            if self.word[i]==letter:
                self.corrects[i]=letter
                replaced+=1
        return bool(replaced)

    def add_wrong(self,letter):

        self.wrongs.append(letter)
        self.stickman_level+=1
        return

    def print_mistakes(self):
        template = "Wrong Guesses: {}   {} left"
        mistkes_left=self.wrong_limit-self.stickman_level
        if self.stickman_level==0:
            print(template.format('None',mistkes_left))
        else:
            print(template.format(' '.join(self.wrongs),mistkes_left))

        return

    def is_end(self) -> bool:
        """checks if game has ended by checkning wether all of the word is found, 
        and if wrong_limit has been reached. 
        if any is true, returns 'win' or 'lose'. else, returns False
        """

        if self.corrects==self.word:
            return 'win'
        if self.stickman_level==self.wrong_limit:
            return 'lose'
        return False

def run_hangman(words,stickman=Stickman()):

    Message.banner()
    time.sleep(1)
    Message.intro()

    if not(input() is '1'):
        Message.exit()
        return

    game=Hangman(words, wrong_limit=stickman.max_level())
    Message.first_guess()

    while game.is_end() is False:
        print(*game.corrects)
        guess=input()
        while game.input_is_valid(guess) is False:
            guess=input()

        replaced=game.replace_blanks(guess)
        if replaced is False:
            game.add_wrong(guess)

        stickman.print(level=game.stickman_level)
        game.print_mistakes()

    if game.is_end() == 'win':
        Message.win()
    else:
        Message.lose(''.join(game.word))

    time.sleep(2)
    Message.replay()
    if input()=='1':
        run_hangman(words)
    return

from hangman import words

run_hangman(words)