import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, precision_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from matplotlib import pyplot

year = int(input())
data = pd.read_csv("../Data/CompleteDF.csv")
dataframe = data.copy()
trainer = dataframe[dataframe.Season < year]
x_train = trainer.drop(["Driver", "Podium"], axis=1)
y_train = trainer.Podium

scaler = StandardScaler()
x_train = pd.DataFrame(scaler.fit_transform(x_train), columns=x_train.columns)

def regression(model):
    score = 0
    for circuit in dataframe[dataframe.Season == year]["Round"].unique():
        test = dataframe[(dataframe.Season == year) & (dataframe["Round"] == circuit)]
        x_test = test.drop(["Driver", "Podium"], axis=1)
        driver = test.Driver
        y_test = test.Podium

        x_test = pd.DataFrame(scaler.transform(x_test), columns=x_test.columns)
        prediction = pd.DataFrame(model.predict(x_test), columns=["Results"])
        prediction["Podium"] = y_test.reset_index(drop=True)
        prediction["Driver"] = driver.reset_index(drop=True)
        prediction["Actual"] = prediction.Podium.map(lambda x: 1 if x==1 else 0)
        prediction.sort_values("Results", ascending=True, inplace=True)
        prediction.reset_index(inplace=True, drop=True)
        prediction["Predicted"] = prediction.index
        prediction["Predicted"] = prediction.Predicted.map(lambda x: 1 if x==0 else 0)
        score += precision_score(prediction.Actual, prediction.Predicted)
        print(prediction)
    model_score = score/dataframe[dataframe.Season==year]["Round"].unique().max()
    coefficients = pd.concat([pd.DataFrame(dataframe.columns),pd.DataFrame(np.transpose(model.coef_))], axis=1)
    coefficients.to_csv("Feature_Importance.csv", index=False)
    return model_score

def main():
    parameters = {"fit_intercept": ["True", "False"]}
    for fit_intercept in parameters["fit_intercept"]:
        model_para = (fit_intercept)
        model = LinearRegression(fit_intercept = fit_intercept)
        model.fit(x_train, y_train)
                
        model_score = regression(model)
        print(model_score)
        

if __name__ == "__main__":
    main()
