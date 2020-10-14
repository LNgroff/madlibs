"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display gamepage."""

    return render_template("compliment.html")


# @app.route('/hello')
# def say_hello():
#     """Say hello to user."""

#     return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")


    return render_template("compliment.html",
                           person=player)

@app.route('/game')
def show_madlib_form():
    """Ask to play a game."""

    # return render_template("compliment.html")
    answer = request.args.get("game")
    print(answer)

    if answer == "no":
        return render_template("goodbye.html",
                                game=answer)
    elif answer == "yes": 
        return render_template("game.html", game = answer)

# def show_madlib_form():
#     """Ask to play a game."""

    

@app.route('/madlib')
def show_madlib():

    person = request.args.get("person")
    color = request.args.get("color")
    noun = request.args.get("noun")

    return render_template("madlib.html", person=person, color=color, noun =noun)



if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
