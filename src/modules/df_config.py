from datetime import datetime

import streamlit as st

__DATETIME_FORMAT = "YYYY/MM/DD hh:mm"

__DISP_COLUMNS = [
    "id_by_user",
    "name",
    "type",
    "size_x",
    "size_y",
    "size_z",
    "remarks",
    "first_upload",
    "update",
    "reference",
    "rate",
    "status",
]


DF_CONFIG = {
    "width": 2500,
    "height": {"small": 230, "tall": 570},
    "disabled columns": [
        "id_by_user",
        "first_upload",
        "update",
        "rate",
        "status",
        "reference",
    ],
    "disp columuns": __DISP_COLUMNS,
    "column config": {
        "id_by_user": st.column_config.TextColumn(
            "ID",
            max_chars=50,
            # validate="^st\.[a-z_]+$",
        ),
        "name": st.column_config.TextColumn(
            "Name",
            max_chars=50,
        ),
        "type": st.column_config.TextColumn(
            "Type",
            max_chars=50,
        ),
        "size_x": st.column_config.NumberColumn(
            "Size X [cm]",
            help="size x of the weapon",
            min_value=0,
            max_value=1000,
            step=0.01,
            format="%.2f",
        ),
        "size_y": st.column_config.NumberColumn(
            "Size Y [cm]",
            help="size y of the weapon",
            min_value=0,
            max_value=1000,
            step=0.01,
            format="%.2f",
        ),
        "size_z": st.column_config.NumberColumn(
            "Size Z [cm]",
            help="size z of the weapon",
            min_value=0,
            max_value=1000,
            step=0.01,
            format="%.2f",
        ),
        "remarks": st.column_config.TextColumn(
            "Remarks",
            max_chars=200,
        ),
        "first_upload": st.column_config.DatetimeColumn(
            "First Upload",
            min_value=datetime(2024, 6, 1),
            max_value=datetime(2030, 1, 1),
            format=__DATETIME_FORMAT,
            step=60,
        ),
        "update": st.column_config.DatetimeColumn(
            "Last Update",
            min_value=datetime(2024, 6, 1),
            max_value=datetime(2030, 1, 1),
            format=__DATETIME_FORMAT,
            step=60,
        ),
        "reference": st.column_config.ListColumn(
            "References",
            help="The reference files you have uploaded",
            width="medium",
        ),
        "rate": st.column_config.ProgressColumn(
            "Rate",
            format="%.2f",
            min_value=0,
            max_value=1,
        ),
        "status": st.column_config.TextColumn(
            "Status",
        ),
    },
}
