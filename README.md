# ChatGPT Override Project

### Overview & Purpose:
The integration of AI chatbots is becoming more prevalent across industries, particularly for tasks like customer support, virtual assistance, and knowledge management. While large models like ChatGPT provide impressive responses, they may occasionally produce contextually incorrect or irrelevant responses, leading to user frustration or misinformation. Similarly, models like these are only trained on public information, making them unsuited for answering questions about private or situationally-specific information. For this project, I will use knowledge embedding to override GPT responses so that they remain relevant to the topic of the training data, regardless of the prompt. My goal for this project is to build an understanding of prompt engineering, explore hallucination challenges, and learn about methods for improving the contextual accuracy of AI chatbots.

### This Project's Use Case:
I developed a chatbot that specializes in Python-specific advice and solutions. Trained on a dataset of Python Stack Overflow question-and-answer pairs, this chatbot's primary objective is to deliver accurate and contextually relevant advice, even when faced with vague or distracting user prompts.

### Topics Explored in this Project:
- Loading and Preprocessing CSV Data
- Vectorizing Data
- Running Similarity Searches
- LLMChain and Prompt Engineering
- Retrieval Augmented Generation (RAG)
 
- Learn and understand:
  - prompt engineering with LLMs
  - what a vector DB is & how to use it
  - examples of good and bad tests
  - Is load running a good scenario
  - fine-tuning vs. prompt engineering

### Contributors:
- Dev: Jess Houghton
- Mentor: Mark Farra

### Other Real-World Application Examples:
- **Customer Support:** To ensure accurate and relevant responses.
- **Educational Platforms:** Tailoring responses to match course curriculum & student knowledge levels.
- **Technical Documentation:** Providing relevant, precise, and up-to-date information.
- **Company Knowledge Bases:** Prevent responses referencing outdated or unrelated external information when inquiring about internal company topics.
