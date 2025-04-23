def calculate_fairness(df):
    result = {}
    for group in df['gender'].unique():
        group_data = df[df['gender'] == group]
        tp = sum((group_data['actual'] == 1) & (group_data['predicted'] == 1))
        fp = sum((group_data['actual'] == 0) & (group_data['predicted'] == 1))
        fn = sum((group_data['actual'] == 1) & (group_data['predicted'] == 0))
        tpr = tp / (tp + fn + 1e-6)
        fpr = fp / (fp + (len(group_data) - tp - fp - fn) + 1e-6)
        result[group] = {"TPR": round(tpr, 2), "FPR": round(fpr, 2)}
    return result
