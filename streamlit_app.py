#######################
# Import libraries
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

#######################
# Page configuration
st.set_page_config(
    page_title="US Population Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("default")

#######################
# CSS styling
st.markdown("""
<style>

[data-testid="block-container"] {
    padding-left: 2rem;
    padding-right: 2rem;
    padding-top: 1rem;
    padding-bottom: 0rem;
    margin-bottom: -7rem;
}

[data-testid="stVerticalBlock"] {
    padding-left: 0rem;
    padding-right: 0rem;
}

[data-testid="stMetric"] {
    background-color: #393939;
    text-align: center;
    padding: 15px 0;
}

[data-testid="stMetricLabel"] {
  display: flex;
  justify-content: center;
  align-items: center;
}

[data-testid="stMetricDeltaIcon-Up"] {
    position: relative;
    left: 38%;
    -webkit-transform: translateX(-50%);
    -ms-transform: translateX(-50%);
    transform: translateX(-50%);
}

[data-testid="stMetricDeltaIcon-Down"] {
    position: relative;
    left: 38%;
    -webkit-transform: translateX(-50%);
    -ms-transform: translateX(-50%);
    transform: translateX(-50%);
}

</style>
""", unsafe_allow_html=True)


#######################
# Load data
df_reshaped = pd.read_csv('ugv_mission_dataset_220rows.csv') ## 분석 데이터 넣기


#######################
# Sidebar
with st.sidebar:

    st.title("UGV Environment Dashboard")
    st.markdown("### ⚙️ 분석 옵션 설정")

    st.markdown("---")
    st.subheader("🔎 데이터 필터")

    # 필터: 장애물 밀도
    obstacle_filter = st.multiselect(
        "Obstacle Density (장애물 밀도)",
        options=sorted(df_reshaped["ObstacleDensity"].unique()),
        default=sorted(df_reshaped["ObstacleDensity"].unique())
    )

    # 필터: 지형 난이도
    terrain_min, terrain_max = st.slider(
        "Terrain Difficulty (지형 난이도)",
        float(df_reshaped["TerrainDifficulty"].min()),
        float(df_reshaped["TerrainDifficulty"].max()),
        (float(df_reshaped["TerrainDifficulty"].min()),
         float(df_reshaped["TerrainDifficulty"].max()))
    )

    # 필터: 통신 품질
    comm_min, comm_max = st.slider(
        "Comm Quality (통신 품질)",
        float(df_reshaped["CommQuality"].min()),
        float(df_reshaped["CommQuality"].max()),
        (float(df_reshaped["CommQuality"].min()),
         float(df_reshaped["CommQuality"].max()))
    )

    # 필터: 기상 영향도
    weather_min, weather_max = st.slider(
        "Weather Impact (기상 영향도)",
        float(df_reshaped["WeatherImpact"].min()),
        float(df_reshaped["WeatherImpact"].max()),
        (float(df_reshaped["WeatherImpact"].min()),
         float(df_reshaped["WeatherImpact"].max()))
    )

    st.markdown("---")
    st.subheader("🤖 머신러닝 옵션")

    # 클러스터링 사용 여부
    use_cluster = st.checkbox("클러스터링 적용 (K-Means)", value=True)

    if use_cluster:
        k_clusters = st.slider(
            "클러스터 개수 (K)",
            min_value=2,
            max_value=6,
            value=3
        )

    # 회귀 모델 사용 여부
    use_regression = st.checkbox("위협도(Threat Level) 회귀 예측 모델", value=True)

    if use_regression:
        st.markdown(
            """
            - 모델: Random Forest Regressor  
            - 예측 변수: TerrainDifficulty, CommQuality, SensorInterference, WeatherImpact  
            """
        )

    st.markdown("---")
    st.caption("📌 필터 및 옵션 변경 시 전체 대시보드가 자동 업데이트됩니다.")


#######################
# Plots



#######################
# Dashboard Main Panel
col = st.columns((1.5, 4.5, 2), gap='medium')

# with col[0]:


# with col[1]:



# with col[2]: