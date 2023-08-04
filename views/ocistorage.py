import streamlit as st
import numpy as np
import pandas as pd
import os
from st_files_connection import FilesConnection
os.environ['OCIFS_IAM_TYPE'] = "api_key"



class OciObjectSrore:
    class Model:
        pageTitle = "Read Data from OCI object storage using streamlit experimental connection"

    def view(self, model):
        st.title(model.pageTitle)


        with st.container():
            # Create connection object and retrieve file contents.
            # Specify input format is a csv and to cache the result for 600 seconds.
            conn = st.experimental_connection('oci', type=FilesConnection)
            df = conn.read("oci://Subratbook@idscalqnjgj5/table.csv", input_format="csv", ttl=600)
            st.dataframe(df)
            # Print results.
            #for row in df.itertuples():
            #    st.write(f"{row.DNAME} has a :{row.DNAME}:")
