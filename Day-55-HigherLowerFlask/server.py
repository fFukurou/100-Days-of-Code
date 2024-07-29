#Higher Lower Game Flask Project
#Should've used more decorators (H1 and HTML style) but was too tired zzz

import random

from flask import Flask
app = Flask(__name__)

random_number = random.randint(1, 10)



@app.route('/')
def home():
    return '<html lang="en" style="background-color: black;"></html>'\
    '<h1 style="text-align: center; color: white";> Guess a number between 1 and 10 (in the URL) </h1> '\
    '<img src="https://media.tenor.com/yNMGjXsoYGUAAAAM/cat-cats.gif" '\
    'alt="Cat sus"'\
    'width="400px"'\
    'height="400px"'\
    'style="border: 3px solid white;"/>'\
    ''

def lower_page():
    return '<html lang="en" style="background-color: black;"></html>'\
    '<h1 style="color: white";> Secret number is lower than that. </h1> '\
    '<img src="https://media.tenor.com/daC6nEIkZu8AAAAM/sims-glitch.gif " '\
    'alt="Cat sus"'\
    'width="800px"'\
    'height="400px"'\
    'style="border: 3px solid white;"/>'\
    ''

def higher_page():
    return '<html lang="en" style="background-color: black;"></html>'\
    '<h1 style="color: white";> Secret number is higher than that. </h1> '\
    '<img src="https://media.tenor.com/1K4D8YuyeaIAAAAM/gurren-lagann-simon-gl.gif" '\
    'alt="Cat sus"'\
    'width="700px"'\
    'height="400px"'\
    'style="border: 3px solid white;"/>'\
    ''

def guessed_page():
    return '<html lang="en" style="background-color: black;"></html>'\
    '<h1 style="color: white";> You guessed the secret number... yay </h1> '\
    '<img src="https://media.tenor.com/IMYaOgUHc5AAAAAM/breaking-bad-right.gif" '\
    'alt="Cat sus"'\
    'width="1500px"'\
    'height="400px"'\
    'style="border: 3px solid white;"/>'\
    ''


@app.route('/<number>')
def guess(number):
    if int(number) == random_number:
        return guessed_page()
    elif int(number) >= random_number:
        return lower_page()
    else:
        return higher_page()



if __name__ == "__main__":
    app.run(debug=True)


