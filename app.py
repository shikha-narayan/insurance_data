import streamlit as st
import pandas as pd

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Load the dataset
    data = pd.read_csv(uploaded_file)

    # Continue with the rest of your code...
    # Set the maximum number of cells to be rendered by Pandas Styler
    pd.set_option("styler.render.max_elements", 12582900)

    # Add background color
    st.markdown(
        """
        <style>
        .main {
            background-color: #f0f8ff;
        }
        .title {
            text-align: center;
            color: #2c3e50;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Add a title
    st.markdown('<h1 class="title">Insurance Data</h1>', unsafe_allow_html=True)

    # Display the first 100 rows of the dataset
    st.header('Dataset')
    st.dataframe(data.head(100).style.set_properties(**{
        'background-color': 'lightyellow',
        'color': 'black',
        'border-color': 'black'
    }))

    # Button to load the entire dataset
    if st.button('Load Full Dataset'):
        st.dataframe(data.style.set_properties(**{
            'background-color': 'lightyellow',
            'color': 'black',
            'border-color': 'black'
        }))

    # Display column details
    st.header('Dataset Columns')
    column_details = {
        'ID': 'A unique identifier for each record in the dataset. It starts from 1 and increases by 1 for each subsequent record.',
        'Gender': 'Represents the gender of the policyholder. Values: Male or Female.',
        'Age': 'The age of the policyholder in years.',
        'Driving_License': 'Indicates whether the policyholder has a driving license. Values: 0 = No, 1 = Yes.',
        'Region_Code': 'A numerical code representing the region where the policyholder resides.',
        'Previously_Insured': 'Indicates whether the policyholder has had previous insurance. Values: 0 = No, 1 = Yes.',
        'Vehicle_Age': 'The age of the vehicle. Values: < 1 Year, 1-2 Years, > 2 Years.',
        'Vehicle_Damage': 'Indicates whether the vehicle has been damaged in the past. Values: Yes or No.',
        'Annual_Premium': 'The amount paid by the policyholder annually for the insurance policy.',
        'Policy_Sales_Channel': 'A code representing the sales channel through which the policy was sold.',
        'Vintage': 'The number of days since the policy was taken, representing how long the customer has been with the company.',
        'Response': 'Indicates whether the customer has responded positively to a product or service. Values: 0 = No, 1 = Yes.'
    }
    st.table(pd.DataFrame(list(column_details.items()), columns=['Column', 'Description']))
