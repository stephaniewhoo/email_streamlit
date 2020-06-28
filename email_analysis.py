
import streamlit as st
import argparse
import pandas as pd
import datetime

st.title('Prof Email analysis')
read_and_cache_csv = st.cache(pd.read_csv)

@st.cache
def load_all():
    df_url = "https://raw.githubusercontent.com/stephaniewhoo/email_streamlit/master/date_histogram_categories.csv"
    df = pd.read_csv(df_url, error_bad_lines=False)
    df['date'] = pd.to_datetime(df['date'])
    return df

data_load_state = st.text('Loading data...')
df = load_all()
data_load_state.text("Done!")

st.subheader('Number of emails in each year')
start_year = st.slider('What is the start year you want to see distribution?', 2005, 2019, 2009)
end_year = st.slider('What is the end year you want to see distribution?', 2006, 2020, 2020)
df_yearly = df.loc[(df['date'].dt.year >= start_year) & (df['date'].dt.year <= end_year)]
df_yearly = df_yearly.groupby(pd.Grouper(key='date', freq='Y'))['academic','cfp','funding','misc','personal','research','service-external','service-internal','system','teaching','twitter'].agg('sum').reset_index('date')
df_yearly = df_yearly.set_index('date')
st.bar_chart(df_yearly)

st.subheader('Number of emails in monthly granularity')
start_month = st.date_input('what start date you want to see for bars in monthly granularity?', datetime.date(2009, 5, 1), datetime.date(2001, 12, 31),datetime.date(2020, 5, 15))
end_month = st.date_input('what end date you want to see for bars in monthly granularity?', datetime.date(2009, 7, 1), datetime.date(2003, 4, 12), datetime.date(2020, 5, 29))
df_monthly = df.loc[df['date'].dt.date >= start_month]
df_monthly = df_monthly.loc[df_monthly['date'].dt.date <= end_month]
df_monthly = df_monthly.groupby(pd.Grouper(key='date', freq='M'))['academic','cfp','funding','misc','personal','research','service-external','service-internal','system','teaching','twitter'].agg('sum').reset_index('date')
df_monthly = df_monthly.set_index('date')
st.bar_chart(df_monthly)


st.subheader('Number of emails in weekly granularity')
start_week = st.date_input('what start date you want to see for bars in weekly granularity?', datetime.date(2009, 5, 1), datetime.date(2001, 12, 31),datetime.date(2020, 5, 15))
end_week = st.date_input('what end date you want to see for bars in weekly granularity?', datetime.date(2009, 7, 1), datetime.date(2003, 4, 12), datetime.date(2020, 5, 29))
df_weekly = df.loc[df['date'].dt.date >= start_week]
df_weekly = df_weekly.loc[df_weekly['date'].dt.date <= end_week]
df_weekly = df_weekly.groupby(pd.Grouper(key='date', freq='W'))['academic','cfp','funding','misc','personal','research','service-external','service-internal','system','teaching','twitter'].agg('sum').reset_index('date')
df_weekly = df_weekly.set_index('date')
st.bar_chart(df_weekly)

st.subheader('Number of emails in daily granularity')
start_day = st.date_input('what start date you want to see for bars in daily granularity?', datetime.date(2009, 5, 1), datetime.date(2001, 12, 31),datetime.date(2020, 5, 15))
end_day = st.date_input('what end date you want to see for bars in daily granularity?', datetime.date(2009, 7, 1), datetime.date(2003, 4, 12), datetime.date(2020, 5, 29))
df_daily = df.loc[df['date'].dt.date >= start_day]
df_daily = df_daily.loc[df_daily['date'].dt.date <= end_day]
df_daily = df_daily.set_index('date')
st.bar_chart(df_daily)







