# Air Quality Index Prediction

### Data extraction
Data is extracted from a website and is stored in the form of html files. Later by using beautiful soup, data from the html file is extracted and is converted to proper csv files.

### EDA
Most of the data cleaning is done while creating the csv files itself. Some of the missing values are also fixed.
Checked the correlation using pearson correlation co-effient and also visualized the same.

### Model selection
Used varies regression techniques to find which is the best model for this perticular dataset. RandomForestRegressor and XGBoostRegressors are the models that are performing well

### Model evaluation
Evaluation metrics used for checking the model's strength is **R2score** and loss functions used are **Mean Absolute Error (mae)**, **Mean Sqaured Error (mse)** and **Root Mean Sqaured Error (rmse)**
