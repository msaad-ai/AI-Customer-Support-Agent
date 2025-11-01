from agents import Runner
from model_config import config
from customer_support_agent import customer_support_agent
import chainlit as cl


@cl.on_chat_start
async def start():
    # 👨‍💻 Intro Message with emoji avatar (image avatar not supported directly here)
    await cl.Message(
        author="👨‍💻 Saad",
        content=(
            "## 👋 Welcome to My AI Chatbot Portfolio\n\n"
            "---\n"
            "### 💡 About Me\n"
            "I'm **Saad**, an AI Developer specializing in building intelligent agents and chatbot systems.\n\n"
            "### ⚡ Skills\n"
            "- 🤖 AI Agents (OpenAI Agents SDK)\n"
            "- 🌐 Chainlit UI Integration\n"
            "- 🛠️ Tool Calling & Context Handling\n"
            "- 📊 Tracing, Guardrails, and Sessions\n\n"
            "### 📌 Connect with Me\n"
            "🔗 [GitHub](https://github.com/msaad-ai)\n"
            "💼 [LinkedIn](https://www.linkedin.com/in/msaad-ai)\n"
            "---\n"
            "💬 **Type a message below to start chatting with my AI agent!**"
        )
    ).send()


@cl.on_message
async def on_message(message: cl.Message):
    result = await Runner.run(customer_support_agent, message.content, run_config=config)
    agent_name = result.last_agent.name if hasattr(result, "last_agent") and result.last_agent else "Support Agent"
    await cl.Message(content=f"[{agent_name}]: {result.final_output}").send()
