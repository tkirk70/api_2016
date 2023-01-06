# Import dependencies
import pandas as pd
import streamlit as st 

# Load df from excel
df = pd.read_excel('combined_newbees_draft.xlsx')
# Get rid of index
df.reset_index(drop=True, inplace=True)

# Create header and subheader
st.title('Sortable Newbees Drafts: 2013-2020')
st.subheader('Use the dropdowns on the left to sort through different teams or years.')

# Diplay the default dataframe.
st.dataframe(df)


st.write('Where did you go wrong?')
