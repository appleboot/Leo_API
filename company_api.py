import requests
def validate_company_id(company_id):

    if not company_id.isdigit() or len(company_id) != 8:
        print("統一編號格式錯誤，請輸入 8 位數字")
        return False
    return True

def fetch_company_data(company_id):
    """
    輸入:str
    這邊是公司登記使用的api 網址
    輸出 response_1.json(),response_2.json()
    輸出:list
    """
    url = f"http://data.gcis.nat.gov.tw/od/data/api/5F64D864-61CB-4D0D-8AD9-492047CC1EA6?$format=json&$filter=Business_Accounting_NO eq {company_id}&$skip=0&$top=50"
    business_url = f"http://data.gcis.nat.gov.tw/od/data/api/236EE382-4942-41A9-BD03-CA0709025E7C?$format=json&$filter=Business_Accounting_NO eq {company_id}&$skip=0&$top=50"

    response_1 = requests.get(url)
    response_2 = requests.get(business_url)
        # 先觀察 API 到底回了什麼
    print("統一編號:", company_id)

    print("API 1 狀態:", response_1.status_code)
    # print("API 1 內容:", repr(response_1.text))

    print("API 2 狀態:", response_2.status_code)
    # print("API 2 內容:", repr(response_2.text))

    if response_1.status_code != 200:
        print("回傳有問題不等於200!!")
        return None
    if not response_1.text:
        print("API 1 回傳空資料")
        return None
    # print("===== 公司基本資料 =====")
    # print(response_1.json())

    if response_2.status_code != 200:
        print("回傳有問題不等於200!!")
        return None
    if not response_2.text:
        print("API 2 回傳空資料")
        return None
    # print("===== 營業項目 =====")
    # print(response_2.json())
    # print("基本資料型別：", type(response_1.json()))
    # print("營業項目型別：", type(response_2.json()))
    return [response_1.json(),response_2.json()]

def fetch_business_data(company_id ,agency):
    print("=進入商業 應用一、二 api程序=")
    """
    輸入:str
    1.讀取url 及business_url的api網子
    2.判斷一些空值(None)
    3.輸出 response_1.json(),response_2.json()
    輸出:list
    """
    url = (
    "https://data.gcis.nat.gov.tw/od/data/api/"
    "7E6AFA72-AD6A-46D3-8681-ED77951D912D"
    "?$format=json"
    f"&$filter=President_No eq {company_id} and Agency eq {agency}"
    "&$skip=0"
    )
    business_url = (
    "http://data.gcis.nat.gov.tw/od/data/api/"
    "F570BC9A-DA4C-4813-8087-FB9CE95F9D38"
    "?$format=json"
    f"&$filter=President_No eq {company_id} and Agency eq {agency}"
    "&$skip=0"
    )
    print("[商業應用一API] 查詢統編:", company_id)
    print("[商業應用一API] URL 1:", url)
    

    response_1 = requests.get(url)
    response_2 = requests.get(business_url)

    print("[商業API] response 1:", repr(response_1.text))
    print("[商業API] response 2:", repr(response_2.text))

    if response_1.status_code != 200:
       print("回傳有問題不等於200!!")
       return None
    if not response_1.text:
       print("商業API 1 回傳空資料")
       return None
    if response_2.status_code != 200:
       print("回傳有問題不等於200!!")
       return None
    if not response_2.text:
       print("API 2 回傳空資料")
       return None
    print("===== 商業基本資料=====")
    print("status:", response_1.status_code)
    print("text:", repr(response_1.text))
    print("url:", response_1.url)
    print("===== 營業項目資料=====")
    print("status:", response_2.status_code)
    print("text:", repr(response_2.text))
    print("url:", response_2.url)
    
    
    print("基本資料型別：", type(response_1.json()))
    print("營業項目型別：", type(response_2.json()))
    print("===== 跑完商業應用一、二=====")
    return [response_1.json(),response_2.json()]

def build_company(company_data, business_data):
    """
    輸出:dict
    """
    # print("測試這裡build_company")

    if len(company_data)>0:
        my_company = {
                "company_name": company_data[0]["Company_Name"],
                "company_id": company_data[0]["Business_Accounting_NO"],
                "responsible_name": company_data[0]["Responsible_Name"],
                "company_location": company_data[0]["Company_Location"],
                "capital": company_data[0]["Capital_Stock_Amount"],
                "paid_in_capital": company_data[0]["Paid_In_Capital_Amount"]
            }
        print(type(my_company))
        print("公司第一段的字典",my_company)
    if len(business_data)>0:
        # print(business_data)
        business_list = business_data[0]["Cmp_Business"]
        business_items = []

        for item in business_list:

            one_item = {
                "Seq_NO": item["Business_Seq_NO"],
                "Item": item["Business_Item"],
                "Item_Desc": item["Business_Item_Desc"]
            }

            business_items.append(one_item)
    my_company["business_items"] = business_items
    # print(my_company.keys())
    # print(type(my_company))

    return my_company

def build_business(company_data,business_data):
    """
    輸入:list
    1.company_data,business_datag   這兩個list                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    2. 輸出的資料{'company_name': '鴻燿商品行', 
    'company_id': '15725713', 
    'responsible_name': '陳世昌', 
    'company_location': '臺南市安南區長安里公學路2段55號1樓', 
    'capital': 200000, 
    'business_items': [{'Seq_NO': '1', 'Item': 'F207030', 'Item_Desc': '清潔用品零售業'}]}
    輸出:dict
    """
    if len(company_data) > 0 :
        print("商業名稱:",company_data[0]["Business_Name"])
        # print(type(company_data[0]["Business_Name"]))
        print("統一編號:",company_data[0]["President_No"])
        print("負責人:",company_data[0]["Responsible_Name"])
        print(f"資本額: {company_data[0]['Business_Register_Funds']:,}")
        print("商業登記地址:",company_data[0]["Business_Address"])
        my_business = {
            "company_name": company_data[0]["Business_Name"],
            "company_id": company_data[0]["President_No"],
            "responsible_name": company_data[0]["Responsible_Name"],
            "company_location": company_data[0]["Business_Address"],
            "capital": company_data[0]["Business_Register_Funds"],
            }
        print("這裡字典有基本資料:",my_business)
    if len(business_data)> 0 :
        # print(business_data[0]["Business_Item_Old"][0])
        business_list = business_data[0]["Business_Item_Old"]
        businss_items = []
        #====判斷資料型態=========
        # print(type(business_data))
        # print(business_data)

        # print(type(business_data[0]))
        # print(business_data[0])

        # print(type(business_data[0]["Business_Item_Old"]))
        # print(business_data[0]["Business_Item_Old"])
        #====判斷資料型態=========
        for key in business_list:
            # print(key)
            print("Business_Seq_No值:",key["Business_Seq_No"])
            print("Business_Item值:",key["Business_Item"])
            print("Business_Item_Desc值:",key["Business_Item_Desc"])
                               
            one_item = {
                            "Seq_NO": key["Business_Seq_No"],
                            "Item": key["Business_Item"],
                            "Item_Desc": key["Business_Item_Desc"]
                        }

            businss_items.append(one_item)
        my_business["business_items"] = businss_items
        # print(type(my_business["business_items"]))
        # print(type(my_business))
    return my_business

def fetch_business_basic(company_id):
    """
    輸入str
    輸出list
    """
    #商業應用三url
    url = (
        "http://data.gcis.nat.gov.tw/od/data/api/"
        "426D5542-5F05-43EB-83F9-F1300F14E1F1"
        "?$format=json"
        f"&$filter=President_No eq {company_id}"
        "&$skip=0"
        "&$top=50"
    )
    print("[商業應用三API] 查詢統編:", company_id)
    print("[商業應用三API] URL:", url)
    response = requests.get(url)
    print("[商業應用三response] :", response)
    print("[商業應用三response.text] :", response.text)
    if response.status_code != 200:
        return None

    if not response.text:
        return None

    return response.json()

def agency_detail(agency):
    """
    輸入list
    在list 裡面找到agency = agency[0]["Agency"]
    輸出str
    """
    print("==開始轉換list 取出找到agency====")
    agency = agency[0]["Agency"]
    print("==完成轉換list 取出找到agency====")
    return agency

if __name__ == "__main__":
    ...
    # fetch_business_data("15725713")
    # company_data, business_data = fetch_company_data("84178803")
    # build_company(company_data, business_data)
    # company_data, business_data = fetch_business_data("91551501")
    # build_business(company_data, business_data)
    print("開始執行")
    company_id = "91551501"
    agency = fetch_business_basic(company_id)
    print("這裡出來的型態",type(agency))
    #測試
    agency = agency_detail(agency)    
    print(agency)
    # agency = agency[0]["Agency"]
    # print(agency)
    # print("這裡出來的型態agency[0]Agency",type(agency))
    # print("這裡出來的型態company_id",type(company_id))
    # company_data,business_data = fetch_business_data(company_id,agency)
    # data = build_business(company_data,business_data)
    # print(type(data))
    # print(data)

    # print(type(agency))
    # print("登記機關(Agency)",agency)
    print("結束執行")
    # print(result)
    # print(type(result))
    