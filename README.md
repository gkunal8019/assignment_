
# Assignment_

This project is a web-based application that processes user queries by retrieving relevant information from a given URL, using an AI-powered language model. The application is built with Python and Gradio for the user interface.

## Features

- Retrieves data from a provided URL.
- Processes the data using a vector-based indexing system.
- Uses an AI-powered language model to answer user queries based on the retrieved context.
- Provides a simple and interactive web interface using Gradio.

## Installation

Follow these steps to set up and run the project:

1. **Clone the Repository**  
   Clone this repository to your local machine using:
   ```bash
   git clone https://github.com/gkunal8019/assignment_.git
   cd assignment_
   ```

2. **Set Up a Virtual Environment (Optional but Recommended)**  
   Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**  
   Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**  
   Start the Gradio interface by running:
   ```bash
   python main.py
   ```
   This will launch the application in your default web browser. If not, you can access it via the provided local or public URL.

## Code Overview

### 1. **Main Functionality**
- The `process_query` function takes a URL and a user query as inputs.
- It retrieves data from the URL using `SimpleWebPageReader`.
- The data is indexed using `VectorStoreIndex`, which allows for efficient similarity-based retrieval.
- Relevant content is retrieved based on the user's query using `AutoMergingRetriever`.
- A chat-based query is constructed and sent to an AI language model (`nvllm.stream_chat`) for generating responses.

### 2. **Gradio Interface**
- The Gradio interface includes input fields for the URL and query, a submit button, and an output field for displaying responses.
- When the "Submit" button is clicked, it triggers the `process_query` function.

### 3. **Error Handling**
- The code includes error handling to manage issues like failed data retrieval or processing errors.

## Example Usage

1. Enter a valid URL in the "Enter URL" field.
2. Enter your query in the "Enter Query" field.
3. Click "Submit" to get an AI-generated response based on the content of the provided URL.

## Dependencies

The project uses the following major dependencies:
- [LlamaIndex](https://github.com/jerryjliu/llama_index): For document indexing and retrieval.
- [Gradio](https://gradio.app/): For building an interactive web interface.

## Notes

- Ensure that you have a stable internet connection, as the application fetches data from external URLs and communicates with an AI model.
- Replace `nvllm.stream_chat` with your preferred LLM API or library if needed.

---
