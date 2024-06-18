import streamlit as st
from streamlit import session_state as stss

from modules.utils import read_data
from views.add_data import add_data  # type: ignore
from views.check_metrics import check_metrics  # type: ignore
from views.disp_data import disp_data  # type: ignore
from views.modify_and_calc import modify_and_calc  # type: ignore
from views.search import search  # type: ignore

# セッション状態の初期化
# if "need_update" not in stss:
#     stss.need_update = True

data = read_data()

if "id_add_row" not in stss:
    stss.id_add_row = 0
if "id_add_csv" not in stss:
    stss.id_add_csv = 0
if "id_add_files" not in stss:
    stss.id_add_files = 0
if "need_edit" not in stss:
    stss.need_edit = False


# ページ全般の設定
st.set_page_config(layout="wide")

# ヘッダー
st.header("Wireframe Sample", divider="gray")

# サイドバー: 検索条件入力欄
filtered_df = search(area=st.sidebar, data=data)

# タブ
tabs = st.tabs(["Add Data", "Modify Data & Calculate", "Check Metrics"])
with tabs[0]:
    add_data(area=st, data=data, filtered_df=filtered_df)

with tabs[1]:
    modify_and_calc(area=st, data=data, filtered_df=filtered_df)

with tabs[2]:
    check_metrics(
        area=st, data=data, filtered_df=filtered_df
    )  # 全データ(df)に対する指標を表示
