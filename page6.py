import streamlit as st
from ai_components1 import create_ques_ans, report
import json
from students import student

stud = student()


def app():
    session_state = st.session_state

    if "quiz_data" not in session_state:
        session_state.quiz_data = None
    if "score" not in session_state:
        session_state.score = 0
    title_placeholder = st.empty()
    subheader = st.empty()
    # board_placeholder = st.empty()
    # class_placeholder = st.empty()
    # subject_placeholder = st.empty()
    # lesson_placeholder = st.empty()
    # button2 = st.empty()
    topic_placeholder = st.empty()
    n_placeholder = st.empty()
    standard_placeholder = st.empty()
    # button = st.empty()

    with open('Syllabus1.json', 'r') as f:
        data = json.load(f)

    # if stud.get_board() == None or stud.get_lesson() == None or stud.get_std() == None or stud.get_subject() == None:
    title_placeholder.title("Welcome to AI Quiz Generator!")
    subheader.subheader("Test your knowledge on your choice of topic.")
    # board_names = [board["name"] for board in data["boards"]]
    # board = board_placeholder.selectbox("select board which you are studying",board_names)
    # board = board_placeholder.text_input("Enter the board in which you are studying")
    # board_list = next((b for b in data["boards"] if b["name"] == board), None)

    # class_names = [Class["name"] for Class in board_list["classes"]]
    # class_names = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
    # classe = class_placeholder.selectbox("Select class in which you are studying", class_names)
    # classe_list= next((b for b in board_list["classes"] if b["name"]==classe) , None)

    # subject_names = [subject["name"] for subject in classe_list["subjects"]]
    # subject = subject_placeholder.selectbox("Select subject which you want to study now",subject_names)
    # subject = subject_placeholder.text_input("Enter the subject which you want to study!")
    # subject_list= next((b for b in classe_list["subjects"] if b["name"]==subject) , None)

    # lesson_names = [lesson["name"] for lesson in subject_list["lessons"]]
    # lesson = lesson_placeholder.selectbox("Select Lesson which you want to study now ",lesson_names)
    # lesson = lesson_placeholder.text_input("Enter lesson which you want to study.")

    topic = topic_placeholder.text_input("Enter the topic")

    standard = standard_placeholder.selectbox("select the standard", ["Basic", "Intermediate", "Advanced"])
    n = n_placeholder.number_input("Number of questions", min_value=1, max_value=25, value=1, step=1)

    # lesson_list= next((b for b in subject_list["lessons"] if b["name"]==lesson) , None)
    # if button2.button("Enter"):
    # stud.set_board(board)
    # stud.set_std(classe)
    # stud.set_subject(subject)
    # stud.set_lesson(lesson)
    #     board_placeholder.empty()
    #     class_placeholder.empty()
    #     subject_placeholder.empty()
    #     lesson_placeholder.empty()
    #     topic_placeholder.empty()
    #     standard_placeholder.empty()
    #     button2.empty()
# if stud.get_board() != None and stud.get_lesson() != None and stud.get_std() != None and stud.get_subject() != None:
    # title_placeholder.header(f"You are studying {stud.get_lesson()} chapter")
    # st.subheader(f"Where do you want to test your knowledge")
    # board_list = next((b for b in data["boards"] if b["name"] == stud.get_board()), None)
    # classe_list= next((b for b in board_list["classes"] if b["name"] == stud.get_std()) , None)
    # subject_list= next((b for b in classe_list["subjects"] if b["name"] == stud.get_subject()) , None)
    # lesson_list= next((b for b in subject_list["lessons"] if b["name"] == stud.get_lesson()) , None)

    # st.sidebar.metric(label="Board", value=stud.get_board())
    # st.sidebar.metric(label="Standard", value=stud.get_std())

    # topic = topic_placeholder.text_input("Enter the topic")
    # standard = standard_placeholder.selectbox("select the standard", ["Basic", "Intermediate", "Advanced"])
    # n = n_placeholder.number_input("Number of questions", min_value=1, max_value=25, value=1, step=1)
    if st.button("Generate"):
        st.empty()
        st.empty()
        with st.spinner(f"Generating Quiz "):
            session_state.quiz_data = create_ques_ans(n, topic, standard)

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
