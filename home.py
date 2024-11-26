import streamlit as st
import requests

# Helper function to call the bot API
def call_bot_api(message):
    """
    Call the Flask backend API to get a response from the AI bot.
    """
    url = "http://127.0.0.1:5000/bot_chat"  # Replace with the actual backend URL
    payload = {"message": message}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=50)
        response.raise_for_status()
        return response.json().get("response", "No response from bot.")
    except requests.exceptions.Timeout:
        return "Error: The request timed out. Please try again later."
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Function to display the learning page with chat functionality
def learning_page():
    st.title("Chat with the Bot")

    # Initialize session state for chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Input form for user message
    with st.form("chat_form"):
        user_message = st.text_input("Enter your message:", placeholder="Type your message here")
        submit_button = st.form_submit_button("Send")

    if submit_button and user_message:
        # Call the bot API and get the response
        bot_response = call_bot_api(user_message)

        # Append the user message and bot response to the chat history
        st.session_state.chat_history.append({"sender": "You", "message": user_message})
        st.session_state.chat_history.append({"sender": "Bot", "message": bot_response})

    # Display the chat history
    if st.session_state.chat_history:
        st.write("### Chat History")
        for chat in st.session_state.chat_history:
            st.write(f"**{chat['sender']}:** {chat['message']}")

    # Add a "Back to Home" button
    if st.button("Back to Home"):
        st.session_state.page = "home"
        st.experimental_rerun()

# Function to display the quiz page
def quiz_page():
    st.title("Quiz Page")
    st.write("Answer the following questions:")

    # Example Quiz Questions
    question_1 = st.text_input("Question 1: What is the capital of France?")
    question_2 = st.text_input("Question 2: What is 2 + 2?")
    submit_quiz = st.button("Submit Quiz")

    if submit_quiz:
        # Example validation of answers
        score = 0
        if question_1.lower() == "paris":
            score += 1
        if question_2 == "4":
            score += 1

        st.write(f"Your score: {score}/2")
        st.success("Quiz completed! Well done!")

    # Add a "Back to Home" button
    if st.button("Back to Home"):
        st.session_state.page = "home"
        st.experimental_rerun()

# Main app function
def main():
    # Session state for navigation
    if "page" not in st.session_state:
        st.session_state.page = "home"

    # Navigation
    if st.session_state.page == "home":
        st.title("AI-Powered Quiz Assistant")
        st.write("Welcome to the quiz assistant. Choose an action below.")

        # Buttons for navigation
        if st.button("Start Learning"):
            st.session_state.page = "learning"
            st.experimental_rerun()

        if st.button("Start Quiz"):
            st.session_state.page = "quiz"
            st.experimental_rerun()

    elif st.session_state.page == "learning":
        learning_page()

    elif st.session_state.page == "quiz":
        quiz_page()

if __name__ == "__main__":
    main()
