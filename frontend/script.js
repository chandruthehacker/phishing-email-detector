document.addEventListener("DOMContentLoaded", () => {
  const emailContentTextarea = document.getElementById("emailContent");
  const analyzeButton = document.getElementById("analyzeButton");
  const loadingIndicator = document.getElementById("loadingIndicator");
  const resultDisplay = document.getElementById("resultDisplay");

  const backendApiUrl = "http://127.0.0.1:5000/analyze-email";

  // Format text: convert **bold** to <strong> and line breaks to <br>
  function formatResultText(text) {
    return text
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
      .replace(/\n/g, "<br>");
  }

  // Color based on verdict
  function setResultColors(resultText) {
    const verdict = resultText.toLowerCase();
    resultDisplay.classList.remove(
      "bg-green-100", "text-green-700",
      "bg-red-100", "text-red-700",
      "bg-yellow-100", "text-yellow-700",
      "bg-gray-100"
    );

    if (verdict.includes("likely phishing") || verdict.includes("highly suspicious")) {
      resultDisplay.classList.add("bg-red-100", "text-red-700");
    } else if (verdict.includes("suspicious") || verdict.includes("caution")) {
      resultDisplay.classList.add("bg-yellow-100", "text-yellow-700");
    } else {
      resultDisplay.classList.add("bg-green-100", "text-green-700");
    }
  }

  analyzeButton.addEventListener("click", async () => {
    const emailContent = emailContentTextarea.value.trim();

    if (!emailContent) {
      resultDisplay.innerHTML = "Please paste some email content to analyze.";
      resultDisplay.classList.remove(
        "bg-gray-100", "bg-red-100", "text-red-700",
        "bg-green-100", "text-green-700"
      );
      resultDisplay.classList.add("bg-yellow-100", "text-yellow-700");
      return;
    }

    loadingIndicator.classList.remove("hidden");
    analyzeButton.disabled = true;
    resultDisplay.innerHTML = "";
    resultDisplay.classList.remove(
      "bg-green-100", "text-green-700",
      "bg-red-100", "text-red-700",
      "bg-yellow-100", "text-yellow-700"
    );
    resultDisplay.classList.add("bg-gray-100");

    try {
      const response = await fetch(backendApiUrl, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email_content: emailContent }),
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({ message: "Unknown error" }));
        throw new Error(`Backend error: ${response.status} - ${errorData.message || response.statusText}`);
      }

      const data = await response.json();
      const analysisText = data.result || "No analysis result received.";

      const formattedText = formatResultText(analysisText);
      resultDisplay.innerHTML = formattedText;

      setResultColors(analysisText);
    } catch (error) {
      console.error("Error during analysis:", error);
      resultDisplay.innerHTML = `An error occurred: ${error.message}. Ensure your Python backend is running.`;
      resultDisplay.classList.add("bg-red-100", "text-red-700");
      resultDisplay.classList.remove("bg-gray-100");
    } finally {
      loadingIndicator.classList.add("hidden");
      analyzeButton.disabled = false;
    }
  });

  document.getElementById("pasteButton").addEventListener("click", async () => {
    try {
      const text = await navigator.clipboard.readText();
      document.getElementById("emailContent").value = text;
    } catch (err) {
      alert("Failed to paste from clipboard. Please allow clipboard permissions.");
    }
  });

  document.getElementById("clearButton").addEventListener("click", () => {
    document.getElementById("emailContent").value = "";
  });
});
