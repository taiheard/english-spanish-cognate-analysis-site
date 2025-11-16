# Statistical Analysis Report: False Friends Paradox & Technical Vocabulary Paradox

**Generated:** 2025-11-02 15:01:21

---

## Analysis 1: Frequency Comparison - False Friends vs True Cognates

### Research Question

Are False Friends used more frequently in common vocabulary than True Cognates, contributing to their confusion risk?

**Note:** Lower frequency scores indicate HIGHER frequency (more common usage)

### Descriptive Statistics

| Group | N | Mean | Std Dev | % of Dataset |
|-------|-----|------|---------|-------------|
| False Friends | 170 | 2.9464 | 0.8714 | 5.61% |
| True Cognates | 2633 | 3.7509 | 1.2844 | 86.84% |
| **Difference (FF - TC)** | | **-0.8045** | | |

> ✓ Negative difference confirms False Friends have LOWER scores = HIGHER frequency

### Statistical Tests

**Levene's Test (Equal Variances):** F = 45.1571, p = 0.0000  
→ Variances are **UNEQUAL** (α = 0.05)

**Independent Samples t-test:**

- **t-statistic:** -8.0467
- **Degrees of freedom:** 2801
- **p-value (two-tailed):** 0.000000
- **p-value (one-tailed, FF < TC):** 0.000000
- **Cohen's d (effect size):** -0.6368

- **Effect size interpretation:** medium

**95% Confidence Interval for difference:** [-0.9443, -0.6646]

### Interpretation

✓ **STATISTICALLY SIGNIFICANT**

False Friends (M = 2.9464, SD = 0.8714) have statistically significantly LOWER frequency 
scores than True Cognates (M = 3.7509, SD = 1.2844), t(2801) = -8.0467, 
p = 0.000000 (one-tailed), d = -0.6368.

**Key Finding:** This confirms False Friends appear MORE FREQUENTLY in common usage, creating a 
'treacherous' combination of high frequency + high similarity that increases confusion risk for 
language learners.


### Visualization

![Frequency Analysis](../assets/images/analysis/frequency_analysis.png)

---

## Analysis 2: Technical Vocabulary Paradox - Similarity by Domain

### Research Question

Do technical/scientific cognates show HIGHER orthographic similarity than common/core cognates, suggesting conscious etymological preservation in specialized vocabulary?

### Domain Definitions

**Technical/Scientific Domains:**
- Technology Tools
- Health Medicine

**Core/Common Domains:**
- Family Kinship
- Language Communication
- Nature Geography
- Food Cuisine
- Clothing Appearance

### Descriptive Statistics

| Group | N | Mean | Std Dev |
|-------|-----|------|--------|
| Technical/Scientific | 585 | 0.7710 | 0.1624 |
| Core/Common | 512 | 0.7682 | 0.1896 |
| **Difference (Tech - Common)** | | **0.0027** | |

> ✓ Positive difference suggests technical terms ARE more similar

### Statistical Tests

**Levene's Test (Equal Variances):** F = 15.4707, p = 0.0001  
→ Variances are **UNEQUAL** (α = 0.05)

**Independent Samples t-test:**

- **t-statistic:** 0.2585
- **Degrees of freedom:** 1095
- **p-value (two-tailed):** 0.796042
- **p-value (one-tailed, Tech > Common):** 0.398021
- **Cohen's d (effect size):** 0.0156

- **Effect size interpretation:** negligible

**95% Confidence Interval for difference:** [-0.0183, 0.0238]

### Interpretation

✗ NOT STATISTICALLY SIGNIFICANT (p = 0.398021)

### Visualization

![Technical Paradox Analysis](../assets/images/analysis/technical_paradox_analysis.png)

---

## Comprehensive Summary

### Summary Table

| Analysis | Comparison | Metric | Mean Group 1 | Mean Group 2 | Difference | t-statistic | p-value | Cohen's d | Significant |
|----------|------------|--------|--------------|--------------|------------|-------------|---------|-----------|-------------|
| Frequency Paradox | False Friends vs True Cognates | Frequency Score (Lower=More Frequent) | 2.9464 | 3.7509 | -0.8045 | -8.0467 | 0.000000 | -0.6368 | ✓ YES |
| Technical Vocabulary Paradox | Technical vs Common Cognates | Jaccard Similarity (Higher=More Similar) | 0.7710 | 0.7682 | 0.0027 | 0.2585 | 0.398021 | 0.0156 | ✗ NO |

### Key Findings

1. **False Friends Frequency:** Statistically significant evidence that false friends appear MORE frequently in common usage than true cognates.

2. **Technical Vocabulary Paradox:** **No statistically significant difference** in orthographic similarity between technical/scientific terms and common cognates (p = 0.398, Cohen's d = 0.016).Implications

These findings have important implications for language learning pedagogy and demonstrate sophisticated use of statistical analysis in linguistics:

- **For Language Learners:** False friends' high frequency makes them particularly dangerous, requiring explicit attention in teaching materials.

- **For Curriculum Design:** The lack of significant  difference in orthographic similarity suggests that technical vocabulary does not offer a systematic advantage for cross-linguistic learning,  contrary to common assumptions.

- **For Linguistic Theory:** While technical vocabulary shows slightly higher similarity, the effect is too small and statistically  unreliable to support theories of systematic etymological preservation  in specialized domains. Further research with larger samples may be  needed.

---

*Report generated on 2025-11-02 at 15:01:22*
