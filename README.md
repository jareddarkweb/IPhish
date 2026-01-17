![The GitHub logo](https://github.com/jareddarkweb/IPhish/blob/main/Your_paragraph_text-removebg-preview.png)




#  IPhish - iCloud Research Tool

A streamlined, automated phishing simulation tool designed for security researchers and educational demonstrations. This tool automates the setup of a Flask backend, a SQLite database, and an encrypted public tunnel using Ngrok.

## 🚀 Quick Start (Linux & macOS)

To launch the tool, simply clone the repository and run the automated installer.

1. **Clone the repo:**
   ```bash
   git clone [https://github.com/jareddarkweb/IPhish.git](https://github.com/jareddarkweb/IPhish.git)
   cd IPhish
Run the launcher:

```Bash

chmod +x run.sh
./run.sh

```

🔑 ConfigurationThe tool is designed to be "plug-and-play," but you can fine-tune your environment using a .env file:

| Variable | Description | Default |
| :--- | :--- | :--- |
| **ADMIN_PASSWORD** | Access key for the `/admin-portal` | `admin123` |
| **NGROK_AUTH_TOKEN** | Your private Ngrok tunnel token | *Prompted on run* |
| **FLASK_SECRET** | Encryption key for browser sessions | *Auto-generated* |

⚠️ Disclaimer
This tool is for educational purposes and authorized security testing only. Using this tool against targets without prior written consent is illegal. The developers assume no liability for misuse.
