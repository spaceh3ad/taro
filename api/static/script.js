function sendMessage() {
  const input = document.getElementById("user-input");
  const chatBox = document.getElementById("chat-box");
  const loader = document.getElementById("loader");
  const message = input.value.trim();
  console.log(message);
  if (message) {
    displayMessage(message, "user");
    loader.style.display = "block"; // Show loader
    fetch("/send-message", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: message }),
    })
      .then((response) => response.json())
      .then((data) => {
        displayMessage(data.response, "bot");
      })
      .catch((error) => {
        displayMessage("Error connecting to the server.", "bot");
      })
      .finally(() => {
        loader.style.display = "none"; // Hide loader regardless of success or error
      });
    input.value = "";
  }
}

function displayMessage(message, sender) {
  const messageDiv = document.createElement("div");
  messageDiv.classList.add("message", sender);
  messageDiv.textContent = message;
  const chatBox = document.getElementById("chat-box");
  chatBox.appendChild(messageDiv);
  chatBox.scrollTop = chatBox.scrollHeight; // Auto scroll to the latest message
}

function handleKeyPress(event) {
  if (event.key === "Enter") {
    sendMessage();
  }
}

document.getElementById("send-button").addEventListener("click", sendMessage);
