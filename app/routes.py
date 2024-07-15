# app/routes.py
from flask import render_template, redirect, url_for, request, jsonify
from . import db
from .forms import NameForm
from .models import FormData
from flask import current_app as app

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        age = form.age.data
        gender = form.gender.data

        # Insert form data into the database
        form_data = FormData(name=name, age=age, gender=gender)
        db.session.add(form_data)
        db.session.commit()

        return redirect(url_for('success', name=name, age=age, gender=gender))
    return render_template('index.html', form=form)


@app.route('/success')
def success():
    name = request.args.get('name')
    age = request.args.get('age')
    gender = request.args.get('gender')
    return render_template('success.html', name=name, age=age, gender=gender)


@app.route('/users')
def user_list():
    all_users = FormData.query.all()
    return render_template('users.html', users=all_users)


############ API Routes ##############

@app.route("/api/users", methods=["GET"])
def get_users():
    users = FormData.query.all()
    users_list = []
    for user in users:
        user_data = {
            "id": user.id,
            "name": user.name,
            "age": user.age,
            "gender": user.gender
        }
        users_list.append(user_data)
    return jsonify({"users": users_list}), 200


@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json()

    if not data:
        return {"error": "No input data provided"}, 400
    
    name = data.get("name")
    age = data.get("age")
    gender = data.get("gender")

    if not name or not age or not gender:
        return {"error": "Missing required fields"}, 400
    
    new_user = FormData(name=name, age=age, gender=gender)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User created successfully", "user": {"name": name, "age": age, "gender": gender}}), 201