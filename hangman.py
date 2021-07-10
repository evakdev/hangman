import random
"""
To use for finding suitable symbols: 
https://www.branah.com/unicode-converter
https://www.ssec.wisc.edu/~tomw/java/unicode.html#x0300 """

#import pygsheets

print("\n :::    :::     :::     ::::    :::  ::::::::  ::::    ::::      :::     ::::    ::: \n :+:    :+:   :+: :+:   :+:+:   :+: :+:    :+: +:+:+: :+:+:+   :+: :+:   :+:+:   :+: \n +:+    +:+  +:+   +:+  :+:+:+  +:+ +:+        +:+ +:+:+ +:+  +:+   +:+  :+:+:+  +:+ \n +#++:++#++ +#++:++#++: +#+ +:+ +#+ :#:        +#+  +:+  +#+ +#++:++#++: +#+ +:+ +#+ \n +#+    +#+ +#+     +#+ +#+  +#+#+# +#+   +#+# +#+       +#+ +#+     +#+ +#+  +#+#+# \n #+#    #+# #+#     #+# #+#   #+#+# #+#    #+# #+#       #+# #+#     #+# #+#   #+#+# \n ###    ### ###     ### ###    ####  ########  ###       ### ###     ### ###    #### \n")
print("\n    ┬ ┬┬┌┬┐┬ ┬  ╔╦╗╔═╗╔═╗╔═╗╦    ┬ ┬┌─┐┬─┐┌┬┐┌─┐ \n    ││││ │ ├─┤   ║ ║ ║║╣ ╠╣ ║    ││││ │├┬┘ ││└─┐ \n    └┴┘┴ ┴ ┴ ┴   ╩ ╚═╝╚═╝╚  ╩═╝  └┴┘└─┘┴└──┴┘└─┘ \n")


# pygsheets code preparations
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

#Error function
def error_finder(g):
    global wrongletters
    global userresult
    flag=True
    if g in wrongletters or g in userresult:
        print("You already entered that. Guess a new letter.")
        flag=False
    if not g.isalpha():
        print("That's not a letter. Please enter only letters.")
        flag=False
    if len(g)>1:
        print("Please enter only one letter.")
        flag=False
    return flag



#hanged man steps
facethings = "         --------        \n   	| /     |       \n   	|       |       \n  	|     ෴෴෴    \n   	|    (͡❛ ͜ʖ ❛)    \n   	|      ┏皿┛     \n   	|      / \      \n	|               \n                    "
body = "         --------        \n   	| /     |       \n   	|       |       \n  	|     ෴෴෴    \n   	|     (   )    \n   	|      ┏皿┛     \n   	|      / \      \n	|               \n                    "
head = "         --------        \n   	| /     |       \n   	|       |       \n  	|     ෴෴෴    \n   	|     (   )    \n   	|               \n   	|               \n	|               \n                    "
choobe = "         --------        \n   	| /     |       \n   	|       |       \n  	|               \n   	|              \n   	|               \n   	|               \n	|               \n                    "
dead = "         --------        \n   	| /     |       \n   	|       |       \n  	|     ෴෴෴    \n   	|     (*﹏*)    \n   	|      ┏皿┛     \n   	|      / \      \n	|               \n                    "
hanged = [choobe, head, body, facethings, dead]

#################
begin = int(input("Hi! Ready to play some Hangman? If yes, type '1' to begin. If no, type '0' to end the program. \n"))
while begin:
    begin=0
    myword=list(random.choice(words).lower())
    length=len(myword) 
    userresult=[]
    for i in range (length):
        userresult.append("_")
    
    print("\n Here we go! Guess a letter: \n")
    print(*userresult)
    guess=input().lower()
    mistakes=""
    wrongletters=[]

    while userresult!=myword and len(wrongletters)<5:
        ##Errors
        while error_finder(guess) is False: 
            guess = input("Enter:\n").lower()

        if guess in myword:
            print("\nCorrect!")
            if wrongletters:
                print ("Wrong Guesses:", *wrongletters, f" ({5-len(wrongletters)} left)")
            else:
                print("Wrong Guesses: None", f" ({5-len(wrongletters)} left)")
            for i in range (length): 
                if myword[i]==guess: 
                    userresult[i]=guess  
        else: 
            wrongletters.append(guess)
            print ("Wrong Guesses:",*wrongletters, f" ({5-len(wrongletters)} left)")
            print (hanged[len(wrongletters)-1])
        print(*userresult)

        if userresult != myword and len(wrongletters) <5:
            guess = input("\nGuess another: \n").lower()

    if userresult==myword:
        print("\n You did it! Congrats!")
    elif len(wrongletters)>=5:
        print("\n oops :( the word was", "'"+"".join(myword)+"'", ". You'll get it next time!")
    begin = int(input("type 1 to play again, or type 0 to exit: \n"))


