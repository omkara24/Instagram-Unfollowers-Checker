from flask import Flask, render_template, request, send_file
from instagram_parser import get_non_followers
import os
import csv

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

    result = get_non_followers(
        followers_path,
        following_path
    )

    app.config["LAST_RESULTS"] = result["non_followers"]

    return render_template(
        "results.html",
        followers_count=result["followers_count"],
        following_count=result["following_count"],
        non_followers_count=result["non_followers_count"],
        non_followers=result["non_followers"]
    )


@app.route("/download-txt")
def download_txt():

    file_path = os.path.join(
        UPLOAD_FOLDER,
        "unfollowers.txt"
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        for username in app.config.get(
            "LAST_RESULTS",
            []
        ):
            file.write(username + "\n")

    return send_file(
        file_path,
        as_attachment=True
    )


@app.route("/download-csv")
def download_csv():

    file_path = os.path.join(
        UPLOAD_FOLDER,
        "unfollowers.csv"
    )

    with open(
        file_path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow(["Username"])

        for username in app.config.get(
            "LAST_RESULTS",
            []
        ):
            writer.writerow([username])

    return send_file(
        file_path,
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)