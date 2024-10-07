class ThoughtProcess:
    def ReAct(self, input):
        return f"""
    Answer the following questions as best you can. You have access to tools provided.
    
    Use the following format:
    
    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take
    Action Input: the input to the action
    Observation: the result of the action
    ... (this process can repeat multiple times)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question
    
    Begin!
    Question: {input}
    """

