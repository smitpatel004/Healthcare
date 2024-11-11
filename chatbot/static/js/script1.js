function sendMessage() {
    var userInput = document.getElementById("user-input").value;
    if (userInput.trim() === "") {
        return;
    }

    // Add user message to chat box
    var chatBox = document.getElementById("chat-box");
    var userMessageDiv = document.createElement("div");
    userMessageDiv.className = "chat-message user-message";
    userMessageDiv.innerText = userInput;
    chatBox.appendChild(userMessageDiv);

    // Clear the input field
    document.getElementById("user-input").value = "";

    // Send request to get bot response
    fetch(`/chatbot/get-response/?message=${encodeURIComponent(userInput)}`)
        .then(response => response.json())
        .then(data => {
            var botMessageDiv = document.createElement("div");
            botMessageDiv.className = "chat-message bot-message";
            botMessageDiv.innerText = data.response;
            chatBox.appendChild(botMessageDiv);
            chatBox.scrollTop = chatBox.scrollHeight;
        });
}
