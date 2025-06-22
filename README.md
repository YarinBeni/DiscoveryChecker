
Of course. Here is a `README.md` file for the `analyze_results.py` script.

---

# Evaluation Results Analysis Script

## Overview

This script is designed to analyze the evaluation results of AI models, which are stored in a JSON file (`evaluation_results.json`). It processes this data to generate summary statistics and visualizations that compare the performance of different models across various metrics and categories.

The script performs the following actions:
1.  Loads evaluation data from `agents/evaluation_results.json`.
2.  Processes the data using the `pandas` library to create a structured DataFrame.
3.  Generates three key visualizations and saves them as PNG files in the `agents/` directory:
    *   A bar chart of average scores by model and metric.
    *   A bar chart of average scores by query category.
    *   A heatmap of scores by model and metric.
4.  Prints summary statistics to the console.

## Prerequisites

To run this script, you need Python 3 and the following libraries:
*   `pandas`
*   `matplotlib`
*   `seaborn`
*   `numpy`


## Usage

To execute the script, run the following command from the root directory of the project:

```bash
python analyze_results.py
```

The script will process the data and generate the output files in the `agents/` directory.

## Output

### Generated Plots

The script generates and saves the following plots in the `agents/` directory:

1.  **`average_scores_by_model_and_metric.png`**: A bar chart comparing the average scores of each model across the different evaluation metrics (e.g., Unique Content, Clarity).
2.  **`average_scores_by_category.png`**: A bar chart comparing the average scores for each query category (e.g., Short Query, Technical Terms).
3.  **`heatmap_scores_by_model_and_metric.png`**: A heatmap providing a visual overview of the average scores for each model-metric combination.

### Console Output

The script will also print the following summary statistics to your terminal:
*   Average scores by model.
*   Average scores by metric.
*   Average scores by category.
*   Overall average scores for each model.
