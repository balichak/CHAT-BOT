import React, { useState } from 'react';
import axios from 'axios';

function App() {
    const [message, setMessage] = useState('');
    const [response, setResponse] = useState('');

    const sendMessage = async () => {
        const res = await axios.post('http://localhost:5001/api/chat', { message });
        setResponse(res.data.response);
    };

    return (
        <div>
            <h1>AI Chatbot</h1>
            <input type="text" value={message} onChange={(e) => setMessage(e.target.value)} />
            <button onClick={sendMessage}>Send</button>
            <p>Response: {response}</p>
        </div>
    );
}

export default App;
