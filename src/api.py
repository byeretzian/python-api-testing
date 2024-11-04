from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/get-string-length", methods=["POST"])
def get_length():
    # if we can't get a json body
    try:
        data = request.get_json()
    except:
        # let the requestor know they need a body
        return jsonify({"error": "No request body."}), 400
    # if the body isn't a string
    if type(data["body"]) != str:
        # let them know we need a string
        return jsonify({"error": "The request body must be a string."}), 400
    # if we got a string
    else:
        # return its length
        return jsonify({"length": len(data["body"])}), 200
