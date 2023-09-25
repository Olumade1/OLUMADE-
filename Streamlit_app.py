import streamlit as st
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
import altair as alt
from streamlit_option_menu import option_menu
import plotly.express as px

# Set page config to wide layout
st.set_page_config(layout="wide")

# Add CSS for creating space at the bottom
st.markdown("""
    <style>
        /* Create space at the bottom for the footer */
        .stApp {
            margin-bottom: 130px; /* Adjust the margin to control the space */
        }
    </style>
""", unsafe_allow_html=True)


# Load students data from Excel
def load_students_data():
    df = pd.read_excel("Streamlit_Data.xlsx", dtype={"id": str, "password": str, "chat_history": str})

    # Convert 'results' column to dictionaries
    df['first_term_results'] = df['first_term_results'].apply(lambda x: eval(x) if isinstance(x, str) else x)
    df['second_term_results'] = df['second_term_results'].apply(lambda x: eval(x) if isinstance(x, str) else x)
    df['third_term_results'] = df['third_term_results'].apply(lambda x: eval(x) if isinstance(x, str) else x)
    return df.to_dict(orient="records")


# User authentication
def authenticate(username, password, students_data):
    for student in students_data:
        if student['id'] == username and student['password'] == password:
            print(f"Authentication successful for user: {username}")
            return True
    print(f"Authentication failed for user: {username}")
    return False


# Get student by ID
def get_student_by_id(student_id, students_data):
    for student in students_data:
        if student['id'] == student_id:
            return student
    return None


# View Results page
def view_results(student_id, students_data):
    student = get_student_by_id(student_id, students_data)
    st.markdown(
        '<div style="border: 1px solid #191919; padding: 20px; border-radius: 10px; background-color: #f5f5f5;">'
        '<h3 style="color: #333333;">View Results</h3>'
        '</div>',
        unsafe_allow_html=True
    )

    if student:
        st.subheader(f"Results for {student['name']}")

        # Dropdown for term selection
        selected_term = st.selectbox("Select a term", ["First Term", "Second Term", "Third Term"])

        # Display results based on selected term
        if selected_term == "First Term":
            term_results = student['first_term_results']
            term_comments = student['first_term_teacher_comments']
            term_position = student['first_term_position']
            term_remarks = student['remarks']
        elif selected_term == "Second Term":
            term_results = student['second_term_results']
            term_comments = student['second_term_teacher_comments']
            term_position = student['second_term_position']
            term_remarks = student['remarks']
        elif selected_term == "Third Term":
            term_results = student['third_term_results']
            term_comments = student['third_term_teacher_comments']
            term_position = student['third_term_position']
            term_remarks = student['remarks']
        else:
            term_results = None
            term_comments = None
            term_position = None
            term_remarks = None

        # Display results table
        if term_results:
            st.subheader(f"{selected_term} Results")
            results_df = pd.DataFrame({"Subject": list(term_results.keys()), "Marks": list(term_results.values())})
            # st.table(results_df)
            # Apply style to the result table
            st.table(results_df.style
                     .set_properties(**{'background-color': '#f5f5f5', 'color': 'black', 'border-collapse': 'collapse',
                                        'border': '1px solid gray'})
                     .set_table_styles(
                [{'selector': 'th', 'props': [('background-color', '#000000'), ('color', 'white')]}]))

            st.write("")
        else:
            st.warning(f"{selected_term} results not available.")

        # Display comments, position, and remarks
        table_data = []
        if term_comments:
            # st.subheader(f"{selected_term} Comments")
            table_data.append(f"{selected_term} Comments: {term_comments}")

        if term_position:
            # st.subheader(f"{selected_term} Position")
            table_data.append(f"{selected_term} Position: {term_position}")

        if term_remarks:
            # st.subheader(f"{selected_term} Remarks")
            table_data.append(f"{selected_term} Remarks: {term_remarks}")

            if table_data:
                st.subheader(f"{selected_term} Information")
                info_df = pd.DataFrame({"Information": table_data})
                st.table(info_df.style
                         .set_properties(
                    **{'background-color': '#f5f5f5', 'color': 'black', 'border-collapse': 'collapse',
                       'border': '1px solid gray'})
                         .set_table_styles(
                    [{'selector': 'th', 'props': [('background-color', '#000000'), ('color', 'white')]}]))

            st.markdown(
                '<div style="border: 1px solid #000000; padding: 10px; border-radius: 5px; background-color: #f5f5f5;">'
                '<p style="color: #333333;">Note: These are the results for the current term.</p>'
                '</div>',
                unsafe_allow_html=True
            )

    else:
        st.warning("Student not found.")


# Profile page
def profile(student_id, students_data):

    # Student selection
    student = get_student_by_id(student_id, students_data)
    st.markdown(
        '<div style="border: 1px solid #191919; padding: 20px; border-radius: 10px; background-color: #f5f5f5;">'
        '<h3 style="color: #333333;">Profile</h3>'
        '</div>',
        unsafe_allow_html=True
    )

    # Display profile
    if student:
        st.subheader(f"Profile for {student['name']}")
        # Display the student image with a specified width (e.g., 150 pixels)
        st.image(student['image'], use_column_width=False, width=200)
        # Display profile information in a stylized table
        st.markdown(
            f"""
                        <div style="border: 1px solid #191919; padding: 20px; border-radius: 10px; background-color: #f5f5f5;">
                            <table>
                                <tr>
                                </tr>
                                <tr>
                                    <td><strong>Name:</strong></td>
                                    <td>{student['name']}</td>
                                </tr>
                                <tr>
                                    <td><strong>ID:</strong></td>
                                    <td>{student['id']}</td>
                                </tr>
                                <tr>
                                    <td><strong>Email:</strong></td>
                                    <td>{student['email']}</td>
                                </tr>
                                <tr>
                                    <td><strong>Class:</strong></td>
                                    <td>{student['class']}</td>
                                </tr>
                                <tr>
                                    <td><strong>Guardian Contact:</strong></td>
                                    <td>{student['guardian_contacts']}</td>
                                </tr>
                                <tr>
                                    <td><strong>Date of Birth:</strong></td>
                                    <td>{student['date_of_birth']}</td>
                                </tr>
                                <tr>
                                    <td><strong>Guardian's Name:</strong></td>
                                    <td>{student['guardian_name']}</td>
                                </tr>
                            </table>
                        </div>
                        """,
            unsafe_allow_html=True,
        )



    else:
        st.warning("Student not found.")


# Check Balance page
def check_balance(student_id, students_data):
    student = get_student_by_id(student_id, students_data)
    st.markdown(
        '<div style="border: 1px solid #191919; padding: 20px; border-radius: 10px; background-color: #f5f5f5;">'
        '<h3 style="color: #333333;">Available Balance</h3>'
        '</div>',
        unsafe_allow_html=True
    )

    # Display balance
    if student:
        st.subheader(f"Balance for {student['name']}")
        st.write(f"Balance: ${student['balance']}")
    else:
        st.warning("Student not found.")

    df = pd.read_excel("Streamlit_Data.xlsx", sheet_name="Announcements")
    return df.to_dict(orient="records")


# Announcements and News
def get_announcements():
    # Load your Excel file
    excel_file = "Streamlit_Data.xlsx"

    # Specify the sheet name where announcements are stored
    sheet_name = "Announcements"

    try:
        # Read the announcements data from the Excel sheet
        df = pd.read_excel(excel_file, sheet_name=sheet_name)
        return df
    except Exception as e:
        st.error(f"Error loading announcements: {e}")
        return None


# Course Materials
# Load course materials data from Excel
def load_course_materials_data():
    df = pd.read_excel("Streamlit_Data.xlsx", sheet_name="Course Materials")
    return df.to_dict(orient="records")


# ...

# Course Materials page
def view_course_materials(student_id, students_data):
    st.header("Course Materials")
    # Load course materials data
    course_materials_data = load_course_materials_data()
    st.markdown(
        '<div style="border: 1px solid #191919; padding: 20px; border-radius: 10px; background-color: #f5f5f5;">'
        '<h3 style="color: #333333;">Available Course Materials</h3>'
        '</div>',
        unsafe_allow_html=True
    )
    # Display course materials

    for course_material in course_materials_data:
        st.write(f"**{course_material['Course']}**")
        st.write(f"URL: [{course_material['URL']}]({course_material['URL']})")
        st.write("")  # Add an empty line for separation
    st.markdown(
        '<div style="border: 1px solid #191919; padding: 20px; border-radius: 10px; background-color: #f5f5f5;">'
        '<p style="color: #333333;">Note: Click on the material link to access it.</p>'
        '</div>',
        unsafe_allow_html=True
    )


# Timetable
# Load Timetable from its sheet
def load_timetable_data():
    timetable_df = pd.read_excel("Streamlit_Data.xlsx", sheet_name="Timetable", index_col=0)
    return timetable_df


# Timetable and Scheduling
def view_timetable(timetable_data):
    # Display personalized class schedule for students

    days = timetable_data.columns.tolist()
    timeslots = timetable_data.index.tolist()
    st.markdown(
        '<div style="border: 1px solid #191919; padding: 20px; border-radius: 10px; background-color: #f5f5f5;">'
        '<h3 style="color: #333333;">Time Table and Scheduling</h3>'
        '</div>',
        unsafe_allow_html=True
    )
    st.header("Here")
    st.table(timetable_data.style
             .set_properties(
        **{'background-color': '#f5f5f5', 'color': 'black', 'border-collapse': 'collapse', 'border': '1px solid gray'})
             .set_table_styles([{'selector': 'th', 'props': [('background-color', '#000000'), ('color', 'white')]}]))

    st.write("")


# Progress Tracking
def track_progress(student_id, students_data):
    st.markdown(
        '<div style="border: 1px solid #191919; padding: 20px; border-radius: 10px; background-color: #f5f5f5;">'
        '<h3 style="color: #333333;">Progress Tracking</h3>'
        '</div>',
        unsafe_allow_html=True
    )
    #

    # Allow students to track their academic progress
    # Replace 'YourFile.xlsx' with the path to your Excel file
    file_path = 'Streamlit_Data.xlsx'

    # Replace 'SheetName' with the name of the sheet you want to read
    sheet_name = 'Progress Tracking'

    # Read the data from the specified sheet
    df = pd.read_excel(file_path, sheet_name=sheet_name)

    # Selectbox for selecting a specific term
    selected_term = st.selectbox('Select Term:', ['First Term', 'Second Term', 'Third Term'])

    # Get unique student IDs
    student_ids = df['id'].unique()

    # Create a separate graph for each student
    for student_id in student_ids:
        student_data = df[df['id'] == student_id]

        # Determine the column name for the selected term
        if selected_term == 'First Term':
            term_column = 'first_term_result_score'
        elif selected_term == 'Second Term':
            term_column = 'second_term_result_score'
        elif selected_term == 'Third Term':
            term_column = 'third_term_result_score'

        # Create a bar chart to display subjects vs. scores for the student in the selected term
        fig = px.bar(student_data, x='Subject', y=term_column,
                     title=f'Subjects vs. Scores for {selected_term} (Student ID: {student_id})')

        # Customize the chart layout if needed
        fig.update_xaxes(title='Subject')
        fig.update_yaxes(title='Score')
        fig.update_traces(marker_color='black')  # Change bar color

        # Display the chart for the current student
        st.plotly_chart(fig)

    # You can add more content or text between the charts if needed
    st.write("Here's your Progress chart.")


# Footer
# Icon
st.markdown(
    '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">',
    unsafe_allow_html=True)
# Create a wide footer with contacts, social media links, and copyright information
st.markdown("""
    <style>
        footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #333;
            color: white;
            text-align: center;
            padding:0px 0;
        }
        footer a {
            color: white;
            text-decoration: none;
            margin: 0 0px;
        }
        .social-media {
            margin-top: 0px;
        }
        .social-media a {
            font-size: 24px;
            margin: 0 0px;
        }
                .contact-icon {
            font-size: 18px;
            margin: 0 10px;
            color: white;
            text-decoration: none;
        }

        .contact-icon i {
            margin-right: 5px;
        }
    </style>
    <footer>
        <div class="container">
            <div class="row">
                <div class="col-md-4">
                    <h4>Contact Us</h4>
                    <p>Email: <a href="mailto:Educonnect@gmail.com" class="contact-icon"><i class="far fa-envelope"></i> Educonnect@gmail.com</a>| Phone:<a href="tel:+2348154045941" class="contact-icon"><i class="fas fa-phone"></i> +(234) 8154045941</a>, <a href="tel:+2348154339094" class="contact-icon"><i class="fas fa-phone"></i> +(234) 8154339094</a> | Social Media: <a href="#"><i class="fab fa-linkedin"></i></a></p>
                </div>
                <div class="col-md-4">
                    &copy; 2023 EduConnect
                </div>
            </div>
        </div>
    </footer>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)


# Interactive Forums
def join_forum(student_id, students_data):
    st.header("Interactive Forums")
    # Create discussion forums for students to collaborate


# Personalized Recommendations
def get_recommendations(student_id, students_data):
    st.header("Personalized Recommendations")
    # Provide personalized recommendations based on interests and performance


# Language and Accessibility Options
def set_language(student_id, students_data):
    st.header("Language and Accessibility Options")
    # Allow users to select language and accessibility preferences


# Logout page
def logout(session_state):
    session_state["user_authenticated"] = False
    st.experimental_rerun()  # Rerun the Streamlit app to reset the state


# Main web app
def main():
    # Apply custom CSS to style the login page
    st.markdown(
        """
        <style>
        .login-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }
        .login-box {
            width: 300px;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #f9f9f9;
            box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    # Load students data
    students_data = load_students_data()
    timetable_data = load_timetable_data()
    # Initialize session state
    session_state = st.session_state.setdefault("session_state", {"user_authenticated": False})

    # LOG IN PAGE
    # Login section
    if not session_state["user_authenticated"]:
        col1, col2, col3 = st.columns([1, 2, 1])
        # Center the logo image in the middle colimn
        with col2:
            st.image("edu.jpeg", width=100)
            st.subheader("Login")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.button("Login"):
                if authenticate(username, password, students_data):
                    session_state["user_authenticated"] = True
                    session_state["student_id"] = username

                    st.success("Login successful.")
                else:
                    st.warning("Invalid credentials.")
    else:
        student_id = session_state["student_id"]
        # Page navigation
        st.markdown(
            """
            <style>
                /* Move the menu options to the top */
                div[data-testid="stHorizontalBlock"] {
                    display: flex;
                    justify-content: flex-start;
                    align-items: center;
                    padding: 10px 0;
                    background-color: #333;
                    color: white;
                }

                div[data-testid="stHorizontalBlock"] a {
                    color: white;
                    margin: 0 10px;
                    text-decoration: none;
                    font-weight: bold;
                }

                div[data-testid="stHorizontalBlock"] a:hover {
                    color: #FFA500; /* Change the color on hover */
                }
            </style>
            """,
            unsafe_allow_html=True
        )
        # with st.sidebar:
        selected = option_menu(
            menu_title=None,
            options=["Profile", "View Results", "Check Balance", "Announcements", "Course Materials", "Time Table",
                     "Track Progress", "Logout"],
            icons=["person-lines-fill", "journal", "cash", "megaphone-fill", "book", "table", "bar-chart-fill"],
            # Bootstrap icon
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background color": "white"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text align": "left",
                    "margin": "10px",
                    "--hover-color": "ffee",
                },
                "nav-link-selected": {"background-color": "green"},
            },
        )

        # Handle page selection
        if selected == "Profile":
            profile(student_id, students_data)
        if selected == "View Results":
            view_results(student_id, students_data)
        elif selected == "Check Balance":
            check_balance(student_id, students_data)
        elif selected == "Announcements":
            get_announcements()
        elif selected == "Course Materials":
            view_course_materials(student_id, students_data)
        elif selected == "Time Table":
            view_timetable(timetable_data)
        elif selected == "Track Progress":
            track_progress(student_id, students_data)
        elif selected == "Logout":
            logout(session_state)

            pass


if __name__ == "__main__":
    main()
