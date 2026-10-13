# JARVIS

A personal voice assistant I'm building from scratch to learn Python,
speech recognition, and software architecture along the way.

## Current status: v0.1

Right now, JARVIS can:

- Listen for voice input through the microphone
- Recognize basic hardcoded commands (e.g. saying "hello" gets a spoken response)
- Respond back using text-to-speech

This is an early, minimal version — think of it as proof that the core
listen → understand → respond loop works. More features are being added
incrementally.

## Tech used

- Python
- SpeechRecognition (voice-to-text)
- pyttsx3 (text-to-speech)
- PyAudio (microphone input)

## Setup

```bash
pip install -r requirements.txt
python main.py
```

## Roadmap

- [x] v0.1 — Basic voice recognition and hardcoded responses
- [ ] v0.2 — Control applications (open browser, notepad, etc.)
- [ ] v0.3 — Web search by voice
- [ ] v0.4 — Basic memory/context between commands
- [ ] v1.0 — First complete stable version
