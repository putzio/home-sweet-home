alarm_inputs_visible = false;

function add_alarm_click() {
    if(!alarm_inputs_visible){
     // Show the input elements
     document.getElementById('new_alarm_time').style.display = 'inline-block';
     document.getElementById('new_alarm_describtion').style.display = 'inline-block';
     alarm_inputs_visible = true
    } else {
    }
}

function delete_alarm(id) {
    var alarm_id = id;

    // Make a POST request to the Flask server
    fetch('/api/delete_alarm/1', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        // Optionally, handle the response (e.g., show a success message)
    })
    .catch(error => {
        console.error('Error:', error);
        // Optionally, handle the error (e.g., show an error message)
    });
}