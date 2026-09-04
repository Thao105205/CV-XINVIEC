import streamlit as st
from PIL import Image

# =========================================================
# CẤU HÌNH TRANG
# =========================================================
st.set_page_config(
    page_title="CV - Thu Thảo",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# CSS
# =========================================================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Be Vietnam Pro', Arial, sans-serif;
}

.stApp {
    background-color: #f3f5e7;
}

/* Ẩn menu và footer mặc định */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* Container chính */
.main-container {
    max-width: 1100px;
    margin: 35px auto;
    padding: 45px 55px;
    background-color: #f3f5e7;
}

/* Header */
.header {
    display: grid;
    grid-template-columns: 34% 66%;
    align-items: center;
    margin-bottom: 30px;
}

/* Ảnh */
.photo-box {
    display: flex;
    justify-content: center;
    align-items: center;
}

.profile-photo {
    width: 170px;
    height: 170px;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid #9aa75a;
    padding: 4px;
    background-color: white;
}

/* Tên */
.name {
    font-size: 54px;
    font-weight: 800;
    color: #285934;
    margin: 0 0 25px 0;
    letter-spacing: -1px;
}

/* Thông tin */
.contact {
    font-size: 15px;
    line-height: 1.9;
    color: #3d443c;
}

/* Nội dung 2 cột */
.content {
    display: grid;
    grid-template-columns: 34% 66%;
    column-gap: 55px;
}

/* Cột trái */
.left-column {
    padding-right: 10px;
}

/* Cột phải */
.right-column {
    padding-left: 5px;
}

/* Section */
.section {
    border-top: 2px solid #a9aea1;
    padding-top: 20px;
    margin-top: 25px;
    margin-bottom: 40px;
}

/* Tiêu đề */
.section-title {
    color: #315c3b;
    font-size: 22px;
    font-weight: 800;
    margin-bottom: 15px;
}

/* Nội dung */
.text {
    color: #4a5148;
    font-size: 14.5px;
    line-height: 1.75;
    text-align: left;
}

/* Danh sách */
ul {
    margin-top: 5px;
    padding-left: 22px;
}

li {
    color: #4a5148;
    font-size: 14.5px;
    line-height: 1.65;
    margin-bottom: 5px;
}

/* Kinh nghiệm */
.job-title {
    color: #39463a;
    font-size: 15px;
    font-weight: 700;
    line-height: 1.5;
    margin-top: 12px;
}

.job-date {
    color: #39463a;
    font-size: 14.5px;
    font-weight: 500;
    margin-bottom: 3px;
}

.job-list {
    margin-bottom: 15px;
}

/* Học vấn */
.education {
    color: #4a5148;
    font-size: 14.5px;
    line-height: 1.65;
}

/* Responsive */
@media screen and (max-width: 800px) {

    .main-container {
        margin: 10px;
        padding: 25px;
    }

    .header,
    .content {
        grid-template-columns: 1fr;
    }

    .photo-box {
        margin-bottom: 20px;
    }

    .name {
        text-align: center;
        font-size: 40px;
    }

    .contact {
        text-align: center;
    }

    .right-column {
        padding-left: 0;
    }

    .left-column {
        padding-right: 0;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# ĐỌC ẢNH CV
# =========================================================
try:
    cv_image = Image.open("cv.png")
except:
    cv_image = None


# =========================================================
# HEADER
# =========================================================
st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.markdown("""
<div class="header">

    <div class="photo-box">
<img
    src="img.jpg"
    class="profile-photo"
>
        >
    </div>

    <div>
        <div class="name">Thu Thảo</div>

        <div class="contact">
            338 Nguyễn Thị Minh Khai, Phường Dĩ An, TPHCM<br>
            Sđt: 0374 269 428<br>
            Mail: kieuthao105205@gmail.com
        </div>
    </div>

</div>
""", unsafe_allow_html=True)


# =========================================================
# 2 CỘT
# =========================================================
st.markdown('<div class="content">', unsafe_allow_html=True)


# =========================================================
# CỘT TRÁI
# =========================================================
st.markdown('<div class="left-column">', unsafe_allow_html=True)

# ---------------- MỤC TIÊU ----------------
st.markdown("""
<div class="section">

    <div class="section-title">
        Mục tiêu
    </div>

    <div class="text">
        Là sinh viên chuyên ngành Tài chính - Ngân hàng với nền tảng
        kiến thức vững chãi về tài chính, ngân hàng và phân tích số liệu.
        Tôi mong muốn được làm việc trong môi trường chuyên nghiệp để
        áp dụng kiến thức đã học vào thực tiễn, phát triển kỹ năng
        chuyên môn và tích lũy kinh nghiệm trong lĩnh vực Tài chính - Ngân hàng.
    </div>

</div>
""", unsafe_allow_html=True)


# ---------------- KỸ NĂNG ----------------
st.markdown("""
<div class="section">

    <div class="section-title">
        KỸ NĂNG
    </div>

    <div class="text">

        <ul>
            <li>
                Hiểu và vận dụng kiến thức về tài chính, ngân hàng, tín dụng
            </li>

            <li>
                Phân tích số liệu, đọc và tổng hợp BCTC
            </li>

            <li>
                Sử dụng Excel, Word, PowerPoint và các phần mềm văn phòng
                phục vụ công việc
            </li>

            <li>
                Kỹ năng giao tiếp, làm việc nhóm và thuyết trình
            </li>

            <li>
                Cẩn thận, có trách nhiệm, khả năng học hỏi nhanh
            </li>
        </ul>

    </div>

</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# =========================================================
# CỘT PHẢI
# =========================================================
st.markdown('<div class="right-column">', unsafe_allow_html=True)


# ---------------- KINH NGHIỆM ----------------
st.markdown("""
<div class="section">

    <div class="section-title">
        Kinh nghiệm liên quan
    </div>

    <div class="job-title">
        Hội sinh viên ngành Tài chính, Chi hội trưởng đại học NTT
    </div>

    <div class="job-date">
        Tháng 7, 2023 - Nay
    </div>

    <ul class="job-list">

        <li>
            Hỗ trợ tổ chức các hoạt động học thuật và sự kiện của chi Hội
        </li>

        <li>
            Phụ trách một số công việc hành chính, thu quỹ, tổng hợp thông tin
        </li>

        <li>
            Tham gia chuẩn bị nội dung báo cáo hoạt động định kỳ
        </li>

        <li>
            Rèn luyện kỹ năng giao tiếp, làm việc nhóm
        </li>

    </ul>


    <div class="job-title">
        Tình nguyện viên hỗ trợ hành chính
    </div>

    <div class="job-date">
        Tháng 5, 2024
    </div>

    <ul>

        <li>
            Hỗ trợ các công việc hành chính văn phòng cơ bản theo phân công
        </li>

        <li>
            Thực hiện nhập liệu, sắp xếp và lưu trữ hồ sơ
        </li>

        <li>
            Hỗ trợ gửi và nhận hồ sơ qua email
        </li>

        <li>
            Đảm bảo công việc thực hiện đúng quy trình và thời hạn
        </li>

    </ul>

</div>
""", unsafe_allow_html=True)


# ---------------- HỌC VẤN ----------------
st.markdown("""
<div class="section">

    <div class="section-title">
        Học vấn
    </div>

    <div class="education">
        Cử nhân Tài chính - Ngân hàng<br>
        Đại học Nguyễn Tất Thành - TPHCM<br>
        Dự kiến tốt nghiệp năm 2026<br>
        GPA 2.9/4
    </div>

</div>
""", unsafe_allow_html=True)


st.markdown('</div>', unsafe_allow_html=True)

# đóng content
st.markdown('</div>', unsafe_allow_html=True)

# đóng main-container
st.markdown('</div>', unsafe_allow_html=True)
