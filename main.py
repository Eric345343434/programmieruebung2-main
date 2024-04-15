import streamlit as st

# Eine Überschrift der ersten Ebene
st.write("# EKG APP")
if "current-user" not in st.session_state:
    st.session_state.current_user ="None"

# Eine Überschrift der zweiten Ebene
st.write("## Versuchsperson auswählen")

# Eine Auswahlbox, das Ergebnis wird in current_user gespeichert
st.session_state.current_user = st.selectbox(
    'Versuchsperson',
    options = ["Nutzer1", "Nutzer2"], key="sbVersuchsperson")

st.write(st.session_state.current_user,"wird zurzeit gewählt")