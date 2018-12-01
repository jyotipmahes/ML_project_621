# Machine Learning Project - 621
### This repo contains work for MSDS621 course 
As a part of MSDS621 we have taken up a machine learning project to be completed as a partial requirement for the course.
We have selected [WSDM - KKBox's Music Recommendation Challenge](https://www.kaggle.com/c/kkbox-music-recommendation-challenge) data set to build a recommender/prediction model which predicts whether the user will listen to the same song again within a month.

### Detailed information on data
In this task,we built a model to predict the chances of a user listening to a song repetitively after the first observable listening event within a time window was triggered. If there are recurring listening event(s) triggered within a month after the user’s very first observable listening event, its target is marked 1, and 0 otherwise in the training set. The same rule applies to the testing set.

KKBOX provides a training data set consists of information of the first observable listening event for each unique user-song pair within a specific time duration. Metadata of each unique user and song pair is also provided. The use of public data to increase the level of accuracy of your prediction is encouraged.

The train and the test data are selected from users listening history in a given time period. Note that this time period is chosen to be before the WSDM-KKBox Churn Prediction time period. The train and test sets are split based on time, and the split of public/private are based on unique user/song pairs.


### How to download data
You can directly downlaod the data from **Kaggle API** by running following command ***kaggle competitions download -c kkbox-music-recommendation-challenge***

### Extracting the files from .7z zipped files downloaded from kaggle
Run the `unzip7z.sh` files present in `Helper_functions` to extract the files in `csv` form. **Ensure that you run the `.sh` files in the folder which has files.**

Use following command to run `sh unzip7z.sh`

### Helper_functions
The helper function folder has few custom functions created to help with EDA.

### Resources
Check the resources folder for all relevant resources to refer.
