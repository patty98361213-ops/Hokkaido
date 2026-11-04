import streamlit as st

# 1. 頁面基本設定
st.set_page_config(
    page_title="北海道 7 天 6 夜行程表",
    page_icon="❄️",
    layout="wide"
)

# 2. 法式奶油風 + 精緻文字超連結 CSS 樣式（無底色區塊）
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
    
    /* 精緻超連結樣式：無色塊、僅改變字體顏色與加入優雅底線 */
    .stApp a {
        color: #A67C52 !important;
        text-decoration: none !important;
        border-bottom: 1px dashed #A67C52;
        transition: 0.2s ease;
        font-weight: 500;
    }
    .stApp a:hover {
        color: #735335 !important;
        border-bottom: 1px solid #735335;
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
        - 🕒 **13:30** 搭乘計程車前往飯店寄放行李
        - 🕒 **15:00** 飯店 Check-in：[札幌薄野 Holiday Inn Express](https://maps.google.com/?q=Holiday+Inn+Express+Sapporo+Susukino)
        
        **🏙️ 札幌市區景點**
        - [大通公園](https://maps.google.com/?q=Odori+Park+Sapporo)
        - [札幌電視塔](https://maps.google.com/?q=Sapporo+TV+Tower)
        - [狸小路商店街](https://maps.google.com/?q=Tanukikoji+Shopping+Street)
        - [PARCO 百貨公司](https://maps.google.com/?q=Sapporo+PARCO)
        - [大丸百貨公司](https://maps.google.com/?q=Daimaru+Sapporo)
        
        **🍜 美食推薦**
        - [Soup Curry GARAKU 湯咖哩](https://maps.google.com/?q=Soup+Curry+GARAKU+Sapporo)
        - 🍓 水果吃爆：草莓等特產水果
        """)

    with st.expander("Day 2｜12/07（一）旭川動物園・美瑛一日遊"):
        st.markdown("""
        - 🕒 **07:30** 集合地點：[札幌電視塔 1 樓資訊中心（大通地鐵 27 號出口旁）](https://maps.google.com/?q=Sapporo+TV+Tower)
        
        **🚌 Klook 一日遊景點**
        - [旭川動物園（企鵝散步）](https://maps.google.com/?q=Asahiyama+Zoo)
        - [美瑛青池](https://maps.google.com/?q=Shirogane+Blue+Pond)
        - [白鬚瀑布](https://maps.google.com/?q=Shirahige+Waterfall)
        - [聖誕樹之木](https://maps.google.com/?q=Christmas+Tree+Biei)
        - [精靈露台](https://maps.google.com/?q=Ningle+Terrace)
        - 🕒 **19:30** 返回札幌
        
        **🍜 美食推薦**
        - 🏪 早餐：超商買好車上吃
        - 🕒 **20:00** [味噌拉麵 すみれ (Sumire)](https://maps.google.com/?q=Sumire+Sapporo+Susukino)
        - 🍓 水果吃爆：草莓等
        """)

    with st.expander("Day 3｜12/08（二）定山溪漂流"):
        st.markdown("""
        - 🕒 **09:30** 從薄野公車站搭乘公車前往定山溪
        - 🕒 **11:30** 集合地點：[フリルフスリフ（Friluftsliv）](https://maps.google.com/?q=Friluftsliv+Jozankei)
        - 🚣 漂流活動時間約 5 小時（費用：¥10,000／人）
        
        **🍜 美食推薦**
        - 🕒 **18:00** [羊座](https://maps.app.goo.gl/hFQD9MeCFw2uT5wH6?g_st=ic)
        """)

    with st.expander("Day 4｜12/09（三）小樽一日遊"):
        st.markdown("""
        - 🚇 交通：JR 前往南小樽站（約 40 分鐘）
        
        **🗺️ 預計遊覽順序**
        1. [住吉神社](https://maps.google.com/?q=Sumiyoshi+Shrine+Otaru)
        2. [Un délice (アンデリス 布丁)](https://maps.google.com/?q=Un+delice+Otaru)
        3. [小樽堺町商店街](https://maps.google.com/?q=Otaru+Sakaimachi+Street)
           - [北一硝子館](https://maps.google.com/?q=Kitaichi+Glass+Otaru)
           - [音樂盒堂](https://maps.google.com/?q=Otaru+Music+Box+Museum)
           - [Spoony 茶屋小樽店](https://maps.google.com/?q=Spoony+Otaru)
        4. [小樽出拔小路](https://maps.google.com/?q=Otaru+Debanukoji)
        5. [小樽運河](https://maps.google.com/?q=Otaru+Canal)
        
        **🍜 美食推薦**
        - [若雞時代 なると 本店](https://maps.google.com/?q=Naruto+Main+Shop+Otaru)
        """)

    with st.expander("Day 5｜12/10（四）手稻滑雪場"):
        st.markdown("""
        - 🕒 **07:45** 集合地點：[THE SUSUKINO SQUARE WEST (1樓)](https://maps.google.com/?q=THE+SUSUKINO+SQUARE+WEST)
        - 📍 地址：〒064-0806 北海道札幌市中央区南6条西5丁目3-6
        
        **⛷️ 活動內容**
        - [手稻滑雪場 (Sapporo Teine)](https://maps.google.com/?q=Sapporo+Teine)
        - 滑雪體驗 & 雪盆活動（NT$5,495／人）
        
        **🍜 美食推薦**
        - 🕒 **20:30** [蟹座](https://maps.google.com/?q=Kaniza+Sapporo)
        """)

    with st.expander("Day 6｜12/11（五）札幌市區深入漫遊"):
        st.markdown("""
        - [狸小路商店街逛街](https://maps.google.com/?q=Tanukikoji+Shopping+Street)
        - [中島公園拍照](https://maps.google.com/?q=Nakajima+Park+Sapporo)
        - [白色戀人公園](https://maps.google.com/?q=Shiroi+Koibito+Park)（訂製紀念鐵盒）
        - [北海道神宮](https://maps.google.com/?q=Hokkaido+Shrine)（💡 建議 9:00 前抵達購買限定梅酒與玻璃珠御守）
        
        **🍜 美食推薦**
        - [一蘭拉麵 札幌薄野店](https://maps.google.com/?q=Ichiran+Ramen+Susukino)
        - [トリトン迴轉壽司 (Toriton)](https://maps.google.com/?q=Toriton+Sushi+Sapporo)
        - 🍓 水果吃爆：草莓等
        """)

    with st.expander("Day 7｜12/12（六）新千歲機場・採購返台"):
        st.markdown("""
        - 🕒 **09:00** 從飯店搭乘計程車前往札幌車站
        - 🕒 **10:00** 從札幌搭乘 JR 前往新千歲機場
        - 🕒 **11:00** [新千歲機場逛街與免稅店採購](https://maps.google.com/?q=New+Chitose+Airport)
        - 🕒 **14:00** 搭乘泰亞航 FD243 返回桃園機場
        - 🕒 **17:55** 順利抵達桃園機場
        """)

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
        **[Holiday Inn Express Sapporo Susukino](https://maps.google.com/?q=Holiday+Inn+Express+Sapporo+Susukino)**
        - 日期：12/06 ～ 12/12（6 晚）
        - 價格：NT$7,800 ／ 人
        - 地址：〒064-0805 北海道札幌市中央区南5条西6丁目14-1
        - 交通：札幌市區地鐵「薄野站」4 號出口
        """)

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
    | 巴士接駁 | 12/08 | NT$ 600 |
    | 手稻滑雪場體驗與雪盆 | 12/10 | NT$ 5,495 |
    | eSIM 卡 + 統聯接駁 | - | NT$ 854 |
    """)
