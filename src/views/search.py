import streamlit as st

from modules.utils import filter  # type: ignore


# 検索
def search(area, data):
    area.title("Search Commands")
    status_ = area.multiselect(
        "Status", options=["just_uploaded", "calculating", "calculated"]
    )
    name_ = area.text_input("Name")
    type_ = area.text_input("Type")
    max_size = area.number_input("Max Size", value=None)
    min_size = area.number_input("Min Size", value=None)

    filtered_data = filter(data, name_, type_, max_size, min_size, status_)

    area.title("Reload")
    if area.button("Reload Data"):
        st.rerun()

    return filtered_data
