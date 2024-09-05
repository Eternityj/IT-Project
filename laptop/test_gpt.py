from gpt import *

# Test the function
if __name__ == "__main__":
    book_content = "Long ago, there was a big cat in the house. He caught many mice while they were stealing food. One day the mice had a meeting to talk about the way to deal with their common enemy. Some said this, and some said that. At last a young mouse got up, and said that he had a good idea. We could tie a bell around the neck of the cat. Then when he comes near, we can hear the sound of the bell, and run away. Everyone approved of this proposal, but an old wise mouse got up and said, That is all very well, but who will tie the bell to the cat? The mice looked at each other, but nobody spoke."
    user_question = "What is the proposed solution to deal with the cat?"

    answer = ask_gpt_with_current_page(book_content, user_question)
    print("Answer from GPT-3:")
    print(answer)