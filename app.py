from flask import Flask, render_template, request
from instagram_parser import get_non_followers
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/compare", methods=["POST"])
def compare():
    followers_file = request.files["followers"]
    following_file = request.files["following"]

    followers_path = os.path.join(
        UPLOAD_FOLDER,
        followers_file.filename
    )

    following_path = os.path.join(
        UPLOAD_FOLDER,
        following_file.filename
    )

    followers_file.save(followers_path)
    following_file.save(following_path)

    non_followers = get_non_followers(
        followers_path,
        following_path
    )

    return render_template(
        "results.html",
        non_followers=non_followers,
        total=len(non_followers)
    )


if __name__ == "__main__":
    app.run(debug=True)