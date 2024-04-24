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
1. Is the point of this project to help get GPT on-topic and quickly? Or is the point to prevent it from getting off-topic for the remainder of the conversation after the point where you get GPT to the correct context?
    - Latter: GPT has the Chat Completion API that remembers the entire conversation so you don't have to be specific in every one of your prompts. How would I be able to do a better job than GPT?
    - Former: Are we hoping to have GPT be able to recognize context clues before you even give it a prompt? Like a company VPN, a school wifi, etc? Or will this type of project need to be tailored for a pretty specific use case and dataset like for a specific company or a school or something? In which case you would start the convo by connecting it to your situation's applicable data and from there it should always give you on-topic info?

2. I've done a lot of reading on conversational models and smarter searches using Cypher and knowledge maps, but I assume the actual measure of a high-performing model depends on a decent amount on the data being good, so where can I get a dataset that has information like this with helpful attributes for accurate testing?
    - Follow up: What type of dataset should I look for? One that contains tons of different contexts (so that I can try to trick it into changing the subject) or one that has info on the same topic (so that I can ask it vague questions and see if it still performs well)? 

3. Is a project like this applicable to solving problems like hallucinations?








