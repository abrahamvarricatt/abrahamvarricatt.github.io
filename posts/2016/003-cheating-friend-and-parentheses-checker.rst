.. title: Puzzles: Cheating Friend and Parentheses Checker
.. date: 2016-09-14 19:20:00
.. tags: puzzle, python

I've got two puzzles from `Code Wars <https://www.codewars.com/>`_ today. The first one is,

A friend of mine takes a sequence of numbers from 1 to n (n > 0). Within that sequence he chooses two numbers A and B.
He claims that the product (A * B) should be equal to the sum of all the numbers in the sequence, excluding A and B (
i.e. SUM - (A+B) ). Given a number n, can you identify all the number pairs which match the earlier assertion?

The question wanted me to return the answer as a list. Perfect opportunity for my list comprehension skills! But that
would mean reducing the solution to a form of only one variable. Here's how I performed the reduction,

.. code::

    A * B     = SUM - (A + B)
              = SUM - A - B
    AB + B    = SUM - A
    B (A + 1) = SUM - A
    B         = SUM - A/(A + 1)

A simple formula for B in terms of SUM and variable A! Here's the solution I came up with,

.. code:: python

    def removNb(n):
        total = sum(range(1, n + 1))
        return [(A, int((total - A)/(A + 1))) for A in range(1, n + 1) if float((total - A)/(A + 1)).is_integer() and n > (total - A)/(A + 1)]

The line extends a bit too much to the side, but it's a compact solution which fit in well with the other results. My
skills are improving! :)

Another solution which caught my attention is this,

.. code:: python

    import math

    def removNb(n):
        res = []
        tot = sum(range(n+1))
        for a in range(n,int(math.sqrt(tot)),-1):
            b = tot%a
            if a*b==tot-a-b:
                res.append((b,a))
                res.append((a,b))
        return sorted(res)

Nothing too revolutionary about this one, but it just *feels* inelegant. One thing that's not so inelegant is the
assertion made that B = SUM % A. Which, I couldn't understand. Fortunately, a comment explained it,

.. code::

    SUM - (A + B) = A * B
    SUM           = A * B + (A + B)
    { Perform % A operation on both sides }
    SUM % A       = (A * B + (A + B)) % A
                  = (A * B) % A) + ((A + B) % A)
                  = ((A % A) * (B % A)) + ((A % A) + (B % A))
                  = (0 * (B % A)) + (0 + (B % A))
                  = B % A

That's some very impressive mathematics right there!

The second puzzle is about parenthesis matching. i.e. these things - ``()``. The problem was to identify if they are
ordered correctly in an input string. Which means something like ``(())`` is valid but ``())(`` is not. My solution
went like this,

.. code:: python

    def valid_parentheses(string):
        status = 0
        for letter in string:
            if letter == '(':
                status += 1
            elif letter == ')':
                if status == 0:
                    return False
                else:
                    status -= 1
        if status == 0:
            return True
        else:
            return False

As valid as that is, it just felt a bit too big. But how could I reduce it any further, while maintaining its
readability? The top voted answer showed me,

.. code:: python

    def valid_parentheses(string):
        cnt = 0
        for char in string:
            if char == '(': cnt += 1
            if char == ')': cnt -= 1
            if cnt < 0: return False
        return True if cnt == 0 else False

In an odd sort of way, I'm a bit disappointed to see this. It reads really well, but implies that my Python skills need
polishing - just as I was feeling good about them!


