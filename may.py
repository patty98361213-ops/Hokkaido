<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🇯🇵 北海道 7 天 6 夜冬日奢華之旅 (2026/12/06 - 12/12)</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- FontAwesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Google Font Inter & Noto Sans TC -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Noto+Sans+TC:wght@300;400;500;700&display=swap" rel="stylesheet">
    
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        ice: {
                            50: '#f0f9ff',
                            100: '#e0f2fe',
                            200: '#bae6fd',
                            300: '#7dd3fc',
                            400: '#38bdf8',
                            500: '#0ea5e9',
                            600: '#0284c7',
                            700: '#0369a1',
                            800: '#075985',
                            900: '#0c4a6e',
                        },
                        snow: '#f8fafc',
                    },
                    fontFamily: {
                        sans: ['Inter', 'Noto Sans TC', 'sans-serif'],
                    }
                }
            }
        }
    </script>
    <style>
        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #0f172a;
        }
        ::-webkit-scrollbar-thumb {
            background: #38bdf8;
            border-radius: 4px;
        }
        
        /* Glassmorphism Effect */
        .glass-card {
            background: rgba(15, 23, 42, 0.65);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.12);
        }
        .glass-nav {
            background: rgba(15, 23, 42, 0.85);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        /* Falling Snowflakes Canvas Animation Background */
        #snow-canvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 0;
        }

        /* Checkbox Custom Animation */
        .custom-checkbox:checked + label {
            text-decoration: line-through;
            opacity: 0.6;
        }
    </style>
</head>
<body class="bg-slate-950 text-slate-100 font-sans min-h-screen relative overflow-x-hidden selection:bg-ice-500 selection:text-white">

    <!-- Snow Animation Background -->
    <canvas id="snow-canvas"></canvas>

    <!-- Main Container -->
    <div class="relative z-10 flex flex-col min-h-screen">
        
        <!-- Header & Banner -->
        <header class="relative pt-8 pb-6 px-4 sm:px-8 text-center border-b border-slate-800/60 overflow-hidden">
            <div class="max-w-5xl mx-auto relative z-10">
                <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-ice-500/20 text-ice-300 border border-ice-400/30 text-xs font-semibold tracking-wide uppercase mb-3">
                    <i class="fa-solid fa-snowflake animate-spin" style="animation-duration: 8s;"></i> 2026 冬季限定行程
                </div>
                <h1 class="text-3xl sm:text-5xl font-extrabold tracking-tight bg-gradient-to-r from-white via-ice-200 to-ice-400 bg-clip-text text-transparent mb-2">
                    🇯🇵 日本北海道 7 天 6 夜行程指南
                </h1>
                <p class="text-slate-400 text-sm sm:text-base flex items-center justify-center gap-2">
                    <i class="fa-regular fa-calendar text-ice-400"></i> 2026/12/06（日）～ 12/12（六）
                    <span class="inline-block w-1 h-1 rounded-full bg-slate-600"></span>
                    <i class="fa-solid fa-location-dot text-rose-400"></i> 札幌・旭川・小樽・定山溪
                </p>
            </div>
        </header>

        <!-- Navigation Tabs -->
        <nav class="sticky top-0 z-30 glass-nav shadow-lg">
            <div class="max-w-5xl mx-auto px-2 sm:px-4">
                <div class="flex overflow-x-auto no-scrollbar py-2 space-x-1 sm:space-x-2 text-sm font-medium">
                    <button onclick="switchTab('overview')" id="tab-overview" class="nav-btn active flex items-center gap-2 px-4 py-2.5 rounded-xl transition duration-200 text-white bg-ice-600/80 shadow-lg shadow-ice-500/20 whitespace-nowrap">
                        <i class="fa-solid fa-plane"></i> 機票 & 住宿
                    </button>
                    <button onclick="switchTab('daily')" id="tab-daily" class="nav-btn flex items-center gap-2 px-4 py-2.5 rounded-xl transition duration-200 text-slate-400 hover:text-white hover:bg-slate-800/60 whitespace-nowrap">
                        <i class="fa-solid fa-calendar-days"></i> 每日行程
                    </button>
                    <button onclick="switchTab('budget')" id="tab-budget" class="nav-btn flex items-center gap-2 px-4 py-2.5 rounded-xl transition duration-200 text-slate-400 hover:text-white hover:bg-slate-800/60 whitespace-nowrap">
                        <i class="fa-solid fa-ticket"></i> 票券與預算
                    </button>
                    <button onclick="switchTab('souvenirs')" id="tab-souvenirs" class="nav-btn flex items-center gap-2 px-4 py-2.5 rounded-xl transition duration-200 text-slate-400 hover:text-white hover:bg-slate-800/60 whitespace-nowrap">
                        <i class="fa-solid fa-bag-shopping"></i> 伴手禮清單
                    </button>
                </div>
            </div>
        </nav>

        <!-- Content Sections -->
        <main class="flex-grow max-w-5xl w-full mx-auto p-4 sm:p-6 space-y-8">

            <!-- SECTION 1: 機票 & 住宿 (Overview) -->
            <section id="section-overview" class="tab-content space-y-6">
                <!-- Flights Grid -->
                <h2 class="text-xl font-bold text-ice-300 flex items-center gap-2">
                    <i class="fa-solid fa-plane-departure text-ice-400"></i> 航班資訊 (泰國亞洲航空)
                </h2>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 sm:gap-6">
                    <!-- Departure Flight Card -->
                    <div class="glass-card rounded-2xl p-5 hover:border-ice-400/50 transition duration-300 relative overflow-hidden group">
                        <div class="absolute -right-6 -bottom-6 w-24 h-24 bg-ice-500/10 rounded-full blur-xl group-hover:bg-ice-500/20 transition"></div>
                        <div class="flex justify-between items-center mb-4">
                            <span class="px-3 py-1 rounded-full text-xs font-semibold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
                                去程｜12/06（日）
                            </span>
                            <span class="text-xs text-slate-400">泰亞航 FD242</span>
                        </div>
                        <div class="flex justify-between items-center my-4">
                            <div class="text-center sm:text-left">
                                <div class="text-2xl font-black text-white">05:55</div>
                                <div class="text-xs text-slate-400">桃園機場 (T1)</div>
                            </div>
                            <div class="flex flex-col items-center px-4">
                                <span class="text-[10px] text-ice-300 font-mono mb-1">4h 45m</span>
                                <div class="w-24 sm:w-32 h-[2px] bg-gradient-to-r from-transparent via-ice-400 to-transparent relative">
                                    <i class="fa-solid fa-plane text-ice-400 absolute left-1/2 -top-2.5 -translate-x-1/2 text-xs"></i>
                                </div>
                            </div>
                            <div class="text-center sm:text-right">
                                <div class="text-2xl font-black text-white">10:40</div>
                                <div class="text-xs text-slate-400">新千歲機場</div>
                            </div>
                        </div>
                        <div class="mt-4 pt-4 border-t border-slate-800/80 flex justify-between text-xs text-slate-300">
                            <span><i class="fa-solid fa-suitcase-rolling text-ice-400 mr-1"></i> 手提 7kg / 託運 20kg</span>
                            <span class="font-bold text-ice-300">NT$ 6,934</span>
                        </div>
                    </div>

                    <!-- Return Flight Card -->
                    <div class="glass-card rounded-2xl p-5 hover:border-ice-400/50 transition duration-300 relative overflow-hidden group">
                        <div class="absolute -right-6 -bottom-6 w-24 h-24 bg-amber-500/10 rounded-full blur-xl group-hover:bg-amber-500/20 transition"></div>
                        <div class="flex justify-between items-center mb-4">
                            <span class="px-3 py-1 rounded-full text-xs font-semibold bg-amber-500/20 text-amber-300 border border-amber-500/30">
                                回程｜12/12（六）
                            </span>
                            <span class="text-xs text-slate-400">泰亞航 FD243</span>
                        </div>
                        <div class="flex justify-between items-center my-4">
                            <div class="text-center sm:text-left">
                                <div class="text-2xl font-black text-white">14:00</div>
                                <div class="text-xs text-slate-400">新千歲機場</div>
                            </div>
                            <div class="flex flex-col items-center px-4">
                                <span class="text-[10px] text-amber-300 font-mono mb-1">4h 55m</span>
                                <div class="w-24 sm:w-32 h-[2px] bg-gradient-to-r from-transparent via-amber-400 to-transparent relative">
                                    <i class="fa-solid fa-plane text-amber-400 absolute left-1/2 -top-2.5 -translate-x-1/2 text-xs"></i>
                                </div>
                            </div>
                            <div class="text-center sm:text-right">
                                <div class="text-2xl font-black text-white">17:55</div>
                                <div class="text-xs text-slate-400">桃園機場 (T1)</div>
                            </div>
                        </div>
                        <div class="mt-4 pt-4 border-t border-slate-800/80 flex justify-between text-xs text-slate-300">
                            <span><i class="fa-solid fa-suitcase-rolling text-amber-400 mr-1"></i> 手提 7kg / 託運 25~30kg</span>
                            <span class="font-bold text-amber-300">NT$ 12,379</span>
                        </div>
                    </div>
                </div>

                <!-- Hotel Info Card -->
                <h2 class="text-xl font-bold text-ice-300 flex items-center gap-2 pt-4">
                    <i class="fa-solid fa-hotel text-ice-400"></i> 住宿資訊 (全六晚)
                </h2>
                <div class="glass-card rounded-2xl p-6 border-slate-700/60">
                    <div class="flex flex-col md:flex-row justify-between md:items-start gap-4">
                        <div class="space-y-2">
                            <div class="flex items-center gap-2 flex-wrap">
                                <span class="bg-indigo-500/20 text-indigo-300 text-xs px-2.5 py-1 rounded-md border border-indigo-500/30">連住 6 晚</span>
                                <h3 class="text-lg font-bold text-white">Holiday Inn Express Sapporo Susukino by IHG</h3>
                            </div>
                            <p class="text-sm text-slate-400 font-mono">日文名：ホリデイ・イン エクスプレス札幌すすきの</p>
                            <p class="text-sm text-slate-300 flex items-start gap-2 pt-1">
                                <i class="fa-solid fa-map-marker-alt text-rose-400 mt-1"></i>
                                <span>〒064-0805 北海道札幌市中央区南5条西6丁目14-1</span>
                            </p>
                        </div>
                        <div class="md:text-right bg-slate-900/60 p-4 rounded-xl border border-slate-800">
                            <div class="text-xs text-slate-400">預算每人分攤</div>
                            <div class="text-2xl font-extrabold text-emerald-400">NT$ 7,800 <span class="text-xs text-slate-400 font-normal">/ 人</span></div>
                            <div class="text-xs text-slate-400 mt-1">入住：12/06 ～ 退房：12/12</div>
                        </div>
                    </div>

                    <div class="mt-6 pt-4 border-t border-slate-800 grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs text-slate-300">
                        <div class="flex items-center gap-2 bg-slate-900/40 p-3 rounded-lg">
                            <i class="fa-solid fa-train-subway text-ice-400 text-base"></i>
                            <span><b>交通方式：</b> 札幌市區地鐵（薄野站 4 號出口有電梯）</span>
                        </div>
                        <div class="flex items-center gap-2 bg-slate-900/40 p-3 rounded-lg">
                            <i class="fa-solid fa-copy text-ice-400 text-base cursor-pointer hover:text-white" onclick="copyAddress()" title="點擊複製日文地址"></i>
                            <span id="hotel-address-text"><b>給司機看：</b> ホリデイ・イン エクスプレス札幌すすきの (南5条西6丁目)</span>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SECTION 2: 每日行程 (Daily Itinerary) -->
            <section id="section-daily" class="tab-content hidden space-y-6">
                <!-- Day Select Selector Bar -->
                <div class="flex overflow-x-auto no-scrollbar gap-2 pb-2">
                    <button onclick="showDay(1)" id="day-btn-1" class="day-btn px-4 py-2 rounded-xl text-xs font-bold whitespace-nowrap bg-ice-500 text-white shadow-md">Day 1 (12/06 日)</button>
                    <button onclick="showDay(2)" id="day-btn-2" class="day-btn px-4 py-2 rounded-xl text-xs font-bold whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">Day 2 (12/07 一)</button>
                    <button onclick="showDay(3)" id="day-btn-3" class="day-btn px-4 py-2 rounded-xl text-xs font-bold whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">Day 3 (12/08 二)</button>
                    <button onclick="showDay(4)" id="day-btn-4" class="day-btn px-4 py-2 rounded-xl text-xs font-bold whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">Day 4 (12/09 三)</button>
                    <button onclick="showDay(5)" id="day-btn-5" class="day-btn px-4 py-2 rounded-xl text-xs font-bold whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">Day 5 (12/10 四)</button>
                    <button onclick="showDay(6)" id="day-btn-6" class="day-btn px-4 py-2 rounded-xl text-xs font-bold whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">Day 6 (12/11 五)</button>
                    <button onclick="showDay(7)" id="day-btn-7" class="day-btn px-4 py-2 rounded-xl text-xs font-bold whitespace-nowrap bg-slate-800 text-slate-300 hover:bg-slate-700">Day 7 (12/12 六)</button>
                </div>

                <!-- Timeline Container -->
                <div class="glass-card rounded-2xl p-6 relative">
                    
                    <!-- DAY 1 -->
                    <div id="day-content-1" class="day-content space-y-6">
                        <div class="flex justify-between items-center border-b border-slate-800 pb-4">
                            <div>
                                <span class="text-xs text-ice-400 font-semibold tracking-wide">DAY 1 ｜ 2026/12/06（日）</span>
                                <h3 class="text-2xl font-bold text-white">抵達札幌・市區熱鬧逛街</h3>
                            </div>
                            <span class="px-3 py-1 bg-slate-800 text-ice-300 rounded-full text-xs font-mono">札幌市區</span>
                        </div>

                        <div class="space-y-6 relative border-l-2 border-ice-500/30 ml-3 pl-6">
                            <!-- Step 1 -->
                            <div class="relative">
                                <div class="absolute -left-[31px] top-0 w-4 h-4 rounded-full bg-ice-500 border-4 border-slate-950"></div>
                                <div class="text-xs text-ice-400 font-mono">05:55</div>
                                <h4 class="font-bold text-white">桃園機場第一航廈起飛</h4>
                                <p class="text-xs text-slate-400">搭乘泰國亞洲航空 FD242 班機。</p>
                            </div>
                            <!-- Step 2 -->
                            <div class="relative">
                                <div class="absolute -left-[31px] top-0 w-4 h-4 rounded-full bg-ice-500 border-4 border-slate-950"></div>
                                <div class="text-xs text-ice-400 font-mono">10:40 - 12:00</div>
                                <h4 class="font-bold text-white">抵達新千歲機場 & 入境處理</h4>
                                <p class="text-xs text-slate-400">辦理入境手續、提領行李、開啟 eSIM 網路。</p>
                            </div>
                            <!-- Step 3 -->
                            <div class="relative">
                                <div class="absolute -left-[31px] top-0 w-4 h-4 rounded-full bg-ice-500 border-4 border-slate-950"></div>
                                <div class="text-xs text-ice-400 font-mono">13:00 - 15:00</div>
                                <h4 class="font-bold text-white">JR 前往札幌市區 & 飯店 Check-in</h4>
                                <p class="text-xs text-slate-400">搭乘 JR 快速 Airport 線（約 40 分鐘）至札幌站，轉地鐵至薄野站 Check-in 放置行李。</p>
                            </div>
                            <!-- Step 4 -->
                            <div class="relative">
                                <div class="absolute -left-[31px] top-0 w-4 h-4 rounded-full bg-ice-500 border-4 border-slate-950"></div>
                                <div class="text-xs text-ice-400 font-mono">15:30 之後</div>
                                <h4 class="font-bold text-white">札幌市區熱點巡禮</h4>
                                <div class="flex flex-wrap gap-2 mt-2">
                                    <span class="px-2.5 py-1 bg-slate-800 text-slate-200 text-xs rounded-md">大通公園</span>
                                    <span class="px-2.5 py-1 bg-slate-800 text-slate-200 text-xs rounded-md">札幌電視塔</span>
                                    <span class="px-2.5 py-1 bg-slate-800 text-slate-200 text-xs rounded-md">狸小路商店街</span>
                                    <span class="px-2.5 py-1 bg-slate-800 text-slate-200 text-xs rounded-md">PARCO 百貨</span>
                                    <span class="px-2.5 py-1 bg-slate-800 text-slate-200 text-xs rounded-md">大丸百貨</span>
                                </div>
                            </div>
                            <!-- Food -->
                            <div class="bg-amber-500/10 border border-amber-500/30 rounded-xl p-4 text-xs space-y-2">
                                <div class="font-bold text-amber-300 flex items-center gap-1.5 text-sm">
                                    <i class="fa-solid fa-utensils"></i> 今日美食重點
                                </div>
                                <p class="text-slate-300">🍜 <b>Soup Curry GARAKU Sapporo Main Restaurant</b> (湯咖哩首選)</p>
                                <p class="text-slate-300">🍓 <b>水果吃爆：</b> 日本冬草莓開吃！</p>
                            </div>
                        </div>
                    </div>

                    <!-- DAY 2 -->
                    <div id="day-content-2" class="day-content hidden space-y-6">
                        <div class="flex justify-between items-center border-b border-slate-800 pb-4">
                            <div>
                                <span class="text-xs text-ice-400 font-semibold tracking-wide">DAY 2 ｜ 2026/12/07（一）</span>
                                <h3 class="text-2xl font-bold text-white">旭川動物園・美瑛夢幻一日遊</h3>
                            </div>
                            <span class="px-3 py-1 bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 rounded-full text-xs font-semibold">Klook 預訂行程</span>
                        </div>

                        <div class="space-y-6 relative border-l-2 border-indigo-500/30 ml-3 pl-6">
                            <div class="relative">
                                <div class="absolute -left-[31px] top-0 w-4 h-4 rounded-full bg-indigo-500 border-4 border-slate-950"></div>
                                <div class="text-xs text-indigo-400 font-mono">07:30 (務必準時)</div>
                                <h4 class="font-bold text-white">集合：札幌電視塔 1 樓資訊中心</h4>
                                <p class="text-xs text-slate-400">大通地鐵 27 號出口旁。請提早 15 分鐘抵達。</p>
                            </div>
                            <div class="relative">
                                <div class="absolute -left-[31px] top-0 w-4 h-4 rounded-full bg-indigo-500 border-4 border-slate-950"></div>
                                <div class="text-xs text-indigo-400 font-mono">全天景點</div>
                                <h4 class="font-bold text-white">一日遊路線</h4>
                                <ul class="list-disc list-inside text-xs text-slate-300 space-y-1 mt-1">
                                    <li><b>旭川動物園：</b> 觀賞企鵝散步與可愛北極熊</li>
                                    <li><b>美瑛青池：</b> 冬季結冰點燈美景</li>
                                    <li><b>白鬚瀑布：</b> 藍白相間冰瀑絕景</li>
                                    <li><b>聖誕樹之木：</b> 孤獨的雪中聖誕樹 (視團體行程)</li>
                                    <li><b>精靈露台 (Ningle Terrace)：</b> 點燈森林木屋小鎮</li>
                                </ul>
                            </div>
                            <div class="relative">
                                <div class="absolute -left-[31px] top-0 w-4 h-4 rounded-full bg-indigo-500 border-4 border-slate-950"></div>
                                <div class="text-xs text-indigo-400 font-mono">19:30</div>
                                <h4 class="font-bold text-white">返回札幌</h4>
                            </div>
                            <div class="bg-amber-500/10 border border-amber-500/30 rounded-xl p-4 text-xs space-y-2">
                                <div class="font-bold text-amber-300 flex items-center gap-1.5 text-sm">
                                    <i class="fa-solid fa-utensils"></i> 美食與餐飲安排
                                </div>
                                <p class="text-slate-300">🏪 <b>早餐：</b> 乘車時間長，建議提早於便利商店買好車上吃。</p>
                                <p class="text-slate-300">🍜 <b>晚餐 (約 20:00)：</b> 味噌拉麵 すみれ (Sumire 經典濃郁札幌味噌拉麵)</p>
                            </div>
                        </div>
                    </div>

                    <!-- DAY 3 -->
                    <div id="day-content-3" class="day-content hidden space-y-6">
                        <div class="flex justify-between items-center border-b border-slate-800 pb-4">
                            <div>
                                <span class="text-xs text-ice-400 font-semibold tracking-wide">DAY 3 ｜ 2026/12/08（二）</span>
                                <h3 class="text-2xl font-bold text-white">定山溪冬日冰雪漂流冒險</h3>
                            </div>
                            <span class="px-3 py-1 bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 rounded-full text-xs font-semibold">¥10,000 / 人</span>
                        </div>

                        <div class="space-y-6 relative border-l-2 border-cyan-500/30 ml-3 pl-6">
                            <div class="relative">
                                <div class="absolute -left-[31px] top-0 w-4 h-4 rounded-full bg-cyan-500 border-4 border-slate-950"></div>
                                <div class="text-xs text-cyan-400 font-mono">11:30</div>
                                <h4 class="font-bold text-white">集合點：フリルフスリフ（Friluftsliv）</h4>
                                <p class="text-xs text-slate-400">交通方式待確認 (可搭乘定山溪河童號巴士或接駁專車)。</p>
                            </div>
                            <div class="relative">
                                <div class="absolute -left-[31px] top-0 w-4 h-4 rounded-full bg-cyan-500 border-4 border-slate-950"></div>
                                <div class="text-xs text-cyan-400 font-mono">12:00 - 17:00</div>
                                <h4 class="font-bold text-white">定山溪漂流活動 (約 5 小時)</h4>
                                <p class="text-xs text-slate-300">穿著防寒幹式防寒衣，穿越溪谷體驗冬季雪景漂流。</p>
                            </div>
                            <div class="bg-amber-500/10 border border-amber-500/30 rounded-xl p-4 text-xs space-y-2">
                                <div class="font-bold text-amber-300 flex items-center gap-1.5 text-sm">
                                    <i class="fa-solid fa-utensils"></i> 今日美饌
                                </div>
                                <p class="text-slate-300">🦀 <b>晚餐：</b> 蟹座 (享用北海道頂級螃蟹大餐)</p>
                                <p class="text-slate-300">🍓 <b>點心：</b> 飯店享用季節限定水蜜桃/草莓。</p>
                            </div>
                        </div>
                    </div>

                    <!-- DAY 4 -->
                    <div id="day-content-4" class="day-content hidden space-y-6">
                        <div class="flex justify-between items-center border-b border-slate-800 pb-4">
                            <div>
                                <span class="text-xs text-ice-400 font-semibold tracking-wide">DAY 4 ｜ 2026/12/09（三）</span>
                                <h3 class="text-2xl font-bold text-white">浪漫小樽運河與古木商店街</h3>
                            </div>
                            <span class="px-3 py-1 bg-slate-800 text-ice-300 rounded-full text-xs font-mono">JR約40分鐘</span>
                        </div>

                        <div class="space-y-6 relative border-l-2 border-ice-500/30 ml-3 pl-6">
                            <div class="relative">
                                <div class="absolute -left-[31px] top-0 w-4 h-4 rounded-full bg-ice-500 border-4 border-slate-950"></div>
                                <div class="text-xs text-ice-400 font-mono">上午</div>
                                <h4 class="font-bold text-white">前往南小樽站開始漫步</h4>
                                <p class="text-xs text-slate-400">建議搭乘 JR 至「南小樽站」下車，一路逛回「小樽站」不走回頭路。</p>
                            </div>
                            <div class="relative">
                                <div class="absolute -left-[31px] top-0 w-4 h-4 rounded-full bg-ice-500 border-4 border-slate-950"></div>
                                <div class="text-xs text-ice-400 font-mono">日間景點</div>
                                <h4 class="font-bold text-white">小樽精選散策路線</h4>
                                <ol class="list-decimal list-inside text-xs text-slate-300 space-y-1.5 mt-1">
                                    <li><b>住吉神社：</b> 靜謐的鳥居雪景</li>
                                    <li><b>Un délice (アンデリス)：</b> 必吃特色布丁甜點</li>
                                    <li><b>小樽堺町商店街：</b> 北一硝子館、小樽音樂盒堂、Spoony 茶屋</li>
                                    <li><b>小樽出拔小路：</b> 復古美食小巷</li>
                                    <li><b>小樽運河：</b> 黃昏與點燈浪漫雪景</li>
                                </ol>
                            </div>
                            <div class="bg-amber-500/10 border border-amber-500/30 rounded-xl p-4 text-xs space-y-2">
                                <div class="font-bold text-amber-300 flex items-center gap-1.5 text-sm">
                                    <i class="fa-solid fa-utensils"></i> 小樽經典必吃
                                </div>
                                <p class="text-slate-300">🍗 <b>若鶏時代 なると 本店：</b> 外酥內嫩必吃炸半雞！</p>
                            </div>
                        </div>
                    </div>

                    <!-- DAY 5 -->
                    <div id="day-content-5" class="day-content hidden space-y-6">
                        <div class="flex justify-between items-center border-b border-slate-800 pb-4">
                            <div>
                                <span class="text-xs text-ice-400 font-semibold tracking-wide">DAY 5 ｜ 2026/12/10（四）</span>
                                <h3 class="text-2xl font-bold text-white">手稻滑雪場極致粉雪體驗</h3>
                            </div>
                            <span class="px-3 py-1 bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 rounded-full text-xs font-semibold">NT$5,495 / 人</span>
                        </div>

                        <div class="space-y-6 relative border-l-2 border-emerald-500/30 ml-3 pl-6">
                            <div class="relative">
                                <div class="absolute -left-[31px] top-0 w-4 h-4 rounded-full bg-emerald-500 border-4 border-slate-950"></div>
                                <div class="text-xs text-emerald-400 font-mono">07:45 (嚴禁遲到)</div>
                                <h4 class="font-bold text-white">集合點：THE SUSUKINO SQUARE WEST</h4>
                                <p class="text-xs text-slate-400">1 樓 A・B・E 號（〒064-0806 北海道札幌市中央区南6条西5-3-6）</p>
                            </div>
                            <div class="relative">
                                <div class="absolute -left-[31px] top-0 w-4 h-4 rounded-full bg-emerald-500 border-4 border-slate-950"></div>
                                <div class="text-xs text-emerald-400 font-mono">全天</div>
                                <h4 class="font-bold text-white">手稻滑雪場 (Teine Ski Resort)</h4>
                                <p class="text-xs text-slate-300">・滑雪體驗課（粉雪天堂）<br>・雪盆歡樂活動</p>
                            </div>
                            <div class="bg-amber-500/10 border border-amber-500/30 rounded-xl p-4 text-xs space-y-2">
                                <div class="font-bold text-amber-300 flex items-center gap-1.5 text-sm">
                                    <i class="fa-solid fa-utensils"></i> 滑雪後溫暖美食
                                </div>
                                <p class="text-slate-300">🍜 <b>麵屋雪風 薄野本店：</b> 濃厚香醇味噌拉麵（暖胃極品）</p>
                            </div>
                        </div>
                    </div>

                    <!-- DAY 6 -->
                    <div id="day-content-6" class="day-content hidden space-y-6">
                        <div class="flex justify-between items-center border-b border-slate-800 pb-4">
                            <div>
                                <span class="text-xs text-ice-400 font-semibold tracking-wide">DAY 6 ｜ 2026/12/11（五）</span>
                                <h3 class="text-2xl font-bold text-white">札幌精緻采買・神社神采參拜</h3>
                            </div>
                            <span class="px-3 py-1 bg-slate-800 text-ice-300 rounded-full text-xs font-mono">市區一日</span>
                        </div>

                        <div class="space-y-6 relative border-l-2 border-ice-500/30 ml-3 pl-6">
                            <div class="relative">
                                <div class="absolute -left-[31px] top-0 w-4 h-4 rounded-full bg-ice-500 border-4 border-slate-950"></div>
                                <div class="text-xs text-ice-400 font-mono">09:00 前抵達</div>
                                <h4 class="font-bold text-white">北海道神宮</h4>
                                <p class="text-xs text-slate-300">⚠️ <b>重要：</b> 限量神宮梅酒 9:00 開賣需早到排隊！購買玻璃珠御守。</p>
                            </div>
                            <div class="relative">
                                <div class="absolute -left-[31px] top-0 w-4 h-4 rounded-full bg-ice-500 border-4 border-slate-950"></div>
                                <div class="text-xs text-ice-400 font-mono">日間</div>
                                <h4 class="font-bold text-white">中島公園 & 白色戀人公園</h4>
                                <p class="text-xs text-slate-300">在中島公園拍攝冬雪美景，前往白色戀人公園體驗<b>訂製個人相片鐵盒</b>。</p>
                            </div>
                            <div class="relative">
                                <div class="absolute -left-[31px] top-0 w-4 h-4 rounded-full bg-ice-500 border-4 border-slate-950"></div>
                                <div class="text-xs text-ice-400 font-mono">傍晚</div>
                                <h4 class="font-bold text-white">狸小路 & 薄野最後大採購</h4>
                            </div>
                            <div class="bg-amber-500/10 border border-amber-500/30 rounded-xl p-4 text-xs space-y-2">
                                <div class="font-bold text-amber-300 flex items-center gap-1.5 text-sm">
                                    <i class="fa-solid fa-utensils"></i> 美饌雙連發
                                </div>
                                <p class="text-slate-300">🍣 <b>トリトン壽司 (Triton 回轉壽司)：</b> 北海道極致美味壽司</p>
                                <p class="text-slate-300">🍜 <b>一蘭拉麵 札幌薄野店</b></p>
                            </div>
                        </div>
                    </div>

                    <!-- DAY 7 -->
                    <div id="day-content-7" class="day-content hidden space-y-6">
                        <div class="flex justify-between items-center border-b border-slate-800 pb-4">
                            <div>
                                <span class="text-xs text-ice-400 font-semibold tracking-wide">DAY 7 ｜ 2026/12/12（六）</span>
                                <h3 class="text-2xl font-bold text-white">新千歲機場大採購・滿載返台</h3>
                            </div>
                            <span class="px-3 py-1 bg-amber-500/20 text-amber-300 border border-amber-500/30 rounded-full text-xs font-semibold">返程日</span>
                        </div>

                        <div class="space-y-6 relative border-l-2 border-amber-500/30 ml-3 pl-6">
                            <div class="relative">
                                <div class="absolute -left-[31px] top-0 w-4 h-4 rounded-full bg-amber-500 border-4 border-slate-950"></div>
                                <div class="text-xs text-amber-400 font-mono">10:00</div>
                                <h4 class="font-bold text-white">從札幌出發前往新千歲機場</h4>
                                <p class="text-xs text-slate-400">搭乘 JR 快速 Airport 線（預留充足時間免趕班機）。</p>
                            </div>
                            <div class="relative">
                                <div class="absolute -left-[31px] top-0 w-4 h-4 rounded-full bg-amber-500 border-4 border-slate-950"></div>
                                <div class="text-xs text-amber-400 font-mono">11:00 - 13:00</div>
                                <h4 class="font-bold text-white">新千歲機場最終採買</h4>
                                <p class="text-xs text-slate-300">機場逛街買爆伴手禮、彩妝採購 (Prada 氣墊等免稅品)。</p>
                            </div>
                            <div class="relative">
                                <div class="absolute -left-[31px] top-0 w-4 h-4 rounded-full bg-amber-500 border-4 border-slate-950"></div>
                                <div class="text-xs text-amber-400 font-mono">14:00 - 17:55</div>
                                <h4 class="font-bold text-white">搭乘泰亞航 FD243 返回桃園機場</h4>
                                <p class="text-xs text-slate-400">平安抵達台灣，結束美好北海道冰雪旅程！</p>
                            </div>
                        </div>
                    </div>

                </div>
            </section>

            <!-- SECTION 3: 票券與預算 (Budget & Checklists) -->
            <section id="section-budget" class="tab-content hidden space-y-6">
                <!-- Activities & Cost Card -->
                <h2 class="text-xl font-bold text-ice-300 flex items-center gap-2">
                    <i class="fa-solid fa-receipt text-ice-400"></i> 已預訂行程與票券預算
                </h2>

                <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                    <div class="glass-card p-4 rounded-xl">
                        <div class="text-xs text-slate-400">12/07 旭川美瑛一日遊</div>
                        <div class="text-lg font-bold text-white mt-1">Klook 一日遊</div>
                        <div class="text-sm font-semibold text-ice-300 mt-2">NT$ 1,775 /人</div>
                    </div>
                    <div class="glass-card p-4 rounded-xl">
                        <div class="text-xs text-slate-400">12/08 定山溪漂流</div>
                        <div class="text-lg font-bold text-white mt-1">Friluftsliv 漂流</div>
                        <div class="text-sm font-semibold text-ice-300 mt-2">¥ 10,000 /人</div>
                    </div>
                    <div class="glass-card p-4 rounded-xl">
                        <div class="text-xs text-slate-400">12/10 手稻滑雪體驗</div>
                        <div class="text-lg font-bold text-white mt-1">滑雪 + 雪盆</div>
                        <div class="text-sm font-semibold text-ice-300 mt-2">NT$ 5,495 /人</div>
                    </div>
                </div>

                <!-- Checklist -->
                <h2 class="text-xl font-bold text-ice-300 flex items-center gap-2 pt-4">
                    <i class="fa-solid fa-list-check text-ice-400"></i> 行前準備與行前票券 CheckList
                </h2>

                <div class="glass-card rounded-2xl p-6 space-y-4">
                    <div class="flex items-center justify-between pb-3 border-b border-slate-800">
                        <span class="text-sm font-medium text-slate-300">準備完成度</span>
                        <span id="ticket-progress-text" class="text-xs font-mono text-ice-300 font-bold">0 / 5</span>
                    </div>

                    <div class="space-y-3" id="ticket-checklist">
                        <div class="flex items-center gap-3">
                            <input type="checkbox" id="chk-esim" onchange="updateProgress()" class="custom-checkbox w-5 h-5 accent-ice-500 rounded cursor-pointer">
                            <label for="chk-esim" class="text-sm text-slate-200 cursor-pointer">eSIM 日本網卡 (NT$459／人)</label>
                        </div>
                        <div class="flex items-center gap-3">
                            <input type="checkbox" id="chk-ubus" onchange="updateProgress()" class="custom-checkbox w-5 h-5 accent-ice-500 rounded cursor-pointer">
                            <label for="chk-ubus" class="text-sm text-slate-200 cursor-pointer">統聯客運車票 - 往桃園機場 (NT$395／人)</label>
                        </div>
                        <div class="flex items-center gap-3">
                            <input type="checkbox" id="chk-suica" onchange="updateProgress()" class="custom-checkbox w-5 h-5 accent-ice-500 rounded cursor-pointer">
                            <label for="chk-suica" class="text-sm text-slate-200 cursor-pointer">Suica 交通卡 (iPhone 錢包完成加值)</label>
                        </div>
                        <div class="flex items-center gap-3">
                            <input type="checkbox" id="chk-tax" onchange="updateProgress()" class="custom-checkbox w-5 h-5 accent-ice-500 rounded cursor-pointer">
                            <label for="chk-tax" class="text-sm text-slate-200 cursor-pointer">退稅相關線上登錄／免稅認證設定</label>
                        </div>
                        <div class="flex items-center gap-3">
                            <input type="checkbox" id="chk-vjw" checked onchange="updateProgress()" class="custom-checkbox w-5 h-5 accent-ice-500 rounded cursor-pointer">
                            <label for="chk-vjw" class="text-sm text-slate-200 cursor-pointer">Visit Japan Web 線上入境填寫申請 (已完成)</label>
                        </div>
                    </div>
                </div>
            </section>

            <!-- SECTION 4: 伴手禮採購 (Souvenirs) -->
            <section id="section-souvenirs" class="tab-content hidden space-y-6">
                <div class="flex justify-between items-center">
                    <h2 class="text-xl font-bold text-ice-300 flex items-center gap-2">
                        <i class="fa-solid fa-gift text-ice-400"></i> 伴手禮與購物採購清單
                    </h2>
                    <span id="souvenir-count" class="text-xs bg-slate-800 text-ice-300 px-3 py-1 rounded-full border border-slate-700">已採購 0 / 6</span>
                </div>

                <!-- Shopping Items Grid -->
                <div class="glass-card rounded-2xl p-6 space-y-4">
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4" id="souvenir-list">
                        <div class="flex items-center p-3 rounded-xl bg-slate-900/60 border border-slate-800 hover:border-ice-500/40 transition">
                            <input type="checkbox" id="souv-1" onchange="updateSouvenirProgress()" class="custom-checkbox w-5 h-5 accent-ice-500 rounded cursor-pointer mr-3">
                            <label for="souv-1" class="text-sm text-slate-200 cursor-pointer font-medium">白色戀人 (經典巧克力餅乾)</label>
                        </div>
                        <div class="flex items-center p-3 rounded-xl bg-slate-900/60 border border-slate-800 hover:border-ice-500/40 transition">
                            <input type="checkbox" id="souv-2" onchange="updateSouvenirProgress()" class="custom-checkbox w-5 h-5 accent-ice-500 rounded cursor-pointer mr-3">
                            <label for="souv-2" class="text-sm text-slate-200 cursor-pointer font-medium">ROYCE 巧克力 / 生巧克力</label>
                        </div>
                        <div class="flex items-center p-3 rounded-xl bg-slate-900/60 border border-slate-800 hover:border-ice-500/40 transition">
                            <input type="checkbox" id="souv-3" onchange="updateSouvenirProgress()" class="custom-checkbox w-5 h-5 accent-ice-500 rounded cursor-pointer mr-3">
                            <label for="souv-3" class="text-sm text-slate-200 cursor-pointer font-medium">薯條三兄弟 (Calbee)</label>
                        </div>
                        <div class="flex items-center p-3 rounded-xl bg-slate-900/60 border border-slate-800 hover:border-ice-500/40 transition">
                            <input type="checkbox" id="souv-4" onchange="updateSouvenirProgress()" class="custom-checkbox w-5 h-5 accent-ice-500 rounded cursor-pointer mr-3">
                            <label for="souv-4" class="text-sm text-slate-200 cursor-pointer font-medium">六花亭餅乾 (蘭姆葡萄奶油夾心)</label>
                        </div>
                        <div class="flex items-center p-3 rounded-xl bg-slate-900/60 border border-slate-800 hover:border-ice-500/40 transition">
                            <input type="checkbox" id="souv-5" onchange="updateSouvenirProgress()" class="custom-checkbox w-5 h-5 accent-ice-500 rounded cursor-pointer mr-3">
                            <label for="souv-5" class="text-sm text-slate-200 cursor-pointer font-medium">北菓樓夢不思議泡芙 / 妖精之森</label>
                        </div>
                        <div class="flex items-center p-3 rounded-xl bg-slate-900/60 border border-slate-800 hover:border-ice-500/40 transition">
                            <input type="checkbox" id="souv-6" onchange="updateSouvenirProgress()" class="custom-checkbox w-5 h-5 accent-ice-500 rounded cursor-pointer mr-3">
                            <label for="souv-6" class="text-sm text-slate-200 cursor-pointer font-medium">Prada 氣墊 (機場彩妝免稅店)</label>
                        </div>
                    </div>
                </div>
            </section>

        </main>

        <!-- Footer -->
        <footer class="text-center py-6 border-t border-slate-900 text-slate-500 text-xs">
            <p>🇯🇵 2026 北海道冬日之旅紀錄 ❄️ 祝旅途愉快平安！</p>
        </footer>

    </div>

    <!-- Copy Toast Message Box -->
    <div id="toast" class="fixed bottom-6 right-6 bg-ice-600 text-white px-4 py-2.5 rounded-xl shadow-2xl text-xs font-semibold transform translate-y-20 opacity-0 transition duration-300 z-50 flex items-center gap-2">
        <i class="fa-solid fa-circle-check"></i> 地址已成功複製到剪貼簿！
    </div>

    <!-- JavaScript Interactions -->
    <script>
        // Tab Switch Logic
        function switchTab(tabName) {
            document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
            document.querySelectorAll('.nav-btn').forEach(btn => {
                btn.classList.remove('active', 'bg-ice-600/80', 'text-white', 'shadow-lg', 'shadow-ice-500/20');
                btn.classList.add('text-slate-400');
            });

            document.getElementById(`section-${tabName}`).classList.remove('hidden');
            const activeBtn = document.getElementById(`tab-${tabName}`);
            activeBtn.classList.add('active', 'bg-ice-600/80', 'text-white', 'shadow-lg', 'shadow-ice-500/20');
            activeBtn.classList.remove('text-slate-400');
        }

        // Daily Schedule Day Switcher
        function showDay(dayNum) {
            document.querySelectorAll('.day-content').forEach(el => el.classList.add('hidden'));
            document.querySelectorAll('.day-btn').forEach(btn => {
                btn.classList.remove('bg-ice-500', 'text-white', 'shadow-md');
                btn.classList.add('bg-slate-800', 'text-slate-300');
            });

            document.getElementById(`day-content-${dayNum}`).classList.remove('hidden');
            const activeDayBtn = document.getElementById(`day-btn-${dayNum}`);
            activeDayBtn.classList.add('bg-ice-500', 'text-white', 'shadow-md');
            activeDayBtn.classList.remove('bg-slate-800', 'text-slate-300');
        }

        // Checkbox Progress Counter
        function updateProgress() {
            const checkboxes = document.querySelectorAll('#ticket-checklist input[type="checkbox"]');
            const checked = document.querySelectorAll('#ticket-checklist input[type="checkbox"]:checked');
            document.getElementById('ticket-progress-text').innerText = `${checked.length} / ${checkboxes.length}`;
        }

        function updateSouvenirProgress() {
            const checkboxes = document.querySelectorAll('#souvenir-list input[type="checkbox"]');
            const checked = document.querySelectorAll('#souvenir-list input[type="checkbox"]:checked');
            document.getElementById('souvenir-count').innerText = `已採購 ${checked.length} / ${checkboxes.length}`;
        }

        // Copy Address Function
        function copyAddress() {
            const textToCopy = "ホリデイ・イン エクスプレス札幌すすきの 〒064-0805 北海道札幌市中央区南5条西6丁目14-1";
            const tempInput = document.createElement("textarea");
            tempInput.value = textToCopy;
            document.body.appendChild(tempInput);
            tempInput.select();
            document.execCommand("copy");
            document.body.removeChild(tempInput);

            const toast = document.getElementById('toast');
            toast.classList.remove('translate-y-20', 'opacity-0');
            setTimeout(() => {
                toast.classList.add('translate-y-20', 'opacity-0');
            }, 2500);
        }

        // Initial Progress Call
        updateProgress();
        updateSouvenirProgress();

        // Snow animation logic for Canvas
        const canvas = document.getElementById('snow-canvas');
        const ctx = canvas.getContext('2d');

        function resizeCanvas() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }
        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();

        const numFlakes = 60;
        const flakes = [];

        for (let i = 0; i < numFlakes; i++) {
            flakes.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                r: Math.random() * 2 + 1,
                d: Math.random() * numFlakes,
                opacity: Math.random() * 0.5 + 0.3
            });
        }

        function drawSnow() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = 'rgba(255, 255, 255, 0.8)';
            ctx.beginPath();
            for (let i = 0; i < numFlakes; i++) {
                const f = flakes[i];
                ctx.moveTo(f.x, f.y);
                ctx.arc(f.x, f.y, f.r, 0, Math.PI * 2, true);
            }
            ctx.fill();
            moveSnow();
        }

        let angle = 0;
        function moveSnow() {
            angle += 0.01;
            for (let i = 0; i < numFlakes; i++) {
                const f = flakes[i];
                f.y += Math.cos(angle + f.d) + 1 + f.r / 2;
                f.x += Math.sin(angle) * 1;

                if (f.x > canvas.width + 5 || f.x < -5 || f.y > canvas.height) {
                    if (i % 3 > 0) {
                        flakes[i] = { x: Math.random() * canvas.width, y: -10, r: f.r, d: f.d, opacity: f.opacity };
                    } else {
                        if (Math.sin(angle) > 0) {
                            flakes[i] = { x: -5, y: Math.random() * canvas.height, r: f.r, d: f.d, opacity: f.opacity };
                        } else {
                            flakes[i] = { x: canvas.width + 5, y: Math.random() * canvas.height, r: f.r, d: f.d, opacity: f.opacity };
                        }
                    }
                }
            }
        }

        window.onload = function() {
            setInterval(drawSnow, 33);
        };
    </script>
</body>
</html>