![Iphish Logo](https://i.ibb.co/THbx6n2/assasdas.jpg)



IPhish is a cybersecurity tool designed for hosting an iCloud login page for security research purposes. This tool is intended for ethical hacking and research only.

## Features

- Hosts a custom iCloud login page
- Allows security researchers to study phishing techniques
- Provides insights into security vulnerabilities

## Installation

To install IPhish, clone the repository and navigate to the project directory:

```sh
git clone https://github.com/your-username/IPhish.git
cd IPhish
```

Usage

Running the iCloud Login Page Locally
Open index.html in a web browser to launch the iCloud login page.

Optionally, you can set up a local server to host the page. For example, using Python's built-in HTTP server:

```
python -m http.server 8000
```
Then, navigate to http://localhost:8000 in your browser.

Exposing the Server Over WAN Using Flask and ngrok
Setting Up Flask
Ensure you have Python installed. Install Flask using pip if you haven't already:

```
pip install Flask
Create a simple Flask server script (app.py):
```

```
from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_file(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    app.run(debug=True)
Run the Flask server:

```

```
python app.py
```
The server will start on http://localhost:5000.

Using ngrok to Expose the Server
Download and install ngrok from ngrok.com.

Start ngrok and point it to your local Flask server:

```
ngrok http 5000
```
ngrok will provide a forwarding URL (e.g., http://abcd1234.ngrok.io). Use this URL to access your Flask server over the WAN.

Disclaimer
IPhish is intended for educational and ethical research purposes only. Unauthorized use of this tool for malicious purposes is strictly prohibited. The developers are not responsible for any misuse of this tool.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any questions or inquiries, please contact jared-calgary-cyber-security@wearehackerone.com.





z

