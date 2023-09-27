import streamlit as st
from page6 import app
import os

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

import pysqlite3
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

app()