import streamlit as st
from streamlit_option_menu import option_menu
from tools.utilities import load_css
from OraConnection.connection import OracleConnect

from views.ocistorage import OciObjectSrore
from views.oracledatabase import OracleOnPrem
from views.ociautonomousdb import OciAutoDB

st.set_page_config(
    page_title="Streamlit Connector Demo",
    page_icon="favicon.ico",
    layout="wide"
)

load_css()


class Model:
    menuTitle = "Streamlit Connector for Oracle"
    option1 = "Connect to OCI storage"
    option2 = "Connect to Oracle OnPrem DB"
    option3 = "Connect To OCI autonomous DB"

    menuIcon = "menu-up"
    icon1 = "speedometer"
    icon2 = "activity"
    icon3 = "motherboard"
  



def view(model):
    with st.sidebar:
        menuItem = option_menu(model.menuTitle,
                               [model.option1, model.option2, model.option3],
                               icons=[model.icon1, model.icon2, model.icon3],
                               menu_icon=model.menuIcon,
                               default_index=0,
                               styles={
                                   "container": {"padding": "5!important", "background-color": "#fafafa"},
                                   "icon": {"color": "black", "font-size": "25px"},
                                   "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px",
                                                "--hover-color": "#eee"},
                                   "nav-link-selected": {"background-color": "#037ffc"},
                               })

    with st.sidebar:
        st.markdown("---")
        st.text("User: Subrata Kumar Parida")
        st.text("Version: 0.0.1")
        st.button("Logout")
        st.markdown("---")

    if menuItem == model.option1:
        OciObjectSrore().view(OciObjectSrore.Model())

    if menuItem == model.option2:
        OracleOnPrem().view(OracleOnPrem.Model())

    if menuItem == model.option3:
        OciAutoDB().view(OciAutoDB.Model())



view(Model())
