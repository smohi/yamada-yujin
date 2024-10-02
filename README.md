
# Yamada-Yujin : Japanese Learning Virtual Assistant

This project is for building a virtual assistant to help learn Japanese. User can have conversations with it in both English and Japanese. If you don't understand something in Japanese, you can ask the bot to say it in English. It'll also try to understand your Japanese when you practice.

## Features
- Listens to uer's voice and understands both English and Japanese.
- Talks back to you using text-to-speech.
- Switches between English and Japanese easily.
- Will translate from Japanese to English if asked.

## How to Set It Up

1. Cloning the project:
   ```bash
   git clone https://github.com/smohi/yamada-yujin.git
   cd yamada-yujin
   ```

2. Creating a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Installing the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run It

Running this to start the assistant:
```bash
python voice_assistant.py
```

Once it starts, it'll ask you to say something. Speak, and it'll respond!


