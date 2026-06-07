from flask import (
    Flask,
    render_template,
    request,
    send_file
)

from instagram_parser import get_non_followers

from io import BytesIO
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


@app.route("/")
def home():

    return render_template(
        "index.html"
    )


@app.route(
    "/compare",
    methods=["POST"]
)
def compare():

    followers_file = request.files["followers"]
    following_file = request.files["following"]

    if (
        not followers_file.filename.endswith(".html")
        or
        not following_file.filename.endswith(".html")
    ):

        return render_template(
            "index.html",
            error=
            "Please upload Instagram HTML files only."
        )

    followers_path = os.path.join(
        UPLOAD_FOLDER,
        followers_file.filename
    )

    following_path = os.path.join(
        UPLOAD_FOLDER,
        following_file.filename
    )

    followers_file.save(
        followers_path
    )

    following_file.save(
        following_path
    )

    result = get_non_followers(
        followers_path,
        following_path
    )

    try:
        os.remove(followers_path)
        os.remove(following_path)
    except:
        pass

    if (
        result["followers_count"] == 0
        or
        result["following_count"] == 0
    ):

        return render_template(
            "index.html",
            error=
            "Invalid Instagram export files."
        )

    app.config[
        "LAST_RESULTS"
    ] = result["non_followers"]

    return render_template(
        "results.html",
        followers_count=
        result["followers_count"],

        following_count=
        result["following_count"],

        non_followers_count=
        result["non_followers_count"],

        non_followers=
        result["non_followers"]
    )


@app.route("/download-txt")
def download_txt():

    content = "\n".join(
        app.config.get(
            "LAST_RESULTS",
            []
        )
    )

    buffer = BytesIO()

    buffer.write(
        content.encode("utf-8")
    )

    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="unfollowers.txt",
        mimetype="text/plain"
    )


@app.route("/download-csv")
def download_csv():

    csv_content = "Username\n"

    for username in app.config.get(
        "LAST_RESULTS",
        []
    ):
        csv_content += (
            username + "\n"
        )

    buffer = BytesIO()

    buffer.write(
        csv_content.encode("utf-8")
    )

    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="unfollowers.csv",
        mimetype="text/csv"
    )


if __name__ == "__main__":
    app.run(debug=True)