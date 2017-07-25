from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route("/mahserver", methods=["POST"])
def mahserver():
    data = request.get_json()
    #print(data)
    tracks = []
    for timestamp, info in data.items():
        artist, track = info["trackname"].split(" - ", 1)
        tracks.append((artist, track))
    print(tracks)

    with open('result.json', 'w') as fp:
    	json.dump(tracks, fp)

    return jsonify(tracks)


app.run(host="0.0.0.0", port=5000, debug=True)
