from flask import Flask, render_template, redirect, url_for

from app import app
from app.classes.user import User
from app.forms.forms import SubmitInvite


@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def main():
    return render_template('main.html')

@app.route("/invites", methods=["GET", "POST"])
def invites():
    users = User.get_users()
    user_count = [*range(1, len(users)+1)]
    users = list(zip(users, user_count))
    return render_template('invites.html', users=users)

@app.route("/invites/<user_id>", methods=["GET", "POST"])
def contact(user_id):
    form = SubmitInvite()
    if form.validate_on_submit():
        User.delete_user_by_id(user_id)
        return redirect(url_for('invites'))
    return render_template('contact.html', user=User.get_user_by_id(user_id), form=form)