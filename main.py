import company_api
import company_storage



def get_company(company_id):
    """
    輸入STR
    依統一編號取得資料。

    查詢順序：
    1. 本機 JSON
    2. 公司登記 API
    3. 商業登記 API
    4. 都找不到回傳 None
    """
    print(f"\n*******開始流程處理 {company_id}*******")
    
    
    # ① 本機
    company = company_storage.load_company(company_id)
    print(company)

    if company is not None:
        print("[1 本機] 找到資料")
        return company
    print("[1 本機] 找不到")
    # ② 公司登記 API
    result = company_api.fetch_company_data(company_id)
    print("result讀出來的資料是",result)
    if result is not None:
        # 有找到的狀況下
        print("[2 公司API] 找到")
        company_data, business_data = result
        print(f"確認company_data的資料行型態是list是",type(result))
        print(f"確認company_data的資料行型態是list的company_data是",type(company_data))
        print(f"確認company_data的資料行型態是list的business_data是",type(business_data))
        # 公司登記建立字典資料
        company = company_api.build_company(company_data, business_data)
        print("兩段字典組合",company)
        print("build_company資料類型",type(company))
    #   #存資料下來
        company_storage.save_company(company)
        return company
    print("[2 公司API] 找不到")
    basic_data = company_api.fetch_business_basic(company_id)
    print("回傳回來fetch_business_basic是資料型態:",type(basic_data))
    print(basic_data)
    print(f"\n******* 結束流程處理 {company_id}*******")  
    if basic_data is not None:
        ...
        print("----------商業應用三結果----------------：", basic_data)
        print("型態：", type(basic_data))
        print("[2 公司應用三API] 開始查詢")
        agency = company_api.agency_detail(basic_data)
        print("型態：", type(agency))
        company_data,business_datag = company_api.fetch_business_data(company_id,agency)
        print("讀取",company_data)
        print("讀取",business_datag)

        try:
            business_data = company_api.build_business(company_data,business_datag)
            company_storage.save_company(business_data)
        except TypeError as e:
            print(f"[跳過] {company_id} 商業資料格式例外：{e}")
            return None
        print("-----------存檔成功 商業登記資料------------")

    
if __name__ == "__main__":


    company_ids = ["91551501",]


    for company_id in company_ids:
        if not company_api.validate_company_id(company_id):
        
            continue
        campany = get_company(company_id)
        print("get_company轉出的資料類型是",type(get_company))
        print(f"===== 結束處理{company_id} =====")


# company_id
# 例如 "91551501"
#         │
#         ▼
# load_company(company_id)
#         │
#      本機有嗎？
#      ┌──┴──┐
#      有    沒有
#      │      │
#      ▼      ▼
#   company  fetch_company_data()
#                 │
#              公司有嗎？
#              ┌──┴──┐
#              有    沒有
#              │      │
#              ▼      ▼
#       build_company()   fetch_business_data(company_id)
#                              │
#                              │
#                              ▼
#                     fetch_business_basic()
#                        【應用三】
#                              │
#                          商業有嗎？
#                          ┌──┴──┐
#                          沒有   有
#                          │      │
#                          ▼      ▼
#                        None   取得 Agency
#                                 │
#                                 ▼
#                       fetch_business_detail()
#                          【應用一】
#                                 │
#                                 ▼
#                         取得資本額等資料
#                                 │
#                                 ▼
#                  return detail_data, basic_data
#                                 │
#                                 ▼
#                          build_business()
#                                 │
#                                 ▼
#                             company
#                                 │
#                                 ▼
#                          save_company()
