from flask import render_template, redirect
import connexion
import network_utils as nu

#Create the application instance
app = connexion.App(__name__, specification_dir='./')

#Configure the REST endpoints
app.add_api('swagger.yml')


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

# print(nu.checkport("www.google.com", 65546))
# print(ping("www.google.com"))
