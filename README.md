# Personal Repository
This is a compilation of projects I have done in my own personal time.

## 1 - Research tool powered by OpenAI
This project focused on implementing an end to end tool that could assist with research of online text resources. The goal was to be able to provide some websites and be able to ask questions about their content. This could be used to help with research in a plethora of scenarios. 

It works in four stages, first the URL is used to load the text from that website, using the Unstructured library. Then the data is split into chunks. This is done in order to minimize computational costs. These chunks are then turned into a vector database using OpenAI embeddings. The user can then create a query, which can be a question, a request for clarification or a summary, which will be also be converted to a vector format before being sent to the OpenAI API for an answer.

![Screenshot 2024-05-20 at 5 11 23 PM](https://github.com/anatolii-sid/personal/assets/146433876/738a1f3a-0392-4157-b129-0dde2fbf744f)

## 2 - Trading bot using Neuro-evolution
This was a test to see if NEAT (Neuro-Evolution Augmented Topology) could be utilized to create a bot that could successfuly live-trade and turn a profit. It utilizes agents controled by neural networks, that are tested on the last three days of BTC-USD prices. The best bots remain and are used to create a new population through crossover and mutation. After a few runs some bots were able to provide a 0.53% return.

![Screenshot 2024-05-20 at 5 09 10 PM](https://github.com/anatolii-sid/personal/assets/146433876/8330279c-7351-430a-a4ce-3eab84960816)

## 3 - 3D Graphics in Python using OpenGL
This was a test of the OpenGL library for python. I wanted to see how I could take a 3D .obj file and show it using Python.

![Screenshot 2024-05-20 at 4 14 24 PM](https://github.com/anatolii-sid/personal/assets/146433876/aeb92e1c-82e4-4dce-8f20-52f66fd99678)

## 4 - This Anatolii Does Not Exist using PyTorch

This project was inspired by the thispersondoesnotexist.com webiste. Through the use Generative Adveserial Networks I was able to train a model to generate images of my face. Although not perfect they are impressive when considering that the data set only had 306 samples. 

![output](https://github.com/anatolii-sid/personal/assets/146433876/bfca2091-a9de-4d40-b33a-fcfed2987b9a)
