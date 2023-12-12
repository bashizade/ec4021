from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    results = {
        "شنبه": [
            "05:01",
            "06:23",
            "11:37",
            "16:51",
            "17:09",
            "22:56",
        ],
        "یکشنبه": [
            "05:02",
            "06:23",
            "11:37",
            "16:52",
            "17:10",
            "22:57",
        ],
        "دوشنبه": [
            "05:02",
            "06:24",
            "11:38",
            "16:52",
            "17:10",
            "22:57",
        ],
        "سه شنبه": [
            "05:03",
            "06:25",
            "11:38",
            "16:52",
            "17:10",
            "22:57",
        ],
        "چهار شنبه": [
            "05:04",
            "06:25",
            "11:39",
            "16:52",
            "17:11",
            "22:58",
        ],
        "پنج شنبه": [
            "05:04",
            "06:26",
            "11:39",
            "16:53",
            "17:11",
            "22:58",
        ],
        "جمعه": [
            "05:05",
            "06:26",
            "11:40",
            "16:53",
            "17:11",
            "22:59",
        ],
    }
    return render_template('index.html', results=results)


if __name__ == '__main__':
    app.run()
