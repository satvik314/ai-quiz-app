import sys
import streamlit as st
import os
import pysqlite3
from ai_components_quiz import create_ques_ans, report

sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]


def app():
    session_state = st.session_state

    if "quiz_data" not in session_state:
        session_state.quiz_data = None
    if "score" not in session_state:
        session_state.score = 0
    title_placeholder = st.empty()
    subheader = st.empty()
    topic_placeholder = st.empty()
    n_placeholder = st.empty()
    standard_placeholder = st.empty()

    title_placeholder.title("Inquiry Based Learning 📖")
    subheader.subheader("🤖 This AI App will help you learn through questions!")

    linkedin_url = "https://www.linkedin.com/in/satvik-paramkusham"
    st.markdown(f"Created by [Satvik]({linkedin_url})")

    topic = topic_placeholder.text_input("Enter the topic")

    standard = standard_placeholder.selectbox("Select the standard", ["Basic", "Intermediate", "Advanced"])
    n = n_placeholder.number_input("Number of questions", min_value=1, max_value=25, value=1, step=1)

    if st.button("Generate"):
        st.empty()
        st.empty()
        with st.spinner(f"Generating Quiz "):
            session_state.quiz_data = create_ques_ans(n,topic, standard)

    if session_state.quiz_data:
        questions = session_state.quiz_data[0]
        options = session_state.quiz_data[1]
        answers = session_state.quiz_data[2]

    ans = []
    if session_state.quiz_data:
        with st.form(key='quiz'):
            question_placeholders = []
            for i, quest in enumerate(questions):
                st.write(f"{i + 1}. {quest}")
                question_placeholder = st.empty()
                question_placeholders.append(question_placeholder)
                options_ = options[i]

                choice = st.radio("", options_, key=i)
                if choice:
                    ans.append(choice)
                st.divider()
            if session_state.quiz_data:
                submitted = st.form_submit_button("Submit")
            else:
                submitted = False
            if submitted:
                session_state.score = 0
                for i, user_input in enumerate(answers):
                    question_placeholder = question_placeholders[i]
                    if ans[i] == user_input:
                        session_state.score += 1
                        question_placeholder.success("Correct  Answer!")
                    if ans[i] != user_input:
                        question_placeholder.error(f" Wrong! , right answer is {answers[i]}")
                st.success("Test Score - " + str(session_state.score))
                with st.spinner(f"Generating Quiz "):
                    st.success(f"{report([questions, ans], session_state.score, len(answers))}")
        if session_state.quiz_data:
            new_quiz = st.button("new quiz")
            if new_quiz:
                session_state.quiz_data = None
                session_state.score = 0
                st.experimental_rerun()


app()
