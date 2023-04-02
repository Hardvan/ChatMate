from datetime import datetime
from jokeapi import Jokes
import asyncio


async def GetJokeFromAPI():

    # Initialize the Jokes class
    j = await Jokes()

    # Retrieve a random joke
    joke = await j.get_joke(category="Programming")

    text = ""
    if joke["type"] == "single":
        text = joke["joke"]
    else:
        text = f"{joke['setup']}\n{joke['delivery']}"

    category = joke["category"]

    return f"Here's your {category} joke:\n\n{text}"


def respond_to_message(input_text):

    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup"):
        return "Hey! How are you doing?"

    if user_message in ("who are you", "who are you?"):
        return "I am ChatMate."

    if "time" in user_message:
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    if "date" in user_message:
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y")

        return str(date_time)

    if "name" in user_message:
        return "My name is ChatMate."

    if "joke" in user_message:

        return asyncio.run(GetJokeFromAPI())

    # If none of the above conditions are met, return this
    return "I don't understand you."
