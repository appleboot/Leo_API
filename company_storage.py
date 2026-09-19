from datetime import datetime
import json


def save_company(company):
    """
    將一筆公司資料儲存到 company_data.json。
    如果 JSON 裡原本已有其他公司，會先讀取舊資料，
    再新增或更新這次的公司資料。
    """

    
    # print("company =", company)
    print("type =", type(company))
    # 加入快取時間，記錄這筆公司資料最後更新的時間
    company["cached_at"] = datetime.now().isoformat(timespec="seconds")

    # 先嘗試讀取原本的 JSON
    # companies 代表「所有公司的資料」
    try:
        with open("company_data.json", "r", encoding="utf-8") as file:
            companies = json.load(file)

    # 如果 company_data.json 還不存在
    # 代表目前還沒有任何公司資料，所以建立空字典
    except FileNotFoundError:
        companies = {}

    # 把這次查詢到的 company 放進 companies
    # 使用統一編號當作 key
    #
    # 例如：
    # companies["45879860"] = company
    #
    # 如果統編原本不存在 → 新增
    # 如果統編原本已存在 → 更新（覆蓋）該公司的舊資料
    companies[company["company_id"]] = company

    # 將更新完成的所有公司資料寫回 JSON
    with open("company_data.json", "w", encoding="utf-8") as file:
        print("[save_company] 準備寫入 JSON：")
        json.dump(
            companies,
            file,
            ensure_ascii=False,  # 中文直接顯示，不轉成 Unicode 編碼
            indent=4             # JSON 使用 4 格縮排，比較容易閱讀
        )


# def load_company(company_id):
#     """
#     根據統一編號，從 company_data.json 尋找公司資料。

#     找到：
#         return 該公司的 dict

#     找不到：
#         return None
#     """

#     # 讀取 JSON 裡所有公司的資料
#     with open("company_data.json", "r", encoding="utf-8") as file:
#         companies = json.load(file)

#     # 判斷統一編號是否存在於 companies 的 key 裡
#     #
#     # 例如：
#     # "45879860" in companies
#     if company_id in companies:

#         # 找到公司 → 回傳這家公司的完整資料
#         return companies[company_id]

#     # 找不到公司 → 回傳 None
#     return None


def load_company(company_id):


    try:
        with open("company_data.json", "r", encoding="utf-8") as file:
            companies = json.load(file)

    except FileNotFoundError:

        # 沒有 JSON，就先建立一個空的 JSON
        with open("company_data.json", "w", encoding="utf-8") as file:
            json.dump({}, file)

        return None

    if company_id in companies:
        return companies[company_id]

    return None