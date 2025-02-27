from flask import Blueprint, request, jsonify
from services.openai_service import generate_response

chat_blueprint = Blueprint('chat', __name__)

@chat_blueprint.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No input provided"}), 400
    
    response = generate_response(user_input)
    return jsonify({"response": response})
