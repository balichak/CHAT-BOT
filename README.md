# AI Chatbot Project

## Overview
This project is a full-stack AI-powered chatbot application using Flask for the backend and React for the frontend. The chatbot integrates OpenAI's GPT model to generate responses based on user input.

## Project Structure
```
project_root/
│── backend/
│   ├── app.py
│   ├── config.py
│   ├── routes/
│   │   ├── chat.py
│   │   ├── __init__.py
│   ├── services/
│   │   ├── openai_service.py
│   │   ├── __init__.py
│   ├── __init__.py
│── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── App.js
│   │   ├── index.js
│   ├── package.json
│── requirements.txt
│── README.md
```

## Backend Setup
1. Navigate to the `backend` directory:
   ```sh
   cd backend
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set your OpenAI API key in `config.py`:
   ```python
   openai_api_key = "your_openai_api_key"
   ```
4. Run the backend server:
   ```sh
   python app.py
   ```

## Frontend Setup
1. Navigate to the `frontend` directory:
   ```sh
   cd frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the frontend application:
   ```sh
   npm start
   ```

## API Endpoint
- **POST /api/chat**: Sends a message to the chatbot and receives a response.
  - **Request Body**:
    ```json
    {
      "message": "Hello, how are you?"
    }
    ```
  - **Response**:
    ```json
    {
      "response": "I'm an AI chatbot. How can I help you today?"
    }
    ```

## Technologies Used
- **Backend**: Flask, OpenAI API, Flask-CORS
- **Frontend**: React, Axios

## Features
- AI-powered chatbot using OpenAI's GPT model
- Full-stack implementation with separate frontend and backend
- REST API for handling chatbot interactions
- Interactive UI for user-friendly communication

## Future Enhancements
- Improve chatbot intelligence with fine-tuned models
- Add user authentication and chat history storage
- Deploy the application to a cloud platform

## License
This project is open-source and available for modification and distribution.

---
Developed by Balichak Suman 🚀

