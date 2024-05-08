import streamlit as st

# Initialize connection.
conn = st.connection("snowflake")

# Perform query.
df = conn.query("SELECT * from EMP;", ttl=600)
df2 = conn.query("select * from EMP where SEX='F' and EMP_TITLE_ID ='e0002'")
df2
# Print results.
'''for row in df.itertuples():
    st.write(f"{row.NAME} has a :{row.PET}:")'''