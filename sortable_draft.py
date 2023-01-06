# Import dependencies
import pandas as pd
import streamlit as st 

# Try to increase width of layout
st.set_page_config(layout="wide")

# Load df from excel
df = pd.read_excel('combined_newbees_draft.xlsx')
# # Filter by year
# years = df['year'].drop_duplicates()
# make_choice = st.sidebar.selectbox('Select your year:', years)
# filtered_df = df[df.loc['year'].is_in(make_choice)]
# st.dataframe(filtered_df)

# Get rid of index
# df.reset_index(drop=True, inplace=True)

# Create header and subheader
st.title('Sortable Newbees Drafts: 2013-2020')
st.subheader('Use the dropdowns on the left to sort through different teams or years.')

# Diplay the default dataframe.
st.dataframe(df, use_container_width=True)

options = df['year'].unique().tolist()
selected_options = st.sidebar.multiselect('Which year do you want?',options)

filtered_df = df[df["year"].isin(selected_options)]

st.dataframe(filtered_df)




st.write('Where did you go wrong?')
