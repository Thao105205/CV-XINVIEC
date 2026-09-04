import streamlit as st

# Thiết lập cấu hình trang
st.set_page_config(
    page_title="CV - Thu Thảo",
    page_icon="📄",
    layout="wide"
)

# Thêm CSS tùy chỉnh để định dạng giống mẫu CV
st.markdown("""
    <style>
    /* Nền tổng thể và font chữ */
    .stApp {
        background-color: #F4F6EE;
        color: #2F3E33;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Cấu hình tiêu đề chính */
    .main-title {
        color: #1E3E2B;
        font-size: 38px;
        font-weight: bold;
        margin-bottom: 5px;
    }
    
    /* Cấu hình tiêu đề mục */
    .section-header {
        color: #1E3E2B;
        font-size: 20px;
        font-weight: bold;
        border-bottom: 1.5px solid #A3B19B;
        padding-bottom: 4px;
        margin-top: 15px;
        margin-bottom: 12px;
    }
    
    /* Phân nhóm kinh nghiệm */
    .sub-header {
        font-weight: bold;
        color: #2F3E33;
        font-size: 15px;
        margin-top: 8px;
        margin-bottom: 2px;
    }
    
    .date-text {
        color: #555555;
        font-size: 13px;
        font-style: italic;
        margin-bottom: 6px;
    }
    
    /* Tùy chỉnh danh sách */
    ul {
        margin-top: 0px;
        padding-left: 20px;
    }
    li {
        margin-bottom: 4px;
        font-size: 14px;
        line-height: 1.5;
    }
    p {
        font-size: 14px;
        line-height: 1.5;
    }
    </style>
""", unsafe_allow_html=True)

# Chia layout thành 2 cột: Cột trái (35%) - Cột phải (65%)
col1, col2 = st.columns([0.35, 0.65], gap="large")

# ================= CỘT TRÁI =================
with col1:
    # Ảnh đại diện
    try:
        st.image("image_9d1808.jpg", width=180)
    except:
        # Trường hợp chạy local chưa có ảnh
        st.image("https://via.placeholder.com/180", width=180)
    
    # Mục tiêu
    st.markdown('<div class="section-header">Mục tiêu</div>', unsafe_allow_html=True)
    st.markdown("""
    Là sinh viên chuyên ngành Tài chính - Ngân hàng với nền tảng kiến thức vững chãi về tài chính, ngân hàng và phân tích số liệu. Tôi mong muốn được làm việc trong môi trường chuyên nghiệp để áp dụng kiến thức đã học vào thực tiễn, phát triển kỹ năng chuyên môn và tích lũy kinh nghiệm trong lĩnh vực Tài chính - Ngân hàng.
    """)
    
    # Kỹ năng
    st.markdown('<div class="section-header">KỸ NĂNG</div>', unsafe_allow_html=True)
    st.markdown("""
    * Hiểu và vận dụng kiến thức về tài chính, ngân hàng, tín dụng
    * Phân tích số liệu, đọc và tổng hợp BCTC
    * Sử dụng Excel,
