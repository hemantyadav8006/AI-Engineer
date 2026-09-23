# Day 2: System Roles and Temperature

This example demonstrates how system and user messages influence an AI response when using the Groq chat-completions API.

The script:

- Uses a system message to define the assistant's role, such as a brand manager.
- Sends a user message containing the task or question.
- Compares how different system roles can produce different responses.
- Uses the `temperature` parameter to control response randomness. A value of `0` produces the most consistent output, while values closer to `2` allow more variation.

## Setup

Create a `.env` file in this folder and add your Groq API key:

```env
GROQ_API_KEY=your_api_key_here
```

Run the example with:

```bash
python system_temp.py
```
