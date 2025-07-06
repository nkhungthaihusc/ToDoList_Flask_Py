from flask import Blueprint, render_template,flash,request , jsonify
from flask_login import current_user , login_required
from .models import Note
from . import db
import json


view = Blueprint("view", __name__)



@view.route('/' , methods = ["GET" , "POST"])
@view.route("/home" , methods = ["GET" , "POST"])
def home():
    if request.method == "POST":
        note = request.form.get("note")
        if len(note) < 1:
            flash("Note is too short" , "error")
        else:
            new_note = Note(content= note , user_id = current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note added" , "success")

    return render_template('index.html' , user=current_user , user_name=current_user.user_name , icon_path="note.png")

@view.route("/delete-note" , methods=["GET" , "POST"])
def delete_note():
    note = json.loads(request.data)
    print(note)
    note_id = note["note_id"]
    result = Note.query.get(note_id)
    print(result)
    if result:
        if result.user_id == current_user.id:
            db.session.delete(result)
            db.session.commit()
    return jsonify({"code" : 200 })
