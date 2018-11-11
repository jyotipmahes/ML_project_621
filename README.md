# ML_project_621
### This repo contains work for MSDS621 course 
As a part of MSDS621 we have taken up a machine learning project to be completed as a partial requirement for the course.
We have selected [WSDM - KKBox's Music Recommendation Challenge](https://www.kaggle.com/c/kkbox-music-recommendation-challenge) data set to build a recommender/prediction model which predicts whether the user will listen to the same song again within a month.

### Detailed information on data
In this task, you will be asked to predict the chances of a user listening to a song repetitively after the first observable listening event within a time window was triggered. If there are recurring listening event(s) triggered within a month after the user’s very first observable listening event, its target is marked 1, and 0 otherwise in the training set. The same rule applies to the testing set.

KKBOX provides a training data set consists of information of the first observable listening event for each unique user-song pair within a specific time duration. Metadata of each unique user and song pair is also provided. The use of public data to increase the level of accuracy of your prediction is encouraged.

The train and the test data are selected from users listening history in a given time period. Note that this time period is chosen to be before the WSDM-KKBox Churn Prediction time period. The train and test sets are split based on time, and the split of public/private are based on unique user/song pairs.


### How to download data
You can directly downlaod the data from **Kaggle API** by running following command ***kaggle competitions download -c kkbox-music-recommendation-challenge***

But before running this you need to complete following steps:
1. Create a kaggle account
2. Get API credentials: To use the Kaggle API, sign up for a Kaggle account at https://www.kaggle.com. Then go to the 'Account' tab of your user profile (https://www.kaggle.com/<username>/account) and select 'Create API Token'. This will trigger the download of `kaggle.json`, a file containing your API credentials. Place this file in the location `~/.kaggle/kaggle.json` (on Windows in the location `C:\Users\<Windows-username>\.kaggle\kaggle.json` - you can check the exact location, sans drive, with echo %HOMEPATH%). You can define a shell environment variable `KAGGLE_CONFIG_DIR` to change this location to `$KAGGLE_CONFIG_DIR/kaggle.json` (on Windows it will be %KAGGLE_CONFIG_DIR%\kaggle.json).
  
  For your security, ensure that other users of your computer do not have read access to your credentials. On Unix-based systems you can do this with the following command:
  
  `chmod 600 ~/.kaggle/kaggle.json`
  
  3. Run the following command to access the Kaggle API using the command line:

`pip install kaggle`

4. Ensure that you enroll in the competition on competition/challenge page(got to data tab)

5. Now got to the location you want to download the data and run `kaggle competitions download -c kkbox-music-recommendation-challenge`

Check https://github.com/Kaggle/kaggle-api for any clarification.



### Extracting the files from .7z zipped files downloaded from kaggle
Run the `unzip7z.sh` files present in `Helper_functions` to extract the files in `csv` form. **Ensure that you run the `.sh` files in the folder which has files.**

Use following command to run `sh unzip7z.sh`

### Helper_functions
The helper function folder has few custom functions created to help with EDA.

### Resources
Check the resources folder for all relevant resources to refer.
