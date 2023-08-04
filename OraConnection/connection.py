from streamlit.connections import ExperimentalBaseConnection
from streamlit.runtime.caching import cache_data
import os
import oracledb
import pandas as pd

class OracleConnect(ExperimentalBaseConnection[oracledb.connect]):
    """Basic st.experimental_connection implementation for OracleDB"""

    def _connect(self, **kwargs) -> oracledb.connect:
        if 'url' in kwargs:
            url = kwargs.pop('url')   
        elif 'url' in os.environ:
            url = os.environ['url']            
        else:
            url = self._secrets['url']
        return oracledb.connect(url)
    
    def cursor(self) -> oracledb.connect:
        return self._instance.cursor()

    def query(self, query: str, ttl: int = 3600, **kwargs) -> pd.DataFrame:
        @cache_data(ttl=ttl)
        def _query(query: str, **kwargs) -> pd.DataFrame:
            cursor = self.cursor()
            cursor.execute(query, **kwargs)
            return cursor.df()        
        return _query(query, **kwargs)
        
