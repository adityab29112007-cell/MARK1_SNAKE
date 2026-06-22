async function identifySnake() {

    const fileInput =
        document.getElementById("imageInput");

    const file =
        fileInput.files[0];

    if (!file) {
        alert("Please select an image");
        return;
    }

    const formData = new FormData();

    formData.append("file", file);

    const response = await fetch(
        "http://127.0.0.1:8000/identify-snake",
        {
            method: "POST",
            body: formData
        }
    );

    const data = await response.json();

    const result = data.result;

    document.getElementById("result").innerHTML = `
        <div class="card">
            <h2>🐍 Snake Information</h2>

            <p><strong>Common Name:</strong>
            ${result.common_name}</p>

            <p><strong>Scientific Name:</strong>
            ${result.scientific_name}</p>

            <p><strong>Venomous Status:</strong>
            ${result.venomous_status}</p>

            <p><strong>Confidence:</strong>
            ${result.confidence}</p>

            <hr>

            <p style="color:red;">
            ⚠ AI Prediction Only.
            Do not rely on this for medical emergencies.
            </p>
        </div>
    `;
}