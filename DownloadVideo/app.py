from flask import Flask, render_template, request, redirect, url_for
from pytubefix import YouTube

app = Flask(__name__)

def valid_link(link):
    try:
        return YouTube(link)
    except:
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        link = request.form.get("url")
        video = valid_link(link)
        if video:
            return redirect(url_for("confirm", url=link))
        else:
            return render_template("index.html", error="Invalid YouTube link!")

    return render_template("index.html")

@app.route("/confirm")
def confirm():
    link = request.args.get("url")
    video = valid_link(link)
    if not video:
        return redirect(url_for("index"))

    return render_template("confirm.html", title=video.title, url=link)

@app.route("/download")
def download():
    link = request.args.get("url")
    video = valid_link(link)
    if video:
        video.streams.get_highest_resolution().download()
        return "Download Complete! Check your folder."
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)