## Day 1 Learning

### Understand Your First LLM Call

#### Virtual Environment (`venv`)

A virtual environment isolates a project's Python packages and dependency versions from other projects and the global Python installation. It is used for package isolation, not hardware-driver isolation.

```bash
python -m venv venv
```

Activate it with `venv\Scripts\activate` on Windows or `source venv/bin/activate` on Linux/macOS; run `deactivate` when finished.

#### LLM API Call

An LLM API call sends instructions and input from an application to an LLM server, which processes the request and returns a generated response. The basic flow is: client -> API request -> model processing -> API response.

An API request usually includes an API key, model name, and messages. Keep the API key secret by storing it in an environment variable or `.env` file, never in public repositories or frontend code.

#### Model and Messages

The model identifies which LLM processes the request; models can differ in reasoning ability, speed, cost, context window, and multimodal support.

Messages contain a `role` and `content`: `system` sets behavior and rules, `user` provides the request, and `assistant` stores earlier model responses for conversation context.

#### LLM Response

The response contains the generated answer and may include metadata such as input, output, and total token usage. Some APIs expose the answer through `response.choices[0].message.content`, but response formats vary by provider.

A token is a small unit of text, such as a word, part of a word, punctuation mark, or symbol. Tokens affect API cost, context limits, input size, and output size.

#### Python Project Setup with `uv`

Create the project with `uv init day1`, enter it with `cd day1`, and create a Python 3.11 environment with `uv venv --python 3.11`.

Install the Groq client and environment-variable loader with `uv add groq python-dotenv`, then load `GROQ_API_KEY` from `.env` before creating the client and sending a chat completion request.

#### Complete LLM Call Flow

Configure the client -> provide the API key -> select a model -> create messages -> send the request -> receive the response -> extract the generated answer.

**Key terms:** API key authenticates the application; client communicates with the provider; model generates the response; role identifies the message sender; content contains the prompt; response is the provider's result; choices contain possible generated answers.
