
# EXPLORATORY ANALYSIS OF REDWINE DATA USING R

### DATA SET USED
(https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/)

### SUMMARY

<p>This is an exploratory analysis of the Red wine quality based on 12 parameters.The analysis is performed using R -primarily using ggplot library.The response variable quality is a categorical variable (typical case of Multi class classification) ranging from 1 to 10 with 1 denoting lowest quality and 10 rating denoting the highest.</p>

### Pointers on the analysis performed
<ol>
<li>Univariate analysis is performed to check the range of each variable and to check if scaling to log/Sqrt is required to observe a normal pattern.Primarily histograms and box plots are used</li>
<li>Corelation matrix used to check the realtionship(pearsons coefficient between) various features and then scatter plots/lin e charts/box plots are used to observe and validate the relationships</li>
<li>Linear model is used to arrive at the coefficients and the f-statistic value is used to verify the goodness of fit of the model</li>
<li>Validation is performed by splitting the data into training and test sets</li>
</ol>

