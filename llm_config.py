from llama_index.embeddings.nvidia import NVIDIAEmbedding
from llama_index.llms.nvidia import NVIDIA
from llama_index.core import Settings, VectorStoreIndex
llm_model = "meta/llama-3.1-90b-instruct"
nvllm = NVIDIA(
    model=llm_model,
    #base_url="http://local-host:2000/v1/chat/completions",
    api_key="mentioned-the-api-key"
)

embedder = NVIDIAEmbedding(
    base_url="http://local-host:8000/v1",
    model="nvidia/nv-embedqa-e5-v5",#"nvidia/llama-3.2-nv-embedqa-1b-v2",##
    truncate="END"
)

# Settings for LLM and embeddings
Settings.llm = nvllm
Settings.embed_model = embedder
Settings.context_window = 4096
Settings.num_output = 1100
