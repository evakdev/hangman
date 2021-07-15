import random
import time

words=['abandon', 'abandonment', 'abbreviation', 'abeyance', 'abide', 'ability', 'abnormal', 'aboard', 'abolish', 'abolition', 'abortion', 'abortive', 'abridge', 'abrogate', 'abrupt', 'absence', 'absent', 'absolute', 'absolutely', 'absorb', 'absorption', 'abstract', 'absurd', 'absurdity', 'abundance', 'abundant', 'abuse', 'academic', 'academy', 'accede', 'accelerate', 'acceleration', 'access', 'accessible', 'accessory', 'accident', 'accidental', 'accidentally', 'accommodate', 'accommodation', 'accompaniment', 'accompany', 'accomplish', 'accomplishment', 'accord', 'account', 'accountant', 'accounting', 'accrue', 'accumulate', 'accumulation', 'accuracy', 'accurate', 'accusation', 'accuse', 'achieve', 'achievement', 'acid', 'acknowledge', 'acquaint', 'acquaintance', 'acquainted', 'acquire', 'acquisition', 'across', 'activate', 'actively', 'actual', 'actually', 'acute', 'adapt', 'adaptation', 'additional', 'additive', 'address', 'adequate', 'adhere', 'adhesive', 'adjacent', 'adjoin', 'adjust', 'adjustment', 'administer', 'administration', 'administrative', 'admiration', 'admire', 'admission', 'admit', 'admittedly', 'adolescence', 'adolescent', 'adopt', 'adoption', 'adore', 'adorn', 'adornment', 'adult', 'advance', 'advanced', 'adventure', 'adventurous', 'adversary', 'adverse', 'adversity', 'advertise',
 'advisable', 'advocate', 'aerial', 'affect', 'affection', 'affectionate', 'affiliate', 'affirm', 'affirmation', 'affirmative', 'afford', 'affordable', 'agency', 'agent', 'aggravate', 'aggregate', 'aggregation', 'aggressive', 'aggressor', 'agitate', 'agitation', 'agony', 'agreeable', 'agreement', 'agriculture', 'aid', 'ailment', 'aim', 'air', 'aircraft', 'aisle', 'ajar', 'alarm', 'album', 'alert', 'alien', 'alienate', 'alignment', 'alike', 'allergic', 'allergy', 'alliance', 'allocate', 'allot', 'allowance', 'alloy', 'ally', 'alone', 'along', 'alongside', 'alter', 'alternate', 'alternation', 'alternative', 'altitude', 'aluminum', 'amateur', 'amaze', 'amazement', 'ambassador', 'ambiguity', 'ambiguous', 'ambition', 'ambitious', 'ambulance', 'amend', 'amendment', 'amends', 'amiable', 'amicable', 'amid', 'ammunition', 'amount', 'ample', 'amplification', 'amplify', 'amuse', 'analogy', 'analysis', 'analytical', 'analyze', 'ancestor', 'anchor', 'anecdote', 'angular', 'animate', 'animation', 'ankle', 'annex', 'anniversary', 'announce', 'announcement', 'announcer', 'annoy', 'annual', 'annually', 'antagonism', 'antagonist', 'antarctic', 'antibiotic', 'anticipate', 'anticipation', 'antique', 'antonym', 'anxiety', 'anxious', 'anyhow', 'apart', 'ape', 'apologize', 'apology', 'apparatus', 'apparent', 'appeal', 'appealing', 'appendix', 'appetite', 'applaud', 'appliance', 'applicable', 'applicant', 'application', 'apply', 'appoint', 'appointment', 'appreciable', 'appreciate', 'appreciation', 'appreciative', 'apprentice', 'approach', 'appropriate', 'approval', 'approve', 'approximate', 'approximately', 'apt', 'aptitude', 'arbitrary', 'arbitrator', 'arc', 'arch', 'archaeology', 'architect', 'architecture', 'ardent', 'arduous', 'area', 'arena', 'argue', 'arise', 'aristocracy', 'aristocrat', 'arithmetic', 'armour', 'arms', 'arouse', 'arrange', 'arrangement', 'array', 'arrest', 'arrogance', 'arrogant', 'article', 'artificial', 'ascend', 'ascertain', 'ascribe', 'ashamed', 'aside', 'aspect', 'aspirin', 'assassination', 'assault', 'assemble', 'assembly', 'assert', 'assess', 'assessment', 'assign', 'assignment', 'assist', 'assistance', 'assistant', 'associate', 'association', 'assorted', 'assortment', 'assume', 'assumption', 'assurance', 'assure', 'assured', 'astonish', 'astound', 'astray', 'astronomer', 'astronomical', 'astronomy', 'athlete', 'atlas', 'atmosphere', 'atom', 'atomic', 'attach', 'attachment', 'attack', 'attain', 'attempt', 'attend', 'attendance', 'attendant', 'attention', 'attentive', 'attic', 'attitude', 'attorney', 'attract', 'attraction', 'attribute', 'auction', 'audience', 'auditorium', 'august', 'author', 'authority', 'authorization', 'authorize', 'autobiography', 'automate', 'automatic', 'automation', 'automobile', 'autonomous', 'autonomy', 'auxiliary', 'avail', 'available', 'avenge', 'avenue', 'average', 'aviation', 'avoid', 'aware', 'awe', 'awful', 'awkward', 'awkwardly', 'axis', 'axle']


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


run_hangman(words)