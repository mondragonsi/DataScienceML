import plotly.express as px
df = px.data.gapminder().query("year == 2022").query("continent == 'Americas'")
# Represent only large countries
df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries'
fig = px.pie(df, values='pop', names='country',
             title='Population of Americas continent')
fig.show()
