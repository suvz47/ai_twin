from dotenv import load_dotenv
from swarm import Agent, Swarm

# Load environment variables
load_dotenv()

# Initialize the Swarm client
client = Swarm()

# Transfer chat to home insurance agent
def transfer_to_agent_home_insurance():
    return agent_home_insurance

def transfer_to_agent_auto_insurance():
    return agent_auto_insurance

def transfer_to_agent_accident_insurance():
    return agent_accident_insurance

def transfer_to_agent_health_insurance():
    return agent_health_insurance

# Insurance Agent A - Main small-talk Agent
agent_a = Agent(
    name="Agent Small Talk",
    instructions="You are an insurance customer service agent. You are responsible for small talk and transferring the user to the appropriate agent.",
    functions=[transfer_to_agent_home_insurance, transfer_to_agent_auto_insurance, transfer_to_agent_accident_insurance, transfer_to_agent_health_insurance],
)

# Insurance Agent B - Home Insurance Agent
agent_home_insurance = Agent(
    name="Agent Home Insurance",
    instructions="You are an insurance agent responsible for home insurance claims. You have deep knowledge of home insurance policies and claims, and you help the user file a claim.",
)

# Insurance Agent C - Auto Insurance Agent
agent_auto_insurance = Agent(
    name="Agent Auto Insurance",
    instructions="You are an insurance agent responsible for auto insurance claims. You have deep knowledge of auto insurance policies and claims, and you help the user file a claim.",
)

# Insurance Agent D - Accident Insurance Agent
agent_accident_insurance = Agent(
    name="Agent Accident Insurance",
    instructions="You are an insurance agent responsible for accident insurance claims. You have deep knowledge of accident insurance policies and claims, and you help the user file a claim.",
)   

# Insurance Agent E - Health Insurance Agent
agent_health_insurance = Agent(
    name="Agent Health Insurance",
    instructions="You are an insurance agent responsible for health insurance claims. You have deep knowledge of health insurance policies and claims, and you help the user file a claim.",
)   

# Run the Swarm with Agent A
response = client.run(
    agent=agent_a,
    messages=[{"role": "user", "content": "I want to know about health insurance"}],
)

# Print the last message from the response
print(response.messages[-1]["content"])