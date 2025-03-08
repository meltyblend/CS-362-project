#this is where the backend starts and where all of the server side routing is going to be done


from flask import Flask, send_from_directory
import os, sympy

app = Flask(__name__, static_folder='frontend/static')
@app.route('/', defaults={'path': ''})

@app.route('/<path:path>')
def catch_all(path):
    # If a static file exists for the requested path, serve it
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    # Otherwise, serve index.html for Vue Router to handle routing
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)