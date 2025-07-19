import streamlit as st
import pandas as pd

st.set_page_config(page_title="Quiz App", page_icon="🧠")

st.title("🧠 Python Quiz App with Report")

# Questions and options
questions = {
    "What is the output of 2 ** 3?": ["6", "8", "9", "12"],
    "Which keyword is used to define a function in Python?": ["func", "def", "define", "function"],
    "What is the data type of [1, 2, 3]?": ["List", "Tuple", "Set", "Dictionary"],
    "Which operator is used for comparison in Python?": ["=", "==", "!=", "equals"],
    "What will be the output of bool(0)?": ["True", "False", "0", "None"]
}

correct_answers = {
    "What is the output of 2 ** 3?": "8",
    "Which keyword is used to define a function in Python?": "def",
    "What is the data type of [1, 2, 3]?": "List",
    "Which operator is used for comparison in Python?": "==",
    "What will be the output of bool(0)?": "False"
}

# Session state init
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "answers" not in st.session_state:
    st.session_state.answers = {q: None for q in questions}

with st.form("quiz_form"):
    for q, opts in questions.items():
        st.session_state.answers[q] = st.radio(
            q,
            opts,
            index=None,
            key=q
        )
    submitted = st.form_submit_button("Submit Quiz")

    if submitted:
        if None in st.session_state.answers.values():
            st.warning("⚠️ Please answer all questions before submitting.")
        else:
            st.session_state.submitted = True

# Report after submission
if st.session_state.submitted:
    report_data = []
    score = 0

    for q in questions:
        user_ans = st.session_state.answers[q]
        correct = correct_answers[q]
        is_correct = user_ans == correct
        if is_correct:
            score += 1

        report_data.append({
            "Question": q,
            "Your Answer": user_ans,
            "Correct Answer": correct,
            "Result": "✅ Correct" if is_correct else "❌ Wrong"
        })

    df_report = pd.DataFrame(report_data)

    st.markdown("### 📊 Quiz Report")
    st.dataframe(df_report, use_container_width=True)

    st.success(f"🎯 You scored **{score} out of {len(questions)}**")
    if score == len(questions):
        st.balloons()
