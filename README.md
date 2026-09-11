<<<<<<< HEAD
# Build Real-Time AI Voice Assistant With RAG Pipeline And Memory | Mistral LLM | Ollama

This repository contains code for a voice assistant that interacts with an AI model for natural language understanding (NLU). The assistant is designed to record audio input from users, transcribe it, and then interact with the AI model to provide relevant responses.

 <img width="1360" height="597" alt="image" src="https://github.com/user-attachments/assets/d5a2c732-9cd7-4627-b718-0fb6f4253061" />

 1. The customer speaks a query, and Whisper converts the voice into text.
 2. The text is sent to the RAG system, which uses Chat Memory to understand the previous conversation and retrieve relevant information.
 3. Ollama runs the Mistral LLM, which uses the retrieved context to generate an accurate response.
 4. The response is converted from text to voice using GTTS, and the Voice Assistant Bot speaks the answer back to the customer.

 <img width="1179" height="660" alt="image" src="https://github.com/user-attachments/assets/3b7ce416-91d8-4564-bb1c-dd3520b6cc7e" />

 This architecture shows how documents like PDF, PPT, and TXT are converted into text, divided into smaller chunks, and transformed into embeddings.
 These embeddings are stored in Qdrant Vector Database, where the system retrieves the most relevant information using Top-K retrieval based on the user's query.
 The retrieved information is then given to the LLM, which generates a context-aware answer and returns it to the user through the Streamlit interface.
## Features

- Record audio input from users in chunks.
- Transcribe the recorded audio using a pre-trained AI model.
- Interact with the AI model to generate responses based on user input.
- Utilizes a knowledge base for context-aware responses.

## Prerequisites

Before running the code, ensure you have the following dependencies installed:

- Python above 3.8
- `pyaudio`
- `numpy`
- `faster_whisper` (Installable via pip)
- `qdrant_client` (Installable via pip)
- Other dependencies specified in `requirements.txt`
## 1. Business Problem

Traditional voice assistants often depend on cloud-based APIs and have limited knowledge about user-specific documents or custom knowledge bases. They may also struggle to maintain context across conversations and can incur API costs.

Users need a voice assistant that can:

- Understand natural spoken queries
- Convert speech into text accurately
- Retrieve relevant information from a custom knowledge base
- Generate context-aware responses
- Maintain conversational context
- Work locally without depending entirely on cloud-based AI services

## 2. Possible Solution

A local AI voice assistant can be developed by combining speech recognition, a Large Language Model, Retrieval-Augmented Generation, vector database search, conversational memory, and text-to-speech.

The system receives voice input from the user, converts the speech into text using Faster-Whisper, retrieves relevant information from a knowledge base using Qdrant, and generates a response using a locally running LLM through Ollama.

This approach provides relevant and context-aware answers while keeping the AI processing primarily local.

## 3. Implemented Solution

We built a real-time AI Voice Assistant that accepts audio input from the user and converts the speech into text using Faster-Whisper.

The transcribed query is processed by the AI pipeline and relevant information is retrieved from the knowledge base using a RAG architecture with Qdrant.

The Ollama-based local LLM uses the retrieved context to generate an appropriate response. Conversational memory allows the assistant to maintain context across interactions.

The generated response can then be converted into speech using the text-to-speech component, allowing the user to interact with the system through natural voice conversations.

## 4. Tech Stack Used

The project uses the following technologies:

- Python - Core programming language
- Ollama - Local LLM inference
- Faster-Whisper - Speech-to-text
- Qdrant - Vector database for knowledge retrieval
- LlamaIndex - RAG and document processing
- RAG - Retrieval-Augmented Generation
- PyAudio - Audio recording and microphone input
- NumPy - Audio data processing
- Text-to-Speech - Converts AI responses into speech
- Git & GitHub - Version control and project management
=======
# VoiceGPT-RAG-Assistant
An AI-powered voice assistant built with Python, Ollama, Faster-Whisper, Qdrant, and LlamaIndex. Supports speech-to-text, RAG-based knowledge retrieval, local LLM inference, and text-to-speech for real-time conversational interactions.


<img width="1472" height="1432" alt="image" src="https://github.com/user-attachments/assets/7908ef77-65d9-48b2-a421-55fb14f104de" />

>>>>>>> b6d0cb78a7b7ef6e30b9309a83d8f7bce1e05408
