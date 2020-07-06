
import streamlit as st
import argparse
import pandas as pd
import datetime
import math

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


granularity = st.selectbox(
    "What granularity you would like to see",
    ("Yearly", "Monthly", "Weekly", "Daily")
)


if (granularity == 'Yearly'):
    st.subheader('Number of emails in each year')
    start_year, end_year = st.slider("Select year Range:", 2001, 2020, (2003, 2018), 1)
    df_yearly = df.loc[(df['date'].dt.year >= start_year) & (df['date'].dt.year <= end_year)]
    df_yearly = df_yearly.groupby(pd.Grouper(key='date', freq='Y'))['academic','cfp','funding','misc','personal','research','service-external','service-internal','system','teaching','twitter'].agg('sum').reset_index('date')
    df_yearly['date'] = df_yearly['date'].dt.year
    df_yearly = df_yearly.set_index('date')
    st.bar_chart(df_yearly)

if (granularity == 'Monthly'):
    st.subheader('Number of emails in monthly granularity')
    start_m, end_m = st.slider("Select date range to see monthly granularity plot:", 2001.0+10/12, 2021.0-1/12, (2003+1/12, 2018.0+1/12), 1/12, format = '')
    ms = math.ceil((start_m - int(start_m)) * 12)
    me = math.ceil((end_m - int(end_m)) * 12)
    start_month = datetime.date(int(start_m), ms, 1)
    end_month = datetime.date(int(end_m), me, 1)
    st.text(f"From: {start_month:%Y}-{start_month:%m} to {end_month:%Y}-{end_month:%m} ")
    df_monthly = df.loc[df['date'].dt.date >= start_month]
    df_monthly = df_monthly.loc[df_monthly['date'].dt.date <= end_month]
    df_monthly = df_monthly.groupby(pd.Grouper(key='date', freq='M'))['academic','cfp','funding','misc','personal','research','service-external','service-internal','system','teaching','twitter'].agg('sum').reset_index('date')
    df_monthly = df_monthly.set_index('date')
    st.bar_chart(df_monthly)

if (granularity == 'Weekly'):
    st.subheader('Number of emails in weekly granularity')
    start_w, end_w = st.slider("Select date range to see weekly granularity plot:",  2001.0+10/12, 2021.0-1/12, (2003+1/12, 2018.0+1/12), 1/12, format = '')
    ws = math.ceil((start_w - int(start_w)) * 12)
    we = math.ceil((end_w - int(end_w)) * 12)
    start_week = datetime.date(int(start_w), ws, 1)
    end_week = datetime.date(int(end_w), we, 1)
    st.text(f"From: {start_week:%Y}-{start_week:%m} to {end_week:%Y}-{end_week:%m} ")
    df_weekly = df.loc[df['date'].dt.date >= start_week]
    df_weekly = df_weekly.loc[df_weekly['date'].dt.date <= end_week]
    df_weekly = df_weekly.groupby(pd.Grouper(key='date', freq='W'))['academic','cfp','funding','misc','personal','research','service-external','service-internal','system','teaching','twitter'].agg('sum').reset_index('date')
    df_weekly = df_weekly.set_index('date')
    st.bar_chart(df_weekly)

if (granularity == 'Daily'):
    st.subheader('Number of published documents in daily granularity')
    start_d, end_d = st.slider("Select date range to see daily granularity plot:",  2001.0+10/12, 2021.0-1/12, (2003+1/12, 2018.0+1/12), 1/12, format = '')
    ds = math.ceil((start_d - int(start_d)) * 12)
    de = math.ceil((end_d - int(end_d)) * 12)
    start_day = datetime.date(int(start_d), ds, 1)
    end_day = datetime.date(int(end_d), de, 1)
    st.text(f"From: {start_day:%Y}-{start_day:%m} to {end_day:%Y}-{end_day:%m} ")
    df_daily = df.loc[df['date'].dt.date >= start_day]
    df_daily = df_daily.loc[df_daily['date'].dt.date <= end_day]
    df_daily = df_daily.set_index('date')
    st.bar_chart(df_daily)






