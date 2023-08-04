mport streamlit as st
import oracledb
import pandas as pd


class OracleOnPrem:
    class Model:
        pageTitle = "Streamlit Connect Oracle Database On Premses"

    def view(self, model):
        st.title(model.pageTitle)


        with st.container():
            conn = st.experimental_connection('oracle_onprem_db', type='sql')
            sql1 = conn.query('select * from Oracle_Onprem_demo', ttl=100)
            st.dataframe(sql1)
