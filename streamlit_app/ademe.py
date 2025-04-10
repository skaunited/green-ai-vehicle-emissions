import sys
import os
from pathlib import Path

# Ajouter le chemin racine au PYTHONPATH
root_dir = Path(__file__).parent.parent  # remonte à mon_projet/
sys.path.append(str(root_dir))

import streamlit as st
import pandas as pd
from data.raw.ADEME.scripts.DataCleaner import DataCleaner

st.write('fic_etiq_edition_2001.xls')
df_edition_2001 = DataCleaner.load_and_clean_xls('data/raw/ADEME/data/fic_etiq_edition_2001.xls')
st.dataframe(df_edition_2001)

st.write('fic_etiq_edition_2002.xls')
df_edition_2002 = DataCleaner.load_and_clean_xls('data/raw/ADEME/data/fic_etiq_edition_2002.xls')
st.dataframe(df_edition_2002)

st.write('fic_etiq_edition_2003.xls')
df_edition_2003 = DataCleaner.load_and_clean_xls('data/raw/ADEME/data/fic_etiq_edition_2003.xls')
st.dataframe(df_edition_2003)

st.write('fic_etiq_edition_2004.xls')
df_edition_2004 = DataCleaner.load_and_clean_xls('data/raw/ADEME/data/fic_etiq_edition_2004.xls')
st.dataframe(df_edition_2004)

#st.write('fic_etiq_edition_2005.xls')
#df_edition_2005 = DataCleaner.load_and_clean_xls('data/raw/ADEME/data/fic_etiq_edition_2005.xls')
#st.dataframe(df_edition_2005)

#st.write('fic_etiq_edition_2006.xls')
#df_edition_2006 = DataCleaner.load_and_clean_xls('data/raw/ADEME/data/fic_etiq_edition_2006.xls')
#st.dataframe(df_edition_2006)

st.write('fic_etiq_edition_2007.xls')
df_edition_2007 = DataCleaner.load_and_clean_xls('data/raw/ADEME/data/fic_etiq_edition_2007.xls')
st.dataframe(df_edition_2007)

st.write('fic_etiq_edition_2008.xls')
df_edition_2008 = DataCleaner.load_and_clean_xls('data/raw/ADEME/data/fic_etiq_edition_2008.xls')
st.dataframe(df_edition_2008)

st.write('fic_etiq_edition_2009.xls')
df_edition_2009 = DataCleaner.load_and_clean_xls('data/raw/ADEME/data/fic_etiq_edition_2009.xls')
st.dataframe(df_edition_2009)

st.write('fic_etiq_edition_2010.xls')
df_edition_2010 = DataCleaner.load_and_clean_xls('data/raw/ADEME/data/fic_etiq_edition_2010.xls')
st.dataframe(df_edition_2010)

st.write('fic_etiq_edition_2011.xls')
df_edition_2011 = DataCleaner.load_and_clean_xls('data/raw/ADEME/data/fic_etiq_edition_2011.xls')
st.dataframe(df_edition_2011)

st.write("2012")
df_clean_2012 = DataCleaner.load_and_clean_csv('data/raw/ADEME/data/fic_etiq_edition_2012.csv')
st.dataframe(df_clean_2012)

st.write("2013")
df_clean_2013 = DataCleaner.load_and_clean_csv('data/raw/ADEME/data/fic_etiq_edition_2013.csv')
st.dataframe(df_clean_2013)

st.write("2014")
df_clean_2014 = DataCleaner.load_and_clean_csv('data/raw/ADEME/data/fic_etiq_edition_2014.csv')
st.dataframe(df_clean_2014)

st.write("2015")
df_clean_2015 = DataCleaner.load_and_clean_csv('data/raw/ADEME/data/fic_etiq_edition_2015.csv')
st.dataframe(df_clean_2015)
