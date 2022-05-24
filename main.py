from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, SearchField, StringField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "princeviditauditaakshay"

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)


class Hospitals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hospital_name = db.Column(db.String(100), unique=False)
    hospital_location = db.Column(db.String(100))
    hospital_beds = db.Column(db.Integer)
    hospital_doctors = db.Column(db.Integer)
    hospital_ambulance = db.Column(db.Integer)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.hospital_name


class Ngos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ngo_name = db.Column(db.String(100), unique=False)
    ngo_location = db.Column(db.String(100))
    ngo_volunteers = db.Column(db.Integer)
    img_url = db.Column(db.String(250), nullable=False)


class Campaigns(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    campaign_name = db.Column(db.String(100), unique=False)
    campaign_location = db.Column(db.String(100))
    campaign_volunteers = db.Column(db.Integer)
    img_url = db.Column(db.String(250), nullable=False)


db.create_all()


class SolaceForm(FlaskForm):
    TypeOfSearch = StringField("What are you searching for?", validators=[DataRequired()])
    location = StringField("Your Location", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search", methods=['GET', 'POST'])
def search():
    form = SolaceForm()
    if form.validate_on_submit():
        health = form.TypeOfSearch.data
        location = form.location.data
        hospitals = Hospitals.query.all()
        campaigns = Campaigns.query.all()
        ngos = Ngos.query.all()
        return render_template("show_post.html", all_hospitals=hospitals, all_campaigns=campaigns, all_ngos=ngos,
                               form_health=health, form_location=location)
    return render_template("hospitals.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
