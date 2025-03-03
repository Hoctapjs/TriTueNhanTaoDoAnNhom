import pandas as pd

# Dữ liệu khoảng cách giữa các tỉnh
distances = {
    "An Giang": { "Bạc Liêu": 150, "Bến Tre": 120, "Cà Mau": 180, "Đồng Tháp": 80, "Hậu Giang": 60, "Kiên Giang": 110, "Long An": 140, "Sóc Trăng": 90, "Tiền Giang": 160, "Trà Vinh": 200, "Vĩnh Long": 170 },
    "Bạc Liêu": { "An Giang": 150, "Bến Tre": 100, "Cà Mau": 70, "Đồng Tháp": 140, "Hậu Giang": 120, "Kiên Giang": 90, "Long An": 180, "Sóc Trăng": 60, "Tiền Giang": 160, "Trà Vinh": 150, "Vĩnh Long": 130 },
    "Bến Tre": { "An Giang": 120, "Bạc Liêu": 100, "Cà Mau": 190, "Đồng Tháp": 110, "Hậu Giang": 130, "Kiên Giang": 160, "Long An": 90, "Sóc Trăng": 80, "Tiền Giang": 60, "Trà Vinh": 70, "Vĩnh Long": 50 },
    "Cà Mau": { "An Giang": 180, "Bạc Liêu": 70, "Bến Tre": 190, "Đồng Tháp": 160, "Hậu Giang": 120, "Kiên Giang": 150, "Long An": 210, "Sóc Trăng": 90, "Tiền Giang": 250, "Trà Vinh": 230, "Vĩnh Long": 220 },
    "Đồng Tháp": { "An Giang": 80, "Bạc Liêu": 140, "Bến Tre": 110, "Cà Mau": 160, "Hậu Giang": 50, "Kiên Giang": 120, "Long An": 90, "Sóc Trăng": 70, "Tiền Giang": 140, "Trà Vinh": 110, "Vĩnh Long": 100 },
    "Hậu Giang": { "An Giang": 60, "Bạc Liêu": 120, "Bến Tre": 130, "Cà Mau": 120, "Đồng Tháp": 50, "Kiên Giang": 80, "Long An": 150, "Sóc Trăng": 40, "Tiền Giang": 160, "Trà Vinh": 130, "Vĩnh Long": 110 },
    "Kiên Giang": { "An Giang": 110, "Bạc Liêu": 90, "Bến Tre": 160, "Cà Mau": 150, "Đồng Tháp": 120, "Hậu Giang": 80, "Long An": 190, "Sóc Trăng": 70, "Tiền Giang": 140, "Trà Vinh": 180, "Vĩnh Long": 170 },
    "Long An": { "An Giang": 140, "Bạc Liêu": 180, "Bến Tre": 90, "Cà Mau": 210, "Đồng Tháp": 90, "Hậu Giang": 150, "Kiên Giang": 190, "Sóc Trăng": 130, "Tiền Giang": 60, "Trà Vinh": 70, "Vĩnh Long": 80 },
    "Sóc Trăng": { "An Giang": 90, "Bạc Liêu": 60, "Bến Tre": 80, "Cà Mau": 90, "Đồng Tháp": 70, "Hậu Giang": 40, "Kiên Giang": 70, "Long An": 130, "Tiền Giang": 100, "Trà Vinh": 90, "Vĩnh Long": 80 },
    "Tiền Giang": { "An Giang": 160, "Bạc Liêu": 160, "Bến Tre": 60, "Cà Mau": 250, "Đồng Tháp": 140, "Hậu Giang": 160, "Kiên Giang": 140, "Long An": 60, "Sóc Trăng": 100, "Trà Vinh": 150, "Vĩnh Long": 110 },
    "Trà Vinh": { "An Giang": 200, "Bạc Liêu": 150, "Bến Tre": 70, "Cà Mau": 230, "Đồng Tháp": 110, "Hậu Giang": 130, "Kiên Giang": 180, "Long An": 70, "Sóc Trăng": 90, "Tiền Giang": 150, "Vĩnh Long": 120 },
    "Vĩnh Long": { "An Giang": 170, "Bạc Liêu": 130, "Bến Tre": 50, "Cà Mau": 220, "Đồng Tháp": 100, "Hậu Giang": 110, "Kiên Giang": 170, "Long An": 80, "Sóc Trăng": 80, "Tiền Giang": 110, "Trà Vinh": 120 }
}

# Chuyển đổi dữ liệu sang DataFrame
data = []
for city1, connections in distances.items():
    for city2, distance in connections.items():
        data.append([city1, city2, distance])

# Tạo DataFrame
df = pd.DataFrame(data, columns=["Tỉnh Thành 1", "Tỉnh Thành 2", "Khoảng Cách (km)"])

# Lưu DataFrame vào file Excel
df.to_excel("khoang_cach_tinh_thanh.xlsx", index=False)
print("Đã tạo file khoang_cach_tinh_thanh.xlsx")
