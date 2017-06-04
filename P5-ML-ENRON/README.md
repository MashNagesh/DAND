
# MACHINE LEARNING PROJECT USING ENRON DATA SET


### DATASET 

Link to the ENRON Corpus - (https://www.cs.cmu.edu/~./enron/)

### FILES INCLUDED AND THEIR DESCRIPTION
<ol>
<li>poi_id.py - Main executable file in python</li> 
<li>my_classifier.pkl - generated from poi_id.py</li>
<li>my_dataset.pkl - generated from poi_id.py</li>
<li>my_feature_list.pkl - generated from poi_id.py</li>
<li>Reference Link.txt - Links to references used in the project</li>
<li>Project_Q&A.pdf - Answers to the project questions as part of the course</li>
</ol>

### Summary of work done in poi_id.py
Tools folder is required to execute the file.

<p> The dataset contains financial features and email data of about 150 people associated with ENRON at the time of fraud along with a feature which lables them as a POI(Person of interest).POI is a 1/0 boolean field indicating the status of the person.

The task in hand is to train the features (financial+email) and come up with a algorithm/formula to classify new data.
Precision and recall rates expected out of this project is >0.3.This is a classic case of logistic regression.A number of concepts involved in machine learning is applied in this project.</p>

<li> - Data exploration</li>
<li> - NaN handling.(how non availability of data is handled)</li>
<li> - outlier detection and removal/handling</li>
<li> - feature engineering</li>
<li> - feature selection using Kbest and importance scores</li>
<li> - scaling of features using minmaxscaler
<li> - application of classifiers like Naive Bayes/Decision trees/SVM/Random forest </li>
<li> - Tuning Using PCA ,using Pipelines and  gridsearchcv </li>
<li> - Chosing the final algorithm and parameters based on Precision/Recall and f1 score </li>
<li> - Applying cross validation techniques like stratifiedshufflesplit </li>

<p> The entire project uses various modules from the sklearn library</p>





