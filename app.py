
from flask import Flask, request, render_template, session, flash
import query

app = Flask(__name__)

"""@app.route("/") 
def frontpage():
    return render_template('front_page.html')

"""
@app.route('/', methods=('GET','POST','BACK'))

def dropdown():
    if request.method == 'BACK':
        countries = query.distinct_country()
        return render_template('home.html', countries = countries)

    if request.method == 'POST':
        requirements_lst=[]
        requirements_lst.append(request.form["country"])
        print(request.form["country"])
        print("------------------------Requirements_lst", requirements_lst)
        passwords = query.top200passwords(requirements_lst[0])
        return render_template('passwords.html', passwords=passwords)
    # virker ikke
    if request.method == 'POST':
        print("hello")
        requirements_lst=[]
        requirements_lst.append(request.form["example"])

        print("------------------------Requirements_lst", requirements_lst)
        
        
    
        

    countries = query.distinct_country()
    return render_template('home.html', countries = countries)

if __name__ == "__main__":
    app.run(port=5001)