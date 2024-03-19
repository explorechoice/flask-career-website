from flask import Flask, render_template

app = Flask(__name__)

openings = [
  {
    "id": 123,
    "title": "Software Developer",
    "location": "Pune, India",
    "salary": "Rs. 10,00,000"
  },
  {
    "id": 23,
    "title": "ML/AI engineer",
    "location": "Bangalore, India",
    "salary": "Rs. 18,00,000"
  },
  {
    "id": 28,
    "title": "Frontend Developer",
    "location": "Noida, India",
    "salary": "Rs. 8,00,000"
  },
  {
    "id": 96,
    "title": "DevOps Engineer",
    "location": "Pune, India",
    "salary": "Rs. 12,00,000"
  }
]


@app.route("/")
def home():
  return render_template(template_name_or_list='home.html', openings=openings)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)