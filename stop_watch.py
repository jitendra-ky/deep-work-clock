from datetime import timedelta
import streamlit as st
import time
from mylib import read_state

st.set_page_config(
    page_title="stop-watch",
    page_icon="⏱️",
    layout="centered",
)

st.title("⏱️ Stop Watch")

states = read_state("state_stop_watch.txt")
elapsed_time = int(states.get("elapsed_time", 0))
elapsed_time

'Press the button to start the stop watch'
time_show = st.text("Elapsed Time: 0.00 sec")
if st.button("replay"):
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time 
        time_show.text(f"Elapsed Time: {elapsed_time:.2f} sec")
        time.sleep(0.1)
    st.write("Stop Watch Stopped")

st.button("reset")