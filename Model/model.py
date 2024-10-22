from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import numpy as np

iris = load_iris()
X, y = iris.data, iris.target

class Model:
    def __init__(self):
        self.model = None
        self.algorithm = None
        self.best_params = None
        self.cv = 5
        self.trained = False
        self.training_accuracy = None
    
    def train(self, algorithm, params):

        if algorithm == "decision_tree":
            model = DecisionTreeClassifier()
            param_grid = params if params else {
                'max_depth': [2, 5, 7, 10],
                'criterion': ['entropy', 'gini']
            }
        elif algorithm == "random_forest":
            model = RandomForestClassifier()
            param_grid = params if params else {
                'n_estimators': [10, 50, 100],
                'max_depth': [2, 5, 7, 10]
            }
        else:
            return ValueError(f"Model {algorithm} is not supported! Please try again.")
        
        grid_search = GridSearchCV(model, param_grid, cv=self.cv, scoring='accuracy')
        grid_search.fit(X, y)

        self.model = grid_search.best_estimator_
        self.best_params = grid_search.best_params_
        self.algorithm = algorithm
        self.trained = True

        self.training_accuracy = np.mean(self.model.predict(X) == y) # Calculating training accuracy

        return {
            "best_params": grid_search.best_params_,
            "best_score": grid_search.best_score_,
            "training_accuracy": self.training_accuracy
        }
    
    def predict(self, input):
        if not self.trained:
            raise ValueError('Model has not been trained yet, Please consider training a model first!')

        return self.model.predict([input])
    
    def fetch_status(self):
        return {
            'is_trained': self.trained,
            'model_algorithm': self.algorithm,
            'best_params': self.best_params,
            'training_accuracy': self.training_accuracy
        }

model = Model()



