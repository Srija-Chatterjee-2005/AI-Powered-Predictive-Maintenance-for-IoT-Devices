import pandas as pd

# Load dataset
def load_data(path):
    df = pd.read_csv(path)
    return df

# Preprocess dataset
def preprocess(df):
    df = df.copy()
    df.dropna(inplace=True)

    # Feature Engineering
    df['temp_vibration_ratio'] = df['temperature'] / (df['vibration'] + 1)

    X = df[['temperature', 'vibration', 'current', 'temp_vibration_ratio']]
    y = df['failure']

    return X, y, df