import datetime
import requests

class CommandHandler:
    def handle_command(self, command):
        command = command.lower()
        if "time" in command:
            return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}."
        elif "weather" in command:
            return self.get_weather()
        elif "joke" in command:
            return self.get_joke()
        else:
            return "Sorry, I didn't understand that command."

    def get_weather(self):
        api_key = "bacad1101c4ac8e9f8ab4eba7b60bee4"
        city = "Shiraz"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url).json()
        if response.get("main"):
            temp = response["main"]["temp"]
            description = response["weather"][0]["description"]
            return f"The weather in {city} is {temp}°C with {description}."
        else:
            return "Unable to fetch weather information."

    def get_joke(self):
        response = requests.get("https://official-joke-api.appspot.com/random_joke").json()
        return f"{response['setup']} - {response['punchline']}"
