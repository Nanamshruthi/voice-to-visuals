'''import tkinter as tk
from tkinter import messagebox, filedialog
import requests
import speech_recognition as sr
from PIL import Image, ImageTk
from googletrans import Translator  # Import Translator from googletrans library
from io import BytesIO

# Create a translator object
translator = Translator()         


def speech_to_text():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Open the microphone and capture audio
    with sr.Microphone() as source:
        print("Please start speaking...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source, timeout=10)  # Listen for up to 10 seconds

    try:
        # Use Google Web Speech API to recognize the audio
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print(f"Sorry, an error occurred during the request: {e}")

    return None

def generate_image(prompt):
    
    url = f"https://image.pollinations.ai/prompt/{prompt},32k,uhd,ultra realistic,blurless,realistic"

    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        content = response.content
    
        # Specify the file name and extension (e.g., "image.jpg")
        file_name = f"image.jpg"
        
        # Save the binary content to a file
        with open(file_name, "wb") as file:
            file.write(content)
        return file_name
    else:
        return None

def translate_to_english(text, source_language):
    # Translate the given text to English using the translator object
    translation = translator.translate(text, src=source_language, dest="en")
    return translation.text

def recognize_speech():
    result = speech_to_text()

    if result:
        detected_language = translator.detect(result).lang
        translated_text = translate_to_english(result, detected_language)
        recognized_text.set(translated_text)
        original_text.set(result)
        app.update_idletasks()
        display_generated_image()

def display_generated_image():
    result = generate_image(recognized_text.get())
    if result:
        image = Image.open(result)
        photo = ImageTk.PhotoImage(image)
        generated_image_label.config(image=photo)
        generated_image_label.photo = photo
        generated_image_bytes = BytesIO()
        image.save(generated_image_bytes, format="PNG")
        generated_image_bytes.seek(0)
        return generated_image_bytes
    else:
        messagebox.showerror("Error", "Image generation failed.")

def save_image():
    generated_image_bytes = display_generated_image()
    if generated_image_bytes:
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            with open(file_path, "wb") as image_file:
                image_file.write(generated_image_bytes.read())
            messagebox.showinfo("Image Saved", f"Generated image has been saved as '{file_path}'.")

app = tk.Tk()
app.title("Voice2Visual")

logo_image = tk.PhotoImage(file="logo.png")
logo_label = tk.Label(app, image=logo_image)
logo_label.pack()

generate_button = tk.Button(app, text="Generate Image", command=recognize_speech)

original_text = tk.StringVar()
original_text_label = tk.Label(app, text="Original Text:")
original_text_display = tk.Label(app, textvariable=original_text, wraplength=400)

recognized_text = tk.StringVar()
text_label = tk.Label(app, text="Translated Text:")
text_display = tk.Label(app, textvariable=recognized_text, wraplength=400)

generated_image_label = tk.Label(app)

save_image_button = tk.Button(app, text="Save Image", command=save_image)

generate_button.pack()
original_text_label.pack()
original_text_display.pack()
text_label.pack()
text_display.pack()
generated_image_label.pack()
save_image_button.pack()

app.mainloop()'''




import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from tkinter.font import Font
import requests
import speech_recognition as sr
from PIL import Image, ImageTk
from googletrans import Translator
from io import BytesIO

# Initialize translator
translator = Translator()

# ----- Speech to Text -----
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=10)

    try:
        return recognizer.recognize_google(audio)
    except Exception as e:
        print("Speech error:", e)
        return None

# ----- Image Generator -----
def generate_image(prompt):
    url = f"https://image.pollinations.ai/prompt/{prompt},32k,uhd,ultra realistic,blurless,realistic"
    response = requests.get(url)
    if response.status_code == 200:
        file_name = "image.jpg"
        with open(file_name, "wb") as f:
            f.write(response.content)
        return file_name
    return None

# ----- Translate Text -----
def translate_to_english(text, source_lang):
    return translator.translate(text, src=source_lang, dest="en").text

# ----- Speech to Visual Flow -----
def recognize_speech():
    status_text.set("Listening...")
    app.update_idletasks()

    result = speech_to_text()

    if result:
        try:
            lang = translator.detect(result).lang
            translated = translate_to_english(result, lang)

            original_text.set(result)
            translated_text.set(translated)

            status_text.set("Generating Image...")
            update_image()
            status_text.set("Done")
        except Exception as e:
            status_text.set("Translation failed.")
            messagebox.showerror("Error", str(e))
    else:
        status_text.set("Could not understand. Please try again.")

# ----- Display Generated Image -----
def update_image():
    result = generate_image(translated_text.get())
    if result:
        img = Image.open(result).resize((400, 300))
        photo = ImageTk.PhotoImage(img)
        generated_image_label.config(image=photo)
        generated_image_label.photo = photo

        global image_bytes
        image_bytes = BytesIO()
        img.save(image_bytes, format="PNG")
        image_bytes.seek(0)
    else:
        messagebox.showerror("Error", "Failed to generate image.")

# ----- Save Image -----
def save_image():
    if image_bytes:
        file_path = filedialog.asksaveasfilename(defaultextension=".png")
        if file_path:
            with open(file_path, "wb") as f:
                f.write(image_bytes.read())
            messagebox.showinfo("Saved", "Image saved successfully!")

# ---------- GUI ----------
app = tk.Tk()
app.title("Voice2Visual")
app.geometry("600x750")
app.configure(bg="#f0f0f0")

style = ttk.Style()
style.configure("TButton", font=("Segoe UI", 12), padding=10)
style.configure("TLabel", font=("Segoe UI", 11))

header_font = Font(family="Helvetica", size=24, weight="bold")
subheader_font = Font(family="Helvetica", size=14)

# Load Logo
logo_image = ImageTk.PhotoImage(Image.open("logo.png").resize((250, 100)))
tk.Label(app, image=logo_image, bg="#f0f0f0").pack(pady=(10, 0))
tk.Label(app, text="Voice2Visual", font=header_font, bg="#f0f0f0").pack()
tk.Label(app, text="Transforming Words into Art.", font=subheader_font, bg="#f0f0f0").pack(pady=(0, 20))

# Buttons and Text
ttk.Button(app, text="🎙️ Generate Image", command=recognize_speech).pack()

original_text = tk.StringVar()
translated_text = tk.StringVar()
status_text = tk.StringVar(value="Status: Idle")

ttk.Label(app, text="Original Text:").pack(pady=(20, 0))
ttk.Label(app, textvariable=original_text, wraplength=500).pack()

ttk.Label(app, text="Translated Text:").pack(pady=(20, 0))
ttk.Label(app, textvariable=translated_text, wraplength=500).pack()

ttk.Label(app, textvariable=status_text, foreground="blue").pack(pady=10)

generated_image_label = tk.Label(app, bg="#f0f0f0")
generated_image_label.pack(pady=20)

ttk.Button(app, text="💾 Save Image", command=save_image).pack(pady=10)

image_bytes = None

app.mainloop()
