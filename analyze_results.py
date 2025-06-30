import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

plt.style.use('seaborn-v0_8')
with open('agents/evaluation_results.json', 'r') as f:
    results = json.load(f)
metrics = ["Unique Content", "True & Well-Supported", "Relevant Sources", 
          "Detailed Explanation", "New Ideas & Insights", "Clarity & Organization"]
data = []
for model in ['PaperQA2', 'Ai2ScholarQA']:
    for category in results[model]:
        entry = results[model][category]
        if entry:
            for metric in metrics:
                if metric in entry:
                    justification = entry.get('Justification', {}).get(metric, '')
                    data.append({
                        'Model': model,
                        'Category': category,
                        'Metric': metric,
                        'Score': entry[metric],
                        'Justification': justification
                    })

df = pd.DataFrame(data)
plt.figure(figsize=(12, 6))
avg_scores = df.groupby(['Model', 'Metric'])['Score'].mean().unstack()
avg_scores.plot(kind='bar', ax=plt.gca(), color=sns.color_palette('Set2', n_colors=6))
plt.title('Average Scores by Model and Metric')
plt.xticks(rotation=45)
plt.legend(title='Metrics', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('agents/average_scores_by_model_and_metric.png', dpi=300, bbox_inches='tight')
plt.close()

plt.figure(figsize=(12, 6))
cat_map = {
    'Short Query': 'Short', 'Long Query': 'Long', 'Narrow Focus': 'Narrow',
    'Broad Focus': 'Broad', 'No Time Constraint': 'No Time', 'Recent Time Window': 'Recent',
    'Low Entity Count': 'Low Ent.', 'High Entity Count': 'High Ent.',
    'Common Terms': 'Common', 'Technical Terms': 'Technical'
}
df['Category'] = df['Category'].map(cat_map)
cat_scores = df.groupby(['Model', 'Category'])['Score'].mean().unstack()
cat_scores.plot(kind='bar', ax=plt.gca(), color=sns.color_palette('tab10', n_colors=10))
plt.title('Average Scores by Category')
plt.xticks(rotation=45)
plt.legend(title='Categories', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('agents/average_scores_by_category.png', dpi=300, bbox_inches='tight')
plt.close()

plt.figure(figsize=(10, 6))
pivot = df.pivot_table(values='Score', index='Model', columns='Metric', aggfunc='mean')
sns.heatmap(pivot, annot=True, cmap='YlOrRd', fmt='.2f')
plt.title('Heatmap of Scores by Model and Metric')
plt.tight_layout()
plt.savefig('agents/heatmap_scores_by_model_and_metric.png', dpi=300, bbox_inches='tight')
plt.close()

print(f"\nSummary Statistics:\n\nAverage scores by model:\n{df.groupby('Model')['Score'].mean()}\n\nAverage scores by metric:\n{df.groupby('Metric')['Score'].mean()}\n\nAverage scores by category:\n{df.groupby('Category')['Score'].mean()}\n\nOverall average scores:\n{df.groupby('Model')['Score'].mean().round(2)}") 
