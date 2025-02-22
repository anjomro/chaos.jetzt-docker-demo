from flask import Flask
import os
app = Flask(__name__)


name = os.environ.get('CHAOS_NAME', 'Chaos')
password = os.environ.get('PASSWORD', 'foo')
@app.route('/')
def hello_world():  # put application's code here
    return f'Hello {name}! Dein Password ist {password}'


if __name__ == '__main__':
    app.run()
