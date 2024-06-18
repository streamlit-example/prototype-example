import streamlit as st

from modules.df_config import DF_CONFIG  # type: ignore


def disp_data(area=st, data=None, height="small", edit=False, delete_=False, key=None):
    if edit:
        d = area.data_editor(
            data,
            width=DF_CONFIG["width"],
            height=DF_CONFIG["height"][height],
            hide_index=True,
            column_config=DF_CONFIG["column config"],
            disabled=DF_CONFIG["disabled columns"],
            column_order=DF_CONFIG["disp columuns"],
        )
    elif delete_:
        d = area.dataframe(
            data,
            width=DF_CONFIG["width"],
            height=DF_CONFIG["height"][height],
            hide_index=True,
            column_config=DF_CONFIG["column config"],
            column_order=DF_CONFIG["disp columuns"],
            selection_mode=["multi-row"],
            on_select="rerun",
            key=key,
        )
    else:
        d = area.dataframe(
            data,
            width=DF_CONFIG["width"],
            height=DF_CONFIG["height"][height],
            hide_index=True,
            column_config=DF_CONFIG["column config"],
            column_order=DF_CONFIG["disp columuns"],
            selection_mode=["multi-row"],
        )
    return d
