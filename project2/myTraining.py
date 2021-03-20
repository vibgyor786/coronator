import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

def data_split(data,ratio):
    shuffled=np.random.permutation(len(data))
    test_size=int(len(data)*ratio)
    test_indices=shuffled[:test_size]
    train_indices=shuffled[test_size:]
    return data.iloc[train_indices],data.iloc[test_indices]


if __name__ == "__main__":
    df=pd.read_csv('CovidData.csv')
    train,test=data_split(df,0.25)
    
    x_train=train[['Fever','Weakness','Dry Cough','Breathing Difficulty','Sore Throat','Body Pain','NasalBlock','Runny Nose','Diarrhea','Age','Gender']].to_numpy()
    x_test=test[['Fever','Weakness','Dry Cough','Breathing Difficulty','Sore Throat','Body Pain','NasalBlock','Runny Nose','Diarrhea','Age','Gender']].to_numpy()
    
    y_train=train[['Virusprob']].to_numpy()
    y_test=test[['Virusprob']].to_numpy()

    clf=LogisticRegression()
    clf.fit(x_train,y_train)

    file=open('model.pkl','wb')
    pickle.dump(clf,file)
    file.close()





