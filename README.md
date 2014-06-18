# Programming Challenge

Hello, intrepid hacker! We have prepared a set of challenges for you to complete in your own time.

To get started just use this repo as your origin. Start hacking away at the problems and commit back here. Please commit and push often so that we can follow your progress.

The first problem comes with test cases, which you can use and extend. For the following problems you are expected to write your own tests.

You should be able to finish the problems below in less than two hours.


## Problem 1: Counting Words

The classic problem: how often did she say 'I love you'?

Given a stream of text on stdin, report on stdout the number of times each word appears, sorted by mentions with the most often mentioned word first. To break a tie, order the words in lexicographical order.

You will find a test case in `001-counting-words/test_count_words.py`. `cd` into the directory and run it with `py.test`.


## Problem 2: List Length

You are given a list implementation, aptly named `SingleMethodList`. This list
contains only one method:

```python
class SingleMethodList(object):

    def get(self, index):
        """ Returns the list item at `index`, otherwise returns None. """
        ...
```

You are required to calculate the length of this list, but due to immense
beaurocratic restrictions at OmniCorp, you are not allowed to modify the interface
of this class and you have to use it as is.

For this task you need to write a function `list_length(single_method_list)` that takes
a `SingleMethodList` instance and returns its length. Feel free to create your
own dummy implementation of `SingleMethodList` for your tests.


## Problem 3: Chaining Names

Your friends love music, and they like to play games. One game they like to play is to select the next song to play based on the current song. The next song has to begin with the same letter as the current song ends in.

For example, this playlist is valid:

+ 'Rock Me, Amadeus'
+ 'Song of the South'
+ 'Hooked on a Feeling'
+ 'Go Tell It on the Mountain'

So, given any starting and ending song, create a playlist that connects the two. For example: 'Island in the Sun' to 'Around the World'.

For extra credit, create the shortest playlist (in terms of duration!) that connects the two.

Your data set lives in `song-library.json` and should be self-describing.

Please include an analysis of the data structures and algorithms you chose, with a brief discussion of any alternative solutions you discarded and/or problems you faced and solved.


