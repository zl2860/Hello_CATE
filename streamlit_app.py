#!/usr/bin/env python3
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# ------------------- Page Config -------------------
st.set_page_config(
    page_title="CATEcalc: <i>H. pylori</i> Eradication Benefit Estimator",
    layout="wide"
)

# ------------------- SNP Data -------------------
@st.cache_data
def load_snp_data():
    return [
        {'rsid': "rs10762496", 'weights': [-0.140, -0.046, 0.247], 'chr': "10", 'pos': "73701004", 'ref': "G", 'alt': "A", 'gene': "ANAPC16", 'eaf': 0.30, 'pathways': "Cell cycle"},
        {'rsid': "rs7894516", 'weights': [-0.015, -0.197, -0.265], 'chr': "10", 'pos': "73729650", 'ref': "C", 'alt': "A", 'gene': "ANAPC16", 'eaf': 0.17, 'pathways': "Cell cycle"},
        {'rsid': "rs17773251", 'weights': [-0.100, 0.187, 0.068], 'chr': "13", 'pos': "37678884", 'ref': "G", 'alt': "C", 'gene': "CSNK1A1L", 'eaf': 0.04, 'pathways': "Gastric cancer | Wnt signaling pathway"},
        {'rsid': "rs9975448", 'weights': [-0.152, -0.103, 0.115], 'chr': "21", 'pos': "34626855", 'ref': "G", 'alt': "A", 'gene': "IFNAR2", 'eaf': 0.45, 'pathways': "PI3K-Akt signaling pathway"},
        {'rsid': "rs368403298", 'weights': [-0.053, -0.236, -0.380], 'chr': "5", 'pos': "112710688", 'ref': "C", 'alt': "A", 'gene': "MCC", 'eaf': 0.09, 'pathways': "Wnt signaling pathway"},
        {'rsid': "rs877447", 'weights': [0.059, -0.077, -0.276], 'chr': "17", 'pos': "64626533", 'ref': "C", 'alt': "T", 'gene': "PRKCA", 'eaf': 0.48, 'pathways': "Wnt signaling pathway | PI3K-Akt signaling pathway | MAPK signaling pathway"},
        {'rsid': "rs142784890", 'weights': [-0.032, -0.279, -0.180], 'chr': "3", 'pos': "54498494", 'ref': "T", 'alt': "C", 'gene': "CACNA2D3", 'eaf': 0.14, 'pathways': "MAPK signaling pathway"},
        {'rsid': "rs4969266", 'weights': [-0.140, -0.089, 0.026], 'chr': "17", 'pos': "78761546", 'ref': "T", 'alt': "C", 'gene': "RPTOR", 'eaf': 0.49, 'pathways': "PI3K-Akt signaling pathway"},
        {'rsid': "rs7860304", 'weights': [-0.045, -0.217, -1.925], 'chr': "9", 'pos': "139819398", 'ref': "C", 'alt': "T", 'gene': "TRAF2", 'eaf': 0.12, 'pathways': "MAPK signaling pathway"},
        {'rsid': "rs6887323", 'weights': [0.003, -0.155, -0.089], 'chr': "5", 'pos': "170848124", 'ref': "G", 'alt': "A", 'gene': "FGF18", 'eaf': 0.41, 'pathways': "Gastric cancer | PI3K-Akt signaling pathway | MAPK signaling pathway"},
        {'rsid': "rs12806363", 'weights': [0.015, -0.089, -0.189], 'chr': "11", 'pos': "64138447", 'ref': "G", 'alt': "A", 'gene': "RPS6KA4", 'eaf': 0.46, 'pathways': "MAPK signaling pathway"}
    ]

def get_interpretation(score, threshold=0.806):
    if score >= threshold:
        return "Highly beneficial from <i>H. pylori</i> eradication"
    return "Moderately beneficial from <i>H. pylori</i> eradication"

# ------------------- Academic Header -------------------
# Convert image to base64 for embedding in HTML
import base64
with open("kitty_icon.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()

st.markdown(
    f"""<div style="background: linear-gradient(90deg, #1e3a8a, #1e40af); padding: 1.5rem 2rem; color: white; box-shadow: 0 2px 6px rgba(0,0,0,0.3);">
        <h1 style="margin:0; font-size:2rem; font-weight:800; color:white;">
            <img src="data:image/png;base64,{encoded_string}" alt="Hello Kitty" style="width:80px; height:80px; vertical-align:middle; margin-right:10px;">
            Hello CATE
        </h1>
        <p style="margin:0.3rem 0 0; font-size:1rem; opacity:0.95;">
            Welcome to our personalized prediction tool! This is a genotype-specific <b>C</b>onditional <b>A</b>verage <b>T</b>reatment <b>E</b>ffect Calculator for <i>H. pylori</i> Eradication, designed to predict individualized preventive benefit of <i>H. pylori</i> treatment for gastric cancer prevention.
        </p>
        <p style="margin:0.6rem 0 0; font-size:0.85rem; line-height:1.3; opacity:0.9;">
            <b>For more information please see our manuscript:</b><br>
            <i>Host genetic profiles enable personalized assessment on benefit of <i><i>Helicobacter pylori</i></i> eradication
            for targeted gastric cancer prevention: an exploratory post-hoc analysis of two randomized trials</i>
        </p>
        <p style="margin:1rem 0 0; font-size:0.85rem; line-height:1.4; opacity:0.95;">
            Zong-Chao Liu<sup>†,1</sup>, Yu-Xin Wang<sup>†,1</sup>, Heng-Min Xu<sup>†,1</sup>, 
            Xuan Han<sup>1</sup>, Hui Ma<sup>1</sup>, Yang Zhang<sup>2</sup>, 
            Jing-Ying Zhang<sup>2</sup>, Tong Zhou<sup>2</sup>, Wei-Cheng You<sup>2</sup>, 
            Kai-Feng Pan<sup>1,*</sup>, Wen-Qing Li<sup>1,*</sup>
        </p>
        <p style="margin:0.5rem 0 0; font-size:0.8rem; opacity:0.85;">
            <sup>†</sup>These authors contributed equally to the study | 
            <sup>*</sup>Corresponding authors <br>
            E-mail: <a href="mailto:wenqing_li@bjmu.edu.cn" style="color:#bfdbfe;">wenqing_li@bjmu.edu.cn</a> (W.-Q. Li); 
            <a href="mailto:pan-kf@263.net" style="color:#bfdbfe;">pan-kf@263.net</a> (K.-F. Pan)
        </p>
        <p style="margin:0.8rem 0 0; font-size:0.75rem; line-height:1.3; opacity:0.8;">
            1 State Key Laboratory of Holistic Integrative Management of Gastrointestinal Cancers, 
            Department of Cancer Epidemiology, Peking University Cancer Hospital & Institute, Beijing 100142, China <br>
            2 Key Laboratory of Carcinogenesis and Translational Research (Ministry of Education/Beijing), 
            Department of Cancer Epidemiology, Peking University Cancer Hospital & Institute, Haidian District, Beijing 100142, China
        </p>
    </div>""",
    unsafe_allow_html=True
)

# ------------------- SNP Card Renderer -------------------
def render_snp_card(snp):
    st.markdown(f"""
    <div style="
        background: #f9fafb;
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        padding: 0.8rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08);
        margin-bottom: 0.8rem;">
        <div style="font-weight:600; font-size:0.9rem; color:#1e3a8a;">{snp['rsid']}</div>
        <div style="font-size:0.75rem; color:#6b7280;">Chr{snp['chr']}:{snp['pos']}</div>
        <div style="font-size:0.75rem; color:#2563eb; margin-bottom:0.2rem;">{snp['gene']}</div>
        <div style="font-size:0.7rem; color:#475569;">REF: {snp['ref']} | ALT: {snp['alt']}</div>
        <div style="font-size:0.7rem; color:#059669; margin-top:0.2rem;">EAF: {snp['eaf']}</div>
        <div style="font-size:0.65rem; color:#7c3aed; margin-top:0.1rem;">{snp['pathways']}</div>
    </div>
    """, unsafe_allow_html=True)

    genotype = st.radio(
        f"Genotype for {snp['rsid']}",
        options=[0, 1, 2],
        format_func=lambda x: f"Hom Ref ({snp['ref']}/{snp['ref']})" if x == 0
                            else f"Heterozygous ({snp['ref']}/{snp['alt']})" if x == 1
                            else f"Hom Alt ({snp['alt']}/{snp['alt']})",
        key=f"snp_{snp['rsid']}",
        horizontal=True,
        label_visibility="collapsed"
    )
    return snp['rsid'], genotype

# ------------------- Main Layout -------------------
snp_data = load_snp_data()
col_left, col_right = st.columns([2, 1], gap="large")

with col_left:
    st.subheader("SNP Selection")
    
    # Add genotype legend for clarity
    st.markdown("""
    <div style="background:#f0f9ff; border:1px solid #0ea5e9; border-radius:6px; padding:0.8rem; margin-bottom:1rem;">
        <p style="margin:0; font-size:0.9rem; color:#0c4a6e; font-weight:600;">📋 Genotype Selection Guide:</p>
        <ul style="margin:0.3rem 0 0; font-size:0.8rem; color:#0c4a6e;">
            <li><b>Hom Ref</b> = Homozygous for the reference allele (e.g., A/A)</li>
            <li><b>Heterozygous</b> = One reference + one alternate allele (e.g., A/G)</li>
            <li><b>Hom Alt</b> = Homozygous for the alternate allele (e.g., G/G)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if 'genotypes' not in st.session_state:
        st.session_state.genotypes = {}

    for i in range(0, len(snp_data), 3):
        cols = st.columns(3)
        for j, snp in enumerate(snp_data[i:i+3]):
            with cols[j]:
                rsid, gt = render_snp_card(snp)
                st.session_state.genotypes[rsid] = gt

    if st.button("Calculate Score", use_container_width=True):
        if len(st.session_state.genotypes) == len(snp_data):
            score = -sum(
                snp['weights'][st.session_state.genotypes[snp['rsid']]]
                for snp in snp_data
            )
            st.session_state.score = score
        else:
            st.error("Please select genotypes for all SNPs.")

with col_right:
    st.subheader("Prediction Results")
    if 'score' in st.session_state:
        score = st.session_state.score
        interpretation = get_interpretation(score)
        st.markdown(f"""
        <div style="background:#eff6ff; border:1px solid #bfdbfe; border-radius:8px; padding:1rem; margin-bottom:1rem;">
            <h3 style="margin:0; color:#1e3a8a;">Predicted CATE Score: {score:.3f}</h3>
            <p style="margin:0.3rem 0 0; color:#1f2937; font-weight:500;">Interpretation: {interpretation}</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info("Select genotypes and calculate the score to see results.")

    st.subheader("Notes on Interpretation")
    st.markdown("""
    <div style="background:#fefce8; border:1px solid #fde68a; border-radius:8px; padding:1rem; margin-bottom:1rem;">
        <ul style="font-size:0.85rem; color:#78350f; margin:0;">
            <li>Scores <b>≥ 0.806</b> indicate <b>highly beneficial</b> predicted response to <i>H. pylori</i> eradication.</li>
            <li>Scores <b>&lt; 0.806</b> indicate <b>moderately beneficial</b> predicted response.</li>
            <li><b>Important:</b> This is a <b>genotype-based benefit score</b> derived from genetic markers, and population characteristics, clinical factors, and individual patient context should be considered for final decision making.</li>
            <li>This tool is for <b>exploratory research</b> and <b>professional interpretation</b>. Clinical application requires validation.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # ------------------- Batch Prediction -------------------
    st.subheader("Batch Prediction")
    uploaded_file = st.file_uploader("Upload CSV with genotypes", type=['csv'])
    if st.button("Process File", use_container_width=True):
        if not uploaded_file:
            st.error("Upload a CSV file first.")
        else:
            try:
                batch_df = pd.read_csv(uploaded_file)
                required_cols = ['ID'] + [snp['rsid'] for snp in snp_data]
                if not all(col in batch_df.columns for col in required_cols):
                    st.error("CSV missing required SNP columns.")
                else:
                    st.success("Processing file...")
                    progress = st.progress(0)
                    results = []
                    for i, row in batch_df.iterrows():
                        score = -sum(snp['weights'][row[snp['rsid']]] for snp in snp_data)
                        results.append({'ID': row['ID'], 'Score': score, 'Interpretation': get_interpretation(score)})
                        progress.progress((i+1)/len(batch_df))
                    results_df = pd.DataFrame(results)
                    st.dataframe(results_df.style.format({'Score': '{:.3f}'}), height=200)
                    st.download_button(
                        "Download Results",
                        results_df.to_csv(index=False).encode('utf-8'),
                        f"cate_results_{datetime.now().strftime('%Y%m%d')}.csv",
                        "text/csv",
                        use_container_width=True
                    )
            except Exception as e:
                st.error(f"Error: {e}")

    # Sample CSV
    if snp_data:
        sample_df = pd.DataFrame([{'ID': 'sample1', **{snp['rsid']: np.random.choice([0,1,2]) for snp in snp_data}}])
        st.download_button(
            "Download Sample CSV",
            sample_df.to_csv(index=False).encode('utf-8'),
            "sample_genotypes.csv",
            "text/csv",
            use_container_width=True
        )

# ------------------- Footer -------------------
st.markdown("""
<div style="text-align:center; margin-top:2rem; font-size:0.8rem; color:#6b7280;">
    © 2025 Peking University Cancer Hospital, Department of Cancer Epidemiology.  
    For research use only. Clinical application requires institutional approval.
</div>
""", unsafe_allow_html=True)