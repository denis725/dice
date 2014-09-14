# Dice odds

This simple script allows you to calculate your odds of winning a check using different dice. This might be useful for playing role playing games.

## Usage
In the app folder, run:

    python odds.py 10 6 8 12

This means that you attempt to make a check of *10* (the first argument), using a *d6*, a *d8* and a *d12* (all following arguments). The result is:

    - You attempt to make a check of 10 by rolling a d6, d8 and a d12.
    - The odds of winning are 493 in 576, i.e. roughly 86 %.

## Options
If you have a bonus on your check (and are too lazy to add this up yourself), use the _bonus_ option:

    python odds.py 20 12 6 --bonus 8

This gives:

    - You attempt to make a check of 20 by rolling a d12 and a d6.
    - Your bonus on the check is 8.
    - The odds of winning are 3 in 8, i.e. roughly 37 %.

You may also let python roll the dice for you (but why would you?)
with the -r flag:

    python odds.py 12 6 8 -r
    - You attempt to make a check of 12 by rolling a d6 and a d8.
    - Rolling dice ... the result is 14 (12 was required), you win!

## Web app
You don't want to have your laptop sitting on your table while playing?
For convenience, there is also an integrated web app that allows you
to access a simple web site from your phone. To start the server, do this
in your dice folder (you need flask for that):

    python run.py

This will allow your phone to access the web app from
_<your-ip-address.port:5000>_
From there it should be pretty intuitive to use.

(Use google to find out how to find out your ip-address. You may have
to forward the port 5000 or change the port in _run.py_ to whatever
port it is that you have open. Use the web server at your own risk).

## Tests
If you want to modify something, run py.test to check if you have broken
something (you need pytest for that).

