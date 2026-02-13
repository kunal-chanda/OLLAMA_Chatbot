# Ollama Gemma Chatbot with Role Selection

A Streamlit-based chatbot application that allows users to interact with the Ollama Gemma language model by selecting different AI roles and customizing conversation parameters.

## Features

- **Role-Based Conversations**: Choose from predefined AI roles including:
  - AI Developer
  - AI Teacher
  - Data Scientist
  - AI Researcher

- **Customizable Goals**: Define specific goals for the conversation
- **Context Provision**: Add additional context to guide the AI's responses
- **Dynamic Prompt Generation**: Automatically generates prompts based on selected role, goal, and context
- **Ollama Integration**: Uses local Ollama Gemma 3:1b model for privacy and offline capability

## Prerequisites

- Python 3.7+
- Ollama installed and running locally
- Gemma 3:1b model downloaded in Ollama

## Installation

1. Install Ollama from [ollama.ai](https://ollama.ai/)

2. Download the Gemma model:

   ```bash
   ollama pull gemma3:1b
   ```

3. Install Python dependencies:

   ```bash
   pip install streamlit langchain langchain-community python-dotenv
   ```

4. Ensure Ollama is running:
   ```bash
   ollama serve
   ```

## Usage

1. Run the Streamlit application:

   ```bash
   streamlit run prompt.py
   ```

2. Open your browser to the provided local URL (typically http://localhost:8501)

3. Select an AI role from the dropdown menu

4. Enter your conversation goal in the text input field

5. (Optional) Provide additional context in the text area

6. Click "Ask Gemma" to generate a response

## How It Works

The application uses LangChain's PromptTemplate to dynamically create prompts based on user inputs:

```
You are a {AI_role} and your goal is to {AI_goal}.
Here is some additional context for you: {AI_context}
Answer the user's question based on the above information.
```

The generated prompt is then sent to the Ollama Gemma model, which provides a contextual response based on the selected role and provided information.

## Configuration

- **Model**: Currently configured for `gemma3:1b`. Change the model name in the code to use different Ollama models
- **Roles**: Modify the `st.selectbox` options to add or remove available roles
- **Prompt Template**: Customize the `prompt_text` variable to change how prompts are structured

## Dependencies

- `streamlit`: Web UI framework
- `langchain`: LLM framework for prompt management
- `langchain-community`: Community integrations including Ollama
- `python-dotenv`: Environment variable management

## Troubleshooting

- **Model not found**: Ensure Ollama is running and the Gemma model is downloaded
- **Connection issues**: Verify Ollama is accessible on the default port (11434)
- **Import errors**: Install all required packages and ensure Python path includes the project directory

## Contributing

Feel free to enhance the application by:

- Adding more AI roles
- Implementing conversation history
- Adding support for different Ollama models
- Improving the UI/UX

## License

This project is open-source. Please check the main project license for details.
