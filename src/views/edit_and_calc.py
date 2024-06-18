import time

import streamlit as st

from modules.utils import calc, update_data, write_data  # type: ignore
from views.disp_data import disp_data  # type: ignore


def edit_and_calc(area, data, filtered_data):
    container = area.empty()
    cols = area.columns([12, 7, 8, 58])

    radio = cols[0].radio(
        "Mode",
        ["Edit", "Delete Selected", "Calc All"],
        key="radio",
        label_visibility="collapsed",
        disabled=False,
        # horizontal=True,
    )

    edit_mode = False
    delete_mode = False
    calc_mode = False
    if radio == "Edit":
        edit_mode = True
    elif radio == "Delete Selected":
        delete_mode = True
    else:
        calc_mode = True

    save_button = cols[1].button("Save", disabled=(not edit_mode))
    delete_button = cols[2].button("Delete", disabled=(not delete_mode))
    calc_button = cols[3].button("Calculate", disabled=(not calc_mode))

    df_edited = disp_data(
        area=container,
        data=filtered_data,
        height="tall",
        edit=edit_mode,
        delete_=delete_mode,
        key="edit_and_calc",
    )

    if radio == "Edit":
        # 保存ボタンを押さなければ何もしない
        if not save_button:
            return None

        # 以下は保存ボタンを押した場合
        write_data(df_edited)
        inform_modified()
    elif radio == "Delete Selected":
        # 削除ボタンを押さなければ何もしない
        if not delete_button:
            return None

        # 削除ボタンを押した場合
        uuids_to_delete = list(filtered_data.iloc[df_edited.selection.rows]["uuid"])
        # print(uuids_to_delete)
        print(data[~data["uuid"].isin(uuids_to_delete)])
        write_data(data[~data["uuid"].isin(uuids_to_delete)])
        inform_deleted()
    else:
        # 計算ボタンを押さなければ何もしない
        if not calc_button:
            return None

        # 以下は計算ボタンを押した場合
        calc_request(data)


@st.experimental_dialog("Saved")
def inform_modified():
    time.sleep(0.5)
    st.rerun()


@st.experimental_dialog("Deleted")
def inform_deleted():
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
