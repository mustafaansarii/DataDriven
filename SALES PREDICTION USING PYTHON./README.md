# Sales Prediction Project

This project aims to predict sales figures based on advertising expenditures, leveraging machine learning techniques in Python. The prediction model is trained on a dataset containing information about advertising expenditures on various platforms (TV, radio, newspaper) and corresponding sales figures.

## Overview

Sales prediction involves forecasting the amount of a product that customers will purchase, taking into account various factors such as advertising expenditure, target audience segmentation, and advertising platform selection. In this project, we utilize machine learning techniques to analyze and interpret data, enabling us to make informed decisions regarding advertising costs and optimize advertising strategies to maximize sales potential.

## Dataset

The dataset used in this project (`advertising.csv`) contains the following columns:

- TV: Advertising expenditure on TV (in thousands of dollars).
- Radio: Advertising expenditure on radio (in thousands of dollars).
- Newspaper: Advertising expenditure on newspaper (in thousands of dollars).
- Sales: Sales figures (in thousands of units).

## Approach

1. **Data Preparation**: Clean and format the dataset, handling missing values and encoding categorical variables if necessary.

2. **Feature Selection/Engineering**: Identify relevant features and possibly create new features based on domain knowledge.

3. **Model Selection**: Choose a suitable machine learning model for sales prediction. In this project, we utilized linear regression.

4. **Model Training**: Train the selected model on the training data.

5. **Model Evaluation**: Evaluate the performance of the trained model using metrics such as Root Mean Squared Error (RMSE).

6. **Visualization**: Visualize the actual sales against the predicted sales to assess model performance.

## Results
![Predicted Sales](/CODSOFT_DS_Task-04/assets/Predicted%20Sales.png)
- The trained linear regression model achieved an RMSE of approximately 1.71, indicating that, on average, the model's predictions are within 1.71 units of the actual sales values.

- The scatter plot visualization of actual vs predicted sales shows a close alignment of points around the diagonal line, indicating that the model's predictions closely match the actual sales values.

## Conclusion

This project demonstrates the application of machine learning techniques to predict sales figures based on advertising expenditures. By leveraging predictive modeling, businesses can optimize their advertising strategies and maximize sales potential.