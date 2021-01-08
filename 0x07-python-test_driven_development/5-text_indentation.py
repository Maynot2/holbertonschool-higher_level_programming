#!/usr/bin/python3
"""Contains function(s) to format text"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: .?:"""

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    text = text.replace('.', '.\n\n┴¬')
    text = text.replace('?', '?\n\n┴¬')
    text = text.replace(':', ':\n\n┴¬')

    sentences = text.split('┴¬')

    for sentence in sentences:
        if sentence:
            print(sentence.strip(' \t\b\f\r\v'), end='')
