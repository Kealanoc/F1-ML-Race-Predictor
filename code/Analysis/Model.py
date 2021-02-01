import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, precision_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
import time
start_time = time.time()

year = int(input())
data = pd.read_csv("../Data/CompleteDF.csv")
dataframe = data.copy()
trainer = dataframe[dataframe.Season < year]
x_train = trainer.drop(["Driver", "Podium"], axis=1)
y_train = trainer.Podium
results ={'model':[],'params': [],'score': []}
scaler = StandardScaler()
x_train = pd.DataFrame(scaler.fit_transform(x_train), columns=x_train.columns)

def regression(model):
    score = 0
    predictions = []
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
        predictions.append(prediction)
    model_score = score/dataframe[dataframe.Season==year]["Round"].unique().max()
    #coefficients = pd.concat([pd.DataFrame(dataframe.columns),pd.DataFrame(np.transpose(model.coef_))], axis=1)
    #coefficients.to_csv("Feature_Importance.csv", index=False)
    return model_score, predictions

def linear_regression():
    parameters = {"fit_intercept": ["True", "False"]}
    for fit_intercept in parameters["fit_intercept"]:
        model_params = (fit_intercept)
        model = LinearRegression(fit_intercept=fit_intercept)
        model.fit(x_train, y_train)
        model_score = regression(model)
        results['model'].append('Linear Regression')
        results['params'].append(model_params)
        results['score'].append(model_score)
    random_forest()
    print(results)
        

def random_forest():
    race_results = {}
    params={"criterion": ["mse"],
            "max_features": [0.8, "auto", None],
            'max_depth': list(np.linspace(5, 55, 26)) + [None]}
    count = 0
    best = 0
    for criterion in params["criterion"]:
        for max_features in params["max_features"]:
            for max_depth in params["max_depth"]:
                count +=1
                print(count)
                model_params = (criterion, max_features, max_depth)
                model = RandomForestRegressor(criterion=criterion, max_features=max_features, max_depth=max_depth, random_state=1)
                model.fit(x_train, y_train)
                model_score, predictions = regression(model)
    best = model_score
    best_predictions = predictions
    results['model'].append('random_forest_regressor')
    results['params'].append(model_params)
    results['score'].append(model_score)

    Round = 1
    for i in best_predictions:
        f_name = "{}_{}".format(year,str(Round))
        df = pd.DataFrame(i)
        df.to_csv("../Data/Predictions/{}".format(f_name), index=False)
        Round += 1
    print(results)
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    random_forest()
