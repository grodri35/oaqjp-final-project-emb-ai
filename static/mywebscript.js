function RunSentimentAnalysis() {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    fetch("/emotionDetector", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: textToAnalyze })
    })
    .then(response => {
        if (!response.ok) {
            return response.text().then(error => {
                throw new Error(error);
            });
        }
        return response.text();
    })
    .then(data => {
        document.getElementById("system_response").innerText = data;
    })
    .catch(error => {
        document.getElementById("system_response").innerText = error.message;
    });
}
