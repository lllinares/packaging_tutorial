def format_date(df_bikes):
    df = df_bikes.drop(columns = ['date', 'mois','jour','heure'])
    df.insert(0,"date_formated", df_bikes['date']+"T"+df_bikes['heure']+":00:00+01:00")
    #autre méthode : df.to_date_time(...)
    return df