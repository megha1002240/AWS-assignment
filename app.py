from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="megha",
    password="StrongPassword123",
    database="db"
)

@app.route("/", methods=["GET", "POST"])
def home():
    cursor = db.cursor()

    if request.method == "POST":
        name = request.form["username"]
        cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
        db.commit()

    cursor.execute("SELECT name FROM users")
    users = cursor.fetchall()
    return render_template("index.html", users=users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
