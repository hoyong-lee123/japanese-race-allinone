import streamlit as st
import pandas as pd
import datetime
import plotly.graph_objects as go
import folium
from streamlit_folium import st_folium

from racetrack_data import RACETRACKS
from horse_data import HORSES
from jockey_data import JOCKEYS
from race_schedule import G1_RACES
from betting_data import BET_TYPES, BETTING_STRATEGIES, PADDOCK_GUIDE, TRACK_CONDITIONS

# ==========================================
# 1. 페이지 설정 & 테마
# ==========================================
st.set_page_config(
    page_title="일본 경마 완벽 가이드 대시보드 (JRA & 명마 도감)",
    page_icon="🏇",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 세션 상태 초기화
if 'my_horse' not in st.session_state:
    st.session_state['my_horse'] = "이퀴녹스"

if 'dark_mode' not in st.session_state:
    st.session_state['dark_mode'] = True

# 사이드바 설정
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1534447677768-be436bb09401?w=600&auto=format&fit=crop&q=80", use_container_width=True)
    st.markdown("## 🏇 일본 경마 올인원 대시보드")
    st.caption("JRA 중앙경마 10대 구장 · G1 캘린더 · 명마 도감 · 베팅 가이드")
    
    st.markdown("---")
    st.markdown("### 🌓 화면 모드")
    dark_mode = st.toggle("다크 모드 적용", value=st.session_state['dark_mode'])
    st.session_state['dark_mode'] = dark_mode
    
    st.markdown("---")
    st.markdown("### 📌 빠른 바로가기")
    st.markdown("""
    - [JRA 공식 홈페이지](https://www.jra.go.jp/)
    - [netkeiba (일본 최대 경마 포털)](https://www.netkeiba.com/)
    - [JBIS search (혈통 데이터베이스)](https://www.jbis.or.jp/)
    - [JRA-VAN 데이터 서비스](https://jra-van.jp/)
    """)
    st.caption("제작: 일본 경마 데이터 분석 시스템")

# CSS 스타일 정의
custom_css_dark = """
<style>
    .stApp {
        background-color: #0b0f19;
        color: #f1f5f9;
        font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    .main-title {
        background: linear-gradient(135deg, #f59e0b 0%, #ef4444 50%, #8b5cf6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.3rem;
        font-weight: 800;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        color: #94a3b8;
        font-size: 1.05rem;
        margin-bottom: 1.5rem;
    }
    .custom-card {
        background: #131b2e;
        border: 1px solid #1e293b;
        border-radius: 14px;
        padding: 20px;
        margin-bottom: 16px;
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.3);
    }
    .custom-card:hover {
        border-color: #3b82f6;
        transition: all 0.25s ease;
    }
    .highlight-badge {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.82rem;
        font-weight: 600;
        background: rgba(59, 130, 246, 0.15);
        color: #60a5fa;
        border: 1px solid rgba(59, 130, 246, 0.3);
        margin-right: 6px;
    }
    .gold-badge {
        background: rgba(245, 158, 11, 0.15);
        color: #fbbf24;
        border: 1px solid rgba(245, 158, 11, 0.4);
    }
    .metric-box {
        background: #1e293b;
        border-radius: 10px;
        padding: 12px;
        text-align: center;
        border: 1px solid #334155;
    }
    .metric-value {
        font-size: 1.3rem;
        font-weight: bold;
        color: #38bdf8;
    }
    .metric-label {
        font-size: 0.8rem;
        color: #94a3b8;
    }
</style>
"""

custom_css_light = """
<style>
    .stApp {
        background-color: #f8fafc;
        color: #0f172a;
        font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    .main-title {
        background: linear-gradient(135deg, #d97706 0%, #dc2626 50%, #7c3aed 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.3rem;
        font-weight: 800;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        color: #64748b;
        font-size: 1.05rem;
        margin-bottom: 1.5rem;
    }
    .custom-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 20px;
        margin-bottom: 16px;
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.05);
    }
    .custom-card:hover {
        border-color: #2563eb;
        transition: all 0.25s ease;
    }
    .highlight-badge {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.82rem;
        font-weight: 600;
        background: rgba(37, 99, 235, 0.1);
        color: #2563eb;
        border: 1px solid rgba(37, 99, 235, 0.2);
        margin-right: 6px;
    }
    .gold-badge {
        background: rgba(217, 119, 6, 0.1);
        color: #d97706;
        border: 1px solid rgba(217, 119, 6, 0.3);
    }
    .metric-box {
        background: #f1f5f9;
        border-radius: 10px;
        padding: 12px;
        text-align: center;
        border: 1px solid #cbd5e1;
    }
    .metric-value {
        font-size: 1.3rem;
        font-weight: bold;
        color: #0284c7;
    }
    .metric-label {
        font-size: 0.8rem;
        color: #64748b;
    }
</style>
"""

if st.session_state['dark_mode']:
    st.markdown(custom_css_dark, unsafe_allow_html=True)
else:
    st.markdown(custom_css_light, unsafe_allow_html=True)

# 메인 타이틀
st.markdown('<div class="main-title">🏇 일본 경마 올인원 대시보드</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">JRA 중앙경마 10대 구장 분석 · 연간 G1 일정 · 명마 & 기수 스펙 · 마권 베팅 계산기까지 완벽 정리</div>', unsafe_allow_html=True)

# ==========================================
# 2. 6개 탭 구성
# ==========================================
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "⚙️ 최애마 설정",
    "🔥 G1 레이스 일정",
    "🐎 명마 & 기수 도감",
    "🏟️ 전국 10대 경마장",
    "🎫 마권 종류 & 계산기",
    "🏆 명예의 전당 & 뉴스"
])

# ------------------------------------------
# [TAB 1] 최애마 설정 & 전적 브리핑
# ------------------------------------------
with tab1:
    st.subheader("👑 나의 최애 명마 설정")
    st.caption("선택하신 경주마의 상세 스펙과 커리어 하이라이트를 메인에서 바로 확인하세요.")
    
    horse_names = list(HORSES.keys())
    selected_horse = st.selectbox("최애 경주마를 선택하세요:", horse_names, index=horse_names.index(st.session_state['my_horse']))
    
    if st.button("🌟 최애마로 저장하기"):
        st.session_state['my_horse'] = selected_horse
        st.success(f"'{selected_horse}'(이)가 나의 대표 명마로 설정되었습니다!")
        
    horse_info = HORSES[st.session_state['my_horse']]
    
    col1, col2 = st.columns([1.2, 1])
    
    with col1:
        st.markdown(f"""
        <div class="custom-card">
            <span class="highlight-badge gold-badge">{horse_info['title']}</span>
            <h2 style="margin-top: 8px; margin-bottom: 4px;">{st.session_state['my_horse']} <span style="font-size:1.1rem; color:#94a3b8;">({horse_info['jp_name']})</span></h2>
            <p style="color:#64748b; font-size:0.95rem;">생년: {horse_info['birth_year']}년 | 성별: {horse_info['sex']} | 털색: {horse_info['coat_color']}</p>
            <hr style="border-color:#334155; margin:12px 0;">
            <p><strong>🎯 각질 (주행 스타일):</strong> <span class="highlight-badge">{horse_info['running_style']}</span></p>
            <p><strong>📏 최적 적성 거리:</strong> {horse_info['best_distance']}</p>
            <p><strong>🏆 통산 전적:</strong> {horse_info['record']}</p>
            <p><strong>💰 총 수득 상금:</strong> <span style="color:#f59e0b; font-weight:bold;">{horse_info['earnings']}</span></p>
            <p><strong>👨‍🌾 조교사 / 주전 기수:</strong> {horse_info['trainer']} / {horse_info['jockey']}</p>
            <p><strong>🧬 혈통:</strong> 부: {horse_info['pedigree']['sire']} × 모: {horse_info['pedigree']['dam']} (모부: {horse_info['pedigree']['damsire']})</p>
            <div style="background:rgba(255,255,255,0.03); border-radius:8px; padding:12px; margin-top:14px; border-left:4px solid #f59e0b;">
                <p style="margin:0; font-size:0.92rem; line-height:1.6;"><strong>📖 명승부 스토리:</strong> {horse_info['story']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        # 레이더 차트 표시
        stats = horse_info['stats']
        categories = list(stats.keys())
        values = list(stats.values())
        
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=values + [values[0]],
            theta=categories + [categories[0]],
            fill='toself',
            name=st.session_state['my_horse'],
            line_color=horse_info.get('color', '#3b82f6'),
            fillcolor=horse_info.get('color', '#3b82f6') + '33'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[70, 100]
                )
            ),
            showlegend=False,
            margin=dict(l=40, r=40, t=30, b=30),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            title=f"📊 {st.session_state['my_horse']} 능력치 레이더 분석"
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("#### 🥇 주요 G1 우승 내역")
        for win in horse_info['g1_wins']:
            st.markdown(f"🏆 `{win}`")

# ------------------------------------------
# [TAB 2] G1 레이스 일정 & 역대 명승부
# ------------------------------------------
with tab2:
    st.subheader("🔥 JRA 연간 전체 G1 레이스 캘린더")
    st.caption("일본 중앙경마의 최고봉! 1년 동안 펼쳐지는 24개 G1 중상 경주의 모든 정보입니다.")
    
    col_f1, col_f2 = st.columns([1, 1])
    with col_f1:
        surface_filter = st.selectbox("마장 종류 필터", ["전체", "잔디 (Turf)", "더트 (Dirt)"])
    with col_f2:
        track_filter = st.selectbox("경마장 필터", ["전체"] + list(RACETRACKS.keys()))
        
    filtered_races = G1_RACES
    if surface_filter != "전체":
        if "더트" in surface_filter:
            filtered_races = [r for r in filtered_races if "더트" in r['surface']]
        else:
            filtered_races = [r for r in filtered_races if "잔디" in r['surface']]
            
    if track_filter != "전체":
        filtered_races = [r for r in filtered_races if track_filter in r['racetrack']]
        
    st.markdown(f"**총 {len(filtered_races)}개의 G1 경주가 조회되었습니다.**")
    
    # 2열 카드로 깔끔하게 렌더링
    for i in range(0, len(filtered_races), 2):
        c1, c2 = st.columns(2)
        
        # 첫 번째 카드
        r1 = filtered_races[i]
        with c1:
            st.markdown(f"""
            <div class="custom-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span class="highlight-badge gold-badge">{r1['month']}</span>
                    <span style="font-size:0.85rem; color:#94a3b8;">{r1['racetrack']}</span>
                </div>
                <h3 style="margin-top:10px; margin-bottom:4px;">{r1['name']}</h3>
                <p style="color:#64748b; font-size:0.9rem;">{r1['jp_name']}</p>
                <div style="display:flex; gap:10px; margin: 12px 0;">
                    <span class="highlight-badge">📍 {r1['surface']}</span>
                    <span class="highlight-badge">🎯 {r1['eligibility']}</span>
                </div>
                <p><strong>💰 1착 상금:</strong> <span style="color:#f59e0b; font-weight:bold;">{r1['first_prize']}</span></p>
                <p style="font-size:0.9rem; line-height:1.5;">{r1['description']}</p>
                <p style="font-size:0.85rem; color:#94a3b8; margin-top:8px;"><strong>최근 우승마:</strong> {r1['recent_winner']}</p>
            </div>
            """, unsafe_allow_html=True)
            
        # 두 번째 카드
        if i + 1 < len(filtered_races):
            r2 = filtered_races[i + 1]
            with c2:
                st.markdown(f"""
                <div class="custom-card">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <span class="highlight-badge gold-badge">{r2['month']}</span>
                        <span style="font-size:0.85rem; color:#94a3b8;">{r2['racetrack']}</span>
                    </div>
                    <h3 style="margin-top:10px; margin-bottom:4px;">{r2['name']}</h3>
                    <p style="color:#64748b; font-size:0.9rem;">{r2['jp_name']}</p>
                    <div style="display:flex; gap:10px; margin: 12px 0;">
                        <span class="highlight-badge">📍 {r2['surface']}</span>
                        <span class="highlight-badge">🎯 {r2['eligibility']}</span>
                    </div>
                    <p><strong>💰 1착 상금:</strong> <span style="color:#f59e0b; font-weight:bold;">{r2['first_prize']}</span></p>
                    <p style="font-size:0.9rem; line-height:1.5;">{r2['description']}</p>
                    <p style="font-size:0.85rem; color:#94a3b8; margin-top:8px;"><strong>최근 우승마:</strong> {r2['recent_winner']}</p>
                </div>
                """, unsafe_allow_html=True)

# ------------------------------------------
# [TAB 3] 명마 & 기수 도감
# ------------------------------------------
with tab3:
    st.subheader("🐎 레전드 명마 도감 & 능력치 1:1 비교")
    st.caption("일본 경마사를 빛낸 전설의 명마들을 비교하고 분석해보세요.")
    
    st.markdown("### ⚔️ 두 경주마 1:1 가상 매치업 비교")
    comp_col1, comp_col2 = st.columns(2)
    with comp_col1:
        horse_a = st.selectbox("말 A 선택", list(HORSES.keys()), index=0)
    with comp_col2:
        horse_b = st.selectbox("말 B 선택", list(HORSES.keys()), index=1)
        
    info_a = HORSES[horse_a]
    info_b = HORSES[horse_b]
    
    categories = list(info_a['stats'].keys())
    vals_a = list(info_a['stats'].values())
    vals_b = list(info_b['stats'].values())
    
    fig_comp = go.Figure()
    fig_comp.add_trace(go.Scatterpolar(
        r=vals_a + [vals_a[0]],
        theta=categories + [categories[0]],
        fill='toself',
        name=horse_a,
        line_color='#3b82f6',
        fillcolor='rgba(59, 130, 246, 0.25)'
    ))
    fig_comp.add_trace(go.Scatterpolar(
        r=vals_b + [vals_b[0]],
        theta=categories + [categories[0]],
        fill='toself',
        name=horse_b,
        line_color='#ef4444',
        fillcolor='rgba(239, 68, 68, 0.25)'
    ))
    fig_comp.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[70, 100])),
        showlegend=True,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=40, r=40, t=30, b=30),
        legend=dict(orientation="h", yanchor="bottom", y=1.05, xanchor="right", x=1)
    )
    st.plotly_chart(fig_comp, use_container_width=True)
    
    # 두 말의 스펙 비교표
    comp_df = pd.DataFrame({
        "구분": ["각질", "적성거리", "통산 전적", "수득 상금", "주요 타이틀"],
        horse_a: [info_a['running_style'], info_a['best_distance'], info_a['record'], info_a['earnings'], ", ".join(info_a['g1_wins'][:3]) + "..."],
        horse_b: [info_b['running_style'], info_b['best_distance'], info_b['record'], info_b['earnings'], ", ".join(info_b['g1_wins'][:3]) + "..."]
    })
    st.table(comp_df.set_index("구분"))
    
    st.markdown("---")
    st.subheader("🏇 일본의 전설적 명기수 열전")
    
    for j_name, j_info in JOCKEYS.items():
        st.markdown(f"""
        <div class="custom-card">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <h3>{j_name} <span style="font-size:1rem; color:#94a3b8;">({j_info['jp_name']})</span></h3>
                <span class="highlight-badge gold-badge">{j_info['badge']}</span>
            </div>
            <p style="color:#64748b; font-size:0.9rem;">생년월일: {j_info['birth_date']} | 소속/면허: {j_info['license']}</p>
            <div style="display:flex; gap:12px; margin: 10px 0; flex-wrap:wrap;">
                <span class="highlight-badge">🏆 {j_info['career_wins']}</span>
                <span class="highlight-badge">🥇 {j_info['g1_wins']}</span>
                <span class="highlight-badge">👑 {j_info['derby_wins']}</span>
            </div>
            <p><strong>⭐ 대표 파트너 말:</strong> {", ".join(j_info['iconic_horses'])}</p>
            <p><strong>🎯 기승 스타일:</strong> {j_info['riding_style']}</p>
            <div style="background:rgba(255,255,255,0.03); border-radius:6px; padding:10px; margin-top:8px; border-left:3px solid #3b82f6;">
                <span style="font-style:italic; font-size:0.9rem;">"{j_info['quote']}"</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ------------------------------------------
# [TAB 4] 전국 10대 경마장 완벽 가이드 & 지도
# ------------------------------------------
with tab4:
    st.subheader("🏟️ JRA 전국 10대 중앙 경마장 가이드 & 인터랙티브 맵")
    st.caption("각 경마장의 직선 길이, 언덕 고저차, 유리한 각질을 분석하고 위치를 지도에서 확인하세요.")
    
    selected_track = st.selectbox("분석할 경마장을 선택하세요:", list(RACETRACKS.keys()), index=0)
    track_info = RACETRACKS[selected_track]
    
    # 맵 생성 (Folium)
    m = folium.Map(location=track_info['coords'], zoom_start=14, tiles="OpenStreetMap")
    folium.Marker(
        location=track_info['coords'],
        popup=f"<b>{selected_track}</b><br>{track_info['jp_name']}",
        tooltip=selected_track,
        icon=folium.Icon(color="red", icon="flag")
    ).add_to(m)
    
    map_col, info_col = st.columns([1.1, 1])
    
    with map_col:
        st_folium(m, height=420, use_container_width=True)
        
    with info_col:
        st.markdown(f"""
        <div class="custom-card">
            <h2>{selected_track}</h2>
            <p style="color:#94a3b8; font-size:1rem;">{track_info['jp_name']} | 📍 {track_info['location']}</p>
            <hr style="border-color:#334155; margin:10px 0;">
            <div style="display:grid; grid-template-columns: 1fr 1fr; gap:10px; margin-bottom:12px;">
                <div class="metric-box">
                    <div class="metric-label">잔디 직선 거리</div>
                    <div class="metric-value" style="font-size:1.05rem;">{track_info['straight_turf']}</div>
                </div>
                <div class="metric-box">
                    <div class="metric-label">코스 회전 방향</div>
                    <div class="metric-value" style="font-size:1.05rem;">{track_info['rotation']}</div>
                </div>
                <div class="metric-box">
                    <div class="metric-label">코스 최대 고저차</div>
                    <div class="metric-value" style="font-size:1.05rem;">{track_info['elevation_change']}</div>
                </div>
                <div class="metric-box">
                    <div class="metric-label">더트 직선 거리</div>
                    <div class="metric-value" style="font-size:1.05rem;">{track_info['straight_dirt']}</div>
                </div>
            </div>
            <p><strong>🎯 가장 유리한 각질:</strong> {", ".join([f"<span class='highlight-badge'>{s}</span>" for s in track_info['favored_styles']])}</p>
            <p style="margin-top:8px; line-height:1.5;"><strong>🏟️ 코스 특징:</strong> {track_info['features']}</p>
            <div style="background:rgba(234, 179, 8, 0.1); border:1px solid rgba(234, 179, 8, 0.3); border-radius:8px; padding:10px; margin-top:10px;">
                <strong style="color:#eab308;">💡 공략 핵심 팁:</strong>
                <p style="margin:4px 0 0 0; font-size:0.9rem;">{track_info['course_tip']}</p>
            </div>
            <p style="margin-top:10px; font-size:0.88rem;"><strong>🏆 대표 레이스:</strong> {", ".join(track_info['major_races'])}</p>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("### 📊 10대 구장 잔디 직선 길이 비교 차트")
    track_names = list(RACETRACKS.keys())
    # 직선 길이 숫자 파싱
    straight_lens = [
        658.7, # 니가타 외선
        525.9, # 도쿄
        473.6, # 한신 외선
        412.5, # 주쿄
        404.0, # 교토 외선
        310.0, # 나카야마
        293.0, # 고쿠라
        292.0, # 후쿠시마
        266.1, # 삿포로
        262.1  # 하코다테
    ]
    sorted_tracks = ["니가타(외선)", "도쿄", "한신(외선)", "주쿄", "교토(외선)", "나카야마", "고쿠라", "후쿠시마", "삿포로", "하코다테"]
    
    fig_bar = go.Figure(go.Bar(
        x=sorted_tracks,
        y=straight_lens,
        marker_color=['#f59e0b', '#3b82f6', '#3b82f6', '#10b981', '#10b981', '#ef4444', '#6b7280', '#6b7280', '#8b5cf6', '#8b5cf6'],
        text=[f"{v}m" for v in straight_lens],
        textposition='auto',
    ))
    fig_bar.update_layout(
        title="JRA 경마장별 최종 직선 길이 (m) 비교",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        yaxis_title="직선 길이 (미터)",
        margin=dict(l=40, r=40, t=40, b=40)
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# ------------------------------------------
# [TAB 5] 마권 종류 & 배당 계산기 & 파독 가이드
# ------------------------------------------
with tab5:
    st.subheader("🎫 10가지 마권 종류 & 실시간 배당금 계산기")
    st.caption("복잡했던 일본 경마 마권을 완벽히 이해하고, 나만의 베팅 시뮬레이션을 돌려보세요.")
    
    # 배당률 계산기 위젯
    st.markdown("### 🧮 인터랙티브 마권 환급금 & 수익률 계산기")
    calc_c1, calc_c2, calc_c3 = st.columns(3)
    
    with calc_c1:
        bet_style = st.selectbox("마권 종류 선택", [b['name'] for b in BET_TYPES], index=0)
    with calc_c2:
        bet_amount = st.number_input("베팅 금액 (엔, ¥)", min_value=100, max_value=1000000, value=1000, step=100)
    with calc_c3:
        odds = st.number_input("확정 배당률 (배)", min_value=1.0, max_value=9999.9, value=3.5, step=0.1)
        
    expected_payout = int(bet_amount * odds)
    net_profit = expected_payout - bet_amount
    roi = (net_profit / bet_amount) * 100 if bet_amount > 0 else 0
    krw_payout = int(expected_payout * 9.1) # 약 100엔 = 910원 기준
    
    st.markdown(f"""
    <div style="display:grid; grid-template-columns: repeat(4, 1fr); gap:12px; margin: 15px 0;">
        <div class="metric-box">
            <div class="metric-label">총 베팅 원금</div>
            <div class="metric-value">¥{bet_amount:,}</div>
        </div>
        <div class="metric-box">
            <div class="metric-label">적중 시 총 환급금 (엔)</div>
            <div class="metric-value" style="color:#10b981;">¥{expected_payout:,}</div>
        </div>
        <div class="metric-box">
            <div class="metric-label">순수익 (엔)</div>
            <div class="metric-value" style="color:#f59e0b;">+¥{net_profit:,}</div>
        </div>
        <div class="metric-box">
            <div class="metric-label">원화 환산 예상액</div>
            <div class="metric-value" style="color:#a855f7;">약 {krw_payout:,}원</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 📋 10가지 마권 완벽 정리표")
    
    for bet in BET_TYPES:
        st.markdown(f"""
        <div class="custom-card">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <h4>{bet['name']} <span style="font-size:0.9rem; color:#94a3b8;">({bet['jp_name']})</span></h4>
                <span class="highlight-badge">난이도: {bet['difficulty']}</span>
            </div>
            <p style="margin: 6px 0; font-size:0.95rem;">{bet['description']}</p>
            <div style="display:flex; gap:10px; margin-top:8px; font-size:0.85rem; color:#94a3b8;">
                <span>📊 환급률: {bet['payout_rate']}</span>
                <span>📈 평균 배당대: {bet['avg_odds']}</span>
            </div>
            <p style="margin-top:6px; font-size:0.9rem; color:#38bdf8;">💡 {bet['recommend']}</p>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    st.subheader("🔍 파독(Paddock) 관찰 5대 비법 & 마장 상태(바바)")
    
    p1, p2 = st.columns(2)
    with p1:
        st.markdown("#### 🐎 실전 파독(예시장) 체크리스트")
        for p in PADDOCK_GUIDE:
            st.markdown(f"""
            <div style="background:rgba(255,255,255,0.02); border-left:3px solid #10b981; padding:10px; margin-bottom:10px; border-radius:4px;">
                <strong>{p['point']}</strong>
                <p style="color:#10b981; margin:4px 0; font-size:0.88rem;">🟢 좋은 징조: {p['good']}</p>
                <p style="color:#ef4444; margin:0; font-size:0.88rem;">🔴 나쁜 징조: {p['bad']}</p>
            </div>
            """, unsafe_allow_html=True)
            
    with p2:
        st.markdown("#### 🌧️ 마장 상태 (바바) 4단계와 영향")
        for cond, desc in TRACK_CONDITIONS.items():
            st.markdown(f"""
            <div style="background:rgba(255,255,255,0.02); border-left:3px solid #f59e0b; padding:10px; margin-bottom:10px; border-radius:4px;">
                <strong>{cond}</strong>
                <p style="margin:4px 0 0 0; font-size:0.88rem; line-height:1.5;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

# ------------------------------------------
# [TAB 6] 명예의 전당 & 주요 경마 뉴스
# ------------------------------------------
with tab6:
    st.subheader("🏆 JRA 명예의 전당 & 역대 상금 랭킹")
    st.caption("일본 경마 역사를 수놓은 위대한 명마들의 전설적인 기록입니다.")
    
    rank_col1, rank_col2 = st.columns(2)
    
    with rank_col1:
        st.markdown("#### 💰 역대 수득 상금 랭킹 TOP 8")
        earnings_data = pd.DataFrame({
            "순위": ["1위", "2위", "3위", "4위", "5위", "6위", "7위", "8위"],
            "경주마": ["이퀴녹스", "우슈바 테소로", "아몬드 아이", "키타산 블랙", "티엠 오페라 오", "오르페브르", "젠틸돈나", "딥 임팩트"],
            "총 상금 (엔)": ["22억 1,544만 엔", "22억 1,000만 엔", "19억 1,526만 엔", "18억 6,687만 엔", "18억 3,518만 엔", "15억 7,621만 엔", "15억 6,700만 엔", "14억 5,455만 엔"],
            "주요 업적": ["세계 레이팅 1위", "두바이 월드컵 우승", "잔디 G1 9승", "G1 7승 & 명종마", "세기말 패왕 8연승", "클래식 삼관 & 폭군", "암말 삼관 & 재팬컵", "무패 삼관 & 전설"]
        })
        st.dataframe(earnings_data, use_container_width=True, hide_index=True)
        
    with rank_col2:
        st.markdown("#### 👑 역사상 단 8두! 무패/클래식 삼관마 계보")
        triple_crown = pd.DataFrame({
            "연도": [1941, 1964, 1983, 1984, 1994, 2005, 2011, 2020],
            "경주마": ["세인트 라이트", "신잔 (神賛)", "미스터 CB", "심볼리 루돌프", "나리타 브라이언", "딥 임팩트", "오르페브르", "콘트레일"],
            "특이사항": ["초대 삼관마", "오관마(五冠馬)의 시조", "후방 추입의 미학", "최초의 무패 삼관(황제)", "괴물, 압도적 차이", "21세기 무패 삼관", "폭군, 이케조에 기수", "부자(父子) 무패 삼관"]
        })
        st.dataframe(triple_crown, use_container_width=True, hide_index=True)
        
    st.markdown("---")
    st.subheader("📰 최신 일본 경마 소식 & 추천 가이드")
    
    news_items = [
        {
            "title": "2024~2026 해외 원정 일본마 맹활약 - 포에버 영, 사우디/BC 클래식 두각",
            "date": "2024.11",
            "desc": "야하기 요시토 조교사와 사카이 류세이 기수가 이끄는 3세 더트 스타마 포에버 영이 미국 브리더스컵 클래식에서 세계 최정상급 말들과 치열한 3착을 기록하며 세계를 놀라게 했습니다."
        },
        {
            "title": "타케 유타카 기수, 도듀스와 함께 텐노상(가을) 감동의 제패",
            "date": "2024.10",
            "desc": "도쿄 경마장에서 열린 제170회 텐노상(가을)에서 도듀스가 32.5초라는 경이적인 막판 스퍼트로 14두를 일거에 제치고 통산 G1 4승을 달성했습니다."
        },
        {
            "title": "교토 경마장 리뉴얼 2주년 - '센테니얼 파크' 팬 친화적 시설 호평",
            "date": "2024.09",
            "desc": "새로운 관람 스탠드와 원형 파독, 요도의 언덕 코스 조망을 강화한 교토 경마장이 가족 단위 및 젊은 경마 팬들의 폭발적인 방문을 이끌어내고 있습니다."
        }
    ]
    
    for n in news_items:
        st.markdown(f"""
        <div class="custom-card">
            <span class="highlight-badge gold-badge">{n['date']}</span>
            <h4 style="margin: 8px 0 4px 0;">{n['title']}</h4>
            <p style="color:#94a3b8; font-size:0.92rem; line-height:1.6;">{n['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

# 푸터
st.markdown("---")
st.markdown("<div style='text-align:center; color:#64748b; font-size:0.85rem;'>🏇 일본 경마 올인원 대시보드 | Data provided by JRA, netkeiba & Historical Archives | 2026</div>", unsafe_allow_html=True)

