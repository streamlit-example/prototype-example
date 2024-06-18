import streamlit as st
from streamlit import session_state as stss

from modules.utils import (  # type: ignore
    add_new_data1,
    add_new_data2,
    append_filename_to_reference,
    write_data,
)
from views.disp_data import disp_data  # type: ignore


def add_data(area, data, filtered_data):
    disp_data(area=st, data=filtered_data)
    columns_ = area.columns([2, 3])
    columns_[0].subheader("Upload")
    add_files(area=columns_[0], data=data)
    add_csv(area=columns_[0], data=data)
    add_row(area=columns_[1], data=data)


def add_row(area, data):
    area.subheader("Add Data")

    cols1 = area.columns(3)
    id_by_user = cols1[0].text_input("ID", key=f"add_row_id_{stss.id_add_row}")
    name_ = cols1[1].text_input("Name", key=f"add_row_name_{stss.id_add_row}")
    type_ = cols1[2].text_input("Type", key=f"add_row_type_{stss.id_add_row}")

    cols2 = area.columns(3)
    size_x = cols2[0].number_input(
        "Size 1", value=None, key=f"add_row_s1_{stss.id_add_row}"
    )
    size_y = cols2[1].number_input(
        "Size 2", value=None, key=f"add_row_s2_{stss.id_add_row}"
    )
    size_z = cols2[2].number_input(
        "Size 3", value=None, key=f"add_row_s3_{stss.id_add_row}"
    )

    remarks = area.text_input(
        "Remarks (optional)", "", key=f"add_row_remarks_{stss.id_add_row}"
    )

    if not area.button("Add data"):
        return

    add_new_data1(data, id_by_user, name_, type_, size_x, size_y, size_z, remarks)

    stss.id_add_row += 1
    st.rerun()


def add_files(area, data):
    files = area.file_uploader(
        "Files", accept_multiple_files=True, key=f"files_uploader{stss.id_add_files}"
    )

    # アップロードファイルが未選択の場合ははじく
    if not files:
        return None

    if not area.button("Upload Files"):
        return

    for file in files:
        write_data(append_filename_to_reference(data, file.name))
    stss.id_add_files += 1
    st.rerun()


def add_csv(area, data):
    csv_ = area.file_uploader("CSV", type="csv", key=f"csv_uploader{stss.id_add_csv}")

    # アップロードファイルが未選択の場合ははじく
    if not csv_:
        return None
    if not area.button("Upload CSV"):
        return

    add_new_data2(data, csv_)

    stss.id_add_csv += 1
    st.rerun()
