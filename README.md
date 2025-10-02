🎨 Voice2Visuals

Voice2Visuals is a Python-based project that transforms spoken or written words into visual art.
It combines speech recognition, text processing, and AI-powered image generation with an easy-to-use GUI.

🚀 Features

🎙️ Voice Input – Speak your thoughts and convert them into visuals.

⌨️ Text Input – Type words or sentences to generate images.

🖼️ AI-Generated Images – Converts your input into unique, creative artwork.

💾 Save Images – Save generated visuals locally with one click.

🖥️ User-Friendly GUI – Simple interface for smooth interaction.

🛠️ Tech Stack

Programming Language: Python

Libraries/Modules:

tkinter – GUI

speech_recognition – Voice input

Pillow – Image handling

requests / openai (or any AI API) – Image generation

os, datetime – File handling

📂 Project Structure
Voice2Visuals/
│── static/
│   ├──style              # CSS file 
│── template/
│   └── index             # HTML file
│── venv/
│   └── Lib
│   └── Scripts
│   └── .gitignore
│   └── pyvenv
│── code                  #python source file
│── logo
│── requirements.txt      # Dependencies
│── README.md             # Project documentation

⚡ Installation

Clone the repository:

git clone https://github.com/your-username/Voice2Visuals.git
cd Voice2Visuals


Create and activate a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows


Install dependencies:

pip install -r requirements.txt

▶️ Usage

Run the application:

python code.py

Options in GUI:

Generate Image → Enter text or use mic to create visuals.

Save Image → Save generated art in generated/saved_images/.

🎯 Example

Input:

"A magical forest with glowing mushrooms under the night sky"


Output:
(Generated AI image saved in generated/saved_images/)

📌 Roadmap

 Add multiple AI model support (OpenAI, Stable Diffusion, etc.)

 Allow users to choose image styles (realistic, cartoon, abstract, etc.)

 Cloud deployment (Web app with Flask/Streamlit)

 Mobile app integration

🤝 Contributing

Contributions are welcome!

Fork the repo

Create a new branch (feature-new)

Commit changes

Open a pull request

📜 License

This project is licensed under the MIT License – free to use and modify.

👩‍💻 Author

Nanam Shruthi

📧 Email: shruthinanam7@gmail.com
