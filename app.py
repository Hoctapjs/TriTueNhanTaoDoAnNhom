from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Đọc dữ liệu khoảng cách từ file Excel
def read_distances():
    df = pd.read_excel('distances.xlsx', index_col=0)
    print("Cities in DataFrame:", df.index.tolist())  # Ghi log danh sách các thành phố
    return df

# Thuật toán TSP động đơn giản (Greedy)
def greedy_tsp_dynamic(start_city, locations):
    path = [start_city]  # Đường đi khởi đầu
    total_distance = 0
    current_city = start_city

    while len(path) < len(locations.index):
        print(f"Current city: {current_city}")  # Ghi log thành phố hiện tại
        next_city = min(
            locations.index.difference(path),
            key=lambda city: locations.loc[current_city, city]
        )
        path.append(next_city)
        total_distance += locations.loc[current_city, next_city]
        current_city = next_city

    # Quay về thành phố khởi đầu
    total_distance += locations.loc[current_city, start_city]
    path.append(start_city)
    
    return path, total_distance  # Đảm bảo trả về đúng hai giá trị

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tsp', methods=['POST'])
def calculate_tsp():
    try:
        data = request.get_json()
        start_city = data.get('start_city')

        if not start_city:
            return jsonify({"error": "Thành phố bắt đầu không hợp lệ"}), 400

        # Đọc dữ liệu từ file Excel
        locations = read_distances()

        if start_city not in locations.index:
            return jsonify({"error": "Thành phố bắt đầu không có trong dữ liệu"}), 400

        # Gọi thuật toán TSP
        path, total_distance = greedy_tsp_dynamic(start_city, locations)

        # Lấy khoảng cách giữa các thành phố trong đường đi
        distances = []
        for i in range(len(path) - 1):
            distance = locations.loc[path[i], path[i + 1]]
            distances.append(int(distance))  # Chuyển đổi np.int64 thành int

        # Trả về kết quả cho client
        return jsonify({
            "path": path,
            "distances": distances,
            "total_distance": int(total_distance)  # Chuyển đổi np.int64 thành int
        })
    except Exception as e:
        # Ghi lỗi ra log và trả về JSON lỗi
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

# Hàm đọc dữ liệu từ file Excel và chuyển thành HTML
def read_excel_data1(file_path):
    df = pd.read_excel(file_path)
    return df.to_html(classes='table table-striped')  # Thêm class để bảng đẹp hơn với Bootstrap

@app.route('/data')
def index1():
    # Đọc dữ liệu từ file Excel
    excel_data = read_excel_data1('distances.xlsx')  # Đổi đường dẫn tới file Excel của bạn
    return render_template('index.html', table=excel_data)

if __name__ == '__main__':
    app.run(debug=True)
