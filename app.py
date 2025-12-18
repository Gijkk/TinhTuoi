from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    current_year = datetime.now().year
    age = None
    error = None

    if request.method == "POST":
        birth_year = request.form.get("birth_year", "").strip()

        if not birth_year.isdigit():
            error = "Năm sinh phải là số"
        else:
            birth_year = int(birth_year)
            if birth_year < 1950 or birth_year > current_year:
                error = f"Năm sinh phải từ 1950 đến {current_year}"
            else:
                age = current_year - birth_year

    return render_template(
        "index.html",
        current_year=current_year,
        age=age,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)


