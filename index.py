from src.gpt import process_query
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder="static", template_folder="templates")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/send-message", methods=["POST"])
def send_message():
    # Assuming you receive a 'message' in the request
    user_input = request.json["message"]
    # Here you would integrate with your chat logic as needed
    response = your_chat_function(
        user_input
    )  # Replace with your function that processes input and returns response
    return jsonify(response=response)


def your_chat_function(user_input):
    return process_query(user_input)


if __name__ == "__main__":
    app.run(debug=True)
