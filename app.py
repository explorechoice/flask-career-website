from flask import Flask, render_template, jsonify

from database import load_openings_from_db, load_openings

app = Flask(__name__)

openings = [
  {
    "id": 123,
    "title": "Dvarapalakas",
    "location": "Sri Vaikunta Perumal Temple, Uthiramerur",
    "salary": "Bhagawat Krupa"
  },
  {
    "id": 23,
    "title": "Vishvaksena",
    "location": "Yoganarasimha swamy Temple, Vaikunta",
    "salary": "Bhagawat Krupa"
  },
  {
    "id": 28,
    "title": "Sevakas",
    "location": "Ulagalantha Perumal Temple, Bharat",
    "salary": "Bhagawat Krupa"
  },
  {
    "id": 96,
    "title": "Vaisanavas",
    "location": "Vikuntha Tirtham, Braj",
    "salary": "Bhagawat Krupa"
  }
]

@app.route("/api/jobs")
def list_jobs():
  openings = load_openings()
  return jsonify(openings)


@app.route("/")
def home():
  openings = load_openings_from_db()
  return render_template(template_name_or_list='home.html', openings=openings)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)