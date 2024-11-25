import streamlit as st

# Set page layout to wide
st.set_page_config(layout="wide")

# Initialize a session state to hold the entered text
if "submitted_text" not in st.session_state:
    st.session_state.submitted_text = ""

# Add vertical space to push the form to the bottom
st.markdown("<div style='height: 70vh;'></div>", unsafe_allow_html=True)

# Display the entered text above the input box if it exists
if st.session_state.submitted_text:
    st.write("You entered:", st.session_state.submitted_text)

# Use a form for input and submission
with st.form("my_form"):
    # Create a horizontal layout for the input and button
    col1, col2 = st.columns([3, 1])  # Adjust column proportions if needed

    with col1:
        text_input = st.text_input(
            label="Enter some text", 
            label_visibility="visible", 
            placeholder="Type here..."
        )

    with col2:
        st.markdown(
            """
            <style>
            div.stButton > button:first-child {
                margin-top: 18px;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        submit_button = st.form_submit_button(label="Submit")

# Update the session state if the form is submitted
if submit_button:
    st.session_state.submitted_text = text_input
