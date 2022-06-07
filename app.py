from flask import Flask
from flask import render_template
import query

app = Flask(__name__)

@app.route("/") 
def frontpage():
    return render_template('front_page.html')


@app.route('/countries', methods=['GET'])
def dropdown():
    countries = query.distinct_country()
    return render_template('test.html', countries = countries)

if __name__ == "__main__":
    app.run(port=5000)