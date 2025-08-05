x=df[['Height','Weight']]
le=LabelEncoder()
y=le.fit_transform(df['Gender'])
