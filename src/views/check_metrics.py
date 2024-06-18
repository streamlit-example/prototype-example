import matplotlib.pyplot as plt
import streamlit as st

from views.disp_data import disp_data  # type: ignore


def check_metrics(area, data, filtered_data):
    disp_data(area=st, data=filtered_data)
    cols = area.columns(3)
    cols[0].scatter_chart(data=data, x="size_x", y="rate")
    cols[1].bar_chart(data.sort_values("rate", ascending=False), x="name", y="rate")
    data_count = data["status"].value_counts()
    fig, ax = plt.subplots()
    ax.pie(list(data_count.values), labels=list(data_count.index))
    cols[2].pyplot(fig)
