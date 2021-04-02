# Contraceptive Method Public Health Project  
  
## Overview  
In this project, we examine a dataset of contraceptive methods used by married Indonesian women to see insights and predictions can be made based on various demographic and socioeconomic variables.  

![family_planning](images/indonesian-family.jpeg)  
  
## Motivation  
To make informed recommendations for further action to public health officials to improve the welfare of mothers and children. We hope to have an impact in empowering healthcare autonomy of female citizens in Indonesia, while reducing unwanted pregnancy, abortion rates, birth complications, infant and maternal mortality rates.  
  
## Data  
Our [dataset](https://archive.ics.uci.edu/ml/datasets/Contraceptive+Method+Choice) comes from the [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php), used with permission.  
  
### Features Examined  
Feature Name             |  Type         |     Values  
:------------------------|:--------------|-------------:  
Woman's age              | numerical     |   
Woman's education        | categorical   | 1 = low, 2, 3, 4 = high  
Husband's education      | categorical   | 1 = low, 2, 3, 4 = high  
Number of children       | numerical     |   
Wife's religion          | binary        | 0 = Non-Islam, 1 = Islam  
Wife's now working?      | binary        | 0 = Yes, 1 = No  
Husband's occupation     | categorical   | 1, 2, 3, 4  
Standard-of-living index | categorical   | 1 = low, 2, 3, 4 = high  
Media exposure           | binary        | 0 = Good, 1 = Not good  
  
### Target Variable  
Feature Name             |  Type           |     Values  
:------------------------|:----------------|-------------:  
Contraceptive method used| class attribute |  1 = No-use <br> 2 = Long-term method <br> 3 = Short-term method  
  
<img src="images/readme_contraception_methods.jpg" alt="contraception methods" width="800"/>
  
## Methods  
Our methodology implements the CRISP-DM model for exploratory data analysis, cleaning, modeling, and evaluation.  
We leveraged machine learning models from [Scikit-learn](https://scikit-learn.org/stable/) to determine the relationship between the features and the target variable. We also performed statistical analysis via [SciPy Stats](https://docs.scipy.org/doc/scipy/reference/stats.html) to further make inferences on the data.  
Other tools used include Python, NumPy, and Pandas. Visualizations were created with MatPlotLib and Seaborn.  
  
## Findings
![Distribution by Childcount](images/Distribution%20by%20Childcount.png)

## Conclusions  
## Further Actions  
  
<div align="center";>Authors  
  <div align="center";>Alexander Xin & Mike Flanagan  
    
[GitHub](https://github.com/eggrollofchaos) | [LinkedIn](https://linkedin.com/in/eggrollofchaos)  
[GitHub](https://github.com/mike-flanagan/) | [LinkedIn](https://www.linkedin.com/in/mike-flanagan-data/)
  
  
  
![image](https://user-images.githubusercontent.com/61798935/110971972-7d0f8900-8329-11eb-92f4-1c9a6a4c4c62.png)  
  
<div align="center";>Photo by Luca Micheli on Unsplash</div>  
  
## Index  
- **code/** — directory containing python code file
- **crisp_dm_process/** — directory for initial EDA and model notebook files  
- **data/** — directory of project datasets
  - **Initial_EDA** — notebook file that includes thorough initial data exploration, insights, and takeaways  
  - **Model_Evaluation** — notebook file that includes modeling trials and process.
- **images/** — directory containing the following...  
  - image exports of visualizations  
  - additional images for notebooks, README, and presentation slides
- **Contraception_Indonesia_FINAL.ipynb** — primary project notebook  
- **README.md**  
