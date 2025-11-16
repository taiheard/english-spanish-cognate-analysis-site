#!/usr/bin/env python3
"""
Calculate Business Impact Metrics for Language Learning Applications
Based on actual frequency distribution and domain FFR data
"""

import pandas as pd
import numpy as np
from pathlib import Path

# Load data
data_file = Path(__file__).parent.parent / "language_analysis_masterframe25OCT.csv"
df = pd.read_csv(data_file)

print("=" * 80)
print("BUSINESS IMPACT ANALYSIS: Language Learning Application Metrics")
print("=" * 80)
print()

# 1. HIGH-FFR DOMAIN IMPACT ANALYSIS
print("1. HIGH-FFR DOMAIN PRIORITIZATION IMPACT")
print("-" * 80)

# Calculate FFR by domain
domain_stats = df.groupby('cultural_domain').agg({
    'relationship_type': lambda x: (x == 'false_friends').sum(),
    'english_word': 'count'
}).rename(columns={'relationship_type': 'false_friends', 'english_word': 'total'})

domain_stats['ffr'] = (domain_stats['false_friends'] / domain_stats['total'] * 100)
domain_stats = domain_stats.sort_values('ffr', ascending=False)

# Identify high-risk domains (FFR >= 10%)
high_risk_domains = domain_stats[domain_stats['ffr'] >= 10.0]
print(f"\nHigh-Risk Domains (FFR >= 10%):")
for domain, row in high_risk_domains.iterrows():
    print(f"  - {domain}: {row['ffr']:.2f}% FFR ({int(row['false_friends'])} false friends / {int(row['total'])} pairs)")

# Calculate total false friends in high-risk domains
total_ff = domain_stats['false_friends'].sum()
high_risk_ff = high_risk_domains['false_friends'].sum()
high_risk_coverage = (high_risk_ff / total_ff * 100)

print(f"\nHigh-Risk Domain Coverage:")
print(f"  - False friends in high-risk domains: {int(high_risk_ff)} / {int(total_ff)}")
print(f"  - Coverage: {high_risk_coverage:.1f}% of all false friends")
print(f"  - Impact: Targeting these {len(high_risk_domains)} domains addresses {high_risk_coverage:.1f}% of false friend risk")

# 2. HIGH-FREQUENCY FALSE FRIENDS IMPACT
print("\n2. HIGH-FREQUENCY FALSE FRIENDS IMPACT")
print("-" * 80)

# Get false friends only
false_friends = df[df['relationship_type'] == 'false_friends'].copy()
true_cognates = df[df['relationship_type'] == 'cognates'].copy()

# Define "high frequency" as frequency score <= 3.0 (lower = more frequent)
high_freq_threshold = 3.0

ff_high_freq = false_friends[false_friends['complexity_frequency_complexity'] <= high_freq_threshold]
ff_all = false_friends

print(f"\nFalse Friends Frequency Distribution:")
print(f"  - Mean frequency score (False Friends): {false_friends['complexity_frequency_complexity'].mean():.2f}")
print(f"  - Mean frequency score (True Cognates): {true_cognates['complexity_frequency_complexity'].mean():.2f}")
print(f"  - Threshold for 'high frequency': ≤ {high_freq_threshold}")

high_freq_percentage = (len(ff_high_freq) / len(ff_all) * 100)
print(f"\nHigh-Frequency False Friends:")
print(f"  - Count: {len(ff_high_freq)} / {len(ff_all)}")
print(f"  - Percentage: {high_freq_percentage:.1f}%")
print(f"  - Impact: Prioritizing high-frequency false friends targets {high_freq_percentage:.1f}% of all false friends")

# Daily usage scenario estimate
# Calculate cumulative frequency weight
# Assume frequency distribution follows Zipf's law approximation
# Words with freq_score <= 2.0 = very high freq (daily multiple times)
# Words with freq_score <= 3.0 = high freq (daily)
# Words with freq_score <= 4.0 = medium freq (weekly)

ff_freq_dist = false_friends.groupby(pd.cut(false_friends['complexity_frequency_complexity'], 
                                             bins=[0, 2.0, 3.0, 4.0, 6.0],
                                             labels=['Very High', 'High', 'Medium', 'Low'])).size()

print(f"\nFalse Friends by Frequency Category:")
for cat, count in ff_freq_dist.items():
    pct = (count / len(false_friends) * 100)
    print(f"  - {cat}: {count} ({pct:.1f}%)")

# Estimate daily usage impact (very high + high frequency)
daily_usage_ff = false_friends[false_friends['complexity_frequency_complexity'] <= 3.0]
daily_usage_impact = (len(daily_usage_ff) / len(false_friends) * 100)
print(f"\nDaily Usage Scenario Impact:")
print(f"  - False friends with freq ≤ 3.0: {len(daily_usage_ff)} / {len(false_friends)}")
print(f"  - Percentage: {daily_usage_impact:.1f}%")
print(f"  - Interpretation: Targeting high-frequency false friends impacts ~{daily_usage_impact:.0f}% of daily usage scenarios")

# 3. PARETO PRINCIPLE (80/20 RULE) ANALYSIS
print("\n3. RESOURCE ALLOCATION EFFICIENCY (PARETO ANALYSIS)")
print("-" * 80)

# Sort false friends by frequency (ascending = most frequent first)
ff_sorted = false_friends.sort_values('complexity_frequency_complexity')

# Calculate cumulative distribution
# For simplicity, treat each word as having equal error potential
# (In reality, this could be weighted by frequency)
ff_sorted['cumulative_pct'] = np.arange(1, len(ff_sorted) + 1) / len(ff_sorted) * 100

# Find the percentage of vocabulary that covers 80% of errors
# Using frequency-weighted approach
ff_sorted['freq_weight'] = 1 / (ff_sorted['complexity_frequency_complexity'] + 1)  # Lower score = higher weight
ff_sorted['freq_weight_normalized'] = ff_sorted['freq_weight'] / ff_sorted['freq_weight'].sum()
ff_sorted['cumulative_weight'] = ff_sorted['freq_weight_normalized'].cumsum() * 100

# Find where we hit 80% coverage
coverage_80_idx = (ff_sorted['cumulative_weight'] >= 80).idxmax()
coverage_80_position = ff_sorted.loc[coverage_80_idx, 'cumulative_pct']

print(f"\nPareto Analysis (Frequency-Weighted):")
print(f"  - Top {coverage_80_position:.1f}% of false friends (by frequency)")
print(f"  - Account for: ~80% of potential confusion incidents")
print(f"  - Interpretation: Focus on {coverage_80_position:.1f}% of vocabulary to address 80% of errors")

# Also calculate by domain concentration
domain_ff_count = false_friends.groupby('cultural_domain').size().sort_values(ascending=False)
domain_cumulative = domain_ff_count.cumsum() / domain_ff_count.sum() * 100

domains_for_80 = (domain_cumulative <= 80).sum()
domains_pct = (domains_for_80 / len(domain_ff_count) * 100)

print(f"\nPareto Analysis (Domain-Based):")
print(f"  - Top {domains_for_80} domains (out of {len(domain_ff_count)}) = {domains_pct:.1f}% of domains")
print(f"  - Contain: ~80% of all false friends")
print(f"  - Top domains: {', '.join(domain_ff_count.head(domains_for_80).index.tolist())}")

# 4. COMPREHENSIVE BUSINESS IMPACT SUMMARY
print("\n" + "=" * 80)
print("SUMMARY: DATA-DRIVEN BUSINESS IMPACT METRICS")
print("=" * 80)
print()

print(f"📊 HIGH-FFR DOMAIN PRIORITIZATION:")
print(f"   → Targeting {len(high_risk_domains)} high-risk domains covers {high_risk_coverage:.1f}% of false friend risk")
print()

print(f"📊 HIGH-FREQUENCY FALSE FRIENDS:")
print(f"   → Prioritizing high-frequency false friends impacts {daily_usage_impact:.0f}% of daily usage scenarios")
print()

print(f"📊 RESOURCE ALLOCATION EFFICIENCY:")
print(f"   → Focusing on top {coverage_80_position:.0f}% of vocabulary addresses ~80% of confusion incidents")
print(f"   → Focusing on top {domains_pct:.0f}% of domains ({domains_for_80} domains) covers ~80% of false friends")
print()

print("=" * 80)
print("RECOMMENDED METRICS FOR FINDINGS PAGE:")
print("=" * 80)
print()
print(f"1. Prioritizing high-FFR domains (Family/Kinship, Emotions/Psychology, Food/Cuisine)")
print(f"   could reduce learner confusion by targeting {high_risk_coverage:.0f}% of all false friends.")
print()
print(f"2. Targeting high-frequency false friends first impacts approximately")
print(f"   {daily_usage_impact:.0f}% of daily usage scenarios where confusion is most likely.")
print()
print(f"3. Resource allocation efficiency: focusing on the top {coverage_80_position:.0f}% of false friends")
print(f"   (ranked by frequency) addresses approximately 80% of confusion incidents.")
print()
print(f"   OR: focusing on the top {domains_pct:.0f}% of domains addresses approximately 80% of false friends.")
print()

