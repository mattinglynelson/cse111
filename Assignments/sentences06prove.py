import random
from webbrowser import get


def main(): 
    tense = input('What tense should this sentence be in? ')
    quantity = int(input('What is the quantity of the noun? '))
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase = get_prepositonal_phrase(quantity)
    print(f'{determiner.capitalize()} {noun} {verb} {prepositional_phrase}.')

    return(tense, quantity)





def get_determiner(quantity):
    if quantity  == 1:
        words = ['a', 'the', 'one']
    else:
        words = ['a ton of', 'prolly about 5', 'several', 'the']

    rando_determiner = random.choice(words)

    return rando_determiner

def get_noun(quantity):
    if quantity==1:
        noun_list = ['Daniel','dog', 'human', 'idiot', 'Bill Nye']
        rando_noun = random.choice(noun_list)
    else:
        noun_list = ['Williams','dogs','humans', 'idiots', 'Daniels']
        rando_noun = random.choice(noun_list)
    return rando_noun

def get_verb(quantity, tense):
    verb_list = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    if tense == 'past':
        verb_list = [ "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    if tense == 'present' and quantity == 1:
        verb_list = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    if tense == 'present' and quantity != 1:
        verb_list = [ "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    if tense == 'future':
        verb_list = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    rando_verb = random.choice(verb_list)
    return(rando_verb)

def get_preposition():
    prep_list = [ "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    rando_prep = random.choice(prep_list)
    return rando_prep

def get_prepositonal_phrase(quantity):
    prep_phrase = (f'{get_preposition()} {get_determiner(quantity)} {get_noun(quantity)}')
    return prep_phrase

main()



















