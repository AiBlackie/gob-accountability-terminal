import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(page_title="BB Terminal: Gov't Accountability", page_icon="📉", layout="wide")

# --- HIDE THE DEFAULT STREAMLIT HEADER/FOOTER ---
st.markdown("""
<style>
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .block-container {padding-top: 2rem;}
</style>
""", unsafe_allow_html=True)

# Custom CSS for Bloomberg Terminal Aesthetic
st.markdown("""
<style>
    /* Dark Theme overrides */
    .stApp { background-color: #0e1117; color: #d1d5db; }
    h1, h2, h3 { color: #ffffff !important; font-family: 'Roboto Mono', monospace !important; }
    
    /* Custom Terminal Cards */
    .terminal-card {
        background-color: #1f2937;
        border: 1px solid #374151;
        border-radius: 5px;
        padding: 20px;
        font-family: 'Roboto Mono', monospace;
        color: #d1d5db;
        margin-bottom: 20px;
    }
    
    .terminal-header {
        border-bottom: 1px solid #374151;
        padding-bottom: 10px;
        margin-bottom: 15px;
        font-weight: bold;
        color: #fbbf24; /* Amber warning color */
        font-size: 1.1em;
    }

    .lf-badge {
        background-color: #dc2626;
        color: white;
        padding: 2px 6px;
        border-radius: 3px;
        font-weight: bold;
        font-size: 0.85em;
        font-family: 'Roboto Mono', monospace;
        letter-spacing: 1px;
    }

    .status-ok { color: #10b981; font-weight: bold; }
    .status-warn { color: #f59e0b; font-weight: bold; }
    .status-fail { color: #ef4444; font-weight: bold; }

    /* Custom Link Styling */
    a { color: #60a5fa !important; text-decoration: none; }
    a:hover { text-decoration: underline; }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# HEADER & TICKER
# ============================================================================
st.title("📉 GOB TERMINAL // ACCOUNTABILITY AUDIT")
st.markdown("""
<div class="terminal-card" style="background-color: #111827; border-color: #dc2626;">
    <div style="font-family: 'Roboto Mono', monospace; font-size: 1.2em;">
        <span style="color: #ef4444; font-weight: bold;">BARBADOS.GOV 2024_FS <span class="lf-badge">[LF]</span></span> | 
        STATUS: <span class="status-fail">DELINQUENT / NOT SUBMITTED</span> | 
        DELAY: <span id="top-delay" style="color: #fbbf24;">CALCULATING...</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# THE TERMINAL CLOCK & SECTION 88 ALERT
# ============================================================================
st.markdown("### 🚨 NOTICE OF DELINQUENCY (Section 88(1) PFMA 2019-1)")

# Section 88 Quote Styled in Red
st.markdown("""
<div class="terminal-card" style="border-left: 4px solid #ef4444; background-color: #2a1212; margin-bottom: 20px;">
    <div class="terminal-header" style="color: #ef4444; border-bottom: 1px solid #7f1d1d;">SUBMISSION REQUIREMENT (Section 88(1) PFMA 2019-1)</div>
    <p style="color: #fca5a5; font-style: italic; font-size: 1.05em;">
        "In respect of each financial year and within a period of <strong>4 months</strong> after the close of each financial year, the <strong>Accountant-General</strong> shall prepare, sign and submit..."
    </p>
</div>
""", unsafe_allow_html=True)

due_date_2024 = datetime(2024, 7, 31, 23, 59, 59)
due_date_str = due_date_2024.strftime("%B %d, %Y %H:%M:%S")

html_clock = f"""
<!DOCTYPE html>
<html>
<head>
<style>
    body {{
        font-family: 'Roboto Mono', monospace;
        background-color: transparent;
        margin: 0;
        padding: 0;
    }}
    .terminal-panel {{
        background-color: #1f2937;
        border: 1px solid #374151;
        border-left: 4px solid #ef4444;
        padding: 20px;
        border-radius: 4px;
    }}
    .timer-row {{
        display: flex;
        justify-content: space-between;
        align-items: center;
    }}
    .timer-label {{
        color: #9ca3af;
        font-size: 0.9em;
        text-transform: uppercase;
    }}
    .timer-value {{
        color: #fbbf24;
        font-size: 2em;
        font-weight: bold;
        letter-spacing: 2px;
    }}
    .timer-sub {{
        color: #6b7280;
        font-size: 0.8em;
        margin-top: 5px;
    }}
</style>
</head>
<body>
<div class="terminal-panel">
    <div class="timer-row">
        <div>
            <div class="timer-label">TIME ELAPSED SINCE LEGAL DEADLINE</div>
            <div class="timer-sub">Target: 2024 Financial Statements (Due July 31, 2024)</div>
        </div>
        <div style="text-align: right;">
            <div class="timer-value" id="clock">000D : 00H : 00M : 00S</div>
        </div>
    </div>
</div>

<script>
    var dueDate = new Date("{due_date_str}").getTime();

    function updateClock() {{
        var now = new Date().getTime();
        var distance = now - dueDate; 

        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);

        var dStr = String(days).padStart(3, '0');
        var hStr = String(hours).padStart(2, '0');
        var mStr = String(minutes).padStart(2, '0');
        var sStr = String(seconds).padStart(2, '0');

        document.getElementById("clock").innerText = dStr + "D : " + hStr + "H : " + mStr + "M : " + sStr + "S";
        
        var topDelay = document.getElementById("top-delay");
        if(topDelay) {{
            topDelay.innerText = dStr + " DAYS OVERDUE";
        }}
    }}

    setInterval(updateClock, 1000);
    updateClock();
</script>
</body>
</html>
"""
components.html(html_clock, height=110)

# ============================================================================
# TOP BANNER
# ============================================================================
banner_html = """
<style>
    .alert-banner {
        display: flex;
        width: 100%;
        font-family: 'Roboto Mono', monospace;
        margin-top: 10px;
        margin-bottom: 20px;
        border-radius: 5px;
        overflow: hidden;
        border: 1px solid #374151;
    }
    .banner-item {
        flex: 1;
        text-align: center;
        padding: 12px 5px;
        font-size: 0.9em;
        font-weight: bold;
        border-right: 1px solid #111827;
    }
    .banner-item:last-child {
        border-right: none;
    }
    .banner-year {
        font-size: 0.8em;
        display: block;
        margin-bottom: 5px;
        opacity: 0.8;
    }
    .banner-late {
        background-color: #d97706; /* Amber */
        color: #111827;
    }
    .banner-missing {
        background-color: #dc2626; /* Red */
        color: white;
        animation: flashRed 1.5s infinite;
    }
    @keyframes flashRed {
        0% { background-color: #dc2626; box-shadow: inset 0 0 10px #ef4444; }
        50% { background-color: #7f1d1d; box-shadow: inset 0 0 20px #dc2626; }
        100% { background-color: #dc2626; box-shadow: inset 0 0 10px #ef4444; }
    }
</style>

<div class="alert-banner">
    <div class="banner-item banner-late"><span class="banner-year">FY 2020</span>LATE [LF]</div>
    <div class="banner-item banner-late"><span class="banner-year">FY 2021</span>LATE [LF]</div>
    <div class="banner-item banner-late"><span class="banner-year">FY 2022</span>LATE [LF]</div>
    <div class="banner-item banner-late"><span class="banner-year">FY 2023</span>LATE [LF]</div>
    <div class="banner-item banner-missing"><span class="banner-year">FY 2024</span>NOT SUBMITTED</div>
    <div class="banner-item banner-missing"><span class="banner-year">FY 2025</span>NOT SUBMITTED</div>
</div>
"""
components.html(banner_html, height=80)

st.markdown("---")

# ============================================================================
# TABS
# ============================================================================
tab1, tab2 = st.tabs(["📉 TERMINAL DASHBOARD", "📖 PLAIN ENGLISH GLOSSARY"])

# ============================================================================
# TAB 1: THE MAIN TERMINAL DASHBOARD
# ============================================================================
with tab1:
    # --- THE STRUCTURAL DEFECT (IPSAS 35) ---
    st.markdown("### ⚖️ THE STRUCTURAL DEFECT: IPSAS 35 Consolidation Failure")

    st.markdown("""
    <div class="terminal-card" style="border-left: 4px solid #f59e0b;">
        <div class="terminal-header">AUDIT FINDING: INCOMPLETE FINANCIAL PICTURE</div>
        <p>Even if the Government submits the 2024 Financial Statements, the accounts will <strong>not be fully compliant with accounting standards.</strong></p>
        <p>Under <strong>IPSAS 35</strong>, the Government is required to consolidate the financials of all State-Owned Enterprises (SOEs). Because the Treasury has not collected and audited the accounts of agencies like the Queen Elizabeth Hospital, the Transport Board, and the National Housing Corporation, the Government's financial statements exclude the financial data of these entities.</p>
        <p style="color: #ef4444; font-family: 'Roboto Mono', monospace;">
            > Auditor General's 2024 Report (Page 15): "In the absence of consolidation, the statements do not present a comprehensive view of Government's financial performance and position and it is therefore not in conformity with International Public Sector Accounting Standards (IPSAS)."
        </p>
    </div>
    """, unsafe_allow_html=True)

    # --- REGULATORY FILING STATUS ---
    st.markdown("### 🗄️ REGULATORY FILING STATUS (2020 - Present)")
    st.markdown("Focus: The **Government's Financial Statements** (prepared by the Accountant General) are the primary legal documents required under Section 88(1) of the PFMA.")

    # Table Headers
    h_col1, h_col2, h_col3, h_col4, h_col5, h_col6 = st.columns([1, 1.2, 1.5, 1.5, 1.2, 2.6])
    h_col1.markdown("**FISCAL YEAR**")
    h_col2.markdown("**LEGAL DEADLINE**")
    h_col3.markdown("**ACCT. GEN SIGNED**")
    h_col4.markdown("**AUDITOR GEN SIGNED**")
    h_col5.markdown("**STATUS**")
    h_col6.markdown("**AUDIT OPINION**")
    st.markdown("<hr style='margin: 0px; border-color: #374151;'>", unsafe_allow_html=True)

    # --- ROW 1: 2025 ---
    r1_c1, r1_c2, r1_c3, r1_c4, r1_c5, r1_c6 = st.columns([1, 1.2, 1.5, 1.5, 1.2, 2.6])
    r1_c1.markdown("**2025**")
    r1_c2.markdown("July 31, 2025")
    r1_c3.markdown("--")
    r1_c4.markdown("--")
    r1_c5.markdown('<span class="status-fail">NOT SUBMITTED <span class="lf-badge">[LF]</span></span>', unsafe_allow_html=True)
    r1_c6.markdown("N/A")
    st.markdown("<hr style='margin: 0px; border-color: #374151;'>", unsafe_allow_html=True)

    # --- ROW 2: 2024 ---
    r2_c1, r2_c2, r2_c3, r2_c4, r2_c5, r2_c6 = st.columns([1, 1.2, 1.5, 1.5, 1.2, 2.6])
    r2_c1.markdown("**2024**")
    r2_c2.markdown("July 31, 2024")
    r2_c3.markdown("--")
    r2_c4.markdown("--")
    r2_c5.markdown('<span class="status-fail">NOT SUBMITTED <span class="lf-badge">[LF]</span></span>', unsafe_allow_html=True)
    r2_c6.markdown("N/A")
    st.markdown("<hr style='margin: 0px; border-color: #374151;'>", unsafe_allow_html=True)

    # --- ROW 3: 2023 ---
    r3_c1, r3_c2, r3_c3, r3_c4, r3_c5, r3_c6 = st.columns([1, 1.2, 1.5, 1.5, 1.2, 2.6])
    r3_c1.markdown("**2023**")
    r3_c2.markdown("July 31, 2023")
    r3_c3.markdown("Sept 14, 2023")
    r3_c4.markdown("April 2, 2025")
    r3_c5.markdown('<span class="status-warn">LATE <span class="lf-badge">[LF]</span></span>', unsafe_allow_html=True)
    r3_c6.markdown("**ADVERSE OPINION.**")
    st.markdown("<hr style='margin: 0px; border-color: #374151;'>", unsafe_allow_html=True)

    # --- ROW 4: 2022 ---
    r4_c1, r4_c2, r4_c3, r4_c4, r4_c5, r4_c6 = st.columns([1, 1.2, 1.5, 1.5, 1.2, 2.6])
    r4_c1.markdown("**2022**")
    r4_c2.markdown("July 31, 2022")
    r4_c3.markdown("Aug 31, 2022")
    r4_c4.markdown("Aug 30, 2023")
    r4_c5.markdown('<span class="status-warn">LATE <span class="lf-badge">[LF]</span></span>', unsafe_allow_html=True)
    r4_c6.markdown("**ADVERSE OPINION.**")
    st.markdown("<hr style='margin: 0px; border-color: #374151;'>", unsafe_allow_html=True)

    # --- ROW 5: 2021 ---
    r5_c1, r5_c2, r5_c3, r5_c4, r5_c5, r5_c6 = st.columns([1, 1.2, 1.5, 1.5, 1.2, 2.6])
    r5_c1.markdown("**2021**")
    r5_c2.markdown("July 31, 2021")
    r5_c3.markdown("Dec 31, 2021")
    r5_c4.markdown("July 1, 2022")
    r5_c5.markdown('<span class="status-warn">LATE <span class="lf-badge">[LF]</span></span>', unsafe_allow_html=True)
    r5_c6.markdown("**ADVERSE OPINION.**")
    st.markdown("<hr style='margin: 0px; border-color: #374151;'>", unsafe_allow_html=True)

    # --- ROW 6: 2020 ---
    r6_c1, r6_c2, r6_c3, r6_c4, r6_c5, r6_c6 = st.columns([1, 1.2, 1.5, 1.5, 1.2, 2.6])
    r6_c1.markdown("**2020**")
    r6_c2.markdown("July 31, 2020")
    r6_c3.markdown("April 26, 2021")
    r6_c4.markdown("July 1, 2022")
    r6_c5.markdown('<span class="status-warn">LATE <span class="lf-badge">[LF]</span></span>', unsafe_allow_html=True)
    r6_c6.markdown("**ADVERSE OPINION.**")
    st.markdown("<hr style='margin: 0px; border-color: #374151;'>", unsafe_allow_html=True)

    st.caption("Dates verified from the sign-off pages of the official Government Financial Statements and Auditor General Reports provided in the source PDFs.")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- TERMINAL CROSS-CHECK: DIGITAL EVIDENCE & VERIFICATION ---
    st.markdown("### 🕵️‍♂️ TERMINAL CROSS-CHECK: OFFICIAL GOVERNMENT WEBSITES")
    
    # Section 90 Quote Styled in Red
    st.markdown("""
    <div class="terminal-card" style="border-left: 4px solid #ef4444; background-color: #2a1212; margin-bottom: 20px;">
        <div class="terminal-header" style="color: #ef4444; border-bottom: 1px solid #7f1d1d;">PUBLICATION REQUIREMENT (Section 90 PFMA 2019-1)</div>
        <p style="color: #fca5a5; font-style: italic; font-size: 1.05em;">
            "The Director of Finance shall publish the Financial Statements, the Audit Opinion, and the Annual Report of the Government <strong>on the official website of the Government</strong> no later than one week after these documents have been laid in Parliament..."
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("Verify the data directly at the source. The Government's own websites provide the current filing status.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="terminal-card" style="height: 100%;">
            <div class="terminal-header" style="color: #ef4444;">TREASURY.GOV.BB</div>
            <p><strong>STATUS: OUTDATED</strong></p>
            <p>The Accountant General's official portal lists the most recent financial statement as the <strong>2015-2016</strong> fiscal year.</p>
            <br>
            <p><a href="https://treasury.gov.bb/content/accountant-general-financial-statements" target="_blank">> Access Treasury Portal</a></p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="terminal-card" style="height: 100%;">
            <div class="terminal-header" style="color: #10b981;">BAO.GOV.BB</div>
            <p><strong>STATUS: UP TO DATE</strong></p>
            <p>The Auditor General has published the 2023 and 2022 reports. There is no 2024 or 2025 report listed because the Treasury has not submitted them.</p>
            <br>
            <p><a href="https://bao.gov.bb/reports/" target="_blank">> Access Audit Office Portal</a></p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="terminal-card" style="height: 100%;">
            <div class="terminal-header" style="color: #fbbf24;">BARBADOSPARLIAMENT.COM</div>
            <p><strong>STATUS: LAGGING</strong></p>
            <p>Parliament is actively processing 2026 legislation, yet the latest Auditor General report posted to the Parliament website is the 2022 Report (posted Sept 2023).</p>
            <br>
            <p><a href="https://barbadosparliament.com/document/listall/6" target="_blank">> Access Parliament Documents</a></p>
        </div>
        """, unsafe_allow_html=True)

    st.caption("DATA SOURCES: Public Finance Management Act 2019-1 | Auditor General's Annual Report 2024 | Government of Barbados Treasury Department | Barbados Audit Office | Parliament of Barbados")


# ============================================================================
# TAB 2: PLAIN ENGLISH GLOSSARY
# ============================================================================
with tab2:
    st.markdown("### 📖 PLAIN ENGLISH GLOSSARY")
    st.markdown("Accounting and legal terminology can be dense. This glossary translates the jargon used in the Terminal Dashboard into clear, everyday language.")

    st.markdown("---")

    col_gloss1, col_gloss2 = st.columns(2)

    with col_gloss1:
        st.markdown("""
        <div class="terminal-card" style="border-left: 4px solid #fbbf24;">
            <div class="terminal-header" style="color: #fbbf24;">PFMA (Public Finance Management Act)</div>
            <p><strong>What it is:</strong> A law passed in 2019 to govern how the Government collects, spends, and reports public money.</p>
            <p><strong>Section 88(1):</strong> This specific clause is the "deadline law." It legally requires the Accountant General to hand over the country's financial statements to the Auditor General by July 31st every year.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="terminal-card" style="border-left: 4px solid #ef4444;">
            <div class="terminal-header" style="color: #ef4444;">ADVERSE OPINION</div>
            <p><strong>What it means:</strong> When the Auditor General (the nation's top independent accountant) reviews the government's books and issues an "Adverse Opinion," it means the numbers are considered unreliable.</p>
            <p>It is an official declaration that the financial statements do not present a "true and fair view" of the country's finances. It means the government cannot adequately prove its financial position.</p>
        </div>
        """, unsafe_allow_html=True)

    with col_gloss2:
        st.markdown("""
        <div class="terminal-card" style="border-left: 4px solid #60a5fa;">
            <div class="terminal-header" style="color: #60a5fa;">IPSAS 35 (Consolidation)</div>
            <p><strong>What it is:</strong> International Public Sector Accounting Standards. These are the global rules for government accounting.</p>
            <p><strong>What it means:</strong> It means you cannot leave things out. If the Government owns or controls a company (like a hospital or a water authority), that company's debts and assets <strong>must</strong> be included in the main national accounts. The Auditor General notes that this standard is not currently being met.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="terminal-card" style="border-left: 4px solid #ef4444;">
            <div class="terminal-header" style="color: #ef4444;">[LF] BADGE (Late Filing)</div>
            <p><strong>What it means:</strong> Borrowed from financial markets. When a public company fails to file its financial reports on time, the stock exchange tags their ticker symbol with <strong>.LF</strong> to warn investors.</p>
            <p>We apply it here to indicate that the Government's financial reports are past their legal deadline.</p>
        </div>
        """, unsafe_allow_html=True)