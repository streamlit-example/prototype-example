import time

import streamlit as st

from modules.utils import calc, write_data  # type: ignore
from views.disp_data import disp_data  # type: ignore


def edit_and_calc(area, data, filtered_data):
    container = area.empty()
    col_l, col_r = area.columns([1, 7])
    edit_mode = col_l.checkbox("Edit Mode")

    df_edited = disp_data(
        area=container, data=filtered_data, height="tall", editable=edit_mode
    )

    if edit_mode:
        # 変更反映ボタンを押さなければ何もしない
        if not col_r.button("Save Changes"):
            return None

        # 以下は変更反映ボタンが押された場合

        write_data(df_edited)
        inform_modified()
    else:
        # 計算実行ボタンを押さなければ何もしない
        if not col_r.button("Request Calculation"):
            return None

        # 以下は計算実行ボタンが押された場合
        calc_request(data)


@st.experimental_dialog("Modification saved")
def inform_modified():
    time.sleep(0.5)
    st.rerun()


@st.experimental_dialog("Calculate")
def calc_request(data):
    st.write("Are you sure you want to request calculation?")
    st.text_input("Any Comments:")
    if st.button("Request"):
        calc(data)
        st.success("Requested calculation succesfully")
        time.sleep(0.5)
        st.rerun()
