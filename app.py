import streamlit as st
import random
import time

st.set_page_config(page_title="BioCompiler Glow", page_icon="🧬", layout="wide")
st.title("🧬 BioCompiler Glow")
st.subheader("Virtual Bio Lab for Students, Schools & Research Labs")
st.write("Simulate DNA, Proteins & Experiments — No physical lab needed.")

lab = st.sidebar.selectbox("Select Lab Module", ["DNA Transcriptor", "Protein Simulator", "PCR Lab", "School Dashboard"])

if lab == "DNA Transcriptor":
    st.header("🧬 DNA -> RNA -> Protein")
    dna = st.text_input("Enter DNA Sequence (A,T,C,G)", "ATGCGTAACTGG")
    if dna:
        rna = dna.replace("T","U")
        st.success(f"RNA: {rna}")
        if st.button("Run Transcription"):
            with st.spinner("Compiling DNA..."):
                time.sleep(2)
            st.balloons()
            st.write("✅ Transcription Complete!")

elif lab == "Protein Simulator":
    st.header("🔬 Protein Folding Simulator")
    protein_name = st.selectbox("Choose Protein", ["Insulin", "Hemoglobin", "CRISPR Cas9"])
    if st.button(f"Fold {protein_name}"):
        bar = st.progress(0)
        for i in range(100):
            time.sleep(0.02)
            bar.progress(i+1)
        st.success(f"{protein_name} folded! Stability: {random.randint(85,99)}%")

elif lab == "PCR Lab":
    st.header("🧪 Virtual PCR Machine")
    cycles = st.slider("PCR Cycles", 1, 40, 25)
    if st.button("Start PCR"):
        st.line_chart([random.randint(1,100) for _ in range(cycles)])
        st.success(f"DNA Amplified {2**cycles}x!")

else:
    st.header("🏫 School Dashboard")
    st.metric("Students Active Today", "1,247")
    st.metric("Experiments Run", "8,930")
    st.metric("Lab Cost Saved", "$34,500")