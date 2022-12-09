# Import the NLTK library
import nltk

# Define a list of responses for the chatbot
responses = [
  "Hello, how can I help you?",
  "I'm sorry, I didn't understand what you said. Could you repeat that?",
  "I'm just a chatbot, so I don't have feelings. But I'm here to help you with any questions you have.",
  "I'm not sure, but I can try to find out for you. Can you please provide more information?",
  "I'm sorry, but I can't answer that. Can you please ask a different question?"
]

# Prompt the user for input
user_input = input("What can I help you with? ")

# Use NLTK to tokenize the user's input
tokens = nltk.word_tokenize(user_input)

# Use NLTK to tag the part of speech for each token
pos_tags = nltk.pos_tag(tokens)

# Print the part-of-speech tags for each token
print("Part-of-speech tags:", pos_tags)

# Check if the user's input matches any of the responses
if user_input in responses:
  # If the input matches a response, print the response
  print(user_input)
else:
  # If the input doesn't match any of the responses,
  # select a random response and print it
  import random
  print(random.choice(responses))
