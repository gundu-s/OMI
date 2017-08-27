from flask import Flask, request, jsonify
import json
import requests
import random

app = Flask(__name__)


@app.route("/mahserver", methods=["POST"])
def mahserver():
    data = request.get_json() or {}
    tracks = []
    print(data)
    for timestamp, info in data.items():
        artist, track = info["trackname"].split(" - ", 1)
        tracks.append((artist, track))
    print(tracks)

    with open('result.json', 'w') as fp:
        json.dump(tracks, fp)

    echo_we_dic = echo_we("result.json")

    with open('echowe.json', 'w') as fp:
        json.dump(echo_we_dic, fp)

    return jsonify(echo_we_dic)


def echo_we(filename):
    with open(filename, "r") as f:
        data = json.load(f)

    results = []

    for item in data:
        url = "http://localhost:8888/api/recordings/;limit=1;offset=1"

        r = requests.get(url, params={
            "artist": item[0],
            "title": item[1]
        })
        r.raise_for_status()

        title = r.json()["results"][0]["title"]
        artist = r.json()["results"][0]["artists"][0]
        results.append({
            "title": title,
            "artist": artist,
            "percentage": random.randint(1, 60)
        })

    print('Successfully requested!')
    return results


app.run(host="0.0.0.0", port=5000, debug=True)
