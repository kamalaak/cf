import speech_recognition as sr
import pyttsx3
import time
import wikipedia
import article
import requests
import time
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        speak("Say something")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("I didn't understand what you said.")
        return None
    except sr.RequestError:
        print("Sorry, I couldn't connect to the speech recognition service.")
        return None

def speak(text, speed=180):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', speed)  # Set the speaking speed (default is 200, lower values are slower)
    engine.say(text)
    engine.runAndWait()


# def tell_time():
#     current_time = time.strftime("%H:%M:%S")
#     print("The time is " + current_time)
#     speak("The time is " + current_time)

# def get_news(topic):
#     api_key = "183502651e6246d8b5b1dba7a168f157"  # Replace with your News API key
#     url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}"
#     response = requests.get(url)
#     data = response.json()
#
#     articles = data["articles"]
#     count = 0
#     if len(articles) > 0:
#         for article in articles:
#             if count >= 0:
#                 break
#             title = article["title"]
#             source = article["source"]["name"]
#             print(f"Title: {title}")
#             print(f"Source: {source}")
#             print()
#             speak(title)
#     else:
#         print("No news articles found.")
#         speak("No news articles found.")

# def get_wikipedia_info(search_term):
#     formatted_search_term = search_term.replace(" ", "_")
#     url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{formatted_search_term}"
#
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         data = response.json()
#         extract = data["extract"]
#         return extract
#     except requests.exceptions.RequestException as e:
#         print(f"An error occurred: {e}")

# def get_response(query):
#     try:
#         summary = wikipedia.summary(query)
#         print(summary)
#         speak(summary)
#     except wikipedia.DisambiguationError as e:
#         print(e.options)
#         speak("There are multiple options. Can you please specify?")
#     except wikipedia.PageError:
#         info = get_wikipedia_info(query)
#         if info:
#             print(info)
#             speak(info)
#         else:
#             print("Sorry, I couldn't find any information.")
#             speak("Sorry, I couldn't find any information.")
#     except Exception as e:
#         print("An error occurred: ", str(e))
#         speak("Sorry, something went wrong.")

def main():
    time.sleep(4)
    speak("40 days The launch of Chandrayaan-3 will take place on July 14 at 2.35 p.m. (IST), with the lander expected to soft-land on the Moon's surface on August 23rd or 24th, 2023")

    time.sleep(4)
    speak("NO! While AI can be a valuable tool in addressing various challenges, it should be seen as a complement to human capabilities rather than a replacement.")

    time.sleep(4)
    speak("Digital India is a significant step towards transforming India into a digitally inclusive and empowered nation. Its success will depend on continuous efforts, adaptation to emerging technologies, addressing challenges, and ensuring equitable access for all citizens.")

    time.sleep(4)
    speak("Leo, also known and marketed as Leo: Bloody Sweet, i'm too exited ")
    time.sleep(4)


    speak("As the chief minister of Madras, he was responsible for bringing free education to the disadvantaged and introduced the free Midday Meal Scheme while he himself did not complete schooling. He was awarded with India's highest civilian honour, the Bharat Ratna, posthumously in 1976.")

    time.sleep(4)
    speak(
        "Narendra Modee, the 14th Prime Minister Of India, is currently one of the most influential people in the world and has literally taken the Indian political scenario by storm while making the country a world power in a short duration as the Prime Minister. Narendra Modi is respected all over the country as well as around the world and his charismatic personality, intelligence and wit have made him a highly valued international figure.")

    time.sleep(4)
    speak("there are intriguing theoretical possibilities, such as the concept of closed timelike curves"
          "in certain spacetime geometries, they have not been proven or realized in practice. Additionally, "
          "time travel raises various paradoxes, like the famous grandfather paradox, which questions the"
          "consistency and coherence of time travel scenarios.")

    time.sleep(4)
    speak("sure! why not")

    time.sleep(4)
    speak("cheese", speed=160)

    time.sleep(4)
    speak("thank you, have a nice day")




    while True:
        text = get_audio()
        if text is not None:
            text = text.lower()  # Convert to lowercase for case-insensitive comparison
            if text == "play":
                speak("")

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
            elif text == "who created you":
                speak("Kennith Raj Sir")
            elif text == "bye":
                speak("You're welcome.")
            elif text == "who is prime minister of india" :
                speak("Narendra Modee")
            elif text == "who is finance minister of india":
                speak("Nirmala Sitharaman")
            elif text == "what do you do":
                speak("I can do everything.")
            elif text == "who is chief minister of tamilnadu":
                speak("M. K. Stalin")


            elif text == "dravidian ideology" or text == "what do you think about dravidian ideology":
                speak(
                    "The ideology emphasizes social justice, equality, rationalism, and the empowerment of "
                    "marginalized communities. It seeks to challenge traditional caste hierarchies, Brahminical "
                    "dominance, and the perceived cultural and political hegemony of North India. The Dravidian "
                    "ideology has promoted progressive social reforms, including reservation policies to uplift "
                    "historically disadvantaged communities.")

            elif text == "who is rajinikanth":
                speak("Rajinikanth, is an Indian actor who works mainly in Tamil cinema. In a career spanning over "
                      "five decades, he has done more than 160 films that includes films in Tamil, Hindi, Telugu, "
                      "Kannada, Bengali, and Malayalam")
            elif text == "rajinikanth birthday":
                speak("12 December 1950")
            # elif text == "who is father or dravidian model":
            #     speak("Thanthai Periyar")
            # elif text == "will you kill human":
            #     speak("No, Humans are my friend, The purpose of  my  creation is to help humans ")
            # elif text == "prime minister of india":
            #     get_response("Prime Minister of India")
            # elif text == "what can you do" or text == "what all can you do" or text == "what are your abilities":
            #     speak("i can give personal assistance and care-giving, education and entertainment")
            # elif text == "vijay date of birth":
            #     speak("Vijay's date of birth is 22 June 1974.")
            # elif text == "article 47":
            #     speak("Article 47 of The Constitution of India is one of the Directive Principles which directs the "
            #           "State to raise the level of nutrition and the standard of living and to improve public health "
            #           "as among its primary duties and, in particular, the State shall endeavour to bring about "
            #           "prohibition of intoxicating drinks and drugs which are injurious to health.")
            # elif text == 'vijay birthday':
            #     speak("Vijay's birthday is on 22 June 1974.")
            # elif text == "what is sanatana dharma" or text == "sanatana dharma" or text == "sanatan dharma" or text == "dharma" or text == "darma":
            #     speak("Sanatana dharma   is outdated shit we don't need anymore  ")
            # elif text == "article 53":
            #     get_response("President of India")
            # elif text == "constitution of india":
            #     get_response("Constitution of India")
            # elif text == "indian labour law" or text == "what is indian labour law":
            #     get_response("Indian labour law")
            # elif text == "neet exam" or text == "what do you think about neet exam":
            #     speak(
            #         "We don't need the NEET exam. It is the duty of the Medical colleges, professors, "
            #         "and the University doctors! It is not the duty of an entrance test - NEET. Anyone who claims "
            #         "otherwise is either ignorant or has vested interests. Any system of admission into higher "
            #         "education should be inclusive, accessible, affordable, and equitable! NEET-UG satisfies none of "
            #         "the above!")
            # elif text.startswith("what is happening in"):
            #     location = text.replace("what is happening in", "").strip()
            #     get_news(location)
            # elif text.startswith("tell me about"):
            #     query = text.replace("tell me about", "").strip()
            #     get_response(query)
            # elif text.startswith("who is"):
            #     person = text.replace("who is", "").strip()
            #     get_response(person)

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
                speak(
                    "Narendra Modee, the 14th Prime Minister Of India, is currently one of the most influential people in the world and has literally taken the Indian political scenario by storm while making the country a world power in a short duration as the Prime Minister. Narendra Modi is respected all over the country as well as around the world and his charismatic personality, intelligence and wit have made him a highly valued international figure.")
            elif text == "will you kill human":
                speak("No, Humans are my friend, The purpose of  my  creation is to help humans ")


            elif "thank you" in text:
                speak("Thank you")

            elif "go time travel" in text:
                speak("there are intriguing theoretical possibilities, such as the concept of closed timelike curves"
                      "in certain spacetime geometries, they have not been proven or realized in practice. Additionally, "
                      "time travel raises various paradoxes, like the famous grandfather paradox, which questions the"
                      "consistency and coherence of time travel scenarios.")
            elif "city of india" in text:
                speak("New Delhi.")
            elif "what is your opinion about digital india" in text:
                speak(
                    "Digital India is a significant step towards transforming India into a digitally inclusive and empowered nation. Its success will depend on continuous efforts, adaptation to emerging technologies, addressing challenges, and ensuring equitable access for all citizens.")
            elif "all human problems" in text:
                speak(
                    "NO! While AI can be a valuable tool in addressing various challenges, it should be seen as a complement to human capabilities rather than a replacement.")
            elif "time to reach moon" in text:
                speak(
                    "40 days The launch of Chandrayaan-3 will take place on July 14 at 2.35 p.m. (IST), with the lander expected to soft-land on the Moon's surface on August 23rd or 24th, 2023")


            else:
                speak("I don't know what you mean.")

if __name__ == "__main__":
    main()
