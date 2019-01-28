"""A madlib game that compliments its users."""

from random import choice
from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

COMPLIMENTS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely'
]


@app.route('/')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = choice(COMPLIMENTS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """Show form to play madlibs or say goodbye."""

    play_game = request.args.get("play")

    if play_game == "yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")


@app.route('/madlib')
def show_madlib():
    """Show resulting mablib."""

    name = request.args.get("person")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")

    return render_template("madlib.html",
                           person=name,
                           color=color,
                           noun=noun,
                           adjective=adjective,
                           )


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.
    app.run(host='0.0.0.0', debug=True)