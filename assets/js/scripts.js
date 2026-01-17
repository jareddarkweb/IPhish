document.getElementById('loginForm').addEventListener('submit', function(e) {
  e.preventDefault();
  
  const account = document.getElementById('account').value;
  const password = document.getElementById('password').value;

  // Prepare the data to send
  const loginData = {
    username: account,
    password: password
  };

  // Send data to the Python server
  fetch('http://127.0.0.1:5000/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(loginData)
  })
  .then(response => response.json())
  .then(data => {
    console.log('Success:', data);
    alert('Credentials sent to terminal!');
  })
  .catch((error) => {
    console.error('Error:', error);
    alert('Could not connect to the Python server. Make sure it is running!');
  });
});
