import numpy as np

def precision(recommended_list, relevant_list):
    is_relevant = np.isin(recommended_list, relevant_list)
    precision = np.sum(is_relevant) / len(recommended_list)
    return precision

def recall(recommended_list, relevant_list):
    is_relevant = np.isin(recommended_list, relevant_list)
    recall = np.sum(is_relevant) / len(relevant_list)
    return recall

def f1_score(recommended_list, relevant_list):
    precision_val = precision(recommended_list, relevant_list)
    recall_val = recall(recommended_list, relevant_list)
    f1_score = 2 * (precision_val * recall_val) / (precision_val + recall_val)
    return f1_score

recommended_list = [1, 2, 3, 4, 5]
relevant_list = [1, 2, 4, 5, 6]

precision_val = precision(recommended_list, relevant_list)
recall_val = recall(recommended_list, relevant_list)
f1_score_val = f1_score(recommended_list, relevant_list)

print("Precision:", precision_val)
print("Recall:", recall_val)
print("F1 Score:", f1_score_val)
