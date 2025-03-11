from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.core import StorageContext
from llama_index.core.storage.docstore.simple_docstore import SimpleDocumentStore
from llama_index.core import VectorStoreIndex
from llama_index.core.retrievers import AutoMergingRetriever
from llama_index.core.node_parser import HierarchicalNodeParser
from llama_index.core.chat_engine.context import ContextChatEngine
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core.callbacks import CallbackManager
from llama_index.core import SimpleDirectoryReader
from llm_config import *
from llama_index.readers.web import SimpleWebPageReader
import gradio as gr


def process_query(url, user_query):
    try:
        # Load data from the provided URL
        reader = SimpleWebPageReader(html_to_text=True)
        docs = reader.load_data(urls=[url])
        
        if not docs:
            return "Failed to retrieve data from the URL."
        index = VectorStoreIndex.from_documents(docs)
        storage_context = StorageContext.from_defaults(vector_store=index)        
        base_retriever = index.as_retriever(similarity_top_k=20)
        retriever = AutoMergingRetriever(base_retriever, storage_context, verbose=False)
        nodes = retriever.retrieve(user_query)
        context_str = "\n\n".join([n.node.get_content() for n in nodes])        
        messages = [
            ChatMessage(role=MessageRole.SYSTEM, content="You are a helpful assistant."),
            ChatMessage(
                role=MessageRole.USER,
                content=(
                    "Using the following context, please answer the question below:\n"
                    "---------------------\n"
                    f"{context_str}\n"
                    "---------------------\n"
                    f"{user_query}"
                )
            ),
        ]
        
        response = nvllm.stream_chat(messages)
        full_response = ""

        try:
            # Accumulate the chunks into a single string
            for chunk in response:
                full_response += chunk.delta
        except Exception as e:
            return f"Error occurred: {str(e)}"
        
        # Return the final accumulated response
        return full_response

    except Exception as e:
        return f"Error: {str(e)}"

with gr.Blocks() as demo:
    url_input = gr.Textbox(label="Enter URL")
    query_input = gr.Textbox(label="Enter Query")
    submit_button = gr.Button("Submit")
    output_text = gr.Textbox(label="Response")

    submit_button.click(
        fn=process_query,
        inputs=[url_input, query_input],
        outputs=output_text
    )

demo.launch(share=True, debug=True)
