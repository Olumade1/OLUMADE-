import streamlit as st
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
def main_page():
    st.image("edu.png", width=100)
    st.markdown("# Educonnect Schools 🎈")

    # Hero section HTML and CSS
    hero_section = '''
        <style>
            .hero-container {
                background-image: url('images.jpg');  /* Replace with your image URL */
                background-size: cover;
                background-position: center;
                color: #ffffff;
                text-align: center;
                padding: 100px 0;
            }

            .hero-text {
                font-size: 36px;
                font-weight: bold;
            }

            .hero-subtext {
                font-size: 24px;
                margin-top: 20px;
            }
        </style>
        <div class="hero-container">
            <div class="hero-text">Welcome to Our School</div>
            <div class="hero-subtext">Where Excellence Meets Education</div>
        </div>
    '''

    about_us_section = '''
        <style>
            .about-section {
                background-color: #f0f0f0;
                padding: 40px;
                text-align: center;
            }
            
            .about-heading {
                font-size: 24px;
                color: #0077b6;
            }

            .about-description {
                font-size: 16px;
                color: #333333;
                margin-top: 20px;
            }
        </style>
        <div class="about-section">
            <h2 class="about-heading">About Us</h2>
            <p class="about-description">Welcome to Educonnect, your trusted educational platform for seamless communication and collaboration between teachers, students, and parents. At Educonnect, we are dedicated to transforming education through technology. Our mission is to create a vibrant and connected learning ecosystem that empowers educators, engages students, and supports parents in their educational journey.</p>
            </div>

    '''
    upcoming_events_section = '''
        <style>
            /* Style for the Upcoming Events section */
            .events-section {
                background-color: #ffffff;
                padding: 40px;
                text-align: center;
            }

            .events-heading {
                font-size: 24px;
                color: #0077b6;
            }

            .event {
                font-size: 16px;
                color: #333333;
                margin-top: 20px;
            }
        </style>
        <div class="events-section">
            <h2 class="events-heading">Upcoming Events</h2>
            <div class="event">
                <h3>Event 1</h3>
                <p>Date: January 15, 2023</p>
                <p>Description:Spelling Bee</p>
            </div>
            <div class="event">
                <h3>Event 2</h3>
                <p>Date: February 20, 2023</p>
                <p>Description: Quizes on Current Affairs</p>
            </div>
        </div>
    '''
    admissions_section = '''
        <style>
            /* Style for the Admissions section */
            .admissions-section {
                background-color: #f0f0f0;
                padding: 40px;
                text-align: center;
            }

            .admissions-heading {
                font-size: 24px;
                color: #0077b6;
            }

            .admissions-description {
                font-size: 16px;
                color: #333333;
            margin-top: 20px;
            }
        </style>
        <div class="admissions-section">
            <h2 class="admissions-heading">Admissions</h2>
            <p class="admissions-description">Admissions Now Open!</p>
            <p>We are excited to announce that admissions for the upcoming academic year at [Your School Name] are now open.</p>
            <p>This is your opportunity to join our dynamic and innovative learning community.</p>
            <p>Why Choose [Your School Name]?</p> 
            <p>Excellence in Education: At [Your School Name], we are committed to providing top-quality education that nurtures intellectual curiosity and personal growth.<p/>
            <p>Diverse Learning Environment: Join a diverse student body and experience a rich tapestry of cultures, ideas, and perspectives.</p>
            <p>If you have any questions or need assistance during the admissions process, please don't hesitate to contact our admissions team. We are here to help you make the transition to [Your School Name] as smooth as possible. Thank you for considering [Your School Name] for your educational journey. We look forward to welcoming you into our vibrant learning community.</p>
            <h2>Important Dates:</h2>
            Application Deadline: [Insert Deadline]
            Interview Period: [Insert Dates]
            Acceptance Notifications: [Insert Date]
            Don't miss your chance to become a part of the [Your School Name] family. Start your journey towards academic excellence with us!</p>
        </div>
    '''
    contact_info_section = '''
        <style>
            /* Style for the Contact Info section */
            .contact-section {
                background-color: #ffffff;
                padding: 40px;
                text-align: center;
            }

            .contact-heading {
                font-size: 24px;
                color: #0077b6;
            }

            .contact-info {
                font-size: 16px;
                color: #333333;
                margin-top: 20px;
            }
        </style>
        <div class="contact-section">
            <h2 class="contact-heading">Contact Info</h2>
            <div class="contact-info">
                <p>Address: 123 Main Street, City, Country</p>
                <p>Email: info@example.com</p>
                <p>Phone: +(123) 456-7890</p>
            </div>
        </div>
    '''
    call_to_action_section = '''
        <style>
            /* Style for the Call to Action section */
            .cta-section {
                background-color: #f0f0f0;
                padding: 40px;
                text-align: center;
            }

            .cta-heading {
                font-size: 24px;
                color: #0077b6;
            }

            .cta-button {
                font-size: 18px;
                background-color: #000000;
                color: #ffffff;
                border: none;
                padding: 10px 20px;
                margin-top: 20px;
                cursor: pointer;
            }

            .cta-button:hover {
                background-color: #005b96;
            }
        </style>
        <div class="cta-section">
            <h2 class="cta-heading">Apply for Admission</h2>
            <p class="cta-description">Ready to join our school? Click the button below to apply for admission.</p>
            <a href="mailto:educonnect@gmail.com?subject=Admission%20Application" <button class="cta-button">Apply Now</button></a>
        </div>
    '''


    # Display all section
    st.markdown(hero_section, unsafe_allow_html=True)
    st.markdown(about_us_section, unsafe_allow_html=True)
    st.markdown(upcoming_events_section, unsafe_allow_html=True)
    st.markdown(admissions_section, unsafe_allow_html=True)
    st.markdown(contact_info_section, unsafe_allow_html=True)
    st.markdown(call_to_action_section, unsafe_allow_html=True)


def Student_portal():
    import streamlit as st
    import pandas as pd
    from tabulate import tabulate
    import matplotlib.pyplot as plt
    import altair as alt
    from streamlit_option_menu import option_menu
    import plotly.express as px


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

    # Function to get the grade based on marks
    def get_grade(mark):
        grading_scale = {
            (70, 100): 'A',
            (60, 69): 'B',
            (50, 59): 'C',
            (40, 49): 'D',
            (0, 39): 'F'
        }
        for (lower, upper), grade in grading_scale.items():
            if lower <= mark <= upper:
                return grade
        return 'N/A'  # Return 'N/A' for marks out of the specified range

    # Function to calculate percentage based on total marks and a fixed total
    def calculate_percentage(total_marks, fixed_total=700):
        percentage = (total_marks / fixed_total) * 100
        return percentage
    # View Results page
    def view_results(student_id, students_data):
        df = pd.read_excel("Streamlit_Data.xlsx",
                           dtype={"id": str, "password": str, "chat_history": str})

        # Convert 'results' column to dictionaries
        df['first_term_results'] = df['first_term_results'].apply(lambda x: eval(x) if isinstance(x, str) else x)
        df['second_term_results'] = df['second_term_results'].apply(lambda x: eval(x) if isinstance(x, str) else x)
        df['third_term_results'] = df['third_term_results'].apply(lambda x: eval(x) if isinstance(x, str) else x)

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
                term_units = None
                term_credits = None
                term_comments = None
                term_position = None
                term_remarks = None

            # Display results table
            if term_results:
                st.subheader(f"{selected_term} Results")
                results_data = []
                total_marks = 0  # Initialize total marks

                for subject, mark in term_results.items():
                    results_data.append([subject, mark, get_grade(mark)])
                    total_marks += mark  # Update total marks

                results_df = pd.DataFrame(results_data, columns=["Subject", "Marks", "Grade"])

                # Apply style to the result table
                st.table(results_df.style
                    .set_properties(
                    **{'background-color': '#f5f5f5', 'color': 'black', 'border-collapse': 'collapse',
                       'border': '1px solid gray'})
                    .set_table_styles(
                    [{'selector': 'th', 'props': [('background-color', '#000000'), ('color', 'white')]}]))

                # Calculate the percentage based on the total marks and a fixed total of 700
                percentage = calculate_percentage(total_marks, fixed_total=700)

                # Display the calculated percentage
                st.write(f"**Percentage for {selected_term}:** {percentage:.2f}%")

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
        # st.header("Profile")

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
            **{'background-color': '#f5f5f5', 'color': 'black', 'border-collapse': 'collapse',
               'border': '1px solid gray'})
                 .set_table_styles(
            [{'selector': 'th', 'props': [('background-color', '#000000'), ('color', 'white')]}]))

        st.write("")

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

        # LOG IN PAGE\
        # Check if the 'page' query parameter is set to 'student_login'
        if "page" in st.experimental_get_query_params() and st.experimental_get_query_params()[
            "page"] == "Student_login":
            # Display the student login page
            st.title("Student Login")
        # Login section
        if not session_state["user_authenticated"]:
            col1, col2, col3 = st.columns([1, 2, 1])
            # Center the logo image in the middle colimn
            with col2:
                st.image("edu.png", width=100)
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
                options=["Profile", "View Results", "Check Balance", "Course Materials", "Time Table",
                         "Track Progress", "Logout", ],
                icons=["person-lines-fill", "journal", "cash", "book", "table", "bar-chart-fill", "box-arrow-right"],
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


def Teacher_portal():
    import streamlit as st
    import pandas as pd
    from tabulate import tabulate
    import matplotlib.pyplot as plt
    import altair as alt
    from streamlit_option_menu import option_menu
    import plotly.express as px
    # Load teachers data from Excel
    def load_teacher_data():
        df = pd.read_excel("Streamlit_Data.xlsx", sheet_name="Teacher data", dtype={"id": str, "password": str})
        return df.to_dict(orient="records")

    def load_students_data():
        df = pd.read_excel("Streamlit_Data.xlsx", dtype={"id": str, "password": str, "chat_history": str})

        # Convert 'results' column to dictionaries
        df['first_term_results'] = df['first_term_results'].apply(lambda x: eval(x) if isinstance(x, str) else x)
        df['second_term_results'] = df['second_term_results'].apply(lambda x: eval(x) if isinstance(x, str) else x)
        df['third_term_results'] = df['third_term_results'].apply(lambda x: eval(x) if isinstance(x, str) else x)
        return df.to_dict(orient="records")

    # User authentication
    def authenticate(username, password, teacher_data):
        for teacher in teacher_data:
            if teacher['id'] == username and teacher['password'] == password:
                print(f"Authentication successful for user: {username}")
                return True
            print(f"Authentication failed for user: {username}")
            return False

    # Get teacher by ID
    def get_teacher_by_id(teacher_id, teacher_data):
        for teacher in teacher_data:
            if teacher['id'] == teacher_id:
                return teacher
        return None

    def get_student_by_id(student_id, students_data):
        for student in students_data:
            if student['id'] == student_id:
                return student
        return None

        # Load the Excel data
        data = load_excel_data()
        # Display and edit the data, and send via email
        edit_and_send_data(data)

    # Profile page
    def profile(teacher_id, teacher_data):
        # st.header("Profile")

        # Teacher selection
        teacher = get_teacher_by_id(teacher_id, teacher_data)
        st.markdown(
            '<div style="border: 1px solid #191919; padding: 20px; border-radius: 10px; background-color: #f5f5f5;">'
            '<h3 style="color: #333333;">Profile</h3>'
            '</div>',
            unsafe_allow_html=True
        )

        # Display profile
        if teacher:
            st.subheader(f"Profile for {teacher['name']}")
            # Display the teacher image with a specified width (e.g., 150 pixels)
            st.image(teacher['image'], use_column_width=False, width=200)
            # Display profile information in a stylized table
            st.markdown(
                f"""
                            <div style="border: 1px solid #191919; padding: 20px; border-radius: 10px; background-color: #f5f5f5;">
                                <table>
                                    <tr>
                                    </tr>
                                    <tr>
                                        <td><strong>Name:</strong></td>
                                        <td>{teacher['name']}</td>
                                    </tr>
                                    <tr>
                                        <td><strong>ID:</strong></td>
                                        <td>{teacher['id']}</td>
                                    </tr>
                                    <tr>
                                        <td><strong>Email:</strong></td>
                                        <td>{teacher['email']}</td>
                                    </tr>
                                    <tr>
                                        <td><strong>Class Incharge:</strong></td>
                                        <td>{teacher['class incharge']}</td>
                                    </tr>
                                    <tr>
                                        <td><strong>Date of Birth:</strong></td>
                                        <td>{teacher['date of birth']}</td>
                                    </tr>
                                </table>
                            </div>
                            """,
                unsafe_allow_html=True,
            )



        else:
            st.warning("Teacher not found.")

    # Course Materials
    # Load course materials data from Excel
    def load_course_materials_data():
        df = pd.read_excel("Streamlit_Data.xlsx", sheet_name="Course Materials")
        return df.to_dict(orient="records")
        # Course Materials page

    def view_course_materials(teacher_id, teacher_data):
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
            **{'background-color': '#f5f5f5', 'color': 'black', 'border-collapse': 'collapse',
               'border': '1px solid gray'})
            .set_table_styles(
            [{'selector': 'th', 'props': [('background-color', '#000000'), ('color', 'white')]}]))

        st.write("")

        # Teacher access to student results

    def teacher_access_student_results(teacher_id, teacher_data, students_data):
        st.subheader("Access Student Results")

        # Input field for student ID
        student_id = st.text_input("Enter Student ID:")

        # Button to retrieve results
        if st.button("Retrieve Results"):
            # Call the get_student_results function to retrieve results
            student_results = get_student_by_id(student_id, students_data)

            if student_results:
                student_results.pop('password', None)
                student_df = pd.DataFrame([student_results])
                st.table(student_df.style
                    .set_properties(
                    **{'background-color': '#f5f5f5', 'color': 'black', 'border-collapse': 'collapse',
                       'border': '1px solid gray'})
                    .set_table_styles(
                    [{'selector': 'th', 'props': [('background-color', '#000000'), ('color', 'white')]}]))
                st.write()
                # st.success(f"Results for Student ID {student_id}:")
                # st.write(student_results)
            else:
                st.warning("Student ID not found or no results available.")

    def load_excel_data():
        data = pd.read_excel("Streamlit_Data.xlsx")
        # Drop the 'Password' column
        data_without_password = data.drop(columns=['password'])
        return data_without_password
        # Display and edit the data, and send via email
        edit_and_send_data(data)

    def edit_and_send_data(data):
        st.header("Students Data")

        st.markdown(
            '<div style="border: 1px solid #191919; padding: 20px; border-radius: 10px; background-color: #f5f5f5;">'
            '<h3 style="color: #333333;">Edit Data and Send via Email''</h3>'
            '</div>',
            unsafe_allow_html=True
        )
        st.subheader("Preview of Data")
        st.table(data.style
            .set_properties(
            **{'background-color': '#f5f5f5', 'color': 'black', 'border-collapse': 'collapse',
               'border': '1px solid gray'})
            .set_table_styles(
            [{'selector': 'th', 'props': [('background-color', '#000000'), ('color', 'white')]}]))
        st.write()
        call_to_action_section = '''
            <style>
                /* Style for the Call to Action section */

                .cta-heading {
                    font-size: 24px;
                    color: #0077b6;
                }

                .cta-button {
                    font-size: 18px;
                    background-color: #000000;
                    color: #ffffff;
                    border: none;
                    padding: 10px 20px;
                    margin-top: 20px;
                    cursor: pointer;
                }

                .cta-button:hover {
                    background-color: #005b96;
                }
            </style>
            <div class="cta-section">
                <h2 class="cta-heading"></h2>
                <p class=</p>
                <a href="mailto:educonnect@gmail.com?subject=Result%20Update" <button class="cta-button">Send Now</button></a>
            </div>
        '''
        st.markdown(call_to_action_section, unsafe_allow_html=True)
        st.markdown(
            '<div style="border: 1px solid #000000; padding: 10px; border-radius: 5px; background-color: #f5f5f5;">'
            '<p style="color: #333333;">Note: These are the students data. Copy the Student Results column, edit and send using the button above.</p>'
            '</div>',
            unsafe_allow_html=True
        )

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

        # Load the Excel data

        # Load teacher data
        teacher_data = load_teacher_data()
        timetable_data = load_timetable_data()
        # Load the Excel data
        data = load_excel_data()

        # Load student data
        students_data = load_students_data()

        # Initialize session state
        session_state = st.session_state.setdefault("session_state", {"user_authenticated": False})

        # LOG IN PAGE\
        # Check if the 'page' query parameter is set to 'teacher_login'
        if "page" in st.experimental_get_query_params() and st.experimental_get_query_params()[
            "page"] == "Teacher_login":
            # Display the teacher login page
            st.title("Teacher Login")
        # Login section
        if not session_state["user_authenticated"]:
            col1, col2, col3 = st.columns([1, 2, 1])
            # Center the logo image in the middle colimn
            with col2:
                st.image("edu.png", width=100)
                st.subheader("Login")
                username = st.text_input("Username")
                password = st.text_input("Password", type="password")
                if st.button("Login"):
                    if authenticate(username, password, teacher_data):
                        session_state["user_authenticated"] = True
                        session_state["teacher_id"] = username

                        st.success("Login successful.")
                    else:
                        st.warning("Invalid credentials.")
        else:
            teacher_id = session_state["teacher_id"]
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
            #
            selected = option_menu(
                menu_title=None,
                options=["Profile", "View Students Information", "Course Materials", "Time Table",
                         "Edit and Send", "Logout", ],
                icons=["person-lines-fill", "journal", "book", "table", "pencil-square", "box-arrow-right"],
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
                profile(teacher_id, teacher_data)
            elif selected == "Course Materials":
                view_course_materials(teacher_id, teacher_data)
            elif selected == "Time Table":
                view_timetable(timetable_data)
            elif selected == "View Students Information":
                teacher_access_student_results(teacher_id, teacher_data, students_data)
            elif selected == "Edit and Send":
                edit_and_send_data(data)
            elif selected == "Logout":
                logout(session_state)

                pass

    if __name__ == "__main__":
        main()

def Admin_portal():
    import streamlit as st
    import pandas as pd
    import webbrowser
    from PIL import Image
    import base64
    from io import BytesIO
    from streamlit_option_menu import option_menu
    import os

    # Function to load the Admin Data
    def load_admin_data():
        df = pd.read_excel("Streamlit_Data.xlsx", sheet_name="Admin Data", dtype={"id": str, "password": str})
        return df.to_dict(orient="records")

    # User authentication
    def authenticate(username, password, admin_data):
        for teacher in admin_data:
            if teacher['id'] == username and teacher['password'] == password:
                print(f"Authentication successful for user: {username}")
                return True
        print(f"Authentication failed for user: {username}")
        return False

    def get_admin_by_id(admin_id, admin_data):
        for admin in admin_data:
            if admin['id'] == admin_id:
                return admin

    # Define a function to load student data from an Excel file
    def load_student_data():
        # Load the student data from an Excel file (you can replace this with your own data source)
        df = pd.read_excel("Streamlit_Data.xlsx")
        return df

    # Define a function to display the student records in a table
    def view_student_records(student_data):
        st.subheader("Student Records")
        st.write(student_data)

    # Define a function to add a new student record
    def add_student_record(student_data):
        st.subheader("Add a New Student Record")

        # Input fields for student information
        student_id = st.text_input("Student ID")
        student_name = st.text_input("Student Name")
        student_class = st.text_input("Student Class")
        student_age = st.text_input("Student Age")
        student_guardian = st.text_input("Guardian")
        student_contact = st.text_input("Guardian Contact")
        uploaded_image = st.file_uploader("Upload Student Image", type=["jpg", "png", "jpeg"])

        if st.button("Add Record"):
            # Check if required fields are not empty
            if not student_id or not student_name:
                st.error("Student ID and Name are required.")
                return

            # Save the uploaded image locally
            img_path = None
            if uploaded_image:
                img_path = os.path.join("student_images", f"{student_id}.jpg")
                with open(img_path, "wb") as f:
                    f.write(uploaded_image.read())

            # Add the new record to the DataFrame
            new_record = pd.DataFrame({
                "Student ID": [student_id],
                "Student Name": [student_name],
                "Student Class": [student_class],
                "Student Age": [student_age],
                "Guardian": [student_guardian],
                "Guradian Contact": [student_contact],
                "Image Path": [img_path]
            })
            student_data = student_data.append(new_record, ignore_index=True)
            st.success("Record added successfully!")

            # Clear input fields
            st.text_input("Student ID", value="")
            st.text_input("Student Name", value="")
            st.text_input("Student Class", value="")
            st.text_input("Student Age", value="")
            st.text_input("Guardian", value="")
            st.text_input("Guardian Contact", value="")

            # Open the default email client with the student records
            email_subject = "New Student Record Added"
            email_body = f"Student ID: {student_id}\nStudent Name: {student_name}\nStudent Class: {student_class}\nStudent Age: {student_age}\nGuardian: {student_guardian}\nGuardian Contact: {student_contact}"

            if img_path:
                email_body += f"\n\n<img src='{img_path}' alt='Student Image'>"

            email_url = f"mailto:?subject={email_subject}&body={email_body}"
            webbrowser.open(email_url)

        return student_data

    # Define a function to log out the user
    def logout(session_state):
        session_state["user_authenticated"] = False
        st.experimental_rerun()  # Rerun the Streamlit app to reset the state

    # Define the main function for the admin portal
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

        # Load student data
        student_data = load_student_data()
        # Create the 'student_images' directory if it doesn't exist
        os.makedirs("student_images", exist_ok=True)
        admin_data = load_admin_data()

        # Initialize session state
        session_state = st.session_state.setdefault("session_state", {"user_authenticated": False})

        # LOG IN PAGE
        # Check if the 'page' query parameter is set to 'teacher_login'
        if "page" in st.experimental_get_query_params() and st.experimental_get_query_params()["page"] == "Admin_login":
            # Display the teacher login page
            st.title("Admin Login")

        # Login section
        if not session_state["user_authenticated"]:
            col1, col2, col3 = st.columns([1, 2, 1])
            # Center the logo image in the middle column
            with col2:
                st.image("edu.png", width=100)
                st.subheader("Login")
                username = st.text_input("Username")
                password = st.text_input("Password", type="password")
                if st.button("Login"):
                    if authenticate(username, password, student_data):
                        session_state["user_authenticated"] = True
                        session_state["admin_id"] = username
                        st.success("Login successful.")
                    else:
                        st.warning("Invalid credentials")
        else:
            admin_id = session_state["admin_id"]

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
            selected = option_menu(
                menu_title=None,
                options=["View Student Records", "Add Student Record", "Logout", ],
                icons=["journal", "person-lines-fill", "box-arrow-right"],
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

            # Display selected menu option
            if selected == "View Student Records":
                view_student_records(student_data)
            elif selected == "Add Student Record":
                student_data = add_student_record(student_data)
            elif selected == "Logout":
                logout(session_state)

    # Run the admin portal
    if __name__ == "__main__":
        main()

page_names_to_funcs = {
    "Main Page": main_page,
    "Student Portal": Student_portal,
    "Teacher Portal": Teacher_portal,
    "Admin Portal": Admin_portal,
}
selected_page =st.selectbox("", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()

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


