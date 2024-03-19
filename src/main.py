import json
from route_var import RouteVar 
from route_var import RouteVarQuery

# Định nghĩa hàm để xử lý và chuyển đổi chuỗi JSON
def process_json(json_string):
    # Tách chuỗi thành các phần dựa trên dấu xuống dòng
    json_parts = json_string.split(']\n[')
    # Thêm dấu ngoặc vuông vào đầu và cuối chuỗi, và thay thế ']\n[' bằng '],['
    json_corrected = '[' + '],['.join(json_parts) + ']'
    # Chuyển đổi chuỗi đã sửa thành đối tượng JSON
    return json.loads(json_corrected)

# Đọc file JSON vào biến json_data
with open('src/vars.json', 'r', encoding='utf-8') as file:
    json_data = file.read()

# Sử dụng hàm đã định nghĩa để xử lý chuỗi JSON
data = process_json(json_data)

vars = []
for item in data:
    for obj in item:
        # print(obj)
        var = RouteVar(obj)
        vars.append(var)

# Tạo đối tượng RouteVarQuery
ans = RouteVarQuery(vars).searchByRouteId(1, 3)
print(json.dumps(ans, default=lambda o: o.__dict__, indent=4, ensure_ascii=False))

