import streamlit as st
import pandas as pd


def render_account_page():

    if st.session_state.current_user is None:
        login_tab, signup_tab = st.tabs(["Log in", "Sign up"])

        with login_tab:
            email = st.text_input("Email", key="login_email")
            password = st.text_input("Password", type="password", key="login_password")

            if st.button("Log in", key="login_btn"):
                users = st.session_state.users
                if email in users and users[email]["password"] == password:
                    st.session_state.current_user = email
                    st.success(f"Logged in as {email}")
                    st.rerun()
                else:
                    st.error("Invalid email or password.")

        with signup_tab:
            new_email = st.text_input("New email", key="signup_email")
            new_password = st.text_input("New password", type="password", key="signup_password")

            if st.button("Create account", key="signup_btn"):
                if not new_email or not new_password:
                    st.warning("Please fill in both fields.")
                elif new_email in st.session_state.users:
                    st.warning("This account already exists.")
                else:
                    st.session_state.users[new_email] = {"password": new_password}
                    st.session_state.user_histories[new_email] = []
                    st.success("Account created. You can now log in.")

    else:
        user = st.session_state.current_user
        st.success(f"Logged in as {user}")

        c1, c2 = st.columns([1, 1])
        with c1:
            if st.button("Log out"):
                st.session_state.current_user = None
                st.rerun()

        with c2:
            if st.button("Clear my saved history"):
                st.session_state.user_histories[user] = []
                st.success("Saved history cleared.")

        st.markdown("### Saved search history")
        history = st.session_state.user_histories.get(user, [])

        if not history:
            st.info("No saved searches yet.")
        else:
            hist_df = pd.DataFrame(history)
            st.dataframe(hist_df, use_container_width=True, hide_index=True)