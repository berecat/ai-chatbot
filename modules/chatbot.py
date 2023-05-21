import openai
import config
from typing import Union, Dict, List

openai.api_key = config.api_key
__initial_prompt = ""
__initial_role = ""
__message_stream: Union[List[Dict[str, str]], List[Dict[str, str]]] = []


def new_chat(mode, user_name, user_like, user_dislike, user_personality, user_gender, chatbot_gender):
    global __initial_prompt
    global __initial_role
    __message_stream.clear()

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
        __initial_role = "dating partner"
    elif mode == "friend":
        __initial_prompt = friend_initial_prompt
        __initial_role = "friend"

    __message_stream.append({"role": __initial_role, "content": __initial_prompt})


def send_message(message):
    __message_stream.append({"role": "user", "content": message})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=__message_stream,
    )

    response_text_format = response.choices[0].message.content
    __message_stream.append({"role": __initial_role, "content": response_text_format})

    return response_text_format


def get_message_stream(message_index):
    return __message_stream[message_index]["content"]
