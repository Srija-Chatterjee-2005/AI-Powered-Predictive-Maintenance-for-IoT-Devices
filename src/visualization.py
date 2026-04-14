import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
import os

os.makedirs("outputs", exist_ok=True)

def generate_all_plots(df, y_test, y_pred, model):

    sns.set_style("darkgrid")

    # 1️⃣ Sensor Trend
    df[['temperature','vibration','current']].plot(figsize=(10,5))
    plt.title("Sensor Trends Over Time")
    plt.savefig("outputs/output_1.png")
    plt.clf()

    # 2️⃣ Correlation Heatmap
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title("Feature Correlation")
    plt.savefig("outputs/output_2.png")
    plt.clf()

    # 3️⃣ Failure Distribution
    df['failure'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title("Failure Distribution")
    plt.ylabel("")
    plt.savefig("outputs/output_3.png")
    plt.clf()

    # 4️⃣ Temperature vs Failure
    sns.boxplot(x='failure', y='temperature', data=df)
    plt.title("Temperature vs Failure")
    plt.savefig("outputs/output_4.png")
    plt.clf()

    # 5️⃣ Vibration vs Failure
    sns.boxplot(x='failure', y='vibration', data=df)
    plt.title("Vibration vs Failure")
    plt.savefig("outputs/output_5.png")
    plt.clf()

    # 6️⃣ Current vs Failure
    sns.boxplot(x='failure', y='current', data=df)
    plt.title("Current vs Failure")
    plt.savefig("outputs/output_6.png")
    plt.clf()

    # 7️⃣ Feature Importance 🔥
    import pandas as pd
    importance = model.feature_importances_
    features = ['temperature','vibration','current','temp_vibration_ratio']
    pd.Series(importance, index=features).sort_values().plot(kind='barh')
    plt.title("Feature Importance")
    plt.savefig("outputs/output_7.png")
    plt.clf()

    # 8️⃣ Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title("Confusion Matrix")
    plt.savefig("outputs/output_8.png")
    plt.clf()