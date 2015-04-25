from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! This is the home page. Click here if you want to go to a game: <a href='/decision'>Here</a>"

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return render_template("hello.html")

@app.route('/greet')
def greet_person():
    player = request.args.get("person")

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route('/decision')
def make_decision():
    return  render_template("compliment.html")

@app.route('/game')
def show_game_form():
    # if submit = no send to goodbye.html
    # if submit = yes send to game.html!
    no = request.args.get("no")
    yes = request.args.get("yes")

    if no:
        return render_template("goodbye.html") 
    if yes:
        return render_template("game.html")

@app.route('/madlib')
def show_mad_lib():
    person = request.args.get("person") 
    color = request.args.get("color")
    adjective = request.args.get("adjective")
    noun = request.args.get("noun")

    return render_template("madlib.html", person=person, color=color, 
        adjective=adjective, noun=noun)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)


