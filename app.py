import streamlit as st
import pickle
from time import sleep
from PIL import Image
import base64

# Function to Add Background Image
def add_background_image(image_file):
    with open(image_file, "rb") as file:
        base64_image = base64.b64encode(file.read()).decode()

    # Inject CSS for background image
    css_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{base64_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(css_style, unsafe_allow_html=True)

# Main Function

def main():
    add_background_image("crdt.jpg")  # Replace with the name/path of your image file

    st.sidebar.title(":blue[📌Navigation]")
    page=st.sidebar.radio('Go to',['🏠Home','🔍Prediction'])
    if page == '🏠Home':
        st.title(":blue[💳CreditCard Approval Prediction]")


        #st.markdown(
            #'Hey there......This app is built for the classification of water based on physicoChemical properties')
    elif page=='🔍Prediction':
        st.title(":blue[💳CreditCard Approval Prediction]")
        st.sidebar.info("Predict whether a credit card application will be approved or denied.")
        # # image = Image.open('Credit-cards.jpg')
        # st.image(image, width=500)

        gender = st.radio("Select Gender", ['👩Female', '👨Male'], key="gender")
        gend = 0 if gender == 'Female' else 1

        car_owner = st.radio("Do you own a car?", ['❌No', '✅Yes'], key="car_owner")
        car = 0 if car_owner == 'No' else 1

        property_owner = st.radio("🏠Do you own a property?", ['❌No', '✅Yes'], key="property_owner",
                                  help="Select whether you own a property (house, apartment, etc.).")
        property = 0 if property_owner == 'No' else 1

        children = st.number_input('Number of children:', min_value=0, max_value=10, value=0, key="children",
                                   help="Enter the total number of children in your family.")
        annual_income = st.number_input('Annual Income (in thousands):', min_value=0, max_value=1000000, value=25000,
                                        key="annual_income",
                                        help="Enter your annual income in thousands (e.g., 50 = 50,000).")

        type_income = ['Commercial associate', 'Pensioner', 'State servant', 'Student', 'Working']
        type_inc = st.selectbox("Income Type:", type_income, key="type_income",
                                help="Select your primary source of income")
        inc_type = type_income.index(type_inc)

        education = ['Academic degree', 'Higher education', 'Incomplete higher', 'Lower secondary',
                     'Secondary / secondary special']
        educa = st.selectbox("Education Level:", education, key="education",
                             help="Select the highest level of education you have completed.")
        edu = education.index(educa)

        marital_status = ['Civil marriage', 'Married', 'Separated', 'Single / not married', 'Widow']
        marital = st.selectbox("Family Status:", marital_status, key="marital_status",
                               help="Select your current marital status.")
        marital_sta = marital_status.index(marital)

        housing_type = ['Co-op apartment', 'House / apartment', 'Municipal apartment', 'Office apartment',
                        'Rented apartment', 'With parents']
        house_type = st.selectbox("Housing Type:", housing_type, key="housing_type",
                                  help="Select your current living situation.")
        house = housing_type.index(house_type)

        mobile_phone = st.number_input('Number of mobile phones:', min_value=0, max_value=5, value=1,
                                       key="mobile_phone", help="Enter the number of phones you have")
        work_phone = st.number_input('Number of work phones:', min_value=0, max_value=5, value=0, key="work_phone",
                                     help="Enter the number of phones you use for work.")

        email_id = st.radio("Do you have an email ID?", ['❌No', '✅Yes'], key="email_id",
                            help="Please select 'Yes' if you have an email ID or 'No' if you don't.")
        email = 0 if email_id == 'No' else 1

        job_title = ['Accountants', 'Cleaning staff', 'Cooking staff', 'Core staff', 'Drivers', 'HR staff',
                     'High skill tech staff', 'IT staff', 'Laborers', 'Low-skill Laborers', 'Managers',
                     'Medicine staff', 'Private service staff', 'Realty agents', 'Sales staff', 'Secretaries',
                     'Security staff', 'Waiters/barmen staff']
        job_tit = st.selectbox("Job Type:", job_title, key="job_title",
                               help="Select your current Job.")
        job = job_title.index(job_tit)
        family_members = st.number_input('Number of family members:', min_value=0, max_value=20, value=4,
                                         key="family_members",
                                         help="Enter the number of people in your family, including yourself.")
        Applicant_Age = st.number_input('Age:', min_value=18, max_value=100, value=18, key="Applicant_Age",
                                        help="Enter Your Age")
        Years_of_Working = st.number_input('Years of working:', min_value=0, max_value=50, value=0,
                                           key="Years_of_Working", help="Enter Years of working")
        Total_Bad_Debt = st.number_input('Bad debt:', min_value=0, max_value=50, value=0, key="Total_Bad_Debt",
                                         help="Enter total no.of bad debt")
        Total_Good_Debt = st.number_input('Good debt:', min_value=0, max_value=50, value=0, key="Total_Good_Debt",
                                          help="Enter total no.of goog debt")

        features = [
            gend, car, property, children, annual_income, inc_type,
            edu, marital_sta, house, mobile_phone,
            work_phone, email, job, family_members, Applicant_Age, Years_of_Working, Total_Bad_Debt, Total_Good_Debt]

        scaler=pickle.load(open("scaler.sav",'rb'))
        model=pickle.load(open("rfodel.sav",'rb'))
        pred=st.button('PREDICT')
        if pred:
            result = model.predict(scaler.transform([features]))

            if result == 1:
                st.write("Processing result...")
                #sleep(2)  # Pause for 2 seconds
                #st.write("Still analyzing...")
                sleep(3)  # Pause for another 3 seconds
                st.write(":blue[✅ Credit card approved]")
            else:
                st.write(":red[⚠️ Credit card Denied]")
main()