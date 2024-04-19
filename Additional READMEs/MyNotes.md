# Progress, Ideas, & Questions - Documentation Space
### Progress Reports:
**Week of April 8th:**
- Install Python and any necessary dependencies.
- Set up IDE (Visual Studio Code) and Jupyter Notebook extension.
- Created a new GitHub account and wrote a Profile README
- Configure the version control system (Git) and connect it to my GitHub repository.

**April 17th - 18th:**
- Created a repo for this project.
- Created & filled out a main README for project overview and goals.
- Created a folder containing READMEs for Documentation & FAQ, Installation & Setup, and Usage & Testing (to be filled out as I go).
--------------------
### Notes & Links:
- From Google:
  - "Cypher is Neo4j's graph query language that lets you retrieve data from the graph. It is like SQL for graphs, and was inspired by SQL so it lets you focus on what data you want out of the graph (not how to go get it)." _So basically you tell it: "Here's the data I want, go look for it" (Cypher) instead of "go get me the data that's in this location" (SQL)?_
- [Context-Aware Knowledge Graph Chatbot With GPT-4 and Neo4j (Cypher)](https://medium.com/neo4j/context-aware-knowledge-graph-chatbot-with-gpt-4-and-neo4j-d3a99e8ae21e)
  - [GitHub Code Examples](https://github.com/tomasonjo/NeoGPT-Recommender/tree/main)
- [Azure OpenAI Completion API vs Chat Completion API – Demystifying the Differences!](https://www.linkedin.com/pulse/azure-openai-completion-api-vs-chat-demystifying-qirpc/)
  - This explanation confirms I'll want to use OpenAI's Chat Completion API (also mentioned in the Medium link) if I can!
- [OpenAI Models](https://platform.openai.com/docs/models/overview)
--------------------
### Questions:
- Is a project like this applicable to solving problems like hallucinations?
- Once I get the project to a place where I can see if it is choosing the context correctly or not, is the next step to improve the model or the dataset? And if it's just to improve the model, would any improved model only work on the exact dataset that I trained it on? Or would that model be usable on other datasets? _I assume the answers to these questions get into the purpose of AI models and the tasks of people working in AI in general, but I want to make sure I have a good understanding of this._
- What type of dataset should I look for? One that contains tons of different contexts or one that has info on the same topic? Because I feel like GPT already does a good job of keeping the conversation on-topic once it's already there. But the point of this project is to help GPT get on topic quickly / on the first try, right?

- Is the point of this project to help get GPT on-topic and quickly? Or is the point to prevent it from getting off-topic for the remainder of the conversation after the point where you get GPT to the correct context? If it's the latter, GPT has the Chat Completion API that remembers the entire conversation so you don't have to be specific in every one of your prompts. How would I be able to do a better job than GPT? If it's the former, are we hoping to have GPT be able to reconize context clues before you even give it a prompt? Like a company VPN, a school wifi, etc? Or would the goal for this type of system be for a single-use case? Meaning that we can make a GPT override for a company to use internally, but it would be a very different product from the one we would make for a student education platform?

**- Clean up these questions, make another readme specifically for questions and put them there. Then add Mark to this repo. Go back through GPT and the aritcles I'm reading to remember all the questions I have.**








