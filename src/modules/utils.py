import os
from datetime import datetime
from uuid import uuid4

import numpy as np
import pandas as pd


def filter(data, name_=None, type_=None, size_max=None, size_min=None, status=None):
    df1 = data.copy()  # DataFrameをコピー

    # 'name'カラムに対する部分一致検索
    if name_:
        df1 = df1[df1["name"].str.contains(name_, na=False)]

    # 'type'カラムに対する部分一致検索
    if type_:
        df1 = df1[df1["type"].str.contains(type_, na=False)]

    # 'size'カラムに対する範囲検索
    if size_min is not None:
        df1 = df1[df1["size_x"] >= size_min]
        df1 = df1[df1["size_y"] >= size_min]
        df1 = df1[df1["size_z"] >= size_min]
    if size_max is not None:
        df1 = df1[df1["size_x"] <= size_max]
        df1 = df1[df1["size_y"] <= size_max]
        df1 = df1[df1["size_z"] <= size_max]

    # statusカラムに対する完全一致＆複数検索
    # 何も選択されていない場合、全てのデータを表示
    if status:
        df1 = df1[df1["status"].isin(status)]

    return df1


__DATA_PATH = "./assets/data.csv"


def read_data():
    data = pd.read_csv(__DATA_PATH, encoding="utf-8")  # データの取得
    data["id_by_user"] = data["id_by_user"].astype(str).replace("nan", "")
    data["reference"] = data["reference"].astype(str).replace("nan", "")
    data["first_upload_date"] = pd.to_datetime(data["first_upload_date"])
    data["update_date"] = pd.to_datetime(data["update_date"])
    return data


def write_data(data):
    data["first_upload_date"] = data["first_upload_date"].apply(
        lambda x: x.isoformat() if pd.notnull(x) else None
    )
    data["update_date"] = data["update_date"].apply(
        lambda x: x.isoformat() if pd.notnull(x) else None
    )

    data.to_csv(__DATA_PATH, index=False)


# todo 一括で回るようにするべき
def append_filename_to_reference(data: pd.DataFrame, filename: str):
    # 条件に一致する行を抽出し、referenceカラムの値を文字列型に変換してから末尾にfilenameを付け足す
    filename = os.path.splitext(os.path.basename(filename))[0]
    mask = data["id_by_user"].apply(lambda x: x in filename if x != "" else False)
    print(data["id_by_user"])
    print(mask)
    data.loc[mask, "reference"] = data.loc[mask, "reference"].apply(
        lambda x: (f"{x}, " if x != "" else "") + filename
    )
    return data


def add_new_data1(data, id_by_user, name_, type_, size_x, size_y, size_z, remarks):
    now = pd.to_datetime(datetime.now())
    data_new = pd.DataFrame(
        [
            [
                str(uuid4()),
                id_by_user,
                name_,
                type_,
                size_x,
                size_y,
                size_z,
                remarks,
                now,
                now,
                None,
                -1,
                "just_uploaded",
            ]
        ],
        columns=data.columns,
    )
    write_data(pd.concat([data, data_new]))


def add_new_data2(data, csv_):
    now = pd.to_datetime(datetime.now())
    data_new = pd.read_csv(csv_).rename(columns={"id": "id_by_user"})
    data_new["uuid"] = str(uuid4())
    data_new["first_upload_date"] = now
    data_new["update_date"] = now
    data_new["reference"] = ""
    data_new["rate"] = -1
    data_new["status"] = "just_uploaded"
    write_data(pd.concat([data, data_new]))


def calc(data: pd.DataFrame):
    # statusがjust_uploadedの行をフィルタリング
    mask = data["status"] == "just_uploaded"
    print(mask)

    # 乱数を生成してrateカラムに入れる
    data.loc[mask, "rate"] = np.random.random(size=mask.sum())

    # update_dateカラムに現在の日時を入れる
    now = pd.to_datetime(datetime.now())
    data.loc[mask, "update_date"] = now
    # statusを更新する
    data.loc[mask, "status"] = "under_review"

    # CSVに書き出す
    write_data(data)


def update_data(
    df_filtered_edited: pd.DataFrame, df_filtered: pd.DataFrame, df_total: pd.DataFrame
):
    now = pd.to_datetime(datetime.now())

    # 値が異なる行を取得
    diff = df_filtered_edited[df_filtered_edited.ne(df_filtered)].dropna(how="all")

    # df_totalを更新
    for index, row in diff.iterrows():
        # df_totalの該当行を更新
        df_total.loc[df_total["uuid"] == row["uuid"], df_total.columns] = row
        # update_dateカラムに現在の日時を入れる
        df_total.loc[df_total["uuid"] == row["uuid"], "update_date"] = now

    # CSVに書き出す
    write_data(df_total)
