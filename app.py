from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    role = request.form.get("role")  # "student" or "admin"
    if role == "admin":
        return redirect(url_for("admin_portal"))
    elif role == "student":
        return redirect(url_for("student_portal"))
    else:
        return redirect(url_for("index"))

# -------- Student Routes --------
@app.route("/student")
def student_portal():
    return render_template("student.html")

@app.route("/student/videos")
def student_videos():
    return render_template("videos.html")

@app.route("/student/classnotes")
def student_classnotes():
    return render_template("classnotes.html")

@app.route("/student/dpp")
def student_dpp():
    return render_template("dpp.html")

# -------- Admin Routes --------
@app.route("/admin")
def admin_portal():
    return render_template("admin.html")

if __name__ == "__main__":
    app.run(debug=True)
