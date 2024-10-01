// index.js
const { LMStudioClient } = require("@lmstudio/sdk");

async function main() {
  // Create a client to connect to LM Studio, then load a model
  const client = new LMStudioClient();
  const model = await client.llm.load("TheBloke/Llama-2-7B-Chat-GGUF/llama-2-7b-chat.Q3_K_L.gguf");

  // Predict!
  const prediction = model.respond([
    { role: "system", content: "You are a helpful AI assistant. Format all responses in html." },
    { role: "user", content: "How do you soft boil an egg?" },
  ]);
  for await (const text of prediction) {
    process.stdout.write(text);
  }
}

main();
