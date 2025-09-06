import streamlit as st
from PIL import Image

st.set_page_config(page_title="Cờ Tướng Online", layout="wide")

st.title("🎯 Cờ Tướng Online – Streamlit Edition")
st.markdown("Chào Az! Hãy chọn quân cờ và thực hiện nước đi nhé.")

# Hiển thị bàn cờ
board_img = Image.open("assets/ban_co.png")
st.image(board_img, caption="Bàn cờ tướng", use_column_width=True)

# Chọn quân cờ
col1, col2 = st.columns(2)
with col1:
    piece = st.selectbox("Chọn quân cờ", ["Xe", "Mã", "Pháo", "Tượng", "Sĩ", "Tướng", "Chốt"])
with col2:
    move = st.text_input("Nhập nước đi (ví dụ: Xe 1 bình 4)")

# Nút thực hiện
if st.button("Thực hiện nước đi"):
    st.success(f"Bạn vừa đi: {piece} – {move}")
    # TODO: Kiểm tra hợp lệ, cập nhật bàn cờ

# Tuỳ chọn nâng cao
with st.expander("🔧 Tuỳ chọn nâng cao"):
    st.checkbox("Hiển thị nước đi hợp lệ")
    st.checkbox("Bật chế độ AI phản hồi")

import streamlit as st

st.title("🀄 Bàn Cờ Tướng Tương Tác")

# Khởi tạo bàn cờ 9x10
rows = 10
cols = 9

# Khởi tạo trạng thái bàn cờ (chỉ là ví dụ, bạn có thể thay bằng quân thật)
board = [["" for _ in range(cols)] for _ in range(rows)]

# Ví dụ đặt quân cờ ban đầu
board[0][0] = "🚗"  # Xe
board[0][1] = "🐴"  # Mã
board[0][2] = "🛡️"  # Tượng
board[0][3] = "👑"  # Sĩ
board[0][4] = "🧔"  # Tướng
board[0][5] = "👑"
board[0][6] = "🛡️"
board[0][7] = "🐴"
board[0][8] = "🚗"

# Hiển thị bàn cờ bằng lưới
for i in range(rows):
    cols_ui = st.columns(cols)
    for j in range(cols):
        with cols_ui[j]:
            st.button(board[i][j] or "⬜", key=f"{i}-{j}")
