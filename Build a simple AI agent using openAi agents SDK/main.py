
from agents import Runner, set_tracing_disabled
from my_agent.teacher_agent import agent
set_tracing_disabled( True)  # Disable tracing for the agent
res = Runner.run_sync(starting_agent=agent,input="you are a specialist off open AI aAgent SDK,and Good and friendly, teacher")

print(res.final_output)