import os
import streamlit as st
import google.generativeai as genai

# Configure Google Generative AI
def configure_google_genai():
    api_key = os.getenv("GOOGLE_API_KEY")  # Ensure GOOGLE_API_KEY is set in your environment
    if not api_key:
        st.error("Google API Key is missing. Please set GOOGLE_API_KEY in your environment.")
        return False
    genai.configure(api_key=api_key)
    return True

# Helper function to interact with Google Generative AI
def call_generative_ai(prompt):
    try:
        # Start a chat session with Generative AI
        model = genai.GenerativeModel(
            model_name="gemini-1.5-pro",
            generation_config={
                "temperature": 1,
                "top_p": 0.95,
                "top_k": 40,
                "max_output_tokens": 512,
                "response_mime_type": "text/plain",
            },
        )
        chat_session = model.start_chat()
        response = chat_session.send_message(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error communicating with Generative AI: {e}")
        return None

# Streamlit Application
def main():
    st.title("Interactive Chat with Google Generative AI")

    # Step 1: Ensure API is configured
    if not configure_google_genai():
        st.stop()

    # Step 2: Chat Interface
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # User Input
    user_input = st.text_input("Enter your message:", placeholder="Type your query here...")
    if st.button("Send"):
        if user_input:
            st.session_state.chat_history.append({"sender": "You", "message": user_input})
            bot_response = call_generative_ai(user_input)
            if bot_response:
                st.session_state.chat_history.append({"sender": "Bot", "message": bot_response})

    # Display Chat History
    if st.session_state.chat_history:
        st.write("### Chat History")
        for chat in st.session_state.chat_history:
            st.write(f"**{chat['sender']}:** {chat['message']}")

    # Optional: Add a "Clear Chat" button
    if st.button("Clear Chat History"):
        st.session_state.chat_history = []

if __name__ == "__main__":
    main()
