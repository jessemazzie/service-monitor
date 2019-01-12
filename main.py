from flask import Flask
import network_utils as nu

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, world!"


if __name__ == "__main__":
    app.run(debug=True)

#print(nu.checkport("www.google.com", 65546))
#print(ping("www.google.com"))



