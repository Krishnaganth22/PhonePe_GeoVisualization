# PhonePe_GeoVisualization

This project aims to analyze and visualize data from various sources related to PhonePe transactions and user activities. The data is extracted, transformed, and loaded into a MySQL database for further analysis and visualization.

Project Structure
The project is organized into the following directories:

data: Contains raw data files obtained from various sources.
scripts: Contains Python scripts used for data extraction, transformation, and loading into the database.
visualizations: Contains Jupyter notebooks or Python scripts for data visualization using libraries like Matplotlib, Seaborn, and Plotly.
docs: Contains documentation files related to the project.
Data Sources
The data is obtained from the following sources:

Aggregated Transaction Data: Contains information about transactions, including transaction type, count, and amount, aggregated by state, year, and quarter.
Aggregated User Data: Contains information about users, including brand usage, transaction count, and percentage, aggregated by state, year, and quarter.
Map Transaction Data: Contains geographical information about transactions, including district-level data, aggregated by state, year, and quarter.
Map User Data: Contains geographical information about users, including registered users and app opens, aggregated by state, year, and quarter.
Top Transaction Data: Contains top transaction data by PIN codes, including transaction count and amount, aggregated by state, year, and quarter.
Top User Data: Contains top user data by PIN codes, including registered users, aggregated by state, year, and quarter.
Data Extraction and Loading
Python scripts are used to extract data from JSON files, transform it into pandas DataFrames, and load it into a MySQL database using the mysql-connector library. SQLAlchemy is used for database interaction and management.

Visualizations
Visualizations are created using libraries like Matplotlib, Seaborn, and Plotly. Jupyter notebooks or Python scripts in the visualizations directory demonstrate various visualizations created from the extracted data.

Requirements
Python 3.x
pandas
json
mysql-connector
sqlalchemy
Getting Started
Clone the repository: git clone https://github.com/your_username/phonepe-visualization.git
Navigate to the project directory: cd phonepe-visualization
Install the required dependencies: pip install -r requirements.txt
Run the data extraction and loading scripts in the scripts directory.
Explore the visualizations in the visualizations directory.
Contributing
Contributions to this project are welcome. Please follow the standard GitHub workflow:

Fork the repository.
Create a new branch: git checkout -b feature/new-feature
Make your changes and commit them: git commit -m 'Add new feature'
Push to the branch: git push origin feature/new-feature
Submit a pull request.


Phonepe Pulse Data Visualization and Exploration
This Streamlit web application offers a user-friendly tool for visualizing and exploring data related to transactions and users on the Phonepe platform. Leveraging data from various sources, including JSON files and a MySQL database, it provides insights and geovisualizations to better understand Phonepe usage across different regions and time periods.

Features
# Home: 
Provides an overview of the app's usage and purpose, along with a link to download the Phonepe app.
# Explore:
Allows users to explore top transactions and users based on selected year and quarter, providing insights and visualizations.
# Data Visualization: 
Offers geovisualizations of transaction and user data across different states and districts, aiding in understanding regional patterns and trends.
# Insights:
Provides 10 pre-defined insights derived from the data, offering key observations and trends.
# Installation:
*Clone this repository to your local machine.
*Install the required dependencies using pip install -r requirements.txt.
*Ensure you have a MySQL server set up with the appropriate database and tables populated with Phonepe data.
*Update the MySQL connection details in the code to match your environment.
*Run the Streamlit app using streamlit run app.py.
# Usage:
Upon launching the app, you will be presented with a sidebar containing options to navigate between different sections of the app.
Select the desired section (Home, Explore, Data Visualization, or Insights) to explore the Phonepe data.
In the Explore section, choose the year and quarter to view top transactions and users.
In the Data Visualization section, select the year and quarter to visualize transaction and user data on interactive maps.
The Insights section provides pre-defined insights derived from the data, offering valuable observations and trends.
# Data Sources:
The app utilizes JSON files containing transaction and user data from the Phonepe platform.
Transaction and user data is also fetched from a MySQL database, where it is stored in structured tables.
# Technologies Used:
Streamlit: Used for building the interactive web application.
Plotly: Utilized for creating interactive visualizations and maps.
Pandas: Employed for data manipulation and analysis.
MySQL: Used as the database management system for storing Phonepe data.
Python: The primary programming language used for app development and data processing.


