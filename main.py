import streamlit as st

st.set_page_config(page_title="SST Trading Suite", layout="wide", page_icon="📈")

# --- LEDENLIJST ---
USERS = {
    "admin@swingstocktraders.com": "SST2024!",
    "member@test.nl": "Welkom01"
}

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Login Scherm
if not st.session_state.logged_in:
    st.markdown("<h2 style='text-align: center;'>🔐 SST Premium Login</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        email = st.text_input("E-mailadres")
        password = st.text_input("Wachtwoord", type="password")
        if st.button("Inloggen", use_container_width=True):
            if email in USERS and USERS[email] == password:
                st.session_state.logged_in = True
                st.session_state.user_email = email
                st.rerun()
            else:
                st.error("Onjuiste gegevens")
else:
    # Navigatie Menu
    pg = st.navigation({
        "Dagelijkse Focus": [
            st.Page("pagina_morningcall.py", title="Morning Call", icon="☕"),
        ],
        "Analyse Tools": [
            st.Page("pagina_analyzer.py", title="Signal Analyzer", icon="📊"),
            st.Page("pagina_terminal.py", title="AI Strategy Terminal", icon="🤖"),
        ]
    })
    
    # Sidebar Logout
    with st.sidebar:
        st.write(f"👤 {st.session_state.user_email}")
        if st.button("Uitloggen"):
            st.session_state.logged_in = False
            st.rerun()
            

    pg.run()
