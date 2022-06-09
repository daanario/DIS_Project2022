import re
from tkinter import N
from flask import Flask, request, render_template, session, flash
import query

app = Flask(__name__)


@app.route("/") 
def frontpage():
    return render_template('front_page.html')


# @app.route('/', methods=('GET','POST','BACK'))

@app.route("/dropdown", methods = ('GET','POST','BACK')) 
def dropdown():
    if request.method == 'BACK':
        countries = query.distinct_country()
        return render_template('home.html', countries = countries)

    if request.method == 'POST':
        requirements_lst=[]
        requirements_lst.append(request.form["country"])
        print(request.form["country"])
        print("------------------------Requirements_lst", requirements_lst)
        passwords = query.top200passwords(requirements_lst[0])[0]
        usercounts = query.top200passwords(requirements_lst[0])[1]
        cracktimes = query.top200passwords(requirements_lst[0])[2]
        poslst = [i for i in range(1,201)]
        passwlst= [(ipos, ipass, iuser, icracktime) for ipos, ipass, iuser, icracktime in zip(poslst, passwords, usercounts, cracktimes)]
        return render_template('passwords.html', passwords=passwlst)

    countries = query.distinct_country()
    return render_template('dropdown.html', countries = countries)


@app.route('/search', methods=('GET','POST','BACK'))
def search():
    if request.method == 'BACK':
        countries = query.distinct_country()
        return render_template('home.html', countries = countries)

    if request.method == 'POST':
        requirements_lst=[]
        requirements_lst.append(request.form["password"])

        print("------------------------Requirements_lst", requirements_lst)
        
        countries = query.CountriesWithPassword(requirements_lst[0])
        print("-----------------------------------------------------",requirements_lst[0])
        print("hello",countries)
        return render_template('countries.html', countries=countries)
        
        

    countries = query.distinct_country()
    return render_template('search.html', countries = countries)

@app.route("/About-us")
def about_us():
    return render_template('about_us.html')


    
if __name__ == "__main__":
    app.run(port=5001)