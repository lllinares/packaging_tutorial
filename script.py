import biketrauma

df = biketrauma.Load_db().save_as_df()
df_nicely_formated = biketrauma.format_date(df)
#biketrauma.plot_location(biketrauma.get_accident(df))


