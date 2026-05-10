from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import InMemorySaver

model = init_chat_model(
  "openai:gpt-5.4-mini",
  temperature=0.6,
  max_tokens=1024,
  timeout=300
)

checkpointer = InMemorySaver()