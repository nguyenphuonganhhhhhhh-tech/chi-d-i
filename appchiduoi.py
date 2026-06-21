import streamlit as st
from pathlib import Path
import base64

# =========================
# CẤU HÌNH TRANG
# =========================
st.set_page_config(
    page_title="CHI DƯỚI",
    page_icon="😡",
    layout="wide"
)

st.title("😡 CHI DƯỚI")
st.caption("Nhập đáp án theo từng số. Sau khi nhấn Enter, đáp án đúng sẽ hiện ngay bên dưới và tự động nhảy sang câu tiếp theo.")

# Khởi tạo trạng thái lưu vị trí ô cần nhảy tiếp theo
if "next_focus_idx" not in st.session_state:
    st.session_state.next_focus_idx = None

def giaiphau_next_focus(current_idx):
    st.session_state.next_focus_idx = current_idx + 1

# =========================
# DỮ LIỆU TRẠM
# =========================
STATIONS = [
    {
"name": "Trạm 1",
"image": "1.png",
"answers": {
"1": "xg chậu",
"2": "xg đùi",
"3": "xg bánh chè",
"4": "xg chày",
"5": "xg mác"
        }
    },
    {
       "name": "Trạm 2",
"image": "2.png",
"answers": {
"1": "chỏm xg đùi",
"2": "cổ xg đùi",
"3": "mấu chuyển bé",
"4": "đg gian mấu",
"5": "mấu chuyển lớn",
"6": "hố mấu chuyển",
"7": "mào gian mấu",
"8": "lồi củ cơ mông",
"9": "đg lược",
"10": "hõm xg đùi"
	}
    }, 
    {
"name": "Trạm 3",
"image": "3.png",
"answers": {
"1": "mắt cá trong",
"2": "mắt cá ngoài",
"3": "rãnh mắt cá ngoài",
"4": "hố mắt cá ngoài",
"5": "rãnh mắt cá trong",
"6": "bờ gian cốt",
"7": "bờ trước"
        }
    },
    {
"name": "Trạm 4",
"image": "4.png",
"answers": {
"1": "xg chậu",
"2": "hố ổ cối",
"3": "ụ ngồi",
"4": "khuyết ổ cối",
"5": "xg mu",
"6": "diện nguyệt"
        }
    },
    {
"name": "Trạm 5",
"image": "6.png",
"answers": {
"1": "cơ mông lớn",
"2": "cơ mông nhỡ",
"3": "cơ mông bé",
"4": "cơ vuông đùi",
"5": "cơ sinh đôi dưới",
"6": "cơ bịt trong",
"7": "cơ sinh đôi trên",
"8": "cơ hình lê"
        }
    },
    {
        "name": "Trạm 6",
"image": "6.png",
"answers": {
"1": "tm đùi",
"2": "mạch bh bẹn",
"3": "khớp mụ",
"4": "cơ khép dài",
"5": "đm đùi",
"6": "cơ may",
"7": "dc bẹn",
"8": "tj đùi"
        }
    },
    {
       "name": "Trạm 7",
"image": "7.png",
"answers": {
"1": "cơ bịt ngoài",
"2": "cơ khép lớn",
"3": "cơ lược",
"4": "cơ khép ngắn",
"5": "cơ khép dài",
"6": "cơ thon và gân",
"7": "bám tận cơ may",
"8": "bám tận cơ bán gân",
"9": "gân chân ngỗng",
"10": "lỗ gian cơ khép",
"11": "ống cơ khép",
"12": "khoang đùi trước",
"13": "khoang đùi sau"
        }
    },
    {
"name": "Trạm 8",
"image": "8.png",
"answers": {
"1": "cơ thẳng đùi",
"2": "cơ rộng ngoài",
"3": "cơ rộng trong",
"4": "gân cơ tứ đầu đùi",
"5": "dc bánh chè",
"6": "cơ rộng giữa",
"7": "cơ may"
        }
    },
    {
"name": "Trạm 9",
"image": "9.png",
"answers": {
"1": "tk mác chung",
"2": "màng gian cốt cẳng chân",
"3": "cơ mác dài",
"4": "ròng rọc mác của xg gót",
"5": "cơ mác ngắn"
        }
    },
    {
"name": "Trạm 10",
"image": "10.png",
"answers": {
"1": "cơ dép",
"2": "gân gót (gân achilles)",
"3": "cơ bụng chân",
"4": "cơ gan chân",
"5": "cơ chày sau",
"6": "cơ gấp ngón cái dài,
"7": "cơ gấp các ngón chân dài",
"8": "cơ khoeo"
        }
    },
    {
 "name": "Trạm 11",
"image": "11.png",
"answers": {
"1": "tk mác chung",
"2": "đm khoeo",
"3": "tm khoeo",
"4": "tk chày"
        }
    },
    {
"name": "Trạm 12",
"image": "12.png",
"answers": {
"1": "đầu dài cơ nhị đầu đùi",
"2": "đầu ngắn cơ nhị đầu đùi",
"3": "cơ bán màng",
"4": "cơ bán gân",
"5": "gân khoeo cơ khép lớn"
        }
    },
    {
"name": "Trạm 13",
"image": "13.png",
"answers": {
"1": "đầu chéo cơ khép ngón cái",
"2": "cơ gấp ngắn ngón cái",
"3": "gân cơ chày sau",
"4": "gân cơ mác dài",
"5": "cơ gấp ngón út",
"6": "đầu ngang cơ khép ngón cái"
        }
    },
    {
 "name": "Trạm 14",
"image": "14.png",
"answers": {
"1": "cơ giun",
"2": "gân cơ gấp dài ngón cái",
"3": "gân cơ gấp dài các ngón chân",
"4": "cơ vuông gan chân"
        }
    },
    {
"name": "Trạm 15",
"image": "15.png",
"answers": {
"1": "cơ dạng ngón cái",
"2": "cơ gấp ngắn các ngón chân",
"3": "cơ dạng ngón út"
        }
    },
    {
"name": "Trạm 16",
"image": "16.png",
"answers": {
"1": "cơ duỗi dài ngón cái",
"2": "cơ mác ba",
"3": "cơ duỗi dài các ngón chân",
"4": "cơ chày trước"
        }
    },
    {
"name": "Trạm 17",
"image": "17.png",
"answers": {
"1": "dc gian bàn chân ngang sâu",
"2": "cơ gian cốt mu chân thứ nhất",
"3": "cơ gian cốt mu chân thứ ba"
        }
    },

]

IMAGE_DIR = Path(".")

if "station_index" not in st.session_state:
    st.session_state.station_index = 0

# =========================
# THANH SIDEBAR (ĐÃ THÊM CHỌN TRẠM NHANH)
# =========================
st.sidebar.header("⚙️ Cài đặt")

# Tạo danh sách tên các trạm để sinh viên bấm chọn nhanh
station_names = [s["name"] for s in STATIONS]

# Đồng bộ Selectbox với session_state hiện tại của trạm
selected_station_name = st.sidebar.selectbox(
    "Chọn trạm làm bài nhanh:",
    options=station_names,
    index=st.session_state.station_index
)

# Cập nhật lại chỉ số trạm dựa trên lựa chọn từ Selectbox của sinh viên
station_index = station_names.index(selected_station_name)
if station_index != st.session_state.station_index:
    st.session_state.station_index = station_index
    st.rerun()

station = STATIONS[station_index]

show_all_answers = st.sidebar.checkbox("Hiện toàn bộ đáp án cho giảng viên", value=False)

if st.sidebar.button("🔄 Làm lại trạm này"):
    for key in list(st.session_state.keys()):
        if key.startswith(f"answer_{station_index}_"):
            del st.session_state[key]
    st.rerun()

st.sidebar.markdown("---")
if st.sidebar.button("⬅️ Quay lại trạm trước") and station_index > 0:
    st.session_state.station_index -= 1
    st.rerun()

if st.sidebar.button("➡️ Chuyển sang trạm tiếp theo") and station_index < len(STATIONS) - 1:
    st.session_state.station_index += 1
    st.rerun()

st.markdown("---")
st.subheader(station["name"])

# =========================
# CHIA CỘT CHÍNH (Cột 1: Ảnh cố định, Cột 2: Ô nhập)
# =========================
st.markdown("""
<style>
[data-testid="stColumn"]:nth-of-type(1) {
    position: -webkit-sticky;
    position: sticky;
    top: 50px;
    align-self: start;
    max-height: 85vh;
    overflow: hidden;
}
.sticky-img {
    width: 100%;
    max-height: 80vh;
    object-fit: contain;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}
.answer-divider {
    margin-top: 15px;
    margin-bottom: 15px;
    border-bottom: 1px solid #f0f2f6;
}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([5, 5], gap="large")

with col1:
    image_path = IMAGE_DIR / station["image"]
    if image_path.exists():
        with open(image_path, "rb") as f:
            img_data = base64.b64encode(f.read()).decode()
        ext = image_path.suffix.replace(".", "")
        st.markdown(f'<img class="sticky-img" src="data:image/{ext};base64,{img_data}">', unsafe_allow_html=True)
    else:
        st.error(f"Không tìm thấy ảnh: {image_path}")

with col2:
    st.markdown("### ✍️ Nhập đáp án")
    
    if show_all_answers:
        with st.expander("👁️ Xem nhanh toàn bộ đáp án"):
            for num, ans in station["answers"].items():
                st.write(f"**Số {num}:** {ans}")

    # Lấy danh sách các số câu hỏi của trạm hiện tại
    numbers = list(station["answers"].keys())

    # Vòng lặp sinh các ô điền câu hỏi gốc của Streamlit
    for i, number in enumerate(numbers):
        correct_answer = station["answers"][number]

        st.markdown(f"**Số {number}:**")

        user_answer = st.text_input(
            "",
            key=f"answer_{station_index}_{number}",
            placeholder="Nhập đáp án rồi nhấn Enter...",
            label_visibility="collapsed",
            on_change=giaiphau_next_focus,
            args=(i,)
        )

        if user_answer.strip():
            if user_answer.strip().lower() == correct_answer.strip().lower():
                st.success("✅ Đúng chính xác!")
            else:
                st.error(f"❌ Đáp án đúng: **{correct_answer}**")

        st.markdown('<div class="answer-divider"></div>', unsafe_allow_html=True)

    # ĐOẠN ĐIỀU KHIỂN NHẢY CON TRỎ
    if st.session_state.next_focus_idx is not None:
        st.components.v1.html(f"""
            <script>
            setTimeout(function() {{
                const inputs = window.parent.document.querySelectorAll('input[type="text"]');
                const nextInput = inputs[{st.session_state.next_focus_idx}];
                if (nextInput) {{
                    nextInput.focus();
                    nextInput.scrollIntoView({{behavior: "smooth", block: "center"}});
                }}
            }}, 300);
            </script>
        """, height=0, width=0)
        st.session_state.next_focus_idx = None

    # Nút chuyển tiếp nhanh ở cuối phần điền đáp án
    st.markdown("### 🧭 Điều hướng nhanh")
    nav_col1, nav_col2 = st.columns(2)

    with nav_col1:
        if st.button("⬅️ Trạm trước", key="btn_prev", use_container_width=True) and station_index > 0:
            st.session_state.station_index -= 1
            st.rerun()

    with nav_col2:
        if st.button("Trạm tiếp theo ➡️", key="btn_next", use_container_width=True) and station_index < len(STATIONS) - 1:
            st.session_state.station_index += 1
            st.rerun()
