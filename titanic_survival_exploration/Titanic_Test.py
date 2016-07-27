import numpy as np
import pandas as pd
# RMS Titanic data visualization code 
from titanic_visualizations import survival_stats
from IPython.display import display
#%matplotlib inline

# Load the dataset
in_file = 'titanic_data.csv'
full_data = pd.read_csv(in_file)

# Print the first few entries of the RMS Titanic data
display(full_data.head())
outcomes = full_data['Survived']
data = full_data.drop('Survived',axis=1)
display(data.head())

def accuracy_score(truth,pred):
	if(len(truth) == len(pred)):
		return "Predictions have an accuracy of {:.2f}%".format((truth==pred).mean()*100)
	else:
		return "Predictions do not match number of outcomes"

#predictions = pd.Series(np.ones(5,dtype=int))
#print accuracy_score(outcomes[:5],predictions)


# #Using the RMS Titanic data, how accurate would a prediction be that none of the passengers survived?
# def predictions_0(data):
#     """ Model with no features. Always predicts a passenger did not survive. """

#     predictions = []
#     for _, passenger in data.iterrows():
        
#         # Predict the survival of 'passenger'
#         predictions.append(0)
    
#     # Return our predictions
#     return pd.Series(predictions)

# # Make the predictions
# predictions = predictions_0(data)
# print accuracy_score(outcomes, predictions)

# survival_stats(data, outcomes, 'Sex')
#*How accurate would a prediction be that all female passengers survived and the remaining passengers did not survive?*  
# def predictions_1(data):
#     """ Model with one feature: 
#             - Predict a passenger survived if they are female. """
    
#     predictions = []
#     for _, passenger in data.iterrows():
#         if(passenger['Sex'] == 'female'):
#         	predictions.append(1)
#         else:
#         	predictions.append(0)
        	
    
#     # Return our predictions
#     return pd.Series(predictions)

# # Make the predictions
# predictions = predictions_1(data)
# print accuracy_score(outcomes, predictions)


# survival_stats(data, outcomes, 'Age', ["Sex == 'male'"])
# #How accurate would a prediction be that all female passengers and all male passengers younger than 10 survived?
# def predictions_2(data):
#     """ Model with two features: 
#             - Predict a passenger survived if they are female.
#             - Predict a passenger survived if they are male and younger than 10. """
    
#     predictions = []
#     for _, passenger in data.iterrows():
        
#         if(passenger['Sex'] == 'female' or (passenger['Age']<10 and passenger['Sex']== 'male')):
#         	predictions.append(1)
#         else:
#         	predictions.append(0)
    
#     # Return our predictions
#     return pd.Series(predictions)

# # # Make the predictions
# predictions = predictions_2(data)
#print accuracy_score(outcomes, predictions)
survival_stats(data, outcomes, 'Pclass',["Sex == 'male'"])
# survival_stats(data, outcomes, 'Pclass', ["Sex == 'male'"])
def predictions_3(data):
    """ Model with two features: 
            - Predict a passenger survived if they are female.
            - Predict a passenger survived if they are male and younger than 10. """
    
    predictions = []
    for _, passenger in data.iterrows():
        #if(passenger['Sex'] == 'male' or (passenger['Age'] >= 10 and passenger['Age'] <=20  and passenger['Age']>=30) or (passenger["SibSp"]>2)  or passenger['Fare'] < 7):
    	if(passenger['Sex'] == 'female'):
            if(passenger['SibSp']<=2):
                predictions.append(1)
            else:
                predictions.append(0)    
    	if((passenger['Sex'] == 'male')):
            if(passenger['Pclass'] >=2):
                predictions.append(0)




    
    # Return our predictions
    return pd.Series(predictions)

# # Make the predictions
predictions = predictions_3(data)
print accuracy_score(outcomes, predictions)
