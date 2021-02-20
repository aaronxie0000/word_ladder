#!/bin/python3
from collections import deque
import copy


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony',
    'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots',
    'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    if (start_word == end_word):
        return [start_word]
    # to convert to dictionary
    my_dictionary = {}
    i = 1
    with open(dictionary_file) as f:
        words = f.readlines()
        for entry in words:
            my_dictionary[i] = entry[:-1]
            i += 1
    # start of code
    my_stack = []
    my_stack.append(start_word)
    my_queue = deque([])
    my_queue.append(my_stack)

    while len(my_queue) != 0:
        curr_stack = my_queue.popleft()
        for k, x in list(my_dictionary.items()):
            if _adjacent(curr_stack[-1], x):
                if (x == end_word):
                    curr_stack.append(x)
                    return curr_stack
                copy_stack = copy.copy(curr_stack)
                copy_stack.append(x)
                my_queue.append(copy_stack)
                del my_dictionary[k]
    return None


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if (len(ladder) == 0):
        return False
    for i in range(0, len(ladder)-1):
        if (not _adjacent(ladder[i], ladder[i+1])):
                return False
    return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    if len(word1) != len(word2):
        return False
    list_word_2 = list(word2.lower())
    diff_char = 0
    for i, x in enumerate(list(word1.lower())):
        if x != list_word_2[i]:
            diff_char += 1
    if diff_char != 1:
        return False
    return True
