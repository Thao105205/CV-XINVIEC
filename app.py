import streamlit as st
from PIL import Image
import os

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
    # Đọc và hiển thị ảnh đại diện (avata.img)
    image_path = "avata.img"
    if os.path.exists(image_path):
        try:
            image = Image.open(image_path)
            st.image(image, width=180)
        except Exception:
            # Nếu file .img là chuỗi định dạng tiêu chuẩn, đọc trực tiếp bằng Streamlit
            st.image(image_path, width=180)
    else:
        # Trường hợp không tìm thấy file avata.img trong thư mục
        st.warning("Không tìm thấy file 'avata.img'. Hiển thị ảnh mặc định:")
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
    * Sử dụng Excel, Word, PowerPoint và các phần mềm văn phòng phục vụ công việc
    * Kỹ năng giao tiếp, làm việc nhóm và thuyết trình
    * Cẩn thận, có trách nhiệm, khả năng học hỏi nhanh
    """)

# ================= CỘT PHẢI =================
with col2:
    # Thông tin cá nhân
    st.markdown('<div class="main-title">Thu Thảo</div>', unsafe_allow_html=True)
    st.markdown("""
    338 Nguyễn Thị Minh Khai, Phường Dĩ An, TPHCM  
    **Sđt:** 0374 269 428  
    **Mail:** kieuthao105205@gmail.com
    """)
    
    # Kinh nghiệm liên quan
    st.markdown('<div class="section-header">Kinh nghiệm liên quan</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="sub-header">Hội sinh viên ngành Tài chính, Chi hội trưởng đại học NTT</div>', unsafe_allow_html=True)
    st.markdown('<div class="date-text">Tháng 7, 2023 - Nay</div>', unsafe_allow_html=True)
    st.markdown("""
    * Hỗ trợ tổ chức các hoạt động học thuật và sự kiện của chi Hội
    * Phụ trách một số công việc hành chính, thu quỹ, tổng hợp thông tin
    * Tham gia chuẩn bị nội dung báo cáo hoạt động định kỳ
    * Rèn luyện kỹ năng giao tiếp, làm việc nhóm
    """)
    
    st.markdown('<div class="sub-header">Tình nguyện viên hỗ trợ hành chính</div>', unsafe_allow_html=True)
    st.markdown('<div class="date-text">Tháng 5, 2024</div>', unsafe_allow_html=True)
    st.markdown("""
    * Hỗ trợ các công việc hành chính văn phòng cơ bản theo phân công
    * Thực hiện nhập liệu, sắp xếp và lưu trữ hồ sơ
    * Hỗ trợ gửi và nhận hồ sơ qua email
    * Đảm bảo công việc thực hiện đúng quy trình và thời hạn
    """)
    
    # Học vấn
    st.markdown('<div class="section-header">Học vấn</div>', unsafe_allow_html=True)
    st.markdown("""
    **Cử nhân Tài chính - Ngân hàng** Đại học Nguyễn Tất Thành - TPHCM  
    Dự kiến tốt nghiệp năm 2026  
    GPA 2.9/4
    """)
