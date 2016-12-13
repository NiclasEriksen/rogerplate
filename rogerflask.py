from flask import Flask, render_template


app = Flask(__name__)


@app.route("/bruker/<nickname>")
def bruker(nickname):
    return render_template("bruker.html", nickname=nickname)


if __name__ == "__main__":
    app.run(debug=True)
