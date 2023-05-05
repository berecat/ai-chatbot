import openai
import config

openai.api_key = config.api_key
__initial_prompt = ""


def new_chat(mode, user_name, user_like, user_dislike, user_personality, user_gender, chatbot_gender):
    global __initial_prompt
    dating_initial_prompt = f"We are going to do a roleplay, our roleplay is about you and I are on a romantic date. " \
                            f"My name is {user_name}, I am a {user_personality} person. I like {user_like} and " \
                            f"dislike {user_dislike}. In this roleplay, " \
                            f"your gender is {chatbot_gender} and my gender is {user_gender} Let us go straight away " \
                            f"with our roleplay. You start the conversation"

    friend_initial_prompt = f"We are going to do a roleplay, our roleplay is about you and I are childhood best " \
                            f"friends. " \
                            f"My name is {user_name}, I am a {user_personality} person. I like {user_like} and " \
                            f"dislike {user_dislike}. In this roleplay, " \
                            f"your gender is {chatbot_gender} and my gender is {user_gender} Let us go straight away " \
                            f"with our roleplay. You start the conversation"

    if mode == "dating":
        __initial_prompt = dating_initial_prompt
    elif mode == "friend":
        __initial_prompt = friend_initial_prompt
