# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model is a RandomForest classifier trained to predict whether a person makes over 50K a year 
based on various features extracted from the 1994 Census database. The RandomForest algorithm was 
chosen for its ability to handle a large number of features and its robustness against overfitting.
## Intended Use
The model is intended to be used for income prediction tasks, specifically to determine whether a 
person’s income exceeds 50K a year. However, this is in the context of educational use only.
## Training Data
The training data was extracted from the 1994 Census database by Barry Becker.
## Evaluation Data
The evaluation data was twenty percent of the overall dataset.
## Metrics
_Please include the metrics used and your model's performance on those metrics._
The model’s performance was evaluated using the following metrics:

Precision: 0.7388
Recall: 0.6283
F1 Score: 0.6791
## Ethical Considerations
While the model is designed to predict income levels based on demographic and employment-related 
features, care should be taken to ensure that it is not used to unfairly discriminate against certain
groups. It’s important to note that the model’s predictions are based on patterns in the training 
data and do not determine an individual’s worth or potential.
## Caveats and Recommendations
The model’s performance may vary when used on data that differs significantly from the 1994 Census 
database. Therefore, it’s recommended to retrain the model on more recent data or data from different 
regions as needed. Additionally, while RandomForest is a robust algorithm, it’s always a good idea to 
try different models and choose the one that best meets your specific needs and constraints.
