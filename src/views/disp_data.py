import streamlit as st

from modules.df_config import DF_CONFIG  # type: ignore


def disp_data(area=st, data=None, height="small", editable=False):
    if editable:
        d = area.data_editor(
            data,
            width=DF_CONFIG["width"],
            height=DF_CONFIG["height"][height],
            hide_index=True,
            column_config=DF_CONFIG["column config"],
            disabled=DF_CONFIG["disabled columns"],
            column_order=DF_CONFIG["disp columuns"],
        )
    else:
        d = area.dataframe(
            data,
            width=DF_CONFIG["width"],
            height=DF_CONFIG["height"][height],
            hide_index=True,
            column_config=DF_CONFIG["column config"],
            column_order=DF_CONFIG["disp columuns"],
        )
    return d
