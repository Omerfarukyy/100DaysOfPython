from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

coffee_choice = ["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"]
wifi_choice = ["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"]
power_choice = ["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"]

# def is_url():
#     pass
class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    url = StringField(label="Location URL", validators=[DataRequired()])
    open_time = StringField(label="Open Time", validators=[DataRequired()])
    closing_time = StringField(label="Closing Time", validators=[DataRequired()])
    coffee = SelectField(label="coffee rating", validators=[DataRequired()], choices=coffee_choice)
    wifi = SelectField(label="wifi rating", validators=[DataRequired()], choices=wifi_choice)
    power = SelectField(label="power outlet rating", validators=[DataRequired()], choices=power_choice)

    submit = SubmitField('Submit')


# use a validator to check that the URL field has a URL entered.


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        row = (f"\n{form.cafe.data},{form.url.data},{form.open_time.data},{form.closing_time.data},"
               f"{form.coffee.data},{form.wifi.data},{form.power.data}")

        with open('cafe-data.csv', mode='a', encoding='utf-8') as fd:
            fd.write(row)
        return render_template("index.html")
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
