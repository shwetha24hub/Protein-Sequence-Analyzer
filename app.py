
import streamlit as st
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import pandas as pd

st.set_page_config(page_title="Protein Analyzer", page_icon="🧬")

st.title("🧬 Protein Sequence Analyzer")
st.write("Analyze protein sequences using bioinformatics.")

protein = st.text_area(
    "Enter protein sequence",
    placeholder="Example: MKWVTFISLL"
)

if st.button("Analyze Protein"):

    protein = "".join(protein.upper().split())

    valid_amino_acids = set("ACDEFGHIKLMNPQRSTVWY")

    if not protein:
        st.error("Please enter a protein sequence.")

    elif any(aa not in valid_amino_acids for aa in protein):
        st.error("Invalid sequence! Use standard amino acid letters only.")

    else:
        analysis = ProteinAnalysis(protein)

        st.success("Protein analyzed successfully!")

        st.subheader("📊 Protein Properties")

        col1, col2 = st.columns(2)

        col1.metric("Protein Length", len(protein))
        col2.metric(
            "Molecular Weight",
            f"{analysis.molecular_weight():.2f} Da"
        )

        st.metric(
            "Theoretical Isoelectric Point (pI)",
            f"{analysis.isoelectric_point():.2f}"
        )

        st.subheader("🔬 Amino Acid Composition")

        composition = analysis.count_amino_acids()

        df = pd.DataFrame({
            "Amino Acid": list(composition.keys()),
            "Count": list(composition.values())
        })

        st.dataframe(df, hide_index=True)

        st.subheader("📈 Amino Acid Composition Chart")

        st.bar_chart(df.set_index("Amino Acid"))

st.caption("Built with Python, Biopython and Streamlit")
