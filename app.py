from flask import Flask, render_template
from api import Crypto

app = Flask(__name__)

crypto = Crypto()

@app.route("/")
def home():
    results = crypto.get_top_10()
    for result in results:
        result['quote']['USD']['price'] = '$ ' + "{:.2f}".format(result['quote']['USD']['price'])
    return render_template("index.html",**locals())

if __name__ == "__main__":
    app.run()