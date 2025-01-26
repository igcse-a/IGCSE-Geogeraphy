import random
from difflib import SequenceMatcher
import streamlit as st

# Glossary dictionary containing terms and definitions
glossary = {
    "Weather": "The condition of the atmosphere at a particular place and time, including temperature, precipitation, humidity, and wind.",
    "Climate": "The average weather conditions of a place over a long period, typically 30 years.",
    "Stevenson Screen": "A white, louvered box used to house weather instruments, protecting them from direct sunlight and precipitation while allowing air circulation.",
    "Rain Gauge": "An instrument used to measure the amount of precipitation over a specific period.",
    "Maximum-Minimum Thermometer": "A device that records the highest and lowest temperatures in a day.",
    "Wet-and-Dry Bulb Thermometer (Hygrometer)": "An instrument used to measure relative humidity by comparing the temperatures of a wet bulb and a dry bulb.",
    "Sunshine Recorder": "A device used to measure the duration of sunshine over a given period.",
    "Barometer": "An instrument that measures atmospheric pressure, useful for weather prediction.",
    "Anemometer": "An instrument used to measure wind speed.",
    "Wind Vane": "A device used to determine wind direction.",
    "Cloud Cover": "The amount of the sky covered by clouds, measured in oktas.",
    "Equatorial Climate": "A hot and humid climate typically found near the equator, characterised by high rainfall and little temperature variation throughout the year.",
    "Hot Desert Climate": "A dry climate with high daytime temperatures and cooler nights, characterised by minimal rainfall.",
    "Tropical Rainforest Ecosystem": "A dense forest ecosystem found in equatorial regions, with high biodiversity, consistent warm temperatures, and high rainfall.",
    "Hot Desert Ecosystem": "An ecosystem featuring sparse vegetation, extreme temperatures, and minimal rainfall.",
    "Convectional Rainfall": "Rainfall caused by intense heating of the Earth's surface, leading to the rapid rise of warm air and the formation of clouds.",
    "Relief Rainfall": "Rainfall caused when moist air is forced over a mountain range, cooling and condensing into precipitation.",
    "Latitude": "The distance of a location from the equator, which influences temperature and climate.",
    "Pressure Systems": "Large-scale patterns of high and low pressure that influence weather and climate, such as the Intertropical Convergence Zone (ITCZ).",
    "Winds": "Movements of air caused by differences in pressure, which influence weather and climate patterns.",
    "Distance from the Sea": "A factor affecting climate, where areas closer to the sea have milder temperatures and more consistent rainfall.",
    "Altitude": "The height above sea level, which affects temperature, with higher altitudes generally being cooler.",
    "Ocean Currents": "Large-scale movements of seawater that affect climate, such as the Gulf Stream.",
    "Climate Graph": "Visual representation of temperature and rainfall data, typically shown as a combined bar and line graph.",
    "Soil": "The upper layer of the Earth, influenced by climate and natural vegetation.",
    "Biodiversity": "The variety of plant and animal life in a particular ecosystem, such as a tropical rainforest.",
    "Wildlife": "Animals living in their natural environment, adapted to specific climatic and vegetative conditions.",
    "Global Effects of Deforestation": "Impacts such as climate change, loss of biodiversity, and disruption of global carbon cycles.",
    "Tropical Effects of Deforestation": "Specific issues such as soil erosion, changes in water cycles, and loss of habitat for wildlife."
}

# Helper function to calculate similarity ratio
def similarity_ratio(user_answer, correct_answer):
    return SequenceMatcher(None, user_answer, correct_answer).ratio()

# Main quiz function
def quiz():
    st.title("IGCSE Geography A*")
    st.subheader("Glossary for Weather, Climate & Vegetation 2.4 - 2.5")

    # Initialize session state
    if "current_question" not in st.session_state:
        st.session_state.current_question = 0
        st.session_state.correct_answers = 0
        st.session_state.feedback = []
        st.session_state.questions = list(glossary.keys())
        random.shuffle(st.session_state.questions)

    total_questions = len(st.session_state.questions)

    # Progress bar
    st.progress(st.session_state.current_question / total_questions)

    if st.session_state.current_question < total_questions:
        term = st.session_state.questions[st.session_state.current_question]
        st.subheader(f"What is the definition of '{term}'?")
        user_answer = st.text_area("Your answer:", key=f"answer_{st.session_state.current_question}").strip().lower()

        if st.button("Submit"):
            correct_answer = glossary[term].strip().lower()
            accuracy = similarity_ratio(user_answer, correct_answer)

            if accuracy >= 0.85:
                st.success("Correct!")
                st.session_state.correct_answers += 1
            else:
                st.error(f"Incorrect. The correct definition is: {glossary[term]}")
                st.session_state.feedback.append(term)

            st.session_state.current_question += 1

    else:
        st.header("Quiz Completed!")
        st.write(f"You got {st.session_state.correct_answers} out of {total_questions} questions right.")

        if st.session_state.feedback:
            st.subheader("Things to improve:")
            for item in st.session_state.feedback:
                st.write(f"- {item}")

        # Reset button
        if st.button("Restart Quiz"):
            del st.session_state.current_question
            del st.session_state.correct_answers
            del st.session_state.feedback
            del st.session_state.questions

# Main script to run the quiz
if __name__ == "__main__":
    quiz()
import random
from difflib import SequenceMatcher
import streamlit as st

# Glossary dictionary containing terms and definitions
glossary = {
    "Weather": "The condition of the atmosphere at a particular place and time, including temperature, precipitation, humidity, and wind.",
    "Climate": "The average weather conditions of a place over a long period, typically 30 years.",
    "Stevenson Screen": "A white, louvered box used to house weather instruments, protecting them from direct sunlight and precipitation while allowing air circulation.",
    "Rain Gauge": "An instrument used to measure the amount of precipitation over a specific period.",
    "Maximum-Minimum Thermometer": "A device that records the highest and lowest temperatures in a day.",
    "Wet-and-Dry Bulb Thermometer (Hygrometer)": "An instrument used to measure relative humidity by comparing the temperatures of a wet bulb and a dry bulb.",
    "Sunshine Recorder": "A device used to measure the duration of sunshine over a given period.",
    "Barometer": "An instrument that measures atmospheric pressure, useful for weather prediction.",
    "Anemometer": "An instrument used to measure wind speed.",
    "Wind Vane": "A device used to determine wind direction.",
    "Cloud Cover": "The amount of the sky covered by clouds, measured in oktas.",
    "Equatorial Climate": "A hot and humid climate typically found near the equator, characterised by high rainfall and little temperature variation throughout the year.",
    "Hot Desert Climate": "A dry climate with high daytime temperatures and cooler nights, characterised by minimal rainfall.",
    "Tropical Rainforest Ecosystem": "A dense forest ecosystem found in equatorial regions, with high biodiversity, consistent warm temperatures, and high rainfall.",
    "Hot Desert Ecosystem": "An ecosystem featuring sparse vegetation, extreme temperatures, and minimal rainfall.",
    "Convectional Rainfall": "Rainfall caused by intense heating of the Earth's surface, leading to the rapid rise of warm air and the formation of clouds.",
    "Relief Rainfall": "Rainfall caused when moist air is forced over a mountain range, cooling and condensing into precipitation.",
    "Latitude": "The distance of a location from the equator, which influences temperature and climate.",
    "Pressure Systems": "Large-scale patterns of high and low pressure that influence weather and climate, such as the Intertropical Convergence Zone (ITCZ).",
    "Winds": "Movements of air caused by differences in pressure, which influence weather and climate patterns.",
    "Distance from the Sea": "A factor affecting climate, where areas closer to the sea have milder temperatures and more consistent rainfall.",
    "Altitude": "The height above sea level, which affects temperature, with higher altitudes generally being cooler.",
    "Ocean Currents": "Large-scale movements of seawater that affect climate, such as the Gulf Stream.",
    "Climate Graph": "Visual representation of temperature and rainfall data, typically shown as a combined bar and line graph.",
    "Soil": "The upper layer of the Earth, influenced by climate and natural vegetation.",
    "Biodiversity": "The variety of plant and animal life in a particular ecosystem, such as a tropical rainforest.",
    "Wildlife": "Animals living in their natural environment, adapted to specific climatic and vegetative conditions.",
    "Global Effects of Deforestation": "Impacts such as climate change, loss of biodiversity, and disruption of global carbon cycles.",
    "Tropical Effects of Deforestation": "Specific issues such as soil erosion, changes in water cycles, and loss of habitat for wildlife."
}

# Helper function to calculate similarity ratio
def similarity_ratio(user_answer, correct_answer):
    return SequenceMatcher(None, user_answer, correct_answer).ratio()

# Main quiz function
def quiz():
    st.title("IGCSE Geography A*")
    st.subheader("Glossary for Weather, Climate & Vegetation 2.4 - 2.5")

    # Initialize session state
    if "current_question" not in st.session_state:
        st.session_state.current_question = 0
        st.session_state.correct_answers = 0
        st.session_state.feedback = []
        st.session_state.questions = list(glossary.keys())
        random.shuffle(st.session_state.questions)

    total_questions = len(st.session_state.questions)

    # Progress bar
    st.progress(st.session_state.current_question / total_questions)

    if st.session_state.current_question < total_questions:
        term = st.session_state.questions[st.session_state.current_question]
        st.subheader(f"What is the definition of '{term}'?")
        user_answer = st.text_area("Your answer:", key=f"answer_{st.session_state.current_question}").strip().lower()

        if st.button("Submit"):
            correct_answer = glossary[term].strip().lower()
            accuracy = similarity_ratio(user_answer, correct_answer)

            if accuracy >= 0.85:
                st.success("Correct!")
                st.session_state.correct_answers += 1
            else:
                st.error(f"Incorrect. The correct definition is: {glossary[term]}")
                st.session_state.feedback.append(term)

            st.session_state.current_question += 1

    else:
        st.header("Quiz Completed!")
        st.write(f"You got {st.session_state.correct_answers} out of {total_questions} questions right.")

        if st.session_state.feedback:
            st.subheader("Things to improve:")
            for item in st.session_state.feedback:
                st.write(f"- {item}")

        # Reset button
        if st.button("Restart Quiz"):
            del st.session_state.current_question
            del st.session_state.correct_answers
            del st.session_state.feedback
            del st.session_state.questions

# Main script to run the quiz
if __name__ == "__main__":
    quiz()
