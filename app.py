from flask import Flask, request, Response
from datetime import datetime

app = Flask(__name__)

LOWER_BOUND = 1950
UPPER_BOUND = 2025  # test đang FIX cứng năm này

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        birth_year_raw = request.form.get("birth_year", "")

        # Strip whitespace
        birth_year = birth_year_raw.strip()

        # 1️⃣ Không phải số (rỗng, chữ, chữ+số, thập phân)
        if not birth_year.isdigit():
            return Response(
                "Nam sinh phai la so",
                mimetype="text/plain"
            )

        birth_year = int(birth_year)

        # 2️⃣ Ngoài khoảng
        if birth_year < LOWER_BOUND or birth_year > UPPER_BOUND:
            return Response(
                f"Nam sinh phai tu {LOWER_BOUND} den {UPPER_BOUND}",
                mimetype="text/plain"
            )

        # 3️⃣ Hợp lệ
        age = UPPER_BOUND - birth_year
        return Response(
            f"Tuoi cua ban la {age}",
            mimetype="text/plain"
        )

    return Response("Nhap nam sinh", mimetype="text/plain")


if __name__ == "__main__":
    app.run(debug=True)
