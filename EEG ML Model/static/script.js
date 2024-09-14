const checkModelForm = document.getElementById('checkModelForm');
const predictForm = document.getElementById('predictForm');
const resultDiv = document.getElementById('result');

checkModelForm.addEventListener('submit', async function (event) {
    event.preventDefault();

    const fileInput = document.getElementById('fileInput').files[0];
    if (!fileInput) {
        resultDiv.innerHTML = '<p style="color: red;">Please upload a file.</p>';
        return;
    }

    const formData = new FormData();
    formData.append('file', fileInput);

    try {
        const response = await fetch('/check-model', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error('Failed to process the file');
        }

        const result = await response.json();
        if (result.prediction === 0) {
            resultDiv.innerHTML = '<p style="color: green;">Prediction: Healthy</p>';
        } else if (result.prediction === 1) {
            resultDiv.innerHTML = '<p style="color: red;">Prediction: Schizophrenic</p>';
        } else {
            resultDiv.innerHTML = '<p>Invalid prediction result.</p>';
        }
    } catch (error) {
        resultDiv.innerHTML = `<p style="color: red;">Error: ${error.message}</p>`;
    }
});

predictForm.addEventListener('submit', async function (event) {
    event.preventDefault();

    const fileInput = document.getElementById('fileInput').files[0];
    if (!fileInput) {
        resultDiv.innerHTML = '<p style="color: red;">Please upload a file.</p>';
        return;
    }

    const formData = new FormData();
    formData.append('file', fileInput);

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error('Failed to process the file');
        }

        const result = await response.json();
        if (result.prediction === 0) {
            resultDiv.innerHTML = '<p style="color: green;">Prediction: Healthy</p>';
        } else if (result.prediction === 1) {
            resultDiv.innerHTML = '<p style="color: red;">Prediction: Schizophrenic</p>';
        } else {
            resultDiv.innerHTML = '<p>Invalid prediction result.</p>';
        }
    } catch (error) {
        resultDiv.innerHTML = `<p style="color: red;">Error: ${error.message}</p>`;
    }
});