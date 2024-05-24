import llama_cpp

model = llama_cpp.Llama(
    model_path="./llama.cpp/models/mistral-7b-v0.1.Q4_K_M.gguf",
)

output = model("Q: Name the planets in the solar system? A: ", max_tokens=16, stop=["Q:", "\n"], echo= True)

print(output["choices"][0]["text"])
