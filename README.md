# Machine Learning Project - 621
### This repo contains work for MSDS621 course 
As a part of MSDS621 we have taken up a machine learning project to be completed as a partial requirement for the course.
We have selected [WSDM - KKBox's Music Recommendation Challenge](https://www.kaggle.com/c/kkbox-music-recommendation-challenge) data set to build a recommender/prediction model which predicts whether the user will listen to the same song again within a month.

### Detailed information on data
In this task, we built a model to predict the chances of a user listening to a song repetitively after the first observable listening event within a time window was triggered. If there are recurring listening event(s) triggered within a month after the user’s very first observable listening event, its target is marked 1, and 0 otherwise in the training set. The same rule applies to the testing set.

KKBox provides a training data set which consists of information of the first observable listening event for each unique user-song pair within a specific time duration. Metadata of each unique user and song pair is also provided. The use of public data to increase the level of accuracy of your prediction is encouraged.

The train and the test data are selected from users listening history in a given time period. Note that this time period is chosen to be before the WSDM-KKBox Churn Prediction time period. The train and test sets are split based on time, and the split of public/private are based on unique user/song pairs.

### EDA Notebooks
The EDA notebooks folder contains the Exploratory Data Analysis done on the data. 
1. In this notebook we check the distribution of categorical and continuous variabes and their correlation with the target variables. in train.csv, test.csv, member.csv, songs.csv and songs_extra_info.csv.
2. We use matplotlib and seaborn libraries for this purpose.

### Helper Functions
Helper functions folder contains files that help with the EDA and modeling of the problem.
1. Data_clean_feature_engg_pipeline : Contains feature engineering functions. 
2. summary_fn : This file provides the function required for Data Exploration.
3. unzip7z.sh : This .sh file could be run to extract the .7z files. 

### Models
This file contains notebooks of the models we fitted for the recommendations.
1. Naive_Bayes_featured_data: fit a Naive bayes model. Accuracy achieved was 61.5%.
2. KNN_Featured_Data: Fit a KNN model. Accuracy achieved was 63%.
3. Logistic_regression_featured_data: Fit a logistic regression model. Accuracy achieved was 64%.
4. First_Model_RF_v1 : This was the first model that we built using Random Forest. The accuracy achieved is 65%.
5. Random_Forest_Featured_data :  Fit a Random Forest model. Used the feature engineer notebook to extract all the data which results in 72 columns in total. The accuracy achieved was 76%.
6. LightGBM: Build a light gradient boosting machine and checked the feature importance.The accuracy achieved is 75%.
7. LightGBM_Visualization(pdf): Contains the visualization of a 3 tree model in ligth GBM.
8. Ensembling: Use ensembling models to do predictions of all the models.
9. Feature_Eng_Benchmark: Build feature engineering benchmark. 

### Steps taken for modeling
1. Data Processing: We started off by merging the files together. Removed and imputed the null values.
2. Feature Engineering: Extracted the important features from the existing data. Resulted in 72 total features
3. Built Naive Bayes, KNN, Logistic Regression, RandomForest and LightGBM. The best accuracy was 76% which we got using random forest.

### How to download data
You can directly downlaod the data from **Kaggle API** by running following command ***kaggle competitions download -c kkbox-music-recommendation-challenge***

### Extracting the files from .7z zipped files downloaded from kaggle
Run the `unzip7z.sh` files present in `Helper_functions` to extract the files in `csv` form. **Ensure that you run the `.sh` files in the folder which has files.**
