#Run this script in the folder which has all the
#.7z files downloaded from kaggle website

sudo apt-get install p7zip-full
7z e members.csv.7z
7z e song_extra_info.csv.7z
7z e test.csv.7z
7z e sample_submission.csv.7z
7z e songs.csv.7z
7z e train.csv.7z
