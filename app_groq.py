from dotenv import load_dotenv
from swarm import Agent, Swarm
import openai
import os
# Load environment variables
load_dotenv()


model = "llama-3.2-90b-vision-preview"
llm_client = openai.OpenAI(
  base_url="https://api.groq.com/openai/v1",
  api_key=os.getenv('GROQ_API_KEY'),
)

temperature=0.1
top_p=1
max_tokens=4096

def llmm(messages):
  #messages=[{"role": "user","content": prompt}]
  completion = llm_client.chat.completions.create(
  model=model,
  messages=messages,
  temperature=temperature,
  top_p=top_p,
  max_tokens=max_tokens,
  stream=False
  )
  return completion.choices[0].message.content

def llm(prompt):
  messages=[{"role": "user","content": prompt}]
  completion = llm_client.chat.completions.create(
  model=model,
  messages=messages,
  temperature=temperature,
  top_p=top_p,
  max_tokens=max_tokens,
  stream=False
  )
  return completion.choices[0].message.content


# Initialize the Swarm client
client = Swarm(client=llm_client)

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
agent_small_talk = Agent(
    name="Agent Small Talk",
    instructions="You are an insurance customer service agent. You are responsible for small talk and transferring the user to the appropriate agent.",
    functions=[transfer_to_agent_home_insurance, transfer_to_agent_auto_insurance, transfer_to_agent_accident_insurance, transfer_to_agent_health_insurance],
    model=model,
    tool_choice="none"
)

# Insurance Agent B - Home Insurance Agent
agent_home_insurance = Agent(
    name="Agent Home Insurance",
    instructions="You are an insurance agent responsible for home insurance claims. You have deep knowledge of home insurance policies and claims, and you help the user file a claim.",
    model=model,
    tool_choice="none"
)

# Insurance Agent C - Auto Insurance Agent
agent_auto_insurance = Agent(
    name="Agent Auto Insurance",
    instructions="You are an insurance agent responsible for auto insurance claims. You have deep knowledge of auto insurance policies and claims, and you help the user file a claim.",
    model=model,
    tool_choice="none"
)

# Insurance Agent D - Accident Insurance Agent
agent_accident_insurance = Agent(
    name="Agent Accident Insurance",
    instructions="You are an insurance agent responsible for accident insurance claims. You have deep knowledge of accident insurance policies and claims, and you help the user file a claim.",
    model=model,
    tool_choice="none"
)   

# Insurance Agent E - Health Insurance Agent
agent_health_insurance = Agent(
    name="Agent Health Insurance",
    instructions="You are an insurance agent responsible for health insurance claims. You have deep knowledge of health insurance policies and claims, and you help the user file a claim.",
    model=model,
    tool_choice="none"
)   

# Run the Swarm with Agent A
response = client.run(
    agent=agent_small_talk,
    messages=[{"role": "user", "content": "I want to know about health insurance"}],
)

# Print the last message from the response
print(response.messages[-1]["content"])