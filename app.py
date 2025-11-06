import streamlit as st
from mirrornet import mirror_explain
from hallucinet import hallucination_risk

st.title("MirrorNet Demo")

tab1, tab2 = st.tabs(["MirrorNet", "Hallucinet"])

with tab1:
    text = st.text_area("Enter text:")
    if st.button("Analyze Compression"):
        result = mirror_explain(text)
        st.write(result)

with tab2:
    q = st.text_input("Enter claim to check:")
    if st.button("Check Hallucination Risk"):
        result = hallucination_risk(q)
        st.write(result)
