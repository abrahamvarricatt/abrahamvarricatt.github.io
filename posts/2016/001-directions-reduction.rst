.. title: Puzzle: Directions Reduction
.. date: 2016-08-31 08:07:00
.. tags: puzzle, python

I came across a puzzle on `Code Wars <https://www.codewars.com/>`_ a short while ago. The core question could be summarized as follows,

Given a list of directions, reduce the amount of backtracking needed to arrive at a destination. For example, if ``plan=['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST']`` it can be reduced to ``plan=['WEST']``. The idea, is that opposite directions that are adjacent to each other should be reduced, i.e. ``'NORTH'`` cancels out ``'SOUTH'`` and ``'EAST'`` cancels out ``'WEST'``. A leeway the question gives is that you do not need to worry about circular cancellations. i.e. something like ``['NORTH', 'EAST', 'SOUTH', 'WEST']`` stays the way it is. 

After pondering on the puzzle for a bit, I came to the following solution,

.. code:: python

	reduce_direction = {
	  'NORTH': 'SOUTH',
	  'SOUTH': 'NORTH',
	  'EAST': 'WEST',
	  'WEST': 'EAST',
	  '': '',
	}

	def dirReduc(arr):
		updated = True
		while updated:
			updated = False  # reset marker
			current_result = []
			previous_entry = ''
			for pos, current_entry in enumerate(arr):
				if reduce_direction[previous_entry] == current_entry:
					previous_entry = ''  # To cancel it
					updated = True # A change was made
				else:
					if previous_entry is not '':
						current_result.append(previous_entry)
					previous_entry = current_entry
					if pos + 1 == len(arr):
						# At last element, so add it in
						current_result.append(current_entry)
			arr = current_result # we got new array
		return arr

Here's what went through my mind as I solved it - The first problem was to figure out a mechanism to detect adjacent entries which could be deleted. This meant that if I was looping over the original list and encountered something like ``'NORTH'`` next to a ``'SOUTH'``, it was a match. A dictionary with key-value pairs mapping the different invalid entries seemed like a simple way to accomplish this goal. Which is how ``reduce_direction`` came to be. 

The next question was how to handle the actual deletion, but do I really need to edit the original list? It might be easier (and possibly less destructive) to just make a new list. Then, instead of worrying about what elements to delete, I could just concern myself with the question of what elements to append to my new list! Which was how the for-loop came into being. Admittedly, it isn't as straight-forward as I would have liked. 

Here's how it works - as the loop runs over the list, it keeps a record of the previous entry in the loop, as well as the current entry. If the pair of previous + current, was valid the previous entry would be appended to the new list. It was possible that the current entry might make an invalid pair with the next entry in the list, so I deferred it's addition to the list until the next loop - where it would become the new previous entry. An exception to this is the case when we reach the last element of the list. This would have no next entry to compare against, so if I used ``enumerate()`` and ``len()`` in the for-loop to identify the last element and append it as a special case. 

This procedure would only work for a single iteration of the list. It is possible that, after removing a few invalid pairs, the new list might contain a new set of invalid pairs - which would need to be detected and removed. So, I put the entire thing in a ``while`` loop which would keep running until no changes were made to the solution list. 

And the whole thing worked. This isn't what intuitively felt like an elegant solution, but at least it got the job done. Off the top of my head here were a few concerns I had, 

* too many branches
* time complexity is horrific - the loop within a loop 
* too many variables declared

But how could the solution be imporved upon? I looked into other solutions to the same problem and found enlightenment! Let's go over a few high-lights. 

.. code:: python

	if sorted([arr[i], arr[i-1]]) in [["NORTH", "SOUTH"], ["EAST", "WEST"]]:

The above snippet aesthetically solves the issue of duplicated data with my ``reduce_direction`` dictionary. Instead of storing all four pairs, just club two of them together and use python's ``sorted()`` function to match them up. As much as I like how this looks, I can't help but worry about it's time complexity. Sure, for just 2 elements, ``sorted()`` shouldn't have issues, but the approach just doesn't feel like it would scale well. Still - worth nothing none-the-less. 


.. code:: python

	def dirReduc(arr):
		dir = " ".join(arr)
		dir2 = dir.replace("NORTH SOUTH",'').replace("SOUTH NORTH",'').replace("EAST WEST",'').replace("WEST EAST",'')
		dir3 = dir2.split()
		return dirReduc(dir3) if len(dir3) < len(arr) else dir3

Now, this is a nice bit of code. The author changes the problem from one of matching adjacent list entries to one of just matching strings. It simplifies a lot of the logic to a few ``replace()`` operations. Once that's done, just split the entire thing back into a list and we have a solution! Keep re-iterating until no changes occour. I'm not sure about time complexity for the ``replace()`` operations, but this seems to accomplish what I was trying to do in fewer lines of code. That is something to make a note of!!

.. code:: python

	opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

	def dirReduc(plan):
		new_plan = []
		for d in plan:
			if new_plan and new_plan[-1] == opposite[d]:
				new_plan.pop()
			else:
				new_plan.append(d)
		return new_plan

The top-voted entry however, is in a class of it's own. It actually manages to reduce the time-complexity of the solution to O(n) - something I wasn't sure was possible! The author makes use of a dictionary like I did, but exploits the in-built ``pop()`` and ``append()`` operations available for any python list. I had forgotten about ``pop()`` in lists until I saw this solution. What's really nice is how the author makes use of the ``list[-1]`` notation to grab the last element of the solution-list to compare with the current iterated elment. Damn! I wish I'd remembered that.

Compared to all this, my solution just looks needlessly complicated and embarrassing.

