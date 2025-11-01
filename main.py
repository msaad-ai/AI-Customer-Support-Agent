from agents import Runner
from model_config import config
from customer_support_agent import customer_support_agent



print("👨‍💻 Hi there! I'm **Saad**, AI Developer & Creator of this chatbot. 🚀\nI built this project using the **OpenAI Agents SDK + Chainlit**.")

while True:
    prompt = input("Customer: ")
    if prompt.lower() in ["exit", "quit"]:
        print("Exiting the chat. Goodbye!")
        break

    result = Runner.run_sync(customer_support_agent, prompt, run_config=config)

    # agent ka naam RunResult ke last_agent se le lo
    if hasattr(result, "last_agent") and result.last_agent:
        agent_name = result.last_agent.name
    else:
        agent_name = "Support Agent"

    print(f"[{agent_name}]: {result.final_output}\n")
