from flask import Flask, render_template, session, flash, redirect, request

app = Flask(__name__)
app.secret_key = ' a key'

@app.route('/')
def index():
    return 'Hello World!'

app.run(debug = True)
