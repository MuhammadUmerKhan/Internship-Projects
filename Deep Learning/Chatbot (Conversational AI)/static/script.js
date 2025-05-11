document.getElementById('chatForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const input = document.getElementById('messageInput');
    const chatBox = document.getElementById('chatBox');
    const message = input.value.trim();

    if (!message) return;

    // Add user message
    const userBubble = document.createElement('div');
    userBubble.className = 'chat-bubble flex justify-end mb-3';
    userBubble.innerHTML = `
        <div class="max-w-[70%] bg-blue-600 text-white p-3 rounded-lg shadow">
            ${message}
        </div>
    `;
    chatBox.appendChild(userBubble);

    // Clear input and scroll to bottom
    input.value = '';
    chatBox.scrollTop = chatBox.scrollHeight;

    try {
        // Fetch bot response
        const response = await fetch('/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: `message=${encodeURIComponent(message)}`
        });
        const data = await response.json();
        if (!response.ok) throw new Error(data.detail || 'Network error');

        // Add bot response
        const botBubble = document.createElement('div');
        botBubble.className = 'chat-bubble flex justify-start mb-3';
        botBubble.innerHTML = `
            <div class="max-w-[70%] bg-gray-200 text-gray-800 p-3 rounded-lg shadow">
                ${data.message}
            </div>
        `;
        chatBox.appendChild(botBubble);
    } catch (error) {
        const errorBubble = document.createElement('div');
        errorBubble.className = 'chat-bubble flex justify-start mb-3';
        errorBubble.innerHTML = `
            <div class="max-w-[70%] bg-red-100 text-red-800 p-3 rounded-lg shadow">
                Error: ${error.message}
            </div>
        `;
        chatBox.appendChild(errorBubble);
    }

    // Scroll to bottom after adding new message
    chatBox.scrollTop = chatBox.scrollHeight;
});