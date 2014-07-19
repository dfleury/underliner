Underliner
==========

This is a *space to underline* converter plugin for Sublime Text 3

Motivation
----------

I figured out how boring is write python methods to describe a test case typing
underlines (also called underscore) instead of spaces.
So I made this plugin to replace spaces contained in selected code chunks in a
practical way.

Usage example
-------------

```
test if can sum two numbers
more   than  one spaces
```

After selecting a text like that above, there are many ways to activate the
Underliner command such: context menu, main menu (`Edit > Convert Case >
Underliner`), command list (`[Ctrl/Cmd]+Shift+P > Convert Case: Underliner`)
and the keyboard shortcut (`[Ctrl/Cmd]+Shift+U`), which is my preferred option.
The expected effect is the same text with each space character replaced to a
underline:

```
test_if_can_sum_two_numbers
more___than__one_spaces
```
You can do the reverse too. Same principle: select and execute the command.
Spaces and underlines are counted and the most found charactere will be used as
target to replace, maintaining the less found characteres.

License
-------

The MIT License (MIT) - Copyright (c) 2014 Diego Fleury
