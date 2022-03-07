from sentences06prove import get_determiner, get_noun, get_verb, get_preposition, get_prepositonal_phrase
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ['a', 'the', 'one']

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ['a ton of', 'prolly about 5', 'several', 'the']

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Get a random number between 2 and 10 inclusive.
        quantity = random.randint(2, 11)

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(quantity)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_noun():

    single_nouns = ['Daniel','dog', 'human', 'idiot', 'Bill Nye']

    for _ in range (4):
        word = get_noun(1)
        assert word in single_nouns
    
    plural_nouns = ['Williams','dogs','humans', 'idiots', 'Daniels']

    for _ in range(4):
        quantity = random.randint(2,11)
        word = get_noun(quantity)
        assert word in plural_nouns

def test_verb():
    verb_list =["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    for _ in range(9):
        word = get_verb(1, 'past')
        assert word in verb_list

    past_verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    for _ in range (100):
       
        word = get_verb(1 or 2, 'past')
        assert word in past_verbs

    present_quantity_1_verbs = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range (9):
        word = get_verb(1, 'present')
        assert word in present_quantity_1_verbs

    present_quantity_2_verbs = [ "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    for _ in range (9):
        word = get_verb(2, 'present')
        assert word in present_quantity_2_verbs

    future_verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    for _ in range (9):
        word = get_verb (2 or 1, 'future')
        assert word in future_verbs

def test_get_prep():
    preps = [ "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    for _ in range (100):
        word = get_preposition()
        assert word in preps
quantity = 1
def test_prep_phrase():
    prep_phraser = (f'{get_preposition()} {get_determiner(quantity)} {get_noun(quantity)}')
    for _ in range (100):
        word = get_prepositonal_phrase(quantity)
        assert word in prep_phraser


pytest.main(["-v", "--tb=line", "-rN", __file__])