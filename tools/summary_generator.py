from llama_cpp import Llama

# Initialize Llama model (CPU-only, using GGUF)
llm = Llama(
    model_path="./models/mistral-7b-instruct/mistral-7b-instruct-v0.1.Q3_K_M.gguf",
    n_gpu_layers=0,   # CPU mode
    n_threads=8,      # Optimize for CPU cores
    n_ctx=2048        # Context length (you can increase up to model limit if needed)
)

def generate_summary(text: str, max_tokens: int = 200) -> str:
    """
    Generates a summary for the given text using a locally loaded Llama GGUF model.

    Args:
        text (str): The input text to summarize.
        max_tokens (int): Maximum length of the summary.

    Returns:
        str: The generated summary.
    """

    # Instruction-style prompt for summarization
    prompt = f"Summarize the following text in a concise and clear manner:\n\n{text}\n\nSummary:"

    # Create chat completion using llama_cpp
    response = llm.create_chat_completion(
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant specialized in summarization."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens,
        temperature=0.7  # Lower for more factual summaries
    )

    # Extract summary text
    return response['choices'][0]['message']['content'].strip()


# ✅ For testing the module directly
if __name__ == "__main__":
    test_text = "Large language models such as Mistral and LLaMA are revolutionizing natural language processing by enabling high-quality text generation and summarization."
    print("Generated Summary:\n", generate_summary(test_text))
