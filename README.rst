#########
Happier
#########

A Python development tool that makes you Happier.

Happier formats, lints and sorts your imports. Happier is opinionated,
simple and just works, making you hopefully happier.

To run it just type ``happier`` and your code will be formatted.

*******************
What Happier does
*******************

Happier does a number of things with your code. First it runs
``isort`` to sort your imports and properly format them.

After having sorted them it runs ``autoflake`` to remove unused things.

Finally having done all of that it runs ``black`` to format the code nicely.

*************
Why Happier
*************

Happier was developed by myself, `William Rudenmalm (https://whn.se)`
because I felt that Python was falling behind on automatically
formatting and fixing my code. All the parts where already there I
just needed those 50 lines of code to tie it all together.

With well-wishes and hopes for brigther days ahead in these troubled
times.

~William Rudenmalm

Stockholm, 22 June, 2020
