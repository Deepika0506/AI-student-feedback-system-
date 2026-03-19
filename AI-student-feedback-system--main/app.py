from flask import Flask, request, render_template
import csv
import os
from collections import Counter

# ---------------- APP CONFIG ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "feedbacks.csv")

app = Flask(__name__)  # templates folder is auto-detected

# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("index.html")


# ---------------- STUDENT FEEDBACK FORM ----------------
@app.route("/feedback")
def feedback():
    return render_template("feedback.html")

# ---------------- SAVE FEEDBACK AND SHOW THANK YOU ----------------
@app.route("/save", methods=["POST"])
def save_feedback():
    fields = [
        "student_name", "roll_number", "department", "semester",
        "academic_feedback", "campus_feedback",
        "library_feedback", "hostel_feedback", "admin_feedback"
    ]

    data = [request.form.get(field, "").strip() for field in fields]

    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(fields)
        writer.writerow(data)

    return render_template("thankyou.html", name=data[0])

# ---------------- MANAGEMENT VIEW ----------------
@app.route("/view")
def view_feedback():
    if not os.path.isfile(CSV_FILE):
        return "No feedbacks available yet."

    positive_words = ["good", "excellent", "helpful", "great", "clean", "supportive", "very good"]
    negative_words = ["bad", "poor", "worst", "dirty", "delay", "issue"]

    rows = []
    sentiments = []
    departments = []

    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)  # skip header safely

        for row in reader:
            if len(row) < 9:
                continue

            rows.append(row)
            departments.append(row[2])

            text = " ".join(row[4:]).lower()
            if any(w in text for w in positive_words):
                sentiments.append("Positive")
            elif any(w in text for w in negative_words):
                sentiments.append("Negative")
            else:
                sentiments.append("Neutral")

    sentiment_counts = Counter(sentiments)
    department_counts = Counter(departments)

    # ---------------- SECTION-WISE INSIGHTS ----------------
    section_names = {
        "academic_feedback": "Academic",
        "campus_feedback": "Campus Facilities",
        "library_feedback": "Library",
        "hostel_feedback": "Hostel / Canteen",
        "admin_feedback": "Administration"
    }

    section_insights = {}

    for idx, key in enumerate(section_names.keys(), start=4):
        pos = neg = neu = 0
        for row in rows:
            text = row[idx].lower()
            if any(w in text for w in positive_words):
                pos += 1
            elif any(w in text for w in negative_words):
                neg += 1
            else:
                neu += 1

        if pos >= neg and pos >= neu:
            section_insights[section_names[key]] = "Mostly Positive"
        elif neg >= pos and neg >= neu:
            section_insights[section_names[key]] = "Mostly Negative"
        else:
            section_insights[section_names[key]] = "Mostly Neutral"

    return render_template(
        "management.html",
        total=len(rows),
        sentiment_counts=sentiment_counts,
        department_counts=department_counts,
        section_insights=section_insights
    )

# ---------------- LOCAL RUN (ignored on PythonAnywhere) ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=10000)