# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 15:31:17 2022

@author: carlo
"""
import pandas as pd
import numpy as np
import re, time
import datetime as dt
from datetime import datetime 
from pytz import timezone
import streamlit as st

phtime = timezone('Asia/Manila')

def update():
    st.experimental_memo.clear()
    st.experimental_rerun()


if __name__ == '__main__':
    if 'time_update' not in st.session_state:
        st.session_state['time_update'] = dt.time(3,0, tzinfo=phtime)
        
    t = st.sidebar.time_input('Set app to update at: ', dt.time(3,0, tzinfo=phtime))
    st.session_state['time_update'] = t

    while True:
    # refresh every hour
        time.sleep(10)
        time_now = phtime.localize(datetime.now())
        st.write(st.session_state)
        #time.sleep(3600)
        
        if time_now.hour == st.session_state['time_update'].hour:
            update()
            st.write('Code rerun.')