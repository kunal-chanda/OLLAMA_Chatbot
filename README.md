# RAG Application for YouTube Video Transcripts

This repository contains a Retrieval-Augmented Generation (RAG) application that transcribes text from YouTube videos, processes the transcripts using Large Language Models (LLMs), and generates intelligent answers based on the video content.

## Overview

The application leverages the YouTube Transcript API to fetch video transcripts, splits them into manageable chunks, creates vector embeddings, and stores them in a FAISS vector database. Users can then ask questions about the video content, and the system retrieves relevant transcript segments to provide context-aware answers using LLMs like Ollama's Gemma or OpenAI's models.

## Features

- **YouTube Transcript Extraction**: Automatically fetch transcripts from YouTube videos using video IDs
- **Text Chunking**: Split long transcripts into smaller, semantically meaningful chunks
- **Vector Embeddings**: Create embeddings for efficient similarity search (supports OpenAI embeddings)
- **Vector Storage**: Store embeddings in FAISS for fast retrieval
- **Question Answering**: Ask questions about video content and get AI-generated answers
- **Multiple LLM Support**: Compatible with Ollama (local) and OpenAI models
- **Streamlit Interface**: Web-based UI for interactive chatbot experiences
- **Customizable Prompts**: Flexible prompt templates for different use cases

## Project Structure

- `rag.py`: Main RAG implementation for YouTube transcript processing
- `requirements.txt`: Python dependencies

## Installation

1. Clone this repository:

   ```bash
   git clone <repository-url>
   cd rag
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory
   - Add your OpenAI API key if using OpenAI models: `OPENAI_API_KEY=your_key_here`

4. For Ollama support, ensure Ollama is installed and running locally with the Gemma model:
   ```bash
   ollama pull gemma3:1b
   ```

## Usage

### Basic RAG Pipeline

Run the main RAG script:

```bash
python rag.py
```

## Configuration

- Modify `video_id` in `rag.py` to process different YouTube videos
- Adjust chunk size and overlap in the text splitter
- Switch between different LLMs by uncommenting the appropriate lines

## Dependencies

- langchain
- langchain-community
- langchain-openai
- youtube-transcript-api
- faiss-cpu
- streamlit
- python-dotenv
- google-genai

## Contributing

Feel free to contribute by:

- Adding support for more LLM providers
- Implementing additional vector stores
- Creating more sophisticated prompt templates
- Adding web scraping capabilities for non-YouTube content

## License

This project is open-source. Please check the license file for details.
