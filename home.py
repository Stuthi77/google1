import streamlit as st

# Set page configuration at the very top
st.set_page_config(layout="wide")

# Initialize session state variables
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'show_learning_page' not in st.session_state:
    st.session_state.show_learning_page = False
if 'show_quiz_page' not in st.session_state:
    st.session_state.show_quiz_page = False
if 'submitted_text' not in st.session_state:
    st.session_state.submitted_text = ""

def main():
    if st.session_state.show_learning_page:
        learning_page()
    elif st.session_state.show_quiz_page:
        quiz_page()
    else:
        home()

def home():
    st.title("Welcome to the Learning Platform")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Start Quiz"):
            st.session_state.show_quiz_page = True
            st.experimental_rerun()  # Rerun to switch to the quiz page

    with col2:
        if st.button("Start Learning"):
            st.session_state.show_learning_page = True
            st.experimental_rerun()  # Rerun to switch to the learning page

def quiz_page():
    # Add a "Back to Home" button
    if st.button("Back to Home"):
        st.session_state.show_quiz_page = False
        st.experimental_rerun()  # Rerun to go back to the home page

    # Add a heading for the quiz page
    st.title("Quiz Started")

    # Add placeholder for quiz logic
    st.write("This is where the quiz will take place. Add your quiz questions here.")

def learning_page():
    # Create a container for the top-right "Back to Home" button
    st.markdown(
        """
        <style>
        .top-right-button {
            position: absolute;
            top: 10px;
            right: 10px;
            z-index: 1;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Place the "Back to Home" button using custom CSS
    back_button_container = st.container()
    with back_button_container:
        back_to_home = st.button("Back to Home", key="back_to_home")
        if back_to_home:
            st.session_state.show_learning_page = False
            st.experimental_rerun()

    # Add vertical space to push the form to the bottom
    st.markdown("<div style='height: 70vh;'></div>", unsafe_allow_html=True)

    # Display the entered text above the input box if it exists
    if st.session_state.submitted_text:
        st.write("**You:**", st.session_state.submitted_text)
        if st.session_state.submitted_text.lower() == "hi":
            bot_response = {
                "generated_content": (
                    "Hi there! I'm ready to help your students with a quiz. To get started, please tell me:\n\n"
                    "1. What topic should the quiz cover?\n"
                    "2. How many questions should the quiz have in total?\n"
                    "3. How many multiple-choice questions (MCQs) and how many subjective (short answer or essay) questions would you like?\n"
                    "4. What is the grade level of your students?\n"
                    "5. What difficulty level are you aiming for (easy, medium, hard)?\n"
                )
            }
            st.write("**Bot:**", bot_response["generated_content"])
        else:
            st.write("**Bot:**", "I'm here to assist you!")

    # Input form for text and submission
    with st.form("my_form"):
        # Create a horizontal layout for text input and submit button
        col1, col2 = st.columns([3, 1])
        with col1:
            text_input = st.text_input(
                label="Enter some text",
                label_visibility="visible",
                placeholder="Type here..."
            )
        with col2:
            # Add styling to align the button with the text box
            st.markdown(
                """
                <style>
                div.stButton > button:first-child {
                    margin-top: 18px;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
            submit_button = st.form_submit_button(label="Submit")

    # Update session state when the form is submitted
    if submit_button:
        st.session_state.submitted_text = text_input
        st.session_state.chat_history.append((text_input, "Bot's response"))

    # Display chat history
    if st.button("Show Chat History"):
        display_history()

def display_history():
    st.header("Chat History")
    for user_input, bot_response in st.session_state.chat_history:
        st.write("**You:**", user_input)
        st.write("**Bot:**", bot_response)

if __name__ == "__main__":
    main()
