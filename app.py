import streamlit as st
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="2026 Celebration Wall", page_icon="🎆", layout="centered")

# --- DATABASE LOGIC (Local File) ---
DB_FILE = "names.txt"

def save_name(name):
    # This adds the name to the text file
    with open(DB_FILE, "a", encoding="utf-8") as f:
        f.write(name + "\n")

def get_names():
    # This reads all names from the file
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

# --- SIDEBAR (Your GitHub Advertisement) ---
with st.sidebar:
    st.title("🛠️ Developer Hub")
    st.markdown("### Built by Abhinav")
    st.info("I'm building interactive apps to celebrate 2026! Check out my source code below.")
    # REPLACE THE LINKS BELOW WITH YOUR ACTUAL GITHUB LINKS
    st.markdown("[⭐ Star this Project](https://github.com/)")
    st.markdown("[👤 Follow me on GitHub](https://github.com/)")
    st.divider()
    st.write("Tech Stack: Python & Streamlit")

# --- MAIN INTERFACE ---
st.markdown("""
    # 🥂 The Global Toast 2026
    ### *Where names become legends.*
    ---
""")

# Input Form
with st.form("wish_form", clear_on_submit=True):
    user_name = st.text_input("Enter your name to join the wall:", placeholder="e.g. Abhinav")
    submitted = st.form_submit_button("Send Wishes & Join the Wall ✨")

if submitted:
    if user_name:
        save_name(user_name)
        st.balloons()
        st.success(f"🎆 Happy New Year {user_name}!")
        # st.confetti() # Only works in some versions, balloons are safer!
    else:
        st.warning("Please enter a name first!")

# --- THE WALL OF FAME ---
st.divider()
st.header("👥 The Wall of Fame")

all_names = get_names()

if all_names:
    # Show the count
    st.subheader(f"Total Participants: {len(all_names)}")
    
    # Display names in a nice grid or list
    cols = st.columns(3) # Splits the names into 3 columns to look "dashing"
    for index, name in enumerate(reversed(all_names)): # Newest names first
        cols[index % 3].markdown(f"🎈 **{name}**")
else:
    st.write("The wall is empty. Be the first to leave your mark!")






    # --- ADMIN SECTION ---
st.sidebar.divider()
with st.sidebar.expander("Admin Settings"):
    password = st.text_input("Enter Admin Password", type="password")
    if password == "Abhinav@no.1": # real password
        st.write("Admin Access Granted")
        
        # Get the names
        current_names = get_names()
        
        # Select names to remove
        names_to_delete = st.multiselect("Select names to remove:", current_names)
        
        if st.button("Delete Selected Names"):
            # Filter the list
            updated_names = [n for n in current_names if n not in names_to_delete]
            
            # Overwrite the file
            with open(DB_FILE, "w", encoding="utf-8") as f:
                for n in updated_names:
                    f.write(n + "\n")
            
            st.success("Names removed! Refreshing...")
            st.rerun()