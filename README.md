# Personal Repository
A compilation of personal porjects

## 1 - Research tool powered by OpenAI
This project focused on implementing an end to end tool that could assist with research of online text resources. The goal was to be able to provide some websites and be able to ask questions about their content. This could be used to help with research in a plethora of scenarios. 

It works in four stages, first the URL is used to load the text from that website, using the Unstructured library. Then the data is split into chunks. This is done in order to minimize computational costs. These chunks are then turned into a vector database using OpenAI embeddings. The user can then create a query, which can be a question, a request for clarification or a summary, which will be also be converted to a vector format before being sent to the OpenAI API for an answer.

