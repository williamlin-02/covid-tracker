# William Lin, Jeff Lin, Calvin Chu, Kevin Cai - Team potato_monkeys
# SoftDev2 pd9
# P04 - Let the Data Speak
# 2020-04-30

from flask import Flask, render_template
import urllib.request, json

from pprint import pprint

app = Flask(__name__)

def getdata():
    u = urllib.request.urlopen("https://api.covid19api.com/summary")
    response = u.read()
    data = json.loads(response)
    return data

@app.route("/")
def root():
    try:
        data = getdata()
    except:
        return render_template('error.html')
    return render_template('index.html', data = data, updated = data['Date'])


if __name__ == "__main__":
    app.debug = True
    app.run()
