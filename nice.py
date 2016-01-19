from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

INSULTS = [
    'a jerk', 'a wimp', 'a coward', 'a punk', 'lame-o', 'a loooooser', 'a weirdo', 'weak sauce', 'a monkey',
    'stupid', 'puny']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Landing Page</title>
      </head>
      <body>
        <h1>Hi! This is the home page.</h1>
        <a href="/hello">Say Hello!</a>
      </body>
    </html>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <label>What's your name? <input type="text" name="person"></label>
          <br>
          Select your favorite compliment!
          <select name="compliment">
            <label><option value="awesome">Awesome</option></label>
            <label><option value="terrific">Terrific</option></label>
            <label><option value="fantastic">Fantastic</option></label>
            <label><option value="neato">Neato</option></label>
            <label><option value="fantabulous">Fantabulous</option></label>
            <label><option value="wowza">Wowza</option></label>
            <label><option value="oh-so-not-meh">Oh-So-NOT-Meh</option></label>
            <label><option value="brilliant">Brilliant</option></label>
            <label><option value="ducky">Ducky</option></label>
            <label><option value="coolio">Coolio</option></label>
            <label><option value="incredible">Incredible</option></label>
            <label><option value="wonderful">Wonderful</option></label>
            <label><option value="smashing">Smashing</option></label>
            <label><option value="lovely">Lovely</option></label>
          </select> 
          <br>
          <label><input type="submit"></label>
        </form>
        <br>
        <form action="/burn">
          <h1>Wanna get burned?</h1>
          <label>What's your name? <input type="text" name="person"></label>
          <br>
          <label><input type="submit"></label>
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body style="font-family: sans-serif">
        Hi %s, I think you're %s!
      </body>
    </html>
    """ % (player, compliment)


@app.route('/burn')
def burn_person():
    """Get user by name and insult them."""

    player = request.args.get("person")

    insult = choice(INSULTS)

    return """
    <!doctype html>
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body style="font-family: sans-serif">
        Hi %s, I think you're %s!
      </body>
    </html>
    """ % (player, insult)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
