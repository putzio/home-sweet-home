alarm_inputs_visible = false;

function add_alarm_click() {
    if(!alarm_inputs_visible){
     // Show the input elements
     document.getElementById('new_alarm_time').style.display = 'inline-block';
     document.getElementById('new_alarm_description').style.display = 'inline-block';
     alarm_inputs_visible = true
    } else {
        // Send the data to the server
        var time = document.getElementById('new_alarm_time').value;
        var description = document.getElementById('new_alarm_description').value;
        var data = {time: time, description: description};

        // Send a POST request to the Flask server
        fetch('/set_alarm/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            if (data.status === 'success') {
                window.location.reload();
            }
        })
        .catch(error => console.error('Error:', error));
    }
}

function delete_alarm(id) {
    var data = {id: id};

    // Make a POST request to the Flask server
    fetch('/delete_alarm/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        if (data.status === 'success') {
            window.location.reload();
        }
    })
    .catch(error => {
        console.error('Error:', error);
        // Optionally, handle the error (e.g., show an error message)
    });
}