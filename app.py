from flask import Flask, render_template, request, jsonify
from src.gpt import process_query
import traceback

app = Flask(__name__, static_folder="static", template_folder="templates")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/send-message", methods=["POST"])
def send_message():
    user_input = request.json["message"]
    max_retries = 3  # Set the maximum number of retries
    for attempt in range(max_retries):
        try:
            response = your_chat_function(user_input)
            return jsonify(response=response)
        except Exception as e:
            print(f"An error occurred: {e}")
            traceback.print_exc()
            if attempt < max_retries - 1:
                print(f"Retrying... Attempt {attempt + 1}")
            else:
                print("Max retries reached. Returning error response.")
                response = {
                    "error": "An internal error occurred. Please try again later."
                }
                return jsonify(response=response), 500
    return jsonify(response={"error": "An unexpected error occurred"}), 500


def your_chat_function(user_input):
    # Implement your retry logic here if needed
    return process_query(user_input)


if __name__ == "__main__":
    app.run(debug=True)
