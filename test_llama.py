from llama_cpp import Llama

print("✅ Import worked - CPU only mode")

llm = Llama(
    model_path="./models/mistral-7b-instruct/mistral-7b-instruct-v0.1.Q3_K_M.gguf",
    n_gpu_layers=0,
    n_threads=8
)
print("✅ Llama initialized successfully in CPU mode!")
