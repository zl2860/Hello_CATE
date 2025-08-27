# 🧬 CATE Calculator - H. pylori Eradication

A modern, geek-style Streamlit application for calculating Conditional Average Treatment Effects (CATE) scores for H. pylori eradication treatment based on genetic profiles.

## 🚀 Features

### 🧮 Single Prediction
- **Interactive SNP Selection**: Choose genotypes for each SNP with a modern card-based interface
- **Real-time Calculation**: Instant CATE score calculation with visual feedback
- **Detailed Results**: Comprehensive breakdown of individual SNP contributions
- **Beautiful Visualizations**: Modern gauge charts and result displays

### 📊 Batch Processing
- **CSV Upload**: Process multiple individuals at once
- **Template Download**: Get sample CSV templates for easy data preparation
- **Results Export**: Download processed results as CSV
- **Progress Tracking**: Visual progress indicators for batch operations

### 📈 Data Analysis
- **SNP Overview**: Comprehensive statistics for all SNPs
- **Chromosome Distribution**: Visual representation of SNP distribution across chromosomes
- **Weight Analysis**: Statistical analysis of SNP weights and their distributions
- **Gene Pathway Insights**: Analysis of SNPs by associated genes

## 🎨 Geek-Style UI Features

- **Modern Gradient Design**: Beautiful color gradients and modern aesthetics
- **Interactive Cards**: Hover effects and smooth animations
- **Responsive Layout**: Optimized for all screen sizes
- **Professional Typography**: Clean, readable fonts and spacing
- **Visual Feedback**: Smooth transitions and hover effects

## 🧬 SNP Data

The app uses real SNP data extracted from `CATE_tables_0825.xlsx` with the following information:
- **11 SNPs** across multiple chromosomes
- **Genotype-specific weights** for REF, HET, and ALT alleles
- **Gene associations** and chromosomal positions
- **Clinical relevance** for H. pylori eradication treatment

## 📋 Requirements

```bash
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
plotly>=5.0.0
openpyxl>=3.0.0
```

## 🚀 Installation & Usage

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
streamlit run streamlit_app.py
```

### 3. Access the App
Open your browser and navigate to `http://localhost:8501`

## 📁 File Structure

```
CATE_predict_streamlit/
├── streamlit_app.py          # Main Streamlit application
├── snps_data.json           # Extracted SNP data from Excel
├── extract_snps.py          # Script to extract SNP data from Excel
├── CATE_tables_0825.xlsx    # Original Excel data source
├── requirements.txt          # Python dependencies
├── README.md                # This documentation
└── h_pylori_cate_sample.csv # Sample data template
```

## 🧬 How It Works

### CATE Score Calculation
The CATE score is calculated by summing the weighted contributions of each SNP based on the individual's genotype:

```
CATE Score = Σ(SNP_weight[genotype] for each SNP)
```

### Genotype Coding
- **0 (REF)**: Homozygous reference allele
- **1 (HET)**: Heterozygous (one reference, one alternate)
- **2 (ALT)**: Homozygous alternate allele

### Score Interpretation
- **< -0.5**: Strong predicted benefit from H. pylori eradication 🟢
- **-0.5 to 0**: Moderate predicted benefit from H. pylori eradication 🟡
- **0 to 0.5**: Neutral predicted effect of H. pylori eradication 🟠
- **> 0.5**: Limited predicted benefit from H. pylori eradication 🔴

## 📊 Data Input Format

### Single Prediction
Use the interactive interface to select genotypes for each SNP.

### Batch Processing
Upload a CSV file with the following format:
```csv
ID,rs10762496,rs7894516,rs17773251,...
Sample1,0,1,2,...
Sample2,1,0,1,...
```

## 🔬 Scientific Background

This tool assesses individualized benefits of H. pylori eradication for gastric cancer prevention using genetic profiles. Scores synthesize conditional average treatment effects (CATE) based on metaboQTLs from research studies.

**Important**: This tool is intended for healthcare professionals. Use for research purposes requires institutional approval.

## 🎯 Use Cases

- **Clinical Research**: Individualized treatment benefit assessment
- **Genetic Counseling**: Patient-specific risk evaluation
- **Population Studies**: Large-scale genetic analysis
- **Medical Education**: Understanding genetic treatment effects

## 🚧 Troubleshooting

### Common Issues
1. **SNP data not loading**: Ensure `snps_data.json` exists and is properly formatted
2. **Import errors**: Install all required dependencies with `pip install -r requirements.txt`
3. **Port conflicts**: Use `--server.port` flag to specify a different port

### Support
For technical issues or questions about the application, please check the error logs or contact the development team.

## 📄 License

© 2025 Peking University Cancer Hospital Department of Cancer Epidemiology. All rights reserved.

This tool is intended for healthcare professionals. Use for research purposes requires institutional approval.

## �� Updates

- **v2.0**: Complete redesign with geek-style UI and enhanced functionality
- **v1.0**: Basic CATE calculator functionality

---

*Built with ❤️ using Streamlit, Plotly, and modern web technologies*
