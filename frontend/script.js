let apiBase = "http://localhost:5000";

function uploadFile() {
    const file = document.getElementById("fileUpload").files[0];
    const formData = new FormData();
    formData.append("file", file);

    fetch(`${apiBase}/upload`, {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => alert(data.message))
    .catch(err => console.error(err));
}

function sendQuestion() {
    const input = document.getElementById("userInput");
    const question = input.value;
    if (!question) return;

    const messageDiv = document.getElementById("messages");
    messageDiv.innerHTML += `<div class="user-message"><strong>You:</strong> ${question}</div>`;
    input.value = "";

    fetch(`${apiBase}/ask`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question })
    })
    .then(res => res.json())
    .then(data => {
        // Replace **bold text** with actual <strong>bold text</strong>
        const formattedAnswer = data.answer.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
        messageDiv.innerHTML += `<div class="docq-message"><strong>DocQ:</strong> <div class="response-content">${formattedAnswer}</div></div>`;
        messageDiv.scrollTop = messageDiv.scrollHeight; // scroll to bottom
    })
    .catch(err => {
        console.error(err);
        messageDiv.innerHTML += `<div class="docq-message"><strong>DocQ:</strong> Error occurred</div>`;
        messageDiv.scrollTop = messageDiv.scrollHeight;
    });
}