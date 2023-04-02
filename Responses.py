from datetime import datetime


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

    # If none of the above conditions are met, return this
    return "I don't understand you."
