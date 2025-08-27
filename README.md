# CATE Calculator for H. pylori Eradication

A Streamlit web application for calculating Conditional Average Treatment Effects (CATE) scores for H. pylori eradication treatment based on individual genetic profiles.

## Overview

This tool provides personalized prediction of H. pylori eradication benefit for gastric cancer prevention using genetic markers. The application implements a genotype-specific calculator that assesses individualized treatment response based on 11 Single Nucleotide Polymorphisms (SNPs) and their associated conditional average treatment effects.

## Features

### Individual Prediction
- Interactive SNP genotype selection interface
- Real-time CATE score calculation
- Comprehensive interpretation of results
- Detailed SNP information display including chromosomal position, genes, and pathways

### Batch Processing
- CSV file upload for multiple sample processing
- Automated score calculation for large datasets
- Results export functionality
- Sample template download

### Scientific Accuracy
- Evidence-based SNP weights from published research
- Standardized genotype coding (homozygous reference, heterozygous, homozygous alternate)
- Threshold-based interpretation (≥ 0.806 for highly beneficial response)

## Installation and Usage

### Prerequisites
```bash
Python 3.8 or higher
Required packages listed in requirements.txt
```

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run streamlit_app.py

# Access the application
# Navigate to http://localhost:8501 in your web browser
```

### Cloud Deployment

#### Streamlit Cloud (Recommended)
1. Fork or clone this repository to your GitHub account
2. Visit share.streamlit.io and sign in with GitHub
3. Select "New app" and choose your repository
4. Set main file path to streamlit_app.py
5. Deploy the application

#### Alternative Platforms
- Heroku: Requires Procfile configuration
- Railway: Direct GitHub integration available
- Render: Free tier deployment supported

## Technical Specifications

### SNP Data
The application utilizes 11 carefully selected SNPs across multiple chromosomes:
- rs10762496 (Chr 10) - ANAPC16 gene, Cell cycle pathway
- rs7894516 (Chr 10) - ANAPC16 gene, Cell cycle pathway
- rs17773251 (Chr 13) - CSNK1A1L gene, Gastric cancer/Wnt signaling
- rs9975448 (Chr 21) - IFNAR2 gene, PI3K-Akt signaling
- rs368403298 (Chr 5) - MCC gene, Wnt signaling
- rs877447 (Chr 17) - PRKCA gene, Multiple pathways
- rs142784890 (Chr 3) - CACNA2D3 gene, MAPK signaling
- rs4969266 (Chr 17) - RPTOR gene, PI3K-Akt signaling
- rs7860304 (Chr 9) - TRAF2 gene, MAPK signaling
- rs6887323 (Chr 5) - FGF18 gene, Multiple pathways
- rs12806363 (Chr 11) - RPS6KA4 gene, MAPK signaling

### Score Calculation
```
CATE Score = -Σ(SNP_weight[genotype] for each SNP)
```

### Genotype Encoding
- 0: Homozygous for reference allele
- 1: Heterozygous (one reference, one alternate allele)
- 2: Homozygous for alternate allele

### Interpretation Criteria
- Scores ≥ 0.806: Highly beneficial predicted response to H. pylori eradication
- Scores < 0.806: Moderately beneficial predicted response

## Data Input Format

### Single Prediction
Use the web interface to select genotypes for each SNP through radio button controls.

### Batch Processing
Upload CSV files with the following structure:
```csv
ID,rs10762496,rs7894516,rs17773251,rs9975448,rs368403298,rs877447,rs142784890,rs4969266,rs7860304,rs6887323,rs12806363
Sample1,0,1,2,1,0,1,2,0,1,2,1
Sample2,1,0,1,2,1,0,1,2,0,1,2
```

## Scientific Background

This tool implements research findings on host genetic profiles that enable personalized assessment of H. pylori eradication benefit for targeted gastric cancer prevention. The methodology is based on exploratory post-hoc analysis of randomized controlled trials examining the relationship between genetic variants and treatment response.

### Important Considerations
- This is a genotype-based benefit score derived from genetic markers
- Population characteristics, clinical factors, and individual patient context should be considered for final decision making
- This tool is intended for research purposes and professional interpretation
- Clinical application requires institutional approval and validation

## Use Cases

### Clinical Research
- Individualized treatment benefit assessment
- Genetic association studies
- Treatment response prediction modeling

### Healthcare Applications
- Patient-specific risk evaluation
- Precision medicine implementation
- Clinical decision support (with appropriate validation)

### Academic Research
- Population-level genetic analysis
- Educational demonstrations of genetic treatment effects
- Methodology validation studies

## File Structure

```
Hello_CATE/
├── streamlit_app.py          # Main application
├── requirements.txt          # Python dependencies
├── README.md                # Documentation
├── .gitignore               # Git ignore rules
└── kitty_icon.png           # Application icon
```

## Dependencies

```
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
```

## Troubleshooting

### Common Issues
1. **Import errors**: Ensure all dependencies are installed using `pip install -r requirements.txt`
2. **Port conflicts**: Specify alternative port using `streamlit run streamlit_app.py --server.port 8502`
3. **File upload errors**: Verify CSV format matches the required structure

### Support
For technical issues or questions regarding the application functionality, please review the error logs or contact the development team.

## License and Usage Rights

© 2025 Peking University Cancer Hospital, Department of Cancer Epidemiology. All rights reserved.

This application is intended for healthcare professionals and research purposes. Clinical application requires institutional approval and appropriate validation studies.

## Version History

- **Version 2.0**: Enhanced interface with comprehensive SNP information display
- **Version 1.0**: Basic CATE calculator implementation

## Citation

When using this tool for research purposes, please cite the associated manuscript:

*Host genetic profiles enable personalized assessment on benefit of Helicobacter pylori eradication for targeted gastric cancer prevention: an exploratory post-hoc analysis of two randomized trials*

## Contact Information

For correspondence regarding this tool:
- Wen-Qing Li: wenqing_li@bjmu.edu.cn
- Kai-Feng Pan: pan-kf@263.net

---

Built using Streamlit framework with modern web technologies for scientific computing and data visualization.