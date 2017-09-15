import pandas as pd 
import numpy as np 

file = "/Users/Maternus/Coding/GitRepo/machine-learning/projects/titanic_survival_exploration/titanic_data.csv"
full_data = pd.read_csv(file, sep = ',')
outcomes = full_data['Survived']
data = full_data.drop('Survived', 1)

def compare_pred(truth, pred):
    """ Returns accuracy score for input truth and predictions. """
    
    # Ensure that the number of predictions matches number of outcomes
    if len(truth) == len(pred): 
        # Calculate and return the accuracy as a percent
        return "Predictions have an accuracy of {:.2f}%.".format((truth == pred).mean()*100)
    else:
        return "Number of predictions does not match number of outcomes!"

""" QUESTION 4 """
def predictions_4(data):
       
    predictions = []
    for _, passenger in data.iterrows():
        if passenger['Sex'] == 'female' and passenger['Pclass'] <= 2 \
            or passenger['Sex'] == 'male' and passenger['Age'] <= 10 and passenger['Pclass'] <= 2 \
            or passenger['Sex'] == 'female' and passenger['Age'] <= 16 and passenger['Pclass'] == 3:
            predictions.append(1)
        else:
            predictions.append(0)    
    # Return our predictions
    return pd.Series(predictions)

# Make the predictions
predictions = predictions_4(data)

# compare prediction  
print compare_pred(outcomes, predictions)


""" Extending Question 4 """
""" I kept looking at the sex attribute that we found earlier. Because nearly all female in 1st and 2nd class survived I combined these features
    We also saw in an example that most males under the age of 10 survived, which I also joined to the logic. Last but not least I included the females form class 3.
    which survivors seemed to be younger.
"""

""" Question 5 """
""" I think supervised learning could easily be applied in the field of engineering. Taking an enigne e.g. we have a process of several
    septs where we try several different parts together and try to figure out how they work/perform togeher. In these tests, we gather data about their performance.
    This can then be used to extract different 'success factors' for the performance of the engine and predict the a new engine one's without having
    to build it in the first place. 
    The outcome variable in my oponion would be the performance/degree of efficiency/fit of the several parts combined or however we want to name it. 
    Variables used to predict might be the power itself, the runtime w/o any problems, the specs (performance, voltage, ...) of each part etc.
"""
