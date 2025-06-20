import streamlit as st
import time
from CodeModel import generate_code
def app():
    st.header("CodeGenie: AI-Powered Code Generation")
    user_input = st.text_area(
        "Enter your text prompt below and click the button to submit."
    )

    with st.form("my_form"):
        submit = st.form_submit_button(label="Submit text prompt")

    if submit:
        with st.spinner(text="Generating code ... It may take some time."):
            code, start, end = generate_code(prompt=user_input)
            hours, rem = divmod(end - start, 3600)
            minutes, seconds = divmod(rem, 60)

            st.success(
                "Processing time: {:0>2}:{:0>2}:{:05.2f}.".format(
                    int(hours), int(minutes), seconds
                )
            )

        st.write(code)

    st.sidebar.markdown("## Guide")
    st.sidebar.info("This tool uses Code Llama to generate code from the provided prompt. It supports many of the most popular languages being typed.")
    st.sidebar.markdown("## Examples")
    st.sidebar.write("1. Give a function definition to see how the AI completes it.")
    st.sidebar.write("2. Try different prompts!")
app()
