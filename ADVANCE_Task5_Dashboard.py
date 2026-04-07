# ============================================================
# Task 5: Interactive Business Dashboard
# DevelopersHub Corporation - Data Science Internship
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# ============================================================
# Page Configuration
# ============================================================
st.set_page_config(
    page_title="Global Superstore Dashboard",
    page_icon="📊",
    layout="wide"
)

# ============================================================
# Load Dataset
# ============================================================
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('Global_Superstore2.csv', encoding='utf-8')
    except:
        try:
            df = pd.read_csv('Global_Superstore2.csv', encoding='latin-1')
        except:
            df = pd.read_csv('Global_Superstore2.csv', encoding='cp1252')

    # Clean data
    if 'Row ID' in df.columns:
        df.drop('Row ID', axis=1, inplace=True)
    if 'Postal Code' in df.columns:
        df.drop('Postal Code', axis=1, inplace=True)

    # Convert dates
    if 'Order Date' in df.columns:
        df['Order Date'] = pd.to_datetime(df['Order Date'])
        df['Year'] = df['Order Date'].dt.year
        df['Month'] = df['Order Date'].dt.month

    df.fillna(0, inplace=True)
    return df

df = load_data()

# ============================================================
# Dashboard Title
# ============================================================
st.title("📊 Global Superstore - Business Intelligence Dashboard")
st.markdown("**DevelopersHub Corporation - Data Science Internship**")
st.markdown("---")

# ============================================================
# Sidebar Filters
# ============================================================
st.sidebar.title("🔍 Filters")
st.sidebar.markdown("Use filters to explore data")

# Region Filter
all_regions = ['All Regions'] + sorted(df['Region'].unique().tolist())
selected_region = st.sidebar.selectbox("Select Region:", all_regions)

# Category Filter
all_categories = ['All Categories'] + sorted(df['Category'].unique().tolist())
selected_category = st.sidebar.selectbox("Select Category:", all_categories)

# Sub-Category Filter
if selected_category != 'All Categories':
    subcats = ['All Sub-Categories'] + sorted(
        df[df['Category'] == selected_category]['Sub-Category'].unique().tolist()
    )
else:
    subcats = ['All Sub-Categories'] + sorted(df['Sub-Category'].unique().tolist())
selected_subcat = st.sidebar.selectbox("Select Sub-Category:", subcats)

# Year Filter
if 'Year' in df.columns:
    all_years = ['All Years'] + sorted(df['Year'].unique().tolist())
    selected_year = st.sidebar.selectbox("Select Year:", all_years)
else:
    selected_year = 'All Years'

# ============================================================
# Apply Filters
# ============================================================
filtered_df = df.copy()

if selected_region != 'All Regions':
    filtered_df = filtered_df[filtered_df['Region'] == selected_region]

if selected_category != 'All Categories':
    filtered_df = filtered_df[filtered_df['Category'] == selected_category]

if selected_subcat != 'All Sub-Categories':
    filtered_df = filtered_df[filtered_df['Sub-Category'] == selected_subcat]

if selected_year != 'All Years':
    filtered_df = filtered_df[filtered_df['Year'] == selected_year]

st.sidebar.markdown("---")
st.sidebar.markdown(f"**Showing {len(filtered_df):,} records**")

# ============================================================
# KPI Cards - Row 1
# ============================================================
st.subheader("📈 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

total_sales = filtered_df['Sales'].sum()
total_profit = filtered_df['Profit'].sum()
total_orders = filtered_df['Order ID'].nunique()
profit_margin = (total_profit / total_sales * 100) if total_sales > 0 else 0

with col1:
    st.metric(
        label="💰 Total Sales",
        value=f"${total_sales:,.0f}",
        delta=f"{total_sales/1e6:.2f}M"
    )

with col2:
    st.metric(
        label="📊 Total Profit",
        value=f"${total_profit:,.0f}",
        delta=f"{profit_margin:.1f}% margin"
    )

with col3:
    st.metric(
        label="📦 Total Orders",
        value=f"{total_orders:,}"
    )

with col4:
    total_customers = filtered_df['Customer Name'].nunique()
    st.metric(
        label="👥 Total Customers",
        value=f"{total_customers:,}"
    )

st.markdown("---")

# ============================================================
# Charts - Row 2
# ============================================================
col1, col2 = st.columns(2)

with col1:
    st.subheader("📦 Sales by Category")
    sales_by_cat = filtered_df.groupby('Category')['Sales'].sum().sort_values()

    fig, ax = plt.subplots(figsize=(8, 5))
    colors = ['#4ECDC4', '#FF6B6B', '#45B7D1']
    bars = ax.barh(sales_by_cat.index, sales_by_cat.values,
                   color=colors, edgecolor='black')
    for bar, val in zip(bars, sales_by_cat.values):
        ax.text(val + 100, bar.get_y() + bar.get_height()/2,
                f'${val:,.0f}', va='center',
                fontsize=10, fontweight='bold')
    ax.set_title('Total Sales by Category', fontweight='bold')
    ax.set_xlabel('Sales ($)')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

with col2:
    st.subheader("🌍 Profit by Region")
    profit_by_region = filtered_df.groupby('Region')['Profit'].sum()\
                                   .sort_values(ascending=False).head(10)

    fig, ax = plt.subplots(figsize=(8, 5))
    bar_colors = ['#FF6B6B' if v < 0 else '#4ECDC4'
                  for v in profit_by_region.values]
    ax.bar(range(len(profit_by_region)), profit_by_region.values,
           color=bar_colors, edgecolor='black')
    ax.set_xticks(range(len(profit_by_region)))
    ax.set_xticklabels(profit_by_region.index,
                        rotation=45, ha='right', fontsize=9)
    ax.set_title('Profit by Region (Red = Loss)', fontweight='bold')
    ax.set_ylabel('Profit ($)')
    ax.axhline(y=0, color='black', linewidth=1)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

st.markdown("---")

# ============================================================
# Charts - Row 3
# ============================================================
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏆 Top 5 Customers by Sales")
    top5 = filtered_df.groupby('Customer Name')['Sales'].sum()\
                       .sort_values(ascending=False).head(5)

    fig, ax = plt.subplots(figsize=(8, 5))
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
    bars = ax.barh(top5.index, top5.values,
                   color=colors, edgecolor='black')
    for bar, val in zip(bars, top5.values):
        ax.text(val + 10, bar.get_y() + bar.get_height()/2,
                f'${val:,.0f}', va='center',
                fontsize=10, fontweight='bold')
    ax.set_title('Top 5 Customers by Sales', fontweight='bold')
    ax.set_xlabel('Total Sales ($)')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

with col2:
    st.subheader("🎯 Sales by Segment")
    sales_by_seg = filtered_df.groupby('Segment')['Sales'].sum()

    fig, ax = plt.subplots(figsize=(8, 5))
    colors = ['#4ECDC4', '#FF6B6B', '#45B7D1']
    ax.pie(sales_by_seg.values, labels=sales_by_seg.index,
           colors=colors, autopct='%1.1f%%',
           startangle=90, textprops={'fontsize': 12})
    ax.set_title('Sales Distribution by Segment', fontweight='bold')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

st.markdown("---")

# ============================================================
# Sales Trend Over Time
# ============================================================
if 'Year' in filtered_df.columns:
    st.subheader("📅 Sales Trend Over Time")

    yearly = filtered_df.groupby('Year').agg({
        'Sales': 'sum',
        'Profit': 'sum'
    }).reset_index()

    fig, axes = plt.subplots(1, 2, figsize=(16, 5))

    axes[0].plot(yearly['Year'], yearly['Sales'],
                 marker='o', linewidth=2.5,
                 color='#4ECDC4', markersize=8)
    axes[0].fill_between(yearly['Year'], yearly['Sales'],
                         alpha=0.3, color='#4ECDC4')
    axes[0].set_title('Yearly Sales Trend', fontweight='bold')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Total Sales ($)')
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(yearly['Year'], yearly['Profit'],
                 marker='s', linewidth=2.5,
                 color='#FF6B6B', markersize=8)
    axes[1].fill_between(yearly['Year'], yearly['Profit'],
                         alpha=0.3, color='#FF6B6B')
    axes[1].set_title('Yearly Profit Trend', fontweight='bold')
    axes[1].set_xlabel('Year')
    axes[1].set_ylabel('Total Profit ($)')
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    st.pyplot(fig)
    plt.close()

st.markdown("---")

# ============================================================
# Sub-Category Performance Table
# ============================================================
st.subheader("📋 Sub-Category Performance Summary")

subcat_summary = filtered_df.groupby('Sub-Category').agg({
    'Sales': 'sum',
    'Profit': 'sum',
    'Order ID': 'nunique'
}).rename(columns={'Order ID': 'Orders'}).round(2)

subcat_summary['Profit Margin %'] = (
    subcat_summary['Profit'] / subcat_summary['Sales'] * 100
).round(2)
subcat_summary = subcat_summary.sort_values('Sales', ascending=False)

st.dataframe(subcat_summary.style.format({
    'Sales': '${:,.2f}',
    'Profit': '${:,.2f}',
    'Profit Margin %': '{:.2f}%'
}), use_container_width=True)

st.markdown("---")

# ============================================================
# Footer
# ============================================================
st.markdown("""
**📊 Global Superstore Business Intelligence Dashboard**
Built with Python & Streamlit | DevelopersHub Corporation Data Science Internship
""")