from flask import Flask # Import flasks

app = Flask(__name__)

@app.route("/") # Home page

def index():
    return "Congratulations, it's a web app!" # Returns a string to the web page

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="8080", debug=True) # Start server