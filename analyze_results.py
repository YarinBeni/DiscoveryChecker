import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set style
plt.style.use('seaborn-v0_8')

# Load results
with open('agents/evaluation_results.json', 'r') as f:
    results = json.load(f)

# Create DataFrame
metrics_list = [
    "Unique Content",
    "True & Well-Supported",
    "Relevant Sources",
    "Detailed Explanation",
    "New Ideas & Insights",
    "Clarity & Organization"
]
data = []
for model in ['PaperQA2', 'Ai2ScholarQA']:
    for category in results[model]:
        entry = results[model][category]
        if entry is not None:
            for metric in metrics_list:
                if metric in entry:
                    justification = ''
                    if 'Justification' in entry and metric in entry['Justification']:
                        justification = entry['Justification'][metric]
                    
                    data.append({
                        'Model': model,
                        'Category': category,
                        'Metric': metric,
                        'Score': entry[metric],
                        'Justification': justification
                    })

df = pd.DataFrame(data)

# Create visualizations
# 1. Average scores by model and metric
plt.figure(figsize=(12, 6))
metric_palette = sns.color_palette('Set2', n_colors=6)
avg_scores = df.groupby(['Model', 'Metric'])['Score'].mean().unstack()
avg_scores.plot(kind='bar', ax=plt.gca(), color=metric_palette)
plt.title('Average Scores by Model and Metric')
plt.xticks(rotation=45)
plt.legend(title='Metrics', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('agents/average_scores_by_model_and_metric.png', dpi=300, bbox_inches='tight')
plt.close()

# 2. Average scores by category
plt.figure(figsize=(12, 6))
category_palette = sns.color_palette('tab10', n_colors=10)
# Create a mapping for shorter category names
category_mapping = {
    'Short Query': 'Short',
    'Long Query': 'Long',
    'Narrow Focus': 'Narrow',
    'Broad Focus': 'Broad',
    'No Time Constraint': 'No Time',
    'Recent Time Window': 'Recent',
    'Low Entity Count': 'Low Ent.',
    'High Entity Count': 'High Ent.',
    'Common Terms': 'Common',
    'Technical Terms': 'Technical'
}
# Apply the mapping to the DataFrame
df['Category'] = df['Category'].map(category_mapping)
category_scores = df.groupby(['Model', 'Category'])['Score'].mean().unstack()
category_scores.plot(kind='bar', ax=plt.gca(), color=category_palette)
plt.title('Average Scores by Category')
plt.xticks(rotation=45)
plt.legend(title='Categories', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('agents/average_scores_by_category.png', dpi=300, bbox_inches='tight')
plt.close()

# 3. Heatmap of scores by model and metric
plt.figure(figsize=(10, 6))
pivot_table = df.pivot_table(
    values='Score',
    index='Model',
    columns='Metric',
    aggfunc='mean'
)
sns.heatmap(pivot_table, annot=True, cmap='YlOrRd', fmt='.2f')
plt.title('Heatmap of Scores by Model and Metric')
plt.tight_layout()
plt.savefig('agents/heatmap_scores_by_model_and_metric.png', dpi=300, bbox_inches='tight')
plt.close()

# Print summary statistics
print("\nSummary Statistics:")
print("\nAverage scores by model:")
print(df.groupby('Model')['Score'].mean())

print("\nAverage scores by metric:")
print(df.groupby('Metric')['Score'].mean())

print("\nAverage scores by category:")
print(df.groupby('Category')['Score'].mean())

# Calculate and print the overall average score for each model
print("\nOverall average scores:")
print(df.groupby('Model')['Score'].mean().round(2)) 