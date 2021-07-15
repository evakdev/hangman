import random
"""
To use for finding suitable symbols: 
https://www.branah.com/unicode-converter
https://www.ssec.wisc.edu/~tomw/java/unicode.html#x0300 """



# pygsheets code preparations
#import pygsheets
"""gc = pygsheets.authorize()
sh = gc.open_by_key("1zA-ABM0c6UoZQ_hJLylKZ0NXHsZuemYoNWhxEFT_60U")
sheet1 = sh[0]

words=[]
for i in sheet1.range('a1:a400', returnas='matrix'):
    if len(i[0])>0:
        words.append(i[0])"""


#The Code ABOVE is replaced with this local list to facilitate sharing (and increase speed):
words=['abandon', 'abandonment', 'abbreviation', 'abeyance', 'abide', 'ability', 'abnormal', 'aboard', 'abolish', 'abolition', 'abortion', 'abortive', 'abridge', 'abrogate', 'abrupt', 'absence', 'absent', 'absolute', 'absolutely', 'absorb', 'absorption', 'abstract', 'absurd', 'absurdity', 'abundance', 'abundant', 'abuse', 'academic', 'academy', 'accede', 'accelerate', 'acceleration', 'access', 'accessible', 'accessory', 'accident', 'accidental', 'accidentally', 'accommodate', 'accommodation', 'accompaniment', 'accompany', 'accomplish', 'accomplishment', 'accord', 'account', 'accountant', 'accounting', 'accrue', 'accumulate', 'accumulation', 'accuracy', 'accurate', 'accusation', 'accuse', 'achieve', 'achievement', 'acid', 'acknowledge', 'acquaint', 'acquaintance', 'acquainted', 'acquire', 'acquisition', 'across', 'activate', 'actively', 'actual', 'actually', 'acute', 'adapt', 'adaptation', 'additional', 'additive', 'address', 'adequate', 'adhere', 'adhesive', 'adjacent', 'adjoin', 'adjust', 'adjustment', 'administer', 'administration', 'administrative', 'admiration', 'admire', 'admission', 'admit', 'admittedly', 'adolescence', 'adolescent', 'adopt', 'adoption', 'adore', 'adorn', 'adornment', 'adult', 'advance', 'advanced', 'adventure', 'adventurous', 'adversary', 'adverse', 'adversity', 'advertise',
 'advisable', 'advocate', 'aerial', 'affect', 'affection', 'affectionate', 'affiliate', 'affirm', 'affirmation', 'affirmative', 'afford', 'affordable', 'agency', 'agent', 'aggravate', 'aggregate', 'aggregation', 'aggressive', 'aggressor', 'agitate', 'agitation', 'agony', 'agreeable', 'agreement', 'agriculture', 'aid', 'ailment', 'aim', 'air', 'aircraft', 'aisle', 'ajar', 'alarm', 'album', 'alert', 'alien', 'alienate', 'alignment', 'alike', 'allergic', 'allergy', 'alliance', 'allocate', 'allot', 'allowance', 'alloy', 'ally', 'alone', 'along', 'alongside', 'alter', 'alternate', 'alternation', 'alternative', 'altitude', 'aluminum', 'amateur', 'amaze', 'amazement', 'ambassador', 'ambiguity', 'ambiguous', 'ambition', 'ambitious', 'ambulance', 'amend', 'amendment', 'amends', 'amiable', 'amicable', 'amid', 'ammunition', 'amount', 'ample', 'amplification', 'amplify', 'amuse', 'analogy', 'analysis', 'analytical', 'analyze', 'ancestor', 'anchor', 'anecdote', 'angular', 'animate', 'animation', 'ankle', 'annex', 'anniversary', 'announce', 'announcement', 'announcer', 'annoy', 'annual', 'annually', 'antagonism', 'antagonist', 'antarctic', 'antibiotic', 'anticipate', 'anticipation', 'antique', 'antonym', 'anxiety', 'anxious', 'anyhow', 'apart', 'ape', 'apologize', 'apology', 'apparatus', 'apparent', 'appeal', 'appealing', 'appendix', 'appetite', 'applaud', 'appliance', 'applicable', 'applicant', 'application', 'apply', 'appoint', 'appointment', 'appreciable', 'appreciate', 'appreciation', 'appreciative', 'apprentice', 'approach', 'appropriate', 'approval', 'approve', 'approximate', 'approximately', 'apt', 'aptitude', 'arbitrary', 'arbitrator', 'arc', 'arch', 'archaeology', 'architect', 'architecture', 'ardent', 'arduous', 'area', 'arena', 'argue', 'arise', 'aristocracy', 'aristocrat', 'arithmetic', 'armour', 'arms', 'arouse', 'arrange', 'arrangement', 'array', 'arrest', 'arrogance', 'arrogant', 'article', 'artificial', 'ascend', 'ascertain', 'ascribe', 'ashamed', 'aside', 'aspect', 'aspirin', 'assassination', 'assault', 'assemble', 'assembly', 'assert', 'assess', 'assessment', 'assign', 'assignment', 'assist', 'assistance', 'assistant', 'associate', 'association', 'assorted', 'assortment', 'assume', 'assumption', 'assurance', 'assure', 'assured', 'astonish', 'astound', 'astray', 'astronomer', 'astronomical', 'astronomy', 'athlete', 'atlas', 'atmosphere', 'atom', 'atomic', 'attach', 'attachment', 'attack', 'attain', 'attempt', 'attend', 'attendance', 'attendant', 'attention', 'attentive', 'attic', 'attitude', 'attorney', 'attract', 'attraction', 'attribute', 'auction', 'audience', 'auditorium', 'august', 'author', 'authority', 'authorization', 'authorize', 'autobiography', 'automate', 'automatic', 'automation', 'automobile', 'autonomous', 'autonomy', 'auxiliary', 'avail', 'available', 'avenge', 'avenue', 'average', 'aviation', 'avoid', 'aware', 'awe', 'awful', 'awkward', 'awkwardly', 'axis', 'axle']



def Billboard():
    print(
        "\n :::    :::     :::     ::::    :::  ::::::::  ::::    ::::      :::     ::::    ::: \n :+:    :+:   :+: :+:   :+:+:   :+: :+:    :+: +:+:+: :+:+:+   :+: :+:   :+:+:   :+: \n +:+    +:+  +:+   +:+  :+:+:+  +:+ +:+        +:+ +:+:+ +:+  +:+   +:+  :+:+:+  +:+ \n +#++:++#++ +#++:++#++: +#+ +:+ +#+ :#:        +#+  +:+  +#+ +#++:++#++: +#+ +:+ +#+ \n +#+    +#+ +#+     +#+ +#+  +#+#+# +#+   +#+# +#+       +#+ +#+     +#+ +#+  +#+#+# \n #+#    #+# #+#     #+# #+#   #+#+# #+#    #+# #+#       #+# #+#     #+# #+#   #+#+# \n ###    ### ###     ### ###    ####  ########  ###       ### ###     ### ###    #### \n"
    )
    print(
        "\n    ┬ ┬┬┌┬┐┬ ┬  ╔╦╗╔═╗╔═╗╔═╗╦    ┬ ┬┌─┐┬─┐┌┬┐┌─┐ \n    ││││ │ ├─┤   ║ ║ ║║╣ ╠╣ ║    ││││ │├┬┘ ││└─┐ \n    └┴┘┴ ┴ ┴ ┴   ╩ ╚═╝╚═╝╚  ╩═╝  └┴┘└─┘┴└──┴┘└─┘ \n"
    )
    return


def ErrorCheck(wrongs,corrects,entry):
    errors={
        'Duplicate': "You already entered that. Guess a new letter.",
        'Nonletter': "That's not a letter. Please enter only letters.",
        'OnlyOne' : "Please enter only one letter."
    }

    error=None
    if entry in wrongs or entry in corrects:
        error=self.Duplicate
    if not entry.isalpha():
        error=self.Nonletter
    if len(entry)>1:
        error=self.OnlyOne

    return error

class HangedMan:
    """Gets level of hanging (number of wrong guesses) and returns related art."""

    def __init__(self,level) -> None:
        return self.levels[level]

    face = "         --------        \n   	| /     |       \n   	|       |       \n  	|     ෴෴෴    \n   	|    (͡❛ ͜ʖ ❛)    \n   	|      ┏皿┛     \n   	|      / \      \n	|               \n                    "
    body = "         --------        \n   	| /     |       \n   	|       |       \n  	|     ෴෴෴    \n   	|     (   )    \n   	|      ┏皿┛     \n   	|      / \      \n	|               \n                    "
    head = "         --------        \n   	| /     |       \n   	|       |       \n  	|     ෴෴෴    \n   	|     (   )    \n   	|               \n   	|               \n	|               \n                    "
    choobe = "         --------        \n   	| /     |       \n   	|       |       \n  	|               \n   	|              \n   	|               \n   	|               \n	|               \n                    "
    dead = "         --------        \n   	| /     |       \n   	|       |       \n  	|     ෴෴෴    \n   	|     (*﹏*)    \n   	|      ┏皿┛     \n   	|      / \      \n	|               \n                    "
    levels = {
        0:"",
        1:choobe,
        2: head,
        3: body,
        4: face,
        5: dead
    }

class Message:

    def __init__(self,message,toprint=True):
        msg=random.choices(message)
        if toprint:
            print(msg)
        else:
            return msg

    intro = ["""Hi! Ready to play some Hangman?
    If yes, type '1' to begin. 
    If no, type '0' to end the program. \n"""]

    first_guess = ["\n Here we go! Guess a letter: \n"]

    next_guess= ["Guess another:"]

    correct=[
        'Correct!',
        'Awesome!',
        'Yess!',
        'Woohoo!',
        'You got it!'
    ]

    wrong=[
        'oops!',
        'nope :(',
        "don't lose your head!"
        ]

    congrats=["You did it! Congrats!"]

    fail = ["""\n oops :( 
        the word was {}. You'll get it next time!"""]

    replay = ["type 1 to play again, or type 0 to exit: \n"]

    wrong_list = ["Wrong Guesses: {}   {} left"]

    exit = ['See you later!', 'Bye!', 'Come back soon!']




class Game:
    #The main game flow
    def __init__(self, words, wrong_limit=5) -> None:
        chosen_word:list = list(random.choice(words).lower())
        length:int=len(chosen_word)
        corrects:list = ['_' for i in range (length)]
        wrongs:list=[]
        wrong_limit=wrong_limit




    """def print_corrects(self) -> None:
        print (*self.corrects)
        """
    def print_wrongs(self) -> None:
        wrong_count = len(self.wrongs)
        msg = Message(Message.wrong_list,toprint=False)
        
        if wrong_count==0:
            msg = msg.format('None',self.wrong_limit-wrong_count)
        else:
            msg = msg.format(self.wrongs.join(), self.wrong_limit - wrong_count)

        print (msg)

    def print_hanged_man(self) -> str:

        wrong_count=len(self.wrongs)
        print (HangedMan(level=wrong_count))

    def validate_guess(self):
        while True:
            guess = input()
            is_error = Errors.is_error(wrongs=self.wrongs,
                                       corrects=self.corrects,
                                       entry=guess)
            if is_error:
                print(is_error)
            else:
                return guess

    def is_over(self):
        wrong_count = len(self.wrongs)
        if wrong_count==self.wrong_limit:
            return True
        return False

    def is_success(self):
        if self.chosen_word==self.corrects:
            return True
        return False

    def game_over(self):
        Message(Message.fail)

    def update_corrects(self,guess):
        for i in range (self.length):
            if self.chosen_word[i]==guess:
                self.corrects[i]==guess
        return

    def update_wrongs(self,guess):
        self.wrongs.append(guess)
        return

    def run(self):
        Message(Message.intro)
        if input()=='1':
            self.print_corrects()
            Message(Message.first_guess)

            while not(self.is_over()) and not(self.is_success()):
                guess=self.validate_guess()
                if guess in self.chosen_word:
                    self.update_corrects(guess)
                    Message(Message.correct)
                    self.print_corrects()
                    self.print_hanged_man()
                    self.print_wrongs()


        else:
            Message(Message.exit)
            return

        play=True
        while play is True:
            self.print_corrects()
