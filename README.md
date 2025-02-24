# Steel Industry Energy Consumption Prediction

## Project Overview
This project aims to build a **Machine Learning model based on Linear Regression** to predict energy consumption in the steel industry. By using historical energy consumption data, the project aims to improve operational efficiency and reduce energy waste and carbon emissions.

This application is developed using **Streamlit**, with key features:
**Exploratory Data Analysis (EDA)** to analyze energy consumption patterns.  
**Energy consumption prediction** based on user input.  
**Pre-trained machine learning model** stored in a pipeline (`best_model_pipeline.pkl`).  

**Try the Application on Hugging Face:** [Deployments](https://huggingface.co/spaces/AzkaIrsyad/Deployments)

---
## Data Source
The dataset used in this project is **steel industry energy consumption data**, which includes features such as:
- Electricity consumption (**Usage_kWh**)
- Power factor (**Power Factor**)
- Reactive power (**Reactive Power_kVarh**)
- Carbon emissions (**CO2(tCO2)**)
- Work status (**WeekStatus**)

---
## Introduction
### Background
The steel industry has high energy consumption and significantly contributes to carbon emissions. **Inefficiencies in energy management** can lead to increased operational costs. By leveraging **Machine Learning**, we can **predict energy consumption** more accurately, helping to make better decisions regarding energy management.

### Business Objectives
- **Build an energy consumption prediction model** to improve operational efficiency.
- **Analyze energy consumption patterns** through Exploratory Data Analysis (**EDA**).
- **Reduce energy waste** through data-driven strategies.

---
## SMART Goals
**Specific**: Develop an energy consumption prediction model for the steel industry using **Linear Regression**.  
**Measurable**: Achieve **prediction accuracy above 85%** based on the R² metric.  
**Achievable**: Use historical datasets to build an end-to-end pipeline from **EDA to model prediction**.  
**Relevant**: Address the challenge of high energy consumption in the steel industry.  
**Time-Bound**: Complete within **3 months** with a model ready for use in the Streamlit application.  

---
## Implementation
### Data Preprocessing
- Handled missing values using imputation techniques.
- Scaled numerical features for better model performance.
- Encoded categorical features such as `WeekStatus` and `Load_Type`.

### Model Training & Evaluation
- **Algorithm Used**: Linear Regression
- **Training Split**: 80% training, 20% testing
- **Evaluation Metrics**:
  - R² Score: **0.87**
  - Mean Squared Error (MSE)
  - Mean Absolute Error (MAE)

### Model Deployment
- The trained model was **saved as a pipeline** using `joblib`.
- Integrated into a **Streamlit web application** for real-time predictions.
- Deployed on **Hugging Face Spaces** for public access.

---
## Exploratory Data Analysis (EDA)
EDA is conducted to understand energy consumption patterns, including:
**Energy Consumption Distribution (Usage_kWh)**  
**Relationship between Reactive Power and Energy Consumption**  
**Load Type Analysis on Energy Consumption**  

**View EDA in the Streamlit application!**

---
## Model Deployment
This application is developed using **Streamlit**, with two main features:
**EDA Page (`eda.py`)** → Displays data analysis and energy consumption pattern visualization.  
**Prediction Page (`predict.py`)** → Allows users to input new data and obtain energy consumption predictions based on the pre-trained **Machine Learning model**.

**Pipeline Model:**
- **Model:** Linear Regression
- **Model File:** `best_model_pipeline.pkl`
- **Key Libraries:** `pandas`, `numpy`, `scikit-learn`, `joblib`

---
## How to Run the App
To run this application locally:
```bash
# Clone this repository
$ git clone https://github.com/yourusername/energy-prediction.git
$ cd energy-prediction

# Install dependencies
$ pip install -r requirements.txt

# Run the Streamlit application
$ streamlit run app.py
```

**Application Navigation**
- **EDA Page:** Displays visualizations of energy consumption data.
- **Prediction Page:** Input data to obtain energy consumption predictions.

---
## Results & Findings
The model achieved **an R² accuracy of 0.87**, demonstrating strong predictive performance.  
Identified energy consumption patterns to assist in decision-making for energy savings.  
Optimized energy consumption based on model prediction results.

---
## Author
**Azka Irsyad Choir**  
Email: [azkairsyad24@gmail.com](mailto:azkairsyad24@gmail.com)  
LinkedIn: [linkedin.com/in/azkairsyad](https://www.linkedin.com/in/azka-irsyad-aa2509191/)  
GitHub: [github.com/azka irsyad](https://github.com/Azka24-ui)  
