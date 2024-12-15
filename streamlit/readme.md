# Data Analysis WebApp Dashboard

## Overview

This repository contains the files for a Data Analysis Dashboard created using **Streamlit**. The WebApp is hosted on the server and accessible at [http://dsmlbootcamp.org/](http://dsmlbootcamp.org/). The dashboard showcases the study, analysis, and visualization of data as part of a data analysis project. It highlights the processes of **ETL (Extract, Transform, Load)**, **EDA (Exploratory Data Analysis)**, and **Data Visualization** using a Tableau Dashboard.

---

## Files and Structure

### **Key Files**

- **`app.py`**: The main file required to run the WebApp. It defines the structure and navigation between pages. To run locally, use the command:

  ```bash
  streamlit run app.py
  ```

  On the server, it has been configured as a Linux Ubuntu system service.

- **`about.py`**: Contains information about the team members who worked on the project.

- **`analyze.py`**: Showcases the data analysis process.

- **`clean.py`**: Demonstrates the data cleaning and preprocessing steps.

- **`dashboard.py`**: Integrates with a Tableau Public Dashboard for interactive data exploration. Users can:

  - Download the Tableau Dashboard file.
  - Access the live Tableau Dashboard directly.

- **`data.py`**: Manages data loading and processing for the WebApp.

- **`explore.py`**: Presents the exploratory data analysis process.

- **`home.py`**: The main landing page of the WebApp, describing the project and its goals.

- **`presentation.py`**: Provides a preview of a PDF summarizing the project presentation. It also allows users to download the presentation files.

### **Additional Files**

Other files in the repository are essential for the WebApp's functionality, including configuration files and dependencies.

---

## Importance of Streamlit in Data Science

Streamlit is a powerful and user-friendly framework for creating interactive web applications in Python. Its importance in Data Science lies in its ability to:

- Rapidly prototype and deploy data analysis projects.
- Provide an interactive interface for presenting complex data processes, such as ETL, EDA, and Data Visualization.
- Simplify the sharing of results and insights with stakeholders, without requiring extensive front-end development knowledge.

For this project, Streamlit allowed us to:

- Seamlessly integrate multiple pages that explain the entire data analysis process.
- Connect and interact with a Tableau Dashboard.
- Create an intuitive and engaging experience for users exploring the project outcomes.

---

## How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-name.git
   ```
2. Navigate to the project folder:
   ```bash
   cd your-repo-name
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   streamlit run app.py
   ```

---

## Features

- **Data Cleaning and Preprocessing**: Demonstrates data cleaning steps with the `clean.py` module.
- **Exploratory Data Analysis**: Explains the insights discovered during EDA using `explore.py`.
- **Interactive Tableau Dashboard**: Offers seamless interaction with Tableau Public dashboards through `dashboard.py`.
- **Project Presentation**: Provides a PDF preview and downloadable project presentation with `presentation.py`.

---

## Access the WebApp

Visit the hosted WebApp at: [http://dsmlbootcamp.org/](http://dsmlbootcamp.org/)
