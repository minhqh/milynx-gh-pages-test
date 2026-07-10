import json
import datetime
import urllib.request

# API miễn phí cung cấp các sự thật ngẫu nhiên
url = "https://uselessfacts.jsph.pl/api/v2/facts/random"

try:
    # Gọi API bằng thư viện build-in của Python (không cần cài thêm pip requests)
    response = urllib.request.urlopen(url)
    api_data = json.loads(response.read())
    fact_text = api_data['text']
    author = "Useless Facts API"
except Exception as e:
    fact_text = f"Không thể lấy dữ liệu từ API: {e}"
    author = "System Error"

# Cấu trúc dữ liệu ghi vào file JSON
data = {
    "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC"),
    "fact": fact_text,
    "author": author
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Đã cập nhật dữ liệu mới từ API vào lúc {data['last_updated']}")