import streamlit as st
from bank import Bank

# ----------------------------------------
# Page configuration
# ----------------------------------------
st.set_page_config(
    page_title="Modern Bank",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ----------------------------------------
# Custom CSS
# ----------------------------------------
st.markdown(
    """
    <style>

    .stApp {
        background-color: #f8fafc;
    }

    .main .block-container {
        max-width: 900px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    h1 {
        font-weight: 700;
        letter-spacing: -1px;
    }

    h2, h3 {
        font-weight: 600;
    }

    .bank-card {
        background: rgb(14, 17, 23);
        border: 1px solid #e5e7eb;
        border-radius: 16px;
        padding: 25px;
        margin-top: 20px;
        margin-bottom: 20px;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.04);
    }

    .balance-card {
        background: #111827;
        color: white;
        border-radius: 18px;
        padding: 28px;
        margin-top: 20px;
        margin-bottom: 25px;
    }
    
    .stMainBlockContainer{
        background: rgb(14, 17, 23);
    }

    .balance-title {
        font-size: 14px;
        opacity: 0.7;
    }

    .balance-amount {
        font-size: 34px;
        font-weight: 700;
        margin-top: 5px;
    }

    div[data-testid="stMetric"] {
        background: rgb(14, 17, 23);
        border: 1px solid #e5e7eb;
        padding: 20px;
        border-radius: 14px;
    }

    div.stButton > button {
        border-radius: 10px;
        height: 45px;
        font-weight: 600;
        width: 100%;
    }

    div[data-testid="stTextInput"] input,
    div[data-testid="stNumberInput"] input {
        border-radius: 10px;
    }

    section[data-testid="stSidebar"] {
        background-color: rgb(14, 17, 23);
        border-right: 1px solid #e5e7eb;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ----------------------------------------
# Header
# ----------------------------------------
st.title("🏦 Modern Bank")

st.caption("Simple banking management system built with Python, OOP and Streamlit.")

st.divider()


# ----------------------------------------
# Sidebar menu
# ----------------------------------------
st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "Select an operation",
    [
        "Dashboard",
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "Account Details",
        "Update Account",
        "Delete Account",
    ],
)

st.sidebar.divider()

st.sidebar.caption("Python Bank Management System")


# ========================================
# DASHBOARD
# ========================================

if menu == "Dashboard":

    st.subheader("Dashboard")

    total_users = len(Bank.data)

    total_balance = sum(user["balance"] for user in Bank.data)

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Total Accounts",
            total_users,
        )

    with col2:
        st.metric(
            "Total Bank Balance",
            f"Rs. {total_balance:,}",
        )

    st.markdown("### Welcome")

    st.write("""
        Use the navigation menu to create accounts,
        deposit money, withdraw money, update account
        information or view account details.
        """)


# ========================================
# CREATE ACCOUNT
# ========================================

elif menu == "Create Account":

    st.subheader("Create Account")

    st.write("Enter your information below to create a new bank account.")

    with st.form("create_account_form"):

        name = st.text_input(
            "Full Name",
            placeholder="Enter your full name",
        )

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            step=1,
        )

        email = st.text_input(
            "Email",
            placeholder="example@email.com",
        )

        pin = st.text_input(
            "4 Digit PIN",
            type="password",
            max_chars=4,
            placeholder="****",
        )

        submit = st.form_submit_button("Create Account")

        if submit:

            success, message, account_number = Bank.create_account(
                name,
                age,
                email,
                pin,
            )

            if success:

                st.success(message)

                st.info(f"Your account number is: **{account_number}**")

                st.warning("Please save your account number somewhere safe.")

            else:
                st.error(message)


# ========================================
# DEPOSIT
# ========================================

elif menu == "Deposit Money":

    st.subheader("Deposit Money")

    with st.form("deposit_form"):

        account_number = st.text_input(
            "Account Number",
            placeholder="Enter account number",
        )

        pin = st.text_input(
            "PIN",
            type="password",
            max_chars=4,
        )

        amount = st.number_input(
            "Deposit Amount",
            min_value=0,
            step=100,
        )

        submit = st.form_submit_button("Deposit Money")

        if submit:

            success, message = Bank.deposit(
                account_number,
                pin,
                amount,
            )

            if success:
                st.success(message)

            else:
                st.error(message)


# ========================================
# WITHDRAW
# ========================================

elif menu == "Withdraw Money":

    st.subheader("Withdraw Money")

    with st.form("withdraw_form"):

        account_number = st.text_input("Account Number")

        pin = st.text_input(
            "PIN",
            type="password",
            max_chars=4,
        )

        amount = st.number_input(
            "Withdrawal Amount",
            min_value=0,
            step=100,
        )

        submit = st.form_submit_button("Withdraw Money")

        if submit:

            success, message = Bank.withdraw(
                account_number,
                pin,
                amount,
            )

            if success:
                st.success(message)

            else:
                st.error(message)


# ========================================
# ACCOUNT DETAILS
# ========================================

elif menu == "Account Details":

    st.subheader("Account Details")

    with st.form("details_form"):

        account_number = st.text_input("Account Number")

        pin = st.text_input(
            "PIN",
            type="password",
            max_chars=4,
        )

        submit = st.form_submit_button("View Account")

    if submit:

        success, message, user = Bank.get_details(
            account_number,
            pin,
        )

        if success:

            st.success("Account verified successfully.")

            st.markdown(
                f"""
                <div class="balance-card">

                    <div class="balance-title">
                    AVAILABLE BALANCE
                    </div>

                    <div class="balance-amount">
                    Rs. {user["balance"]:,}
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

            col1, col2 = st.columns(2)

            with col1:

                st.write("**Account Holder**")

                st.write(user["name"])

                st.write("**Email**")

                st.write(user["email"])

            with col2:

                st.write("**Account Number**")

                st.write(user["accountNo"])

                st.write("**Age**")

                st.write(user["age"])

        else:

            st.error(message)


# ========================================
# UPDATE ACCOUNT
# ========================================

elif menu == "Update Account":

    st.subheader("Update Account")

    st.caption("You can change your name, email and PIN.")

    with st.form("update_form"):

        account_number = st.text_input("Account Number")

        current_pin = st.text_input(
            "Current PIN",
            type="password",
            max_chars=4,
        )

        st.divider()

        new_name = st.text_input(
            "New Name",
            placeholder="Leave empty to keep current name",
        )

        new_email = st.text_input(
            "New Email",
            placeholder="Leave empty to keep current email",
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


# ========================================
# DELETE ACCOUNT
# ========================================

elif menu == "Delete Account":

    st.subheader("Delete Account")

    st.warning("Deleting your account is permanent and cannot be undone.")

    with st.form("delete_form"):

        account_number = st.text_input("Account Number")

        pin = st.text_input(
            "PIN",
            type="password",
            max_chars=4,
        )

        confirm = st.checkbox(
            "I understand that my account will be permanently deleted."
        )

        submit = st.form_submit_button("Delete Account")

        if submit:

            if not confirm:

                st.error("Please confirm account deletion.")

            else:

                success, message = Bank.delete_account(
                    account_number,
                    pin,
                )

                if success:
                    st.success(message)

                else:
                    st.error(message)