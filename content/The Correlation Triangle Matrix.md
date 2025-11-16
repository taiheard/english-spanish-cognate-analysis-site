

<h2> The Correlation Triangle Matrix</h2>	



The matrix explicitly visualizes the correlations between the **Core 5 Metrics**

1. **Levenshtein Similarity**
2. **Syllable Count**
3. **Word Length**
4. **Frequency Complexity**
5. **Overall Complexity**



Key Relationships Revealed by the Correlation Matrix

The matrix (or Correlation Network visualization confirms several expected relationships, as well as the crucial finding regarding similarity:

1. Strong Positive Correlations (Complexity Drivers)

The internal components of word complexity are, as expected, highly correlated

. This shows that longer words usually have more syllables and a higher overall complexity score:

• **Word Length** is strongly correlated with **Overall Complexity** (r = **0.861**)

• **Word Length** is strongly correlated with **Syllable Count** (r = **0.806**)

• **Frequency Complexity** is positively correlated with **Overall Complexity** (r = **0.668**)

. (Since a higher numerical frequency score means *lower* actual usage frequency, this correlation shows that **more complex words are used less often**).

• **Syllable Count** is positively correlated with **Overall Complexity** (r = **0.765**)



2. The Weak Link (Similarity vs. Complexity)

The matrix successfully highlights the central qualitative observation noted in the source material—that orthographic distance (similarity) is mostly independent of word complexity:

• **Levenshtein similarity is not strongly correlated (+6%) with complexity**

.

• The correlation coefficients confirm this extreme weakness:

  ◦ Levenshtein Similarity vs. **Overall Complexity**: r = **0.008**

  ◦ Levenshtein Similarity vs. **Syllable Count**: r = **0.009**

  ◦ Levenshtein Similarity vs. **Word Length**: r = **-0.012**

.

**Conclusion**

The low correlation between Levenshtein Similarity and complexity metrics is a valuable finding for your portfolio, especially when combined with the T-test results. It validates that **similarity is an unreliable predictor** of a word's structural or functional complexity (frequency/length/syllables) and supports the earlier pivot away from similarity in predictive modeling

*The matrix operates like a linguistic blueprint, showing that while the complexity elements (length, syllable count, frequency) form a dense, interconnected cluster, the structural similarity (Levenshtein) floats almost entirely disconnected, demonstrating that the visual appearance of a word does not reliably predict its underlying linguistic nature.*