import streamlit as st

# 1. 頁面基本設定
st.set_page_config(
    page_title="北海道 7 天 6 夜行程表",
    page_icon="❄️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. 法式奶油風 (French Cream Aesthetic) CSS 樣式
st.markdown("""
<style>
    /* 全域背景與文字 */
    .stApp {
        background-color: #FDFBF7;
        color: #4A443F;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    /* 側邊欄樣式 */
    section[data-testid="stSidebar"] {
        background-color: #F7F2E8;
        border-right: 1px solid #EAE3D2;
    }
    
    /* 卡片通用樣式 */
    .cream-card {
        background-color: #FFFFFF;
        border: 1px solid #EAE3D2;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(184, 169, 154, 0.08);
    }
    
    /* 標題與重點色 */
    h1, h2, h3 {
        color: #6E5A44 !important;
        font-weight: 600;
    }
    
    /* 行程時間點樣式 */
    .time-badge {
        background-color: #EFE9DB;
        color: #6E5A44;
        padding: 4px 10px;
        border-radius: 6px;
        font-weight: bold;
        font-size: 0.9em;
        display: inline-block;
        margin-bottom: 8px;
    }
    
    /* 連結樣式 */
    a {
        color: #C28D56 !important;
        text-decoration: none !important;
        font-weight: 500;
    }
    a:hover {
        text-decoration: underline !important;
    }
    
    /* 分隔線 */
    hr {
        border-top: 1px solid #EAE3D2;
        margin: 25px 0;
    }
</style>
""", unsafe_allow_html=True)

# 3. 頁面主標題
st.title("🇯🇵 日本北海道 7 天 6 夜行程表")
st.caption("📅 2026/12/06（日）～ 12/12（六）｜ ❄️ 奶油風隨身旅遊指南")

# 4. 側邊欄：票券與清單進度
st.sidebar.header("🎫 票券與待辦事項")

col_sb1, col_sb2 = st.sidebar.columns(2)
with col_sb1:
    esim = st.checkbox("eSIM (NT$459)", value=False)
    ubus = st.checkbox("統聯車票 (NT$395)", value=False)
    suica = st.checkbox("Suica 充值", value=False)
with col_sb2:
    tax = st.checkbox("退稅線上登入", value=False)
    vvisit = st.checkbox("Visit Japan Web", value=True)

st.sidebar.markdown("---")
st.sidebar.header("🛍️ 伴手禮採購清單")
gift1 = st.sidebar.checkbox("白色戀人")
gift2 = st.sidebar.checkbox("ROYCE 巧克力")
gift3 = st.sidebar.checkbox("薯條三兄弟")
gift4 = st.sidebar.checkbox("六花亭餅乾")
gift5 = st.sidebar.checkbox("北菓樓泡芙")
gift6 = st.sidebar.checkbox("Prada 氣墊彩妝")

# 5. 分頁選項
tab_itinerary, tab_info, tab_budget = st.tabs(["📅 每日行程", "✈️ 機票與住宿", "💰 預算與活動"])

# --- TAB 1: 每日行程 ---
with tab_itinerary:
    
    # Day 1
    with st.expander("Day 1｜12/06（日）抵達札幌・市區逛街", expanded=True):
        st.markdown("""
        <div class="cream-card">
            <span class="time-badge">05:55</span> 桃園機場起飛（FD242）<br>
            <span class="time-badge">10:40</span> 抵達新千歲機場（入境預計至 12:00）<br>
            <span class="time-badge">12:30</span> 搭乘 JR 前往札幌（約 40 分鐘）<br>
            <span class="time-badge">15:00</span> <a href="https://maps.google.com/?q=Holiday+Inn+Express+Sapporo+Susukino" target="_blank">📍 飯店 Check-in（札幌薄野 Holiday Inn Express）</a>
            <hr>
            <h4>🏙️ 札幌市區景點</h4>
            <ul>
                <li><a href="https://maps.google.com/?q=Odori+Park+Sapporo" target="_blank">📍 大通公園</a></li>
                <li><a href="https://maps.google.com/?q=Sapporo+TV+Tower" target="_blank">📍 札幌電視塔</a></li>
                <li><a href="https://maps.google.com/?q=Tanukikoji+Shopping+Street" target="_blank">📍 狸小路商店街</a></li>
                <li><a href="https://maps.google.com/?q=Sapporo+PARCO" target="_blank">📍 PARCO 百貨公司</a></li>
                <li><a href="https://maps.google.com/?q=Daimaru+Sapporo" target="_blank">📍 大丸百貨公司</a></li>
            </ul>
            <hr>
            <h4>🍜 美食推薦</h4>
            <ul>
                <li><a href="https://maps.google.com/?q=Soup+Curry+GARAKU+Sapporo" target="_blank">📍 Soup Curry GARAKU 湯咖哩</a></li>
                <li>🍓 水果吃爆：草莓等特產水果</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Day 2
    with st.expander("Day 2｜12/07（一）旭川動物園・美瑛一日遊"):
        st.markdown("""
        <div class="cream-card">
            <span class="time-badge">07:30</span> 集合點：<a href="https://maps.google.com/?q=Sapporo+TV+Tower" target="_blank">📍 札幌電視塔 1 樓資訊中心</a>（大通地鐵 27 號出口旁）
            <hr>
            <h4>🚌 預訂行程景點 (Klook)</h4>
            <ul>
                <li><a href="https://maps.google.com/?q=Asahiyama+Zoo" target="_blank">📍 旭川動物園</a>（企鵝散步）</li>
                <li><a href="https://maps.google.com/?q=Shirogane+Blue+Pond" target="_blank">📍 美瑛青池</a></li>
                <li><a href="https://maps.google.com/?q=Shirahige+Waterfall" target="_blank">📍 白鬚瀑布</a></li>
                <li><a href="https://maps.google.com/?q=Christmas+Tree+Biei" target="_blank">📍 聖誕樹之木</a></li>
                <li><a href="https://maps.google.com/?q=Ningle+Terrace" target="_blank">📍 精靈露台</a></li>
            </ul>
            <span class="time-badge">19:30</span> 返回札幌
            <hr>
            <h4>🍜 美食推薦</h4>
            <ul>
                <li>🏪 早餐：超商買好車上吃</li>
                <li><a href="https://maps.google.com/?q=Sumire+Sapporo+Susukino" target="_blank">📍 20:00 味噌拉麵 すみれ (Sumire)</a></li>
                <li>🍓 水果吃爆：草莓等</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Day 3
    with st.expander("Day 3｜12/08（二）定山溪漂流"):
        st.markdown("""
        <div class="cream-card">
            <span class="time-badge">11:30</span> 集合地點：<a href="https://maps.google.com/?q=Friluftsliv+Jozankei" target="_blank">📍 フリルフスリフ（Friluftsliv）</a><br>
            🚣 漂流活動時間約 5 小時（費用：¥10,000／人）
            <hr>
            <h4>🍜 美食推薦</h4>
            <ul>
                <li><a href="https://maps.google.com/?q=Kaniza+Sapporo" target="_blank">📍 蟹座</a></li>
                <li>🍓 水果吃爆：草莓等</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Day 4
    with st.expander("Day 4｜12/09（三）小樽一日遊"):
        st.markdown("""
        <div class="cream-card">
            🚇 交通：JR 前往南小樽站（約 40 分鐘）
            <hr>
            <h4>🗺️ 預計遊覽順序</h4>
            <ol>
                <li><a href="https://maps.google.com/?q=Sumiyoshi+Shrine+Otaru" target="_blank">📍 住吉神社</a></li>
                <li><a href="https://maps.google.com/?q=Un+delice+Otaru" target="_blank">📍 Un délice (アンデリス 布丁)</a></li>
                <li><a href="https://maps.google.com/?q=Otaru+Sakaimachi+Street" target="_blank">📍 小樽堺町商店街</a>
                    <ul>
                        <li><a href="https://maps.google.com/?q=Kitaichi+Glass+Otaru" target="_blank">📍 北一硝子館</a></li>
                        <li><a href="https://maps.google.com/?q=Otaru+Music+Box+Museum" target="_blank">📍 音樂盒堂</a></li>
                        <li><a href="https://maps.google.com/?q=Spoony+Otaru" target="_blank">📍 Spoony 茶屋小樽店</a></li>
                    </ul>
                </li>
                <li><a href="https://maps.google.com/?q=Otaru+Debanukoji" target="_blank">📍 小樽出拔小路</a></li>
                <li><a href="https://maps.google.com/?q=Otaru+Canal" target="_blank">📍 小樽運河</a></li>
            </ol>
            <hr>
            <h4>🍜 美食推薦</h4>
            <ul>
                <li><a href="https://maps.google.com/?q=Naruto+Main+Shop+Otaru" target="_blank">📍 若雞時代 なると 本店</a></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Day 5
    with st.expander("Day 5｜12/10（四）手稻滑雪場"):
        st.markdown("""
        <div class="cream-card">
            <span class="time-badge">07:45</span> 集合地點：<a href="https://maps.google.com/?q=THE+SUSUKINO+SQUARE+WEST" target="_blank">📍 THE SUSUKINO SQUARE WEST (1樓 A/B/E號)</a><br>
            📍 地址：〒064-0806 北海道札幌市中央区南6条西5丁目3-6
            <hr>
            <h4>⛷️ 活動內容</h4>
            <ul>
                <li><a href="https://maps.google.com/?q=Sapporo+Teine" target="_blank">📍 手稻滑雪場 (Sapporo Teine)</a></li>
                <li>🎿 滑雪體驗 & 🛷 雪盆活動（NT$5,495／人）</li>
            </ul>
            <hr>
            <h4>🍜 美食推薦</h4>
            <ul>
                <li><a href="https://maps.google.com/?q=Menya+Yukikaze+Susukino" target="_blank">📍 麵屋雪風 薄野本店</a></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Day 6
    with st.expander("Day 6｜12/11（五）札幌市區深入漫遊"):
        st.markdown("""
        <div class="cream-card">
            <h4>🛍️ 景點與購物行程</h4>
            <ul>
                <li><a href="https://maps.google.com/?q=Tanukikoji+Shopping+Street" target="_blank">📍 狸小路商店街、薄野商圈逛街</a></li>
                <li><a href="https://maps.google.com/?q=Nakajima+Park+Sapporo" target="_blank">📍 中島公園拍照</a></li>
                <li><a href="https://maps.google.com/?q=Shiroi+Koibito+Park" target="_blank">📍 白色戀人公園</a>（訂製紀念鐵盒）</li>
                <li><a href="https://maps.google.com/?q=Hokkaido+Shrine" target="_blank">📍 北海道神宮</a>（💡 建議 9:00 前抵達購買限定梅酒與玻璃珠御守）</li>
            </ul>
            <hr>
            <h4>🍜 美食推薦</h4>
            <ul>
                <li><a href="https://maps.google.com/?q=Ichiran+Ramen+Susukino" target="_blank">📍 一蘭拉麵 札幌薄野店</a></li>
                <li><a href="https://maps.google.com/?q=Toriton+Sushi+Sapporo" target="_blank">📍 トリトン迴轉壽司 (Toriton)</a></li>
                <li>🍓 水果吃爆：草莓等</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # Day 7
    with st.expander("Day 7｜12/12（六）新千歲機場・採購返台"):
        st.markdown("""
        <div class="cream-card">
            <span class="time-badge">10:00</span> 從札幌搭乘 JR 前往新千歲機場<br>
            <span class="time-badge">11:00</span> <a href="https://maps.google.com/?q=New+Chitose+Airport" target="_blank">📍 新千歲機場逛街與免稅店採購</a><br>
            💄 彩妝採購：Prada 氣墊粉餅<br>
            <span class="time-badge">14:00</span> 搭乘泰亞航 FD243 返回桃園機場<br>
            <span class="time-badge">17:55</span> 順利抵達桃園機場
        </div>
        """, unsafe_allow_html=True)

# --- TAB 2: 機票與住宿 ---
with tab_info:
    col_flight, col_hotel = st.columns(2)
    
    with col_flight:
        st.markdown("""
        <div class="cream-card">
            <h3>✈️ 機票資訊（泰國亞洲航空）</h3>
            <p><b>【去程｜12/06（日）】</b><br>
            • 班機：FD242（05:55 TPE ➔ 10:40 CTS）<br>
            • 航廈：桃園 T1 ➔ 新千歲 T1<br>
            • 價格：NT$6,934 / 人<br>
            • 行李：手提 7kg、托運 20kg</p>
            <hr>
            <p><b>【回程｜12/12（六）】</b><br>
            • 班機：FD243（14:00 CTS ➔ 17:55 TPE）<br>
            • 航廈：新千歲 T1 ➔ 桃園 T1<br>
            • 價格：NT$12,379 / 人<br>
            • 行李：手提 7kg、托運 25/30kg</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_hotel:
        st.markdown("""
        <div class="cream-card">
            <h3>🏠 住宿資訊</h3>
            <p><b>Holiday Inn Express Sapporo Susukino</b><br>
            ホリデイ・イン エクスプレス札幌すすきの</p>
            <p>• 日期：12/06 ～ 12/12（共 6 晚）<br>
            • 價格：NT$7,800 ／ 人<br>
            • 地址：〒064-0805 北海道札幌市中央区南5条西6丁目14-1<br>
            • 交通：札幌市區地鐵「薄野站」4 號出口（有電梯）</p>
            <p><a href="https://maps.google.com/?q=Holiday+Inn+Express+Sapporo+Susukino" target="_blank">🗺️ 在 Google 地圖中開啟飯店位置</a></p>
        </div>
        """, unsafe_allow_html=True)

# --- TAB 3: 預算與活動 ---
with tab_budget:
    st.markdown("""
    <div class="cream-card">
        <h3>💰 已規劃預定活動與費用總覽</h3>
        <table style="width:100%; text-align:left; border-collapse: collapse;">
            <tr style="border-bottom: 1px solid #EAE3D2;">
                <th style="padding: 8px;">項目</th>
                <th style="padding: 8px;">日期</th>
                <th style="padding: 8px;">預估價格（每人）</th>
            </tr>
            <tr style="border-bottom: 1px solid #EAE3D2;">
                <td style="padding: 8px;">去程機票 (FD242)</td>
                <td style="padding: 8px;">12/06</td>
                <td style="padding: 8px;">NT$ 6,934</td>
            </tr>
            <tr style="border-bottom: 1px solid #EAE3D2;">
                <td style="padding: 8px;">回程機票 (FD243)</td>
                <td style="padding: 8px;">12/12</td>
                <td style="padding: 8px;">NT$ 12,379</td>
            </tr>
            <tr style="border-bottom: 1px solid #EAE3D2;">
                <td style="padding: 8px;">薄野 IHG 飯店 (6晚)</td>
                <td style="padding: 8px;">12/06-12/12</td>
                <td style="padding: 8px;">NT$ 7,800</td>
            </tr>
            <tr style="border-bottom: 1px solid #EAE3D2;">
                <td style="padding: 8px;">旭川動物園・美瑛一日遊 (Klook)</td>
                <td style="padding: 8px;">12/07</td>
                <td style="padding: 8px;">NT$ 1,775</td>
            </tr>
            <tr style="border-bottom: 1px solid #EAE3D2;">
                <td style="padding: 8px;">定山溪漂流體驗</td>
                <td style="padding: 8px;">12/08</td>
                <td style="padding: 8px;">¥10,000 (約 NT$ 2,100)</td>
            </tr>
            <tr style="border-bottom: 1px solid #EAE3D2;">
                <td style="padding: 8px;">手稻滑雪場體驗與雪盆</td>
                <td style="padding: 8px;">12/10</td>
                <td style="padding: 8px;">NT$ 5,495</td>
            </tr>
            <tr style="border-bottom: 1px solid #EAE3D2;">
                <td style="padding: 8px;">eSIM 網路卡 + 統聯接駁</td>
                <td style="padding: 8px;">-</td>
                <td style="padding: 8px;">NT$ 854</td>
            </tr>
        </table>
    </div>
    """, unsafe_allow_html=True)
