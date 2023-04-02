from datetime import datetime


def sample_responses(input_text):

    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup"):
        return "Hey! How are you doing?"

    if user_message in ("who are you", "who are you?"):
        return "I am ChatMate."

    if user_message in ("time", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    # If none of the above conditions are met, return this
    return "I don't understand you."
