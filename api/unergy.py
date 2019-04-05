import json
import flask


app = flask.Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def unergy():
    request = flask.request.get_data().decode("utf-8")
    if request:
        request = json.loads(request)

    return flask.Response("Hello")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)



