import streamlit as st
import oracledb
import pandas as pd

class OciAutoDB:
    class Model:
        pageTitle = "Connecting OCI Cloud Oracle Autonomous Database"

    def view(self, model):
        st.title(model.pageTitle)



        with st.container():
            conn = st.experimental_connection('oci_cloud_db', type='sql')
            sql2 = conn.query('select * from OCI_AUTONOMOUS_DB_CONN', ttl=100)
            st.dataframe(sql2)
