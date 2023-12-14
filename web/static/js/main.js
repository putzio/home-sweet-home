function add_alarm() {
        // Redirect to a new page
        window.location.href = '/add_alarm'; // Replace '/new_page' with the actual URL
}


function updateColor() {
    const red = document.getElementById('red-value').value;
    const green = document.getElementById('green-value').value;
    const blue = document.getElementById('blue-value').value;

    const colorCircle = document.getElementById('color-circle');
    colorCircle.style.backgroundColor = `rgb(${red}, ${green}, ${blue})`;

    document.getElementById('red-display').innerText = red;
    document.getElementById('green-display').innerText = green;
    document.getElementById('blue-display').innerText = blue;
  }

function sendColor() {
const red = document.getElementById('red-display').innerText;
const green = document.getElementById('green-display').innerText;
const blue = document.getElementById('blue-display').innerText;

const apiUrl = 'https://your-server.com/api/set-color';

fetch(apiUrl, {
    method: 'POST',
    headers: {
    'Content-Type': 'application/json',
    },
    body: JSON.stringify({ red, green, blue }),
})
.then(response => response.json())
.then(data => {
    document.getElementById('status-message').innerText = data.message;
})
.catch(error => {
    console.error('Error:', error);
    document.getElementById('status-message').innerText = 'Error occurred. Please try again.';
});
}