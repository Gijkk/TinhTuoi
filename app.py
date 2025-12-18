from flask import Flask, request, Response
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        birth_year = request.form.get("birth_year", "").strip()

        if not birth_year.isdigit():
            return Response("Nam sinh khong hop le", mimetype="text/plain")

        birth_year = int(birth_year)
        current_year = datetime.now().year

        if birth_year < 1950 or birth_year > current_year:
            return Response("Nam sinh khong hop le", mimetype="text/plain")

        age = current_year - birth_year
        return Response(f"Tuoi cua ban la {age}", mimetype="text/plain")

    return Response("Nhap nam sinh", mimetype="text/plain")


if __name__ == "__main__":
    app.run(debug=True)
