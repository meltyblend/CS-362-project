#this is where the backend starts and where all of the server side routing is going to be done


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World! Flask backend is running."

if __name__ == '__main__':
    app.run(debug=True)