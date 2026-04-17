def add_features(df):
    df['calorie_per_fat'] = df['Calories'] / (df['Total Fat (g)'] + 1)
    return df