
import pandas as pd

#separation function
def separate(df):
    return df[["Age","Fare"]], df[["Pclass", "Sex", "SibSp", "Parch", "Embarked"]]

#load all the models from pickles
le = pd.read_pickle("le.pickle")
pf = pd.read_pickle("pf.pickle")
ps = pd.read_pickle("ps.pickle")
lr = pd.read_pickle("lr.pickle")


def predict(X):

    X = pd.DataFrame(X)
    #rename all the columns to be correct
    X.rename(columns={0: 'Age', 1: 'Fare', 2:"Pclass",3:"Sex",4:"SibSp",5:"Parch",6:"Embarked"}, inplace=True)
    

    #separate to cont and discr columns
    train_cont_toy,train_discr_toy = separate(X)

    #encode the discrete ones
    train_discr_toy_no_col = le.transform(train_discr_toy)

    #assign the correct column names back
    train_discr_toy = pd.DataFrame(train_discr_toy_no_col, columns = train_discr_toy.columns)

    #generating polynomial features for the continuous values
    train_cont_toy = pf.transform(train_cont_toy)

    #concat them back 
    X_test_toy = pd.concat([pd.DataFrame(train_cont_toy), pd.DataFrame(train_discr_toy).astype("int16")], axis=1)

    #transform all together
    X_test_toy = ps.transform(X_test_toy)

    #predict
    y_pred = lr.predict(X_test_toy)




    if y_pred ==1:
        return "You would"
    return "You would not"

