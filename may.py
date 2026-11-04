import streamlit as st

# 1. 頁面基本設定
st.set_page_config(
    page_title="北海道 7 天 6 夜行程表",
    page_icon="❄️",
    layout="wide"
)

# 2. 法式奶油風 + 精緻導航按鈕 CSS 樣式
st.markdown("""
<style>
    /* 全域背景與文字色彩 */
    .stApp {
        background-color: #FDFBF7;
        color: #4A443F;
    }
    h1, h2, h3 {
        color: #6E5A44 !important;
    }
    
    /* 精緻地圖按鈕卡片樣式 */
    .map-btn-card {
        background-color: #F7F2E8;
        border: 1px solid #EAE3D2;
        border-radius: 10px;
        padding: 12px 16px;
        margin: 8px 0px;
        transition: all 0.2s ease;
    }
    .map-btn-card:hover {
        background-color: #EFE9DB;
        border-color: #C28D56;
    }
    .map-btn-card a {
        color: #8C6239 !important;
        text-decoration: none !important;
        font-weight: 600;
        display: block;
    }
</style>
""", unsafe_allow_html=True)

# 3. 頁面主標題
st.title("🇯🇵 日本北海道 7 天 6 夜行程表")
st.caption("📅 2026/12/06（日）～ 12/12（六）｜ ❄️ 法式奶油風隨身旅遊指南")

# 4. 主頁面頂級分頁
tab1, tab2, tab3, tab4 = st.tabs(["📅 每日行程", "🎫 票券與伴手禮清單", "✈️ 機票與住宿", "💰 預算總覽"])

# --- TAB 1: 每日行程 ---
with tab1:
    st.markdown("### 🗺️ 7 天 6 夜詳細行程與地圖導航")
    
    with st.expander("Day 1｜12/06（日）抵達札幌・市區逛街", expanded=True):
        st.markdown("""
        - 🕒 **05:55** 桃園機場起飛（FD242）
        - 🕒 **10:40** 抵達新千歲機場
        - 🕒 **12:30** 搭乘 JR 前往札幌（約 40 分鐘）
        - 🕒 **15:00** 飯店 Check-in
        """)
        st.markdown("""
        <div class="map-btn-card">
            <a href="https://maps.google.com/?q=Holiday+Inn+Express+Sapporo+Susukino" target="_blank">📍札幌薄野 Holiday Inn Express 飯店導航</a>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("**🏙️ 札幌市區景點**")
        spots_day1 = [
            ("大通公園", "Odori+Park+Sapporo"),
            ("札幌電視塔", "Sapporo+TV+Tower"),
            ("狸小路商店街", "Tanukikoji+Shopping+Street"),
            ("PARCO 百貨公司", "Sapporo+PARCO"),
            ("大丸百貨公司", "Daimaru+Sapporo")
        ]
        for name, q in spots_day1:
            st.markdown(f"""
            <div class="map-btn-card">
                <a href="https://maps.google.com/?q={q}" target="_blank">📍{name}</a>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("**🍜 美食推薦**")
        st.markdown("""
        <div class="map-btn-card">
            <a href="https://maps.google.com/?q=Soup+Curry+GARAKU+Sapporo" target="_blank">📍Soup Curry GARAKU 湯咖哩</a>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("- 🍓 水果吃爆：草莓等特產水果")

    with st.expander("Day 2｜12/07（一）旭川動物園・美瑛一日遊"):
        st.markdown("""
        - 🕒 **07:30** 集合地點
        """)
        st.markdown("""
        <div class="map-btn-card">
            <a href="https://maps.google.com/?q=Sapporo+TV+Tower" target="_blank">📍 札幌電視塔 1 樓資訊中心（大通地鐵 27 號出口旁）</a>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("**🚌 Klook 一日遊景點**")
        spots_day2 = [
            ("旭川動物園（企鵝散步）", "Asahiyama+Zoo"),
            ("美瑛青池", "Shirogane+Blue+Pond"),
            ("白鬚瀑布", "Shirahige+Waterfall"),
            ("聖誕樹之木", "Christmas+Tree+Biei"),
            ("精靈露台", "Ningle+Terrace")
        ]
        for name, q in spots_day2:
            st.markdown(f"""
            <div class="map-btn-card">
                <a href="https://maps.google.com/?q={q}" target="_blank">📍{name}</a>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("- 🕒 **19:30** 返回札幌")

        st.markdown("**🍜 美食推薦**")
        st.markdown("""
        - 🏪 早餐：超商買好車上吃
        <div class="map-btn-card">
            <a href="https://maps.google.com/?q=Sumire+Sapporo+Susukino" target="_blank">📍20:00 味噌拉麵 すみれ (Sumire)</a>
        </div>
        - 🍓 水果吃爆：草莓等
        """, unsafe_allow_html=True)

    with st.expander("Day 3｜12/08（二）定山溪漂流"):
        st.markdown("- 🕒 **11:30** 集合地點")
        st.markdown("""
        <div class="map-btn-card">
            <a href="https://maps.google.com/?q=Friluftsliv+Jozankei" target="_blank">📍フリルフスリフ（Friluftsliv）</a>
        </div>
        - 🚣 漂流活動時間約 5 小時（費用：¥10,000／人）
        
        **🍜 美食推薦**
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="map-btn-card">
            <a href="https://maps.google.com/?q=Kaniza+Sapporo" target="_blank">📍蟹座</a>
        </div>
        - 🍓 水果吃爆：草莓等
        """, unsafe_allow_html=True)

    with st.expander("Day 4｜12/09（三）小樽一日遊"):
        st.markdown("- 🚇 交通：JR 前往南小樽站（約 40 分鐘）\n\n**🗺️ 預計遊覽順序**")
        spots_day4 = [
            ("1. 住吉神社", "Sumiyoshi+Shrine+Otaru"),
            ("2. Un délice (アンデリス 布丁)", "Un+delice+Otaru"),
            ("3. 小樽堺町商店街", "Otaru+Sakaimachi+Street"),
            ("   - 北一硝子館", "Kitaichi+Glass+Otaru"),
            ("   - 音樂盒堂", "Otaru+Music+Box+Museum"),
            ("   - Spoony 茶屋小樽店", "Spoony+Otaru"),
            ("4. 小樽出拔小路", "Otaru+Debanukoji"),
            ("5. 小樽運河", "Otaru+Canal")
        ]
        for name, q in spots_day4:
            st.markdown(f"""
            <div class="map-btn-card">
                <a href="https://maps.google.com/?q={q}" target="_blank">📍{name}</a>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown("**🍜 美食推薦**")
        st.markdown("""
        <div class="map-btn-card">
            <a href="https://maps.google.com/?q=Naruto+Main+Shop+Otaru" target="_blank">📍若雞時代 なると 本店</a>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("Day 5｜12/10（四）手稻滑雪場"):
        st.markdown("- 🕒 **07:45** 集合地點")
        st.markdown("""
        <div class="map-btn-card">
            <a href="https://maps.google.com/?q=THE+SUSUKINO+SQUARE+WEST" target="_blank">📍THE SUSUKINO SQUARE WEST (1樓)</a>
        </div>
        - 📍 地址：〒064-0806 北海道札幌市中央区南6条西5丁目3-6
        
        **⛷️ 活動內容**
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="map-btn-card">
            <a href="https://maps.google.com/?q=Sapporo+Teine" target="_blank">📍手稻滑雪場 (Sapporo Teine)</a>
        </div>
        - 滑雪體驗 & 雪盆活動（NT$5,495／人）
        
        **🍜 美食推薦**
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="map-btn-card">
            <a href="https://maps.google.com/?q=Menya+Yukikaze+Susukino" target="_blank">📍麵屋雪風 薄野本店</a>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("Day 6｜12/11（五）札幌市區深入漫遊"):
        spots_day6 = [
            ("狸小路商店街、薄野商圈逛街", "Tanukikoji+Shopping+Street"),
            ("中島公園拍照", "Nakajima+Park+Sapporo"),
            ("白色戀人公園（訂製紀念鐵盒）", "Shiroi+Koibito+Park"),
            ("北海道神宮（💡 建議 9:00 前抵達購買限定梅酒與玻璃珠御守）", "Hokkaido+Shrine")
        ]
        for name, q in spots_day6:
            st.markdown(f"""
            <div class="map-btn-card">
                <a href="https://maps.google.com/?q={q}" target="_blank">📍{name}</a>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown("**🍜 美食推薦**")
        st.markdown("""
        <div class="map-btn-card">
            <a href="https://maps.google.com/?q=Ichiran+Ramen+Susukino" target="_blank">📍一蘭拉麵 札幌薄野店</a>
        </div>
        <div class="map-btn-card">
            <a href="https://maps.google.com/?q=Toriton+Sushi+Sapporo" target="_blank">📍トリトン迴轉壽司 (Toriton)</a>
        </div>
        - 🍓 水果吃爆：草莓等
        """, unsafe_allow_html=True)

    with st.expander("Day 7｜12/12（六）新千歲機場・採購返台"):
        st.markdown("""
        - 🕒 **10:00** 從札幌搭乘 JR 前往新千歲機場
        - 🕒 **11:00** 機場逛街與免稅店採購
        """)
        st.markdown("""
        <div class="map-btn-card">
            <a href="https://maps.google.com/?q=New+Chitose+Airport" target="_blank">📍新千歲機場</a>
        </div>
        - 🕒 **14:00** 搭乘泰亞航 FD243 返回桃園機場<br>
        - 🕒 **17:55** 順利抵達桃園機場
        """, unsafe_allow_html=True)

# --- TAB 2: 票券與伴手禮清單 ---
with tab2:
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.subheader("🎫 票券與行前準備")
        st.checkbox("eSIM (NT$459)", value=False)
        st.checkbox("統聯車票 (NT$395)", value=False)
        st.checkbox("Suica 充值 (iPhone)", value=False)
        st.checkbox("退稅線上登入", value=False)
        st.checkbox("Visit Japan Web 線上入境申請", value=True)
    with col_t2:
        st.subheader("🛍️ 伴手禮採購清單")
        st.checkbox("白色戀人")
        st.checkbox("ROYCE 巧克力")
        st.checkbox("薯條三兄弟")
        st.checkbox("六花亭餅乾")
        st.checkbox("北菓樓泡芙")
        st.checkbox("LeTao紅茶巧克力餅乾")

# --- TAB 3: 機票與住宿 ---
with tab3:
    col_f, col_h = st.columns(2)
    with col_f:
        st.subheader("✈️ 機票資訊")
        st.markdown("""
        **【去程｜12/06（日）】**
        - 班機：FD242（05:55 TPE ➔ 10:40 CTS）
        - 價格：NT$6,934 / 人（手提 7kg、托運 20kg）
        
        **【回程｜12/12（六）】**
        - 班機：FD243（14:00 CTS ➔ 17:55 TPE）
        - 價格：NT$12,379 / 人（手提 7kg、托運 25/30kg）
        """)
    with col_h:
        st.subheader("🏠 住宿資訊")
        st.markdown("""
        **Holiday Inn Express Sapporo Susukino**
        - 日期：12/06 ～ 12/12（6 晚）
        - 價格：NT$7,800 ／ 人
        - 地址：〒064-0805 北海道札幌市中央区南5条西6丁目14-1
        - 交通：札幌市區地鐵「薄野站」4 號出口
        """)
        st.markdown("""
        <div class="map-btn-card">
            <a href="https://maps.google.com/?q=Holiday+Inn+Express+Sapporo+Susukino" target="_blank">🗺️ 點擊開啟：Google 地圖導航飯店位置</a>
        </div>
        """, unsafe_allow_html=True)

# --- TAB 4: 預算總覽 ---
with tab4:
    st.subheader("💰 已規劃活動與預算一覽")
    st.markdown("""
    | 項目 | 日期 | 預估價格（每人） |
    | :--- | :---: | :--- |
    | 去程機票 (FD242) | 12/06 | NT$ 6,934 |
    | 回程機票 (FD243) | 12/12 | NT$ 12,379 |
    | 薄野 IHG 飯店 (6晚) | 12/06-12/12 | NT$ 7,800 |
    | 旭川動物園・美瑛一日遊 | 12/07 | NT$ 1,775 |
    | 定山溪漂流體驗 | 12/08 | ¥10,000 (約 NT$ 2,100) |
    | 手稻滑雪場體驗與雪盆 | 12/10 | NT$ 5,495 |
    | eSIM 卡 + 統聯接駁 | - | NT$ 854 |
    """)
