import joblib
  # arko file use garna ko lagi (predict vanne file ko predict diabates ko function)

def predict_diabetes(input):  # input chai appy.py bata ayunccha 
    model=joblib.load('Saved/DecisionTreePrediction.pkl') # saved vayako modek ko actual path diyaako 

    prediction=model.predict([input])
    return prediction