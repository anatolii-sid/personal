# Personal Repository
A compilation of personal porjects

## 1 - Research tool powered by OpenAI
This project focused on implementing an end to end tool that could assist with research of online text resources. The goal was to be able to provide some websites and be able to ask questions about their content. This could be used to help with research in a plethora of scenarios. 

It works in four stages, first the URL is used to load the text from that website, using the Unstructured library. Then the data is split into chunks. This is done in order to minimize computational costs. These chunks are then turned into a vector database using OpenAI embeddings. The user can then create a query, which can be a question, a request for clarification or a summary, which will be also be converted to a vector format before being sent to the OpenAI API for an answer.

![Screenshot 2024-05-20 at 5 11 23 PM](https://github.com/anatolii-sid/personal/assets/146433876/738a1f3a-0392-4157-b129-0dde2fbf744f)

## 2 - Trading bot using Neuro-evolution
This was a test to see if NEAT (Neuro-Evolution Augmented Topology) could be utilized to create a bot that could successfuly live-trade and turn a profit. It utilizes agents controled by neural networks, that are tested on the last three days of BTC-USD prices. The best bots remain and are used to create a new population through crossover and mutation. After just a few runs some bots were able to provide a 5.3% return.

![Screenshot 2024-05-20 at 5 09 10 PM](https://github.com/anatolii-sid/personal/assets/146433876/8330279c-7351-430a-a4ce-3eab84960816)

## 3 - 3D Graphics in Python using OpenGL
This was a test of the OpenGL library for python. I wanted to see how I could take a 3D .obj file and show it using Python.

![Screenshot 2024-05-20 at 4 14 24 PM](https://github.com/anatolii-sid/personal/assets/146433876/aeb92e1c-82e4-4dce-8f20-52f66fd99678)
