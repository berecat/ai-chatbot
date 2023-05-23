import openai
import config
from typing import Union, Dict, List

openai.api_key = config.api_key
__initial_prompt = ""
__initial_role = ""
__message_stream: Union[List[Dict[str, str]], List[Dict[str, str]]] = []


def new_chat(mode, user_name, user_like, user_dislike, user_personality, user_gender, chatbot_gender):
    """
    This function is used to create a new chat with the chatbot
    :param mode: The mode of the chat, either dating or friend
    :param user_name: The name of the user
    :param user_like: The like of the user
    :param user_dislike: The dislike of the user
    :param user_personality: The personality of the user
    :param user_gender: The gender of the user
    :param chatbot_gender: The gender of the chatbot
    :return: None
    """

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
    pass


def send_message(message):
    """
    This function is used to send a message to the chatbot
    :param message: The message to be sent to the chatbot
    :return: The content of the message sent by the chatbot
    """

    __message_stream.append({"role": "user", "content": message})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=__message_stream,
    )

    response_text_format = response.choices[0].message.content
    __message_stream.append({"role": __initial_role, "content": response_text_format})

    return __message_stream[-1]["content"]


def load_message_on_stream(is_user, message):
    """
    This function is used to load the message on the stream
    :param is_user: Whether the message is from the user or not
    :param message: The message to be loaded
    :return:
    """

    if is_user:
        __message_stream.append({"role": "user", "content": message})
    else:
        __message_stream.append({"role": __initial_role, "content": message})

    pass


def get_message_stream(index):
    """
    This function is used to get the message stream
    :param index: The index of the message stream
    :return: A list of dictionary containing the message stream
    """

    return __message_stream[index]["content"]
