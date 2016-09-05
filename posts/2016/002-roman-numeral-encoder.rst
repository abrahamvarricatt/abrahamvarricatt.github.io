.. title: Puzzle: Roman Numeral Encoder
.. date: 2016-09-05 20:48:00
.. tags: puzzle, python

This is another one from `Code Wars <https://www.codewars.com/>`_ - write a function to convert an integer into the
string representation of itself, in the `roman numeral format <https://en.wikipedia.org/wiki/Roman_numerals>`_.

The wikipedia page tells us the symbols used in the Roman numeral alphabet as well as how to count them. After studying
this, I came to the realization that the basic sequence was repeated for every digit - the letters were the different,
but for every digit in our base-10 system, the pattern to write them in the Roman pattern was the same! Surely, I could
make use of this insight in my solution? Which was how I came up with this,

.. code:: python

    digit_map = [
        # For one's location
        {
            '1': 'I',
            '5': 'V',
            '0': 'X',
        },
        # For ten's location
        {
            '1': 'X',
            '5': 'L',
            '0': 'C',
        },
        # For hundred's location
        {
            '1': 'C',
            '5': 'D',
            '0': 'M',
        },
        # For thousand's location
        {
            '1': 'M',
            '5': '5',  # not sure beyond this
            '0': '0',
        },
    ]

    def translate_digit(digit, letter_map):
        digit_map_dict = {
            '0': '',
            '1': letter_map['1'],
            '2': letter_map['1'] + letter_map['1'],
            '3': letter_map['1'] + letter_map['1'] + letter_map['1'],
            '4': letter_map['1'] + letter_map['5'],
            '5': letter_map['5'],
            '6': letter_map['5'] + letter_map['1'],
            '7': letter_map['5'] + letter_map['1'] + letter_map['1'],
            '8': letter_map['5'] + letter_map['1'] + letter_map['1'] + letter_map['1'],
            '9': letter_map['1'] + letter_map['0'],
        }
        return digit_map_dict[digit]

    def solution(n):
        result = ''
        for position, digit in enumerate(str(n)[::-1]):
            result = translate_digit(digit, digit_map[position]) + result
        return result

Something about the above solution that I was proud of was the use of ``enumerate()`` in the for-loop. In the initial
write-up, I used a local variable to keep track of the position, but after investigating for a more Pythonic way of
coding, the above solution came to me. One nice tactic I learned was the fast shortcut to reverse a string in Python.
Just add ``[::-1]`` to the end of the string. It treats the string as a list without a start/end location, but
increments backwards - effectively reversing it!

Regardless, there's one thing about my solution that cannot be denied - it's long. That's not really an issue by
itself, but a part of me just felt like there should be a better way of handling that logic - and I couldn't figure
out what that was. Soo, onto the top answers to the puzzle!

.. code:: python

    def solution(n):
        roman_numerals = {
            1000:'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }
        roman_string = ''
        for key in sorted(roman_numerals.keys(),reverse=True):
            while n >= key:
                roman_string += roman_numerals[key]
                n -= key
        return roman_string

And this puts my answer to such shame, that it makes it seem down-right pathetic! But damn, isn't this admirable? This might
arguably, be the first time I'm seeing someone use integers as keys in a python dictionary. It's a feature that I've
seen in documentation, but not in actual use. At first, the solution didn't make sense to me - to exploit the numbers,
you would need a guarantee that they would be picked up in order when looping over them - something which the
documentation for a Python dictionary states as not possible!

It was then that I noticed the ``reverse=True`` part. What would that be passed to? A ``sorted()`` function? How would
that work ..? And then, it hit me! Every Python dictionary has a method called ``keys()`` which returns a list of all
the keys present in the dictionary. What this solution does is sort that list and pass it on as an iterator to a
for-loop. Sheer brilliance! Don't bother iterating the dictionary - if you need it sorted; grab the keys, sort and loop
over them instead!

Doing things in this manner also assures us that the Roman translation is handled from the highest to lowest base-10
digit - allowing us to just append the translated string as we go along - bypassing the need for my earlier prepend
logic.
