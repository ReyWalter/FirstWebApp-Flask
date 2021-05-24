from flask import Flask # Import flasks

app = Flask(__name__)

@app.route("/") # Home page

def index():
    return "<h1>Hello World. I wanna be come a good Python developer</h1>" # Returns a string to the web page

@app.route("/<celsius>")
def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return "invalid input"

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="8080", debug=True) # Start server