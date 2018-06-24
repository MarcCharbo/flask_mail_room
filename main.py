import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation, Donor 

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('all'))

@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)

@app.route('/donate/', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        donor = Donor.select().where(Donor.name == request.form['name']).get()

        if donor:
            donation = Donation(value=request.form['donation'], donor=request.form['name'])
            donation.save()

        else:
            donor = Donor(name=request.form['name'])
            donor.save()
            donation = Donation(value=request.form['donation'], donor=request.form['name'])
            donation.save()

        return render_template('donations.jinja2')

    return render_template('donate.jinja2')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

