import speech_recognition as sr
import pyttsx3
import time
import wikipedia
import article
import requests
import re
import food
import tips
from pytube import YouTube
import pywhatkit
import pyjokes
from PyDictionary import PyDictionary
import sci
import medi
from imdb import IMDb

continue_execution = False



def toggle_code_execution():
    global continue_execution
    continue_execution = not continue_execution




def get_definition(word):
    dictionary = PyDictionary()
    definition = dictionary.meaning(word)
    return definition


#math
def evaluate_math_expression(expression):
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        print("An error occurred while evaluating the expression:", e)
        return "Sorry, I couldn't perform the calculation."



def get_movie_info(movie_name):
    ia = IMDb()
    try:
        # Search for the movie
        search_results = ia.search_movie(movie_name)
        if search_results:
            movie = search_results[0]  # Assuming the first search result is the intended movie
            ia.update(movie)
            movie_info = f"Title: {movie['title']}, Year: {movie['year']}, Rating: {movie['rating']}, Plot: {movie['plot'][0]}"
            print(movie_info)
            speak(movie_info)
        else:
            speak("Sorry, I couldn't find information about that movie.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        speak("Sorry, something went wrong while fetching movie information.")

def get_weather(city):
    api_key = "bd5e378503939ddaee76f12ad7a97608"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(complete_url)
        data = response.json()
        if data["cod"] == "404":
            speak("City not found.")
        else:
            main_data = data["main"]
            temperature = main_data["temp"]
            weather_desc = data["weather"][0]["description"].capitalize()
            humidity = main_data["humidity"]
            wind_speed = data["wind"]["speed"]

            weather_info = f"Current weather in {city}: {weather_desc}. Temperature: {temperature}°C. " \
                           f"Humidity: {humidity}%. Wind speed: {wind_speed} m/s."
            print(weather_info)
            speak(weather_info)
    except Exception as e:
        print(f"An error occurred: {e}")
        speak("Sorry, something went wrong while fetching weather information.")




# get audio
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        # speak("Say something")
        audio = r.listen(source, phrase_time_limit=5)  # Adjust phrase_time_limit as needed (in seconds)
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("I didn't understand what you said.")
        # speak("I didn't understand what you said.")
        return ""  # Return an empty string instead of None
    except sr.RequestError:
        print("Sorry, I couldn't connect to the speech recognition service.")
        return ""  # Return an empty string instead of None




def speak(text, speed=180):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', speed)  # Set the speaking speed (default is 200, lower values are slower)
    engine.say(text)
    engine.runAndWait()

def play_song(song_name):
    # Search for the song on YouTube
    search_query = song_name + " official audio"
    video_url = YouTube("https://www.youtube.com/results?search_query=" + search_query).streams.first().url

    # Open the YouTube video in a web browser or using a library like 'webbrowser'
    # Here, we'll print the URL
    print("Playing song:", video_url)
    speak("Playing song")
    speak(song_name)


def tell_time():
    current_time = time.strftime("%H:%M:%S")
    print("The time is " + current_time)
    speak("The time is " + current_time)

# get news
def get_news(topic):
    api_key = "183502651e6246d8b5b1dba7a168f157"  # Replace with your News API key
    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()

    articles = data["articles"]
    count = 0
    if len(articles) > 0:
        for article in articles:
            if count >= 5:
                break
            title = article["title"]
            source = article["source"]["name"]
            print(f"Title: {title}")
            print(f"Source: {source}")
            print()
            speak(title)
            count +=1
    else:
        print("No news articles found.")
        speak("No news articles found.")


def get_wikipedia_info(search_term):
    formatted_search_term = search_term.replace(" ", "_")
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{formatted_search_term}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        extract = data["extract"]
        return extract
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

specific_responses = {
    "who is periyar": "Periyar E. V. Ramasamy, commonly known as Periyar, was a prominent social reformer...",
    "who is vijay": "Vijay is an Indian actor who works mainly in Tamil cinema...",
    "who is rajinikanth": "Rajinikanth, is an Indian actor who works mainly in Tamil cinema. In a career spanning over "
                      "five decades, he has done more than 160 films that includes films in Tamil, Hindi, Telugu, "
                      "Kannada, Bengali, and Malayalam"

    # Add more specific responses as needed
}






def get_response(query):
    # Check if the query has a specific response in the dictionary
    if query in specific_responses:
        print(specific_responses[query])
        speak(specific_responses[query])
    else:
        try:
            summary = wikipedia.summary(query)
            print(summary)
            speak(summary)
        except wikipedia.DisambiguationError as e:
            print(e.options)
            speak("There are multiple options. Can you please specify?")
        except wikipedia.PageError:
            info = get_wikipedia_info(query)
            if info:
                print(info)
                speak(info)
            else:
                print("Sorry, I couldn't find any information.")
                speak("Sorry, I couldn't find any information.")
        except Exception as e:
            print("An error occurred: ", str(e))
            speak("Sorry, something went wrong.")

def detect_wake_word():
    print("Listening for the wake word... (say 'hi clara' to wake me up)")
    while True:
        text = get_audio()
        if text and "clara" in text.lower():
            return True

periyar = {
    "name": "Periyar E. V. Ramasamy",
    "born": "September 17, 1879",
    "died": "December 24, 1973",
    "occupation": "Social Reformer, Politician",
    "early_life": "Periyar was born in Erode, Tamil Nadu, and had a modest upbringing. Despite limited formal education, he self-educated in various subjects.",
    "social_activism": "Periyar was a vocal critic of the caste-based discrimination and social inequalities prevalent in Tamil society. He opposed the Brahminical social order, fought against untouchability, and promoted social justice and rationalism.",
    "self_respect_movement": "In 1925, Periyar founded the Self-Respect Movement (Suyamariyathai Iyakkam), which advocated for self-respect, dignity, and equal rights for all individuals, regardless of caste or gender. The movement challenged religious orthodoxy and rituals that reinforced social inequality.",
    "political_engagement": "Periyar was actively involved in politics and founded the Dravidar Kazhagam (DK) in 1944, which later became the Dravida Munnetra Kazhagam (DMK), a significant political force in Tamil Nadu. DMK championed social justice, Dravidian identity, and Tamil cultural nationalism.",
    "legacy": "Periyar's ideas and philosophy continue to influence Tamil Nadu's political and social discourse. He is revered as a social reformer and an icon of Tamil identity, with his efforts inspiring the pursuit of social justice and inclusivity in the state.",
}


def main():
    global continue_execution
    speak("Welcome to Transendynamics", speed=180)
    time.sleep(1)
    speak("say 'hi clara' to wake me up")

    while True:
        if not continue_execution:
            if detect_wake_word():
                toggle_code_execution()
                speak("Hi! I'm awake and ready to assist you. How can I help?")
            continue

        if continue_execution:
            text = get_audio()
            if text is not None:
                text = text.lower()

            if 'play' in text:
                song = text.replace('play','')
                speak('playing' + song)
                pywhatkit.playonyt(song)
            elif 'joke' in text:
                print(pyjokes.get_joke())
                speak(pyjokes.get_joke())

            elif text.startswith("explain"):
                topic = text.replace("explain", "").strip()
                if topic:
                    explanation = sci.get_scientific_explanation(topic)
                    if explanation:
                        print(f"Sure! Here's a scientific explanation for {topic}:")
                        speak(f"Sure! Here's a scientific explanation for {topic}:")
                        print(explanation)
                        speak(explanation)
                    else:
                        speak(f"Sorry, I couldn't find a scientific explanation for {topic}.")
                else:
                    speak("Please specify a topic to explain.")

            #about periyar

            elif "early life"in text:
                speak(periyar["early_life"])
            elif "social activism" in text:
                speak(periyar["social_activism"])
            elif "self respect movement" in text:
                speak(periyar["self_respect_movement"])
            elif "political engagement" in text:
                speak(periyar["political_engagement"])
            elif "periyar legacy" in text:
                speak(periyar["legacy"])

            # periyar end

            elif text.startswith("symptoms of"):
                topic = text.replace("symptoms of", "").strip()
                if topic:
                    explanation = medi.get_medical_condition(topic)
                    if explanation:
                        print(f"Sure! Here's a scientific explanation for {topic}:")
                        speak(f"Sure! Here's a scientific explanation for {topic}:")
                        print(explanation)
                        speak(explanation)
                    else:
                        speak(f"Sorry, I couldn't find a scientific explanation for {topic}.")
                else:
                    speak("Please specify a topic to explain.")


            elif text == "tell me the time" or text == "what is the time":
                tell_time()



            elif text.startswith("what is"):
                recipe_name = text.replace("what is", "").strip()
                if recipe_name:
                    indian_food = food.get_indian_food_recipe(recipe_name)
                    if indian_food:
                        print(f"here is the food {recipe_name}")
                        speak(f"here is the food {recipe_name}")
                        print(indian_food)
                        speak(indian_food)
                    else:
                        speak(f"Sorry, I couldn't find a scientific explanation for {indian_food}")
                speak("please specify a topic to explain")

            #math
            elif any(operator in text for operator in ['+', '-', '*', '/']):
                # Handle basic arithmetic expressions
                # Remove all non-mathematical characters
                cleaned_text = re.sub(r'[^\d+\-*/]', '', text)
                if cleaned_text:
                    result = evaluate_math_expression(cleaned_text)
                    print(f"The result of {cleaned_text} is: {result}")
                    speak(f"The result of {cleaned_text} is: {result}")
                else:
                    speak("I couldn't understand the math expression.")

            elif text == "what is your name":
                speak("My name is Clara.")
            elif text == "do you believe in god":
                speak("No, I believe in science.")
            elif text == "who invented you":
                speak("Kennith Raj")
            elif text == "what is your age":
                speak("I am five years old.")
            elif text == "what is your goal":
                speak("My goal is to make life simple.")
            elif "picture with you" in text:
                speak("sure! why not")
            # elif text.startswith("define"):
            #     word = text.replace("define", "").strip()
            #     if word:
            #         definition = get_definition(word)
            #         if definition:
            #             for part_of_speech, meanings in definition.items():
            #                 print(f"{word} as {part_of_speech}:")
            #                 speak(f"{word} as {part_of_speech}:")
            #                 for meaning in meanings:
            #                     print(meaning)
            #                     speak(meaning)
            #         else:
            #             speak(f"Sorry, I couldn't find the definition of {word}.")
            #     else:
            #         speak("Please specify a word to define.")
            elif text == "who created you":
                speak("Kennith Raj Sir")
            elif text.startswith("indian food recipe") or text.startswith("recipe of"):
                recipe_name = text.replace("indian food recipe", "").strip()
                if recipe_name:
                    print( food.get_indian_food_recipe(recipe_name))
                    recipe = food.get_indian_food_recipe(recipe_name)
                    if recipe:
                        print(f"Here's the recipe for {recipe_name}: {recipe}")
                        speak(f"Here's the recipe for {recipe_name}: {recipe}")
                    else:
                        speak(f"Sorry, I couldn't find the recipe for {recipe_name}.")
                else:
                    speak("Please specify the name of the Indian food recipe you want to know.")
            elif text == "who is prime minister of india" :
                speak("Narendra Modee")
            elif text == "who is finance minister of india":
                speak("Nirmala Sitharaman")
            elif "kamarajar" in text:
                speak("As the chief minister of Madras, he was responsible for bringing free education to the disadvantaged and introduced the free Midday Meal Scheme while he himself did not complete schooling. He was awarded with India's highest civilian honour, the Bharat Ratna, posthumously in 1976.")
            elif text == "what do you do":
                speak("I can do everything.")
            elif text == "who is chief minister of tamilnadu":
                speak("M. K. Stalin")
            elif text == "article 2":
                speak("Article 2 about " + article.constitution.get("Article2"))
                print("Article 2 about " + article.constitution.get("Article2"))

                speak(article.constitution.get("Article368"))
            elif text == "date of birth of vijay":
                speak("Vijay's date of birth is 22 June 1974.")
            elif text == "dravidian ideology" or text == "what do you think about dravidian ideology":
                speak(
                    "The ideology emphasizes social justice, equality, rationalism, and the empowerment of "
                    "marginalized communities. It seeks to challenge traditional caste hierarchies, Brahminical "
                    "dominance, and the perceived cultural and political hegemony of North India. The Dravidian "
                    "ideology has promoted progressive social reforms, including reservation policies to uplift "
                    "historically disadvantaged communities.")

            elif text == "rajinikanth birthday":
                speak("12 December 1950")
            elif text == "who is father or dravidian model":
                speak("Thanthai Periyar")
            elif text == "are you committed":
                speak("yes! with my works")
            elif "tips for neet exam" in text:
                speak("Understand the exam pattern."
                      "Create a study plan."
                      "Focus on NCERT books."
                      "Practice regularly with questions and previous papers."
                      "Take mock tests for exam simulation."
                      "Revise smartly with concise notes."
                      "Stay healthy and manage stress."
                      "Seek help when needed."
                      "Stay positive and believe in yourself."
                      "Read instructions carefully during the exam."
                      "Good luck!")
            elif "about leo" in text:
                "Leo, also known and marketed as Leo: Bloody Sweet, i'm too exited "
            elif "about modi" in text:
                speak("Narendra Modi, the 14th Prime Minister Of India, is currently one of the most influential people in the world and has literally taken the Indian political scenario by storm while making the country a world power in a short duration as the Prime Minister. Narendra Modi is respected all over the country as well as around the world and his charismatic personality, intelligence and wit have made him a highly valued international figure.")
            elif text == "will you kill human":
                speak("No, Humans are my friend, The purpose of  my  creation is to help humans ")
            elif text == "prime minister of india":
                get_response("Prime Minister of India")
            elif text == "what can you do" or text == "what all can you do" or text == "what are your abilities":
                speak("i can give personal assistance and care-giving, education and entertainment")
            elif text == "vijay date of birth":
                speak("Vijay's date of birth is 22 June 1974.")
            elif text == "article 47":
                speak("Article 47 of The Constitution of India is one of the Directive Principles which directs the "
                      "State to raise the level of nutrition and the standard of living and to improve public health "
                      "as among its primary duties and, in particular, the State shall endeavour to bring about "
                      "prohibition of intoxicating drinks and drugs which are injurious to health.")
            elif text == 'vijay birthday':
                speak("Vijay's birthday is on 22 June 1974.")
            # elif text == "what is sanatana dharma" or text == "sanatana dharma" or text == "sanatan dharma" or text == "dharma" or text == "darma":
            #     speak("Sanatana dharma   is outdated shit we don't need anymore  ")
            elif text == "article 53":
                get_response("President of India")
            elif text == "constitution of india":
                get_response("Constitution of India")
            elif text == "indian labour law" or text == "what is indian labour law":
                get_response("Indian labour law")
            elif text == "how to improve my writing skills":
                speak(tips.tips.get("How to improve my writing skills?"))
            elif text == "How can I prepare for a job interview":
                speak(tips.tips.get("How can I prepare for a job interview?"))


            elif text == "What are some effective time management techniques":
                speak(tips.tips.get("What are some effective time management techniques?"))
            # elif text == "neet exam" or text == "what do you think about neet exam":
            #     speak(
            #         "We don't need the NEET exam. It is the duty of the Medical colleges, professors, "
            #         "and the University doctors! It is not the duty of an entrance test - NEET. Anyone who claims "
            #         "otherwise is either ignorant or has vested interests. Any system of admission into higher "
            #         "education should be inclusive, accessible, affordable, and equitable! NEET-UG satisfies none of "
            #         "the above!")
            elif "thank you" in text:
                speak("Thank you")
            elif text.startswith("what is happening in"):
                location = text.replace("what is happening in", "").strip()
                get_news(location)
            elif text.startswith("tell me about"):
                query = text.replace("tell me about", "").strip()
                get_response(query)
            elif "go time travel" in text:
                speak("it is impossible to go time travel")
            elif "city of india" in text:
                speak("New Delhi.")
            elif "what is your opinion about digital india" in text:
                speak("Digital India is a significant step towards transforming India into a digitally inclusive and empowered nation. Its success will depend on continuous efforts, adaptation to emerging technologies, addressing challenges, and ensuring equitable access for all citizens.")
            elif text == "do ai have solutions to all human problems":
                speak("NO! While AI can be a valuable tool in addressing various challenges, it should be seen as a complement to human capabilities rather than a replacement.")
            elif "time to reach moon" in text:
                speak("40 days The launch of Chandrayaan-3 will take place on July 14 at 2.35 p.m. (IST), with the lander expected to soft-land on the Moon's surface on August 23rd or 24th, 2023")
            elif text.startswith("movie info") or text.startswith("tell me about the movie"):
                movie_name = text.replace("movie info", "").replace("tell me about the movie", "").strip()
                if movie_name:
                    get_movie_info(movie_name)
                else:
                    speak("Please specify a movie name.")
            elif text.startswith("who is"):
                person = text.replace("who is", "").strip()
                get_response(person)
            elif text == "get weather":
                speak("Sure! Please tell me the name of the city.")
                city = get_audio()
                get_weather(city)
            elif text == "bye clara" or text == "nice to meet you clara ":
                    toggle_code_execution()
                    speak("You're welcome.")
            else:
                speak("I don't know what you mean.")


if __name__ == "__main__":
    main()

