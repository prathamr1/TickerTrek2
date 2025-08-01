"""
Configuration settings module v1
contains configuration static values and settings for trek_app.py
"""

PAGE_CONFIG={
    "page_title": "TickerTrek",
    "page_icon":"📈",
    "layout":"wide",
    "initial_sidebar_state":"expanded",
    "menu_items":{
        'Get Help':'https://github.com/prathamr1/TickerTrek2',
        'Report a bug':'https://github.com/prathamr1/TickerTrek2/issues',
        'About': """
        # TickerTrek is a interactive stocks/equity analytical tool 
          built by: https://githubcom/prathamr1/
          -TickerTrek uses Streamlit as deployment platform and 
            Yahoo Finance API (yfinance in PyPI) for data retrieval.
              
          -Version: 1.0.0          
        """
    }
}

CUSTOM_CSS = """
    <style>
        /* Main header styling*/
        .main-header{
            font-size: 3rem;
            font-weight: bold;
            text-align" center;
            background linear-gradient(90deg. #FF7B7A, #4ECDC4);
            -webkit-background-clip" text;
            -webkit-text-sill-color: transparent;
            margin-bottom: 2rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        .metric-card{
            background: linear-gradient(135deg. #667eea 0%, #764ba2 100%);
            padding:1.5rem;
            border-radius: 15px;
            color: white;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            margin: 0.5rem 0;
            transition: transform 0.3s ease;
        }
        
        .metric-card:hover{
            transform:translateY(-5px);
        }
        .positive{
            color:#00ff00 !important;
            font-weight:bold;
        }
        .negative{
            color:#ff0000 !important;
            font-weight:bold;
        }
        .neutral{
            color: #888888 !important;
            font-weight:bold;
        }
        
        .sidebar .sidebar-content{
            background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
        }
        
        .stButton > button{
            background: linear-gradient(45deg, #FF7B7B, #4ECDC4);
            color:white;
            border: none;
            border-radius:25px;
            padding: 0.5rem 1rem;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        .stButton > button:hover{
            transform:scale(1.05);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        .chart-container {
        background: white;
        border-radius: 15px;
        padding: 1rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin: 1rem 0;
        }
    
        /* Statistics table styling */
        .stats-table {
            background: #f8f9fa;
            border-radius: 10px;
            padding: 1rem;
            margin: 1rem 0;
        }
        
        /* Alert styling */
        .alert-success {
            background: linear-gradient(135deg, #56ab2f 0%, #a8e6cf 100%);
            color: white;
            padding: 1rem;
            border-radius: 10px;
            margin: 1rem 0;
        }
        
        .alert-error {
            background: linear-gradient(135deg, #ff416c 0%, #ff4b2b 100%);
            color: white;
            padding: 1rem;
            border-radius: 10px;
            margin: 1rem 0;
        }
        
        /* Loading spinner styling */
        .stSpinner {
            text-align: center;
            margin: 2rem 0;
        }
        
        /* Footer styling */
        .footer {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-align: center;
            padding: 2rem;
            border-radius: 15px;
            margin-top: 3rem;
        }
        
        /* Responsive design */
        @media (max-width: 768px) {
            .main-header {
                font-size: 2rem;
            }
            
            .metric-card {
                padding: 1rem;
            }
        }
        
        /* Dark theme support */
        @media (prefers-color-scheme: dark) {
            .metric-card {
                background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
            }
            
            .chart-container {
                background: #2c3e50;
                color: white;
            }
        }
    </style>
"""


POPULAR_STOCKS = {
    "Google":"GOOGL",
    "Apple" : "AAPL",
    "Tata Motors":"TATAMOTORS.NS",
    "IOC" : "IOC.NS",
    "LIC":"LICI.NS",
    "Meta": "META",
    "NVIDIA": "NVDA",
    "JPMorgan": "JPM",
}

PERIOD_OPTIONS = {
    "1 Day": "1d",
    "5 Days": "5d",
    "1 Month": "1mo",
    "3 Months": "3mo",
    "6 Months": "6mo",
    "1 Year": "1y",
    "2 Years": "2y"
}

INTERVAL_OPTIONS = {
    "1d": "1h",  # 1 day -> 1 hour intervals
    "5d": "1h",  # 5 days -> 1 hour intervals
    "1mo": "1d",  # 1 month -> 1 day intervals
    "3mo": "1d",  # 3 months -> 1 day intervals
    "6mo": "1d",  # 6 months -> 1 day intervals
    "1y": "1d",  # 1 year -> 1 day intervals
    "2y": "1wk",  # 2 years -> 1 week intervals
    "5y": "1wk",  # 5 years -> 1 week intervals
    "10y": "1mo",  # 10 years -> 1 month intervals
    "max": "1mo"  # Max -> 1 month intervals
}

TECHNICAL_INDICATORS = {
    # Moving averages
    "MA_SHORT": 20,
    "MA_LONG": 50,
    "MA_EXTRA_LONG": 200,

    # RSI settings
    "RSI_PERIOD": 14,
    "RSI_OVERBOUGHT": 70,
    "RSI_OVERSOLD": 30,

    # Bollinger Bands
    "BOLLINGER_PERIOD": 20,
    "BOLLINGER_STD": 2,

    # MACD settings
    "MACD_FAST": 12,
    "MACD_SLOW": 26,
    "MACD_SIGNAL": 9,

    # Stochastic settings
    "STOCH_K": 14,
    "STOCH_D": 3,
    "STOCH_SMOOTH": 3,

    # Williams %R
    "WILLIAMS_R_PERIOD": 14,

    # CCI settings
    "CCI_PERIOD": 20
}

COLOR_SCHEMES = {
    "Default": {
        "primary": "#FF6B6B",
        "secondary": "#4ECDC4",
        "accent": "#45B7D1",
        "background": "#FFFFFF",
        "text": "#333333"
    },
    "Dark": {
        "primary": "#FF6B6B",
        "secondary": "#4ECDC4",
        "accent": "#45B7D1",
        "background": "#2c3e50",
        "text": "#FFFFFF"
    },
    "Colorful": {
        "primary": "#FF6B6B",
        "secondary": "#4ECDC4",
        "accent": "#45B7D1",
        "background": "#F8F9FA",
        "text": "#2C3E50"
    }
}