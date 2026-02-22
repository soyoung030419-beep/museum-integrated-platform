import requests
import pandas as pd
import os

# ==============================
# 1. API 설정
# ==============================

SERVICE_KEY = "dfab5e4c-96ba-43b5-83b5-30a0dde141dc"

url = "http://api.kcisa.kr/openapi/service/CNV/API_CNV_042/request"

params = {
    "serviceKey": SERVICE_KEY,
    "_type": "json"
}

# ==============================
# 2. API 호출
# ==============================

response = requests.get(url, params=params)

if response.status_code != 200:
    print("API 호출 실패:", response.status_code)
    exit()

data = response.json()

# ==============================
# 3. 데이터 추출
# ==============================

try:
    items = data["response"]["body"]["items"]
except KeyError:
    print("JSON 구조가 예상과 다릅니다.")
    print(data)
    exit()

if isinstance(items, dict):
    items = [items]

df = pd.DataFrame(items)

print("수집된 데이터 개수:", len(df))
print("컬럼 목록:", df.columns)

# ==============================
# 4. 엑셀 저장
# ==============================

os.makedirs("../data", exist_ok=True)

output_path = "../data/museum_exhibition_data.xlsx"
df.to_excel(output_path, index=False)

print("엑셀 파일 저장 완료:", output_path)