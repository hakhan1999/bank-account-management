import streamlit as st
from bank import Bank

# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="NeoBank",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ==================================================
# SESSION STATE
# ==================================================

if "theme" not in st.session_state:
    st.session_state.theme = "Light"


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.markdown(
        """
        <div class="brand">
            <div class="brand-icon">N</div>
            <div>
                <div class="brand-title">NeoBank</div>
                <div class="brand-subtitle">Banking System</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Navigation")

    menu = st.radio(
        "Navigation",
        [
            "Dashboard",
            "Create Account",
            "Deposit Money",
            "Withdraw Money",
            "Account Details",
            "Update Account",
            "Delete Account",
        ],
        label_visibility="collapsed",
    )

    st.divider()

    st.markdown("### Appearance")

    theme = st.radio(
        "Theme",
        ["Light", "Dark"],
        horizontal=True,
        key="theme",
        label_visibility="collapsed",
    )

    st.divider()

    st.caption("Built with Python & Streamlit")


# ==================================================
# LIGHT THEME
# ==================================================

if theme == "Light":

    background = "#f6f7f9"
    surface = "#ffffff"
    surface_secondary = "#f9fafb"

    text_primary = "#111827"
    text_secondary = "#6b7280"

    border = "#e5e7eb"

    input_background = "#ffffff"

    sidebar_background = "#ffffff"

    card_shadow = "0 4px 24px rgba(0, 0, 0, 0.04)"

    balance_background = "#111827"
    balance_text = "#ffffff"


# ==================================================
# DARK THEME
# ==================================================

else:

    background = "#0b0f19"
    surface = "#111827"
    surface_secondary = "#161e2e"

    text_primary = "#f9fafb"
    text_secondary = "#9ca3af"

    border = "#263142"

    input_background = "#161e2e"

    sidebar_background = "#0f1522"

    card_shadow = "0 4px 24px rgba(0, 0, 0, 0.25)"

    balance_background = "#2563eb"
    balance_text = "#ffffff"


# ==================================================
# GLOBAL CSS
# ==================================================

st.markdown(
    f"""
    <style>

    /* --------------------------------
       Main App
    -------------------------------- */

    .stApp {{
        background: {background};
        color: {text_primary};
    }}


    .main .block-container {{
        max-width: 1050px;
        padding-top: 2.5rem;
        padding-bottom: 4rem;
    }}


    /* --------------------------------
       Text
    -------------------------------- */

    h1,
    h2,
    h3,
    h4,
    h5,
    h6 {{
        color: {text_primary} !important;
        letter-spacing: -0.3px;
    }}


    p {{
        color: {text_secondary};
    }}


    .stCaption {{
        color: {text_secondary} !important;
    }}


    /* --------------------------------
       Sidebar
    -------------------------------- */

    section[data-testid="stSidebar"] {{
        background: {sidebar_background};
        border-right: 1px solid {border};
    }}


    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {{
        color: {text_primary} !important;
    }}


    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] label {{
        color: {text_primary};
    }}


    /* --------------------------------
       Brand
    -------------------------------- */

    .brand {{
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 32px;
    }}


    .brand-icon {{
        width: 42px;
        height: 42px;

        display: flex;
        align-items: center;
        justify-content: center;

        background: #2563eb;
        color: white;

        border-radius: 12px;

        font-size: 20px;
        font-weight: 700;
    }}


    .brand-title {{
        color: {text_primary};
        font-size: 18px;
        font-weight: 700;
    }}


    .brand-subtitle {{
        color: {text_secondary};
        font-size: 12px;
    }}


    /* --------------------------------
       Inputs
    -------------------------------- */

    div[data-testid="stTextInput"] input,
    div[data-testid="stNumberInput"] input {{
        background: {input_background};
        color: {text_primary};

        border: 1px solid {border};

        border-radius: 10px;

        min-height: 44px;
    }}


    div[data-testid="stTextInput"] input:focus,
    div[data-testid="stNumberInput"] input:focus {{
        border-color: #2563eb;
        box-shadow: 0 0 0 1px #2563eb;
    }}


    div[data-testid="stTextInput"] input::placeholder {{
        color: {text_secondary};
    }}


    label[data-testid="stWidgetLabel"] p {{
        color: {text_primary} !important;
        font-weight: 500;
    }}


    /* --------------------------------
       Buttons
    -------------------------------- */

    div.stButton > button,
    div[data-testid="stFormSubmitButton"] > button {{
        width: 100%;

        min-height: 46px;

        border-radius: 10px;

        border: none;

        background: #2563eb;

        color: white;

        font-weight: 600;

        transition: all 0.2s ease;
    }}


    div.stButton > button:hover,
    div[data-testid="stFormSubmitButton"] > button:hover {{
        background: #1d4ed8;
        color: white;

        border: none;

        transform: translateY(-1px);
    }}


    /* --------------------------------
       Metrics
    -------------------------------- */

    div[data-testid="stMetric"] {{
        background: {surface};

        border: 1px solid {border};

        border-radius: 16px;

        padding: 22px;

        box-shadow: {card_shadow};
    }}


    div[data-testid="stMetricLabel"] {{
        color: {text_secondary};
    }}


    div[data-testid="stMetricValue"] {{
        color: {text_primary};
    }}


    /* --------------------------------
       Forms
    -------------------------------- */

    div[data-testid="stForm"] {{
        background: {surface};

        border: 1px solid {border};

        border-radius: 18px;

        padding: 26px;

        box-shadow: {card_shadow};
    }}


    /* --------------------------------
       Balance Card
    -------------------------------- */

    .balance-card {{
        background: {balance_background};

        color: {balance_text};

        border-radius: 20px;

        padding: 30px;

        margin-top: 24px;
        margin-bottom: 28px;
    }}


    .balance-label {{
        color: rgba(255,255,255,0.7);

        font-size: 12px;

        text-transform: uppercase;

        letter-spacing: 1px;
    }}


    .balance-value {{
        color: white;

        font-size: 38px;

        font-weight: 700;

        margin-top: 8px;
    }}


    .balance-account {{
        color: rgba(255,255,255,0.7);

        margin-top: 16px;

        font-size: 13px;
    }}


    /* --------------------------------
       User Information Cards
    -------------------------------- */

    .info-card {{
        background: {surface};

        border: 1px solid {border};

        border-radius: 14px;

        padding: 20px;

        height: 100%;

        box-shadow: {card_shadow};
    }}


    .info-label {{
        color: {text_secondary};

        font-size: 12px;

        margin-bottom: 5px;
    }}


    .info-value {{
        color: {text_primary};

        font-size: 16px;

        font-weight: 600;
    }}


    /* --------------------------------
       Dashboard Welcome
    -------------------------------- */

    .welcome-card {{
        background: {surface};

        border: 1px solid {border};

        border-radius: 18px;

        padding: 28px;

        margin-top: 25px;

        box-shadow: {card_shadow};
    }}


    .welcome-card h3 {{
        margin-top: 0;
    }}


    .welcome-card p {{
        margin-bottom: 0;

        line-height: 1.7;
    }}


    /* --------------------------------
       Radio Buttons
    -------------------------------- */

    div[role="radiogroup"] label {{
        color: {text_primary} !important;
    }}


    div[role="radiogroup"] p {{
        color: {text_primary} !important;
    }}


    /* --------------------------------
       Checkbox
    -------------------------------- */

    div[data-testid="stCheckbox"] label {{
        color: {text_primary};
    }}


    /* --------------------------------
       Divider
    -------------------------------- */

    hr {{
        border-color: {border} !important;
    }}


    /* --------------------------------
       Alerts
    -------------------------------- */

    div[data-testid="stAlert"] {{
        border-radius: 12px;
    }}


    /* --------------------------------
       Header
    -------------------------------- */

    header[data-testid="stHeader"] {{
        background: transparent;
    }}


    /* Hide Streamlit Menu/Footer */

    #MainMenu {{
        visibility: hidden;
    }}

    footer {{
        visibility: hidden;
    }}
    
    .stFormSubmitButton p{{
        color:white;
    }}

    </style>
    """,
    unsafe_allow_html=True,
)


# ==================================================
# PAGE HEADER
# ==================================================

st.title("Bank Management")

st.caption("Manage accounts, transactions and customer information.")

st.divider()


# ==================================================
# DASHBOARD
# ==================================================

if menu == "Dashboard":

    st.subheader("Dashboard")

    total_accounts = len(Bank.data)

    total_balance = sum(user.get("balance", 0) for user in Bank.data)

    average_balance = total_balance / total_accounts if total_accounts > 0 else 0

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric("Total Accounts", total_accounts)

    with col2:

        st.metric("Total Balance", f"Rs. {total_balance:,.0f}")

    with col3:

        st.metric("Average Balance", f"Rs. {average_balance:,.0f}")

    st.markdown(
        """
        <div class="welcome-card">

            <h3>Welcome to NeoBank</h3>

            <p>
                Use the navigation menu to create a new account,
                deposit or withdraw money, check account details,
                update customer information or delete an account.
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ==================================================
# CREATE ACCOUNT
# ==================================================

elif menu == "Create Account":

    st.subheader("Create Account")

    st.caption("Enter your personal information to create a new account.")

    with st.form("create_account_form"):

        col1, col2 = st.columns(2)

        with col1:

            name = st.text_input("Full Name", placeholder="Enter your full name")

        with col2:

            age = st.number_input("Age", min_value=1, max_value=120, value=18, step=1)

        email = st.text_input("Email Address", placeholder="example@email.com")

        pin = st.text_input(
            "4 Digit PIN", type="password", max_chars=4, placeholder="Enter 4 digit PIN"
        )

        submit = st.form_submit_button("Create Account")

        if submit:

            success, message, account_number = Bank.create_account(
                name, age, email, pin
            )

            if success:

                st.success(message)

                st.info(f"Your account number is " f"**{account_number}**")

                st.warning("Save your account number and PIN securely.")

            else:

                st.error(message)


# ==================================================
# DEPOSIT MONEY
# ==================================================

elif menu == "Deposit Money":

    st.subheader("Deposit Money")

    st.caption("Add money to an existing bank account.")

    with st.form("deposit_form"):

        account_number = st.text_input(
            "Account Number", placeholder="Enter account number"
        )

        pin = st.text_input(
            "PIN", type="password", max_chars=4, placeholder="Enter PIN"
        )

        amount = st.number_input(
            "Deposit Amount", min_value=0.0, max_value=100000.0, value=0.0, step=500.0
        )

        submit = st.form_submit_button("Deposit Money")

        if submit:

            success, message = Bank.deposit(account_number, pin, amount)

            if success:
                st.success(message)

            else:
                st.error(message)


# ==================================================
# WITHDRAW MONEY
# ==================================================

elif menu == "Withdraw Money":

    st.subheader("Withdraw Money")

    st.caption("Withdraw money from your bank account.")

    with st.form("withdraw_form"):

        account_number = st.text_input(
            "Account Number", placeholder="Enter account number"
        )

        pin = st.text_input(
            "PIN", type="password", max_chars=4, placeholder="Enter PIN"
        )

        amount = st.number_input(
            "Withdrawal Amount", min_value=0.0, value=0.0, step=500.0
        )

        submit = st.form_submit_button("Withdraw Money")

        if submit:

            success, message = Bank.withdraw(account_number, pin, amount)

            if success:
                st.success(message)

            else:
                st.error(message)


# ==================================================
# ACCOUNT DETAILS
# ==================================================

elif menu == "Account Details":

    st.subheader("Account Details")

    st.caption("Enter your credentials to view your account.")

    with st.form("details_form"):

        account_number = st.text_input(
            "Account Number", placeholder="Enter account number"
        )

        pin = st.text_input(
            "PIN", type="password", max_chars=4, placeholder="Enter PIN"
        )

        submit = st.form_submit_button("View Account")

    if submit:

        success, message, user = Bank.get_details(account_number, pin)

        if success:

            st.markdown(
                f"""
                <div class="balance-card">

                    <div class="balance-label">
                        Available Balance
                    </div>

                    <div class="balance-value">
                        Rs. {user["balance"]:,.0f}
                    </div>

                    <div class="balance-account">
                        Account {user["accountNo"]}
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

            col1, col2 = st.columns(2)

            with col1:

                st.markdown(
                    f"""
                    <div class="info-card">

                        <div class="info-label">
                            Account Holder
                        </div>

                        <div class="info-value">
                            {user["name"]}
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            with col2:

                st.markdown(
                    f"""
                    <div class="info-card">

                        <div class="info-label">
                            Email Address
                        </div>

                        <div class="info-value">
                            {user["email"]}
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            st.write("")

            col3, col4 = st.columns(2)

            with col3:

                st.markdown(
                    f"""
                    <div class="info-card">

                        <div class="info-label">
                            Account Number
                        </div>

                        <div class="info-value">
                            {user["accountNo"]}
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            with col4:

                st.markdown(
                    f"""
                    <div class="info-card">

                        <div class="info-label">
                            Age
                        </div>

                        <div class="info-value">
                            {user["age"]}
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        else:

            st.error(message)


# ==================================================
# UPDATE ACCOUNT
# ==================================================

elif menu == "Update Account":

    st.subheader("Update Account")

    st.caption(
        "Update your name, email address or PIN. "
        "Leave fields empty if you do not want to change them."
    )

    with st.form("update_account_form"):

        account_number = st.text_input(
            "Account Number", placeholder="Enter account number"
        )

        current_pin = st.text_input(
            "Current PIN", type="password", max_chars=4, placeholder="Enter current PIN"
        )

        st.divider()

        new_name = st.text_input(
            "New Name", placeholder="Leave empty to keep current name"
        )

        new_email = st.text_input(
            "New Email", placeholder="Leave empty to keep current email"
        )

        new_pin = st.text_input(
            "New PIN",
            type="password",
            max_chars=4,
            placeholder="Leave empty to keep current PIN",
        )

        submit = st.form_submit_button("Update Account")

        if submit:

            success, message = Bank.update_account(
                account_number,
                current_pin,
                new_name or None,
                new_email or None,
                new_pin or None,
            )

            if success:
                st.success(message)

            else:
                st.error(message)


# ==================================================
# DELETE ACCOUNT
# ==================================================

elif menu == "Delete Account":

    st.subheader("Delete Account")

    st.warning("Deleting an account is permanent and cannot be undone.")

    with st.form("delete_account_form"):

        account_number = st.text_input(
            "Account Number", placeholder="Enter account number"
        )

        pin = st.text_input(
            "PIN", type="password", max_chars=4, placeholder="Enter PIN"
        )

        confirm = st.checkbox(
            "I understand that this account will be permanently deleted."
        )

        submit = st.form_submit_button("Delete Account")

        if submit:

            if not confirm:

                st.error("Please confirm that you want to delete the account.")

            else:

                success, message = Bank.delete_account(account_number, pin)

                if success:
                    st.success(message)

                else:
                    st.error(message)
