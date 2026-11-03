import streamlit as st

st.set_page_config(
    page_title="FreeTik",
    page_icon="🚀",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: #080810;
    color: white;
}
h1 {
    color: #fe2c55;
}
</style>
""", unsafe_allow_html=True)

st.title("🚀 FreeTik")
st.subheader("Your Free TikTok Growth Platform")

if "points" not in st.session_state:
    st.session_state.points = 100

if "username" not in st.session_state:
    st.session_state.username = ""

username = st.text_input(
    "Enter your TikTok username",
    placeholder="@username"
)

if st.button("Join FreeTik"):

    if username.strip():

        st.session_state.username = username
        st.success("Welcome to FreeTik!")

if st.session_state.username:

    st.divider()

    st.header("Your Dashboard")

    st.write(
        f"Welcome, {st.session_state.username}"
    )

    st.metric("FreeTik Points",
              st.session_state.points)

    st.subheader("🎯 Your Growth Targets")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Follower Target", "5,000")

    with col2:
        st.metric("Like Promotion", "Available")

    st.progress(
        min(st.session_state.points / 5000, 1.0)
    )

    st.subheader("🏆 Earn Rewards")

    if st.button("Complete Creator Challenge"):

        st.session_state.points += 50

        st.success("50 points earned!")

    st.subheader("💎 Rewards")

    st.write(
        "Use your points towards eligible "
        "creator-promotion opportunities."
    )

st.divider()

st.caption("FreeTik © 2026")