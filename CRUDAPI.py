from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

# connecting MySql Database
app = Flask(__name__, template_folder='render html')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/books'
db = SQLAlchemy(app)


class booksdetails(db.Model):
    title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

# adding new book title to our database
@app.route("/", methods=['GET', "POST"])
def addNewTitle():
    if request.method == 'POST':
        book = request.form.get('title')
        entry = booksdetails(title=book)
        db.session.add(entry)
        db.session.commit()
    books = booksdetails.query.all()  # Retrieving books from database
    return render_template("home.html",books=books)


# To Update the books in database
@app.route("/update", methods=["POST"])
def update():
    newtitle = request.form.get("newtitle")
    oldtitle = request.form.get("oldtitle")
    book = booksdetails.query.filter_by(title=oldtitle).first()
    book.title = newtitle
    db.session.commit()
    return redirect("/")


# To Delete the books from database
@app.route("/delete", methods=["POST"])
def delete():
    title = request.form.get("title")
    book = booksdetails.query.filter_by(title=title).first()
    db.session.delete(book)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

