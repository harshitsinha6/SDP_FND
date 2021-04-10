
# Importing Libraries

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier

class models:
    def __init__(self):
        self.model = None
        self.LR_model = LogisticRegression()
        self.DT_model = DecisionTreeClassifier()
        self.GB_model = GradientBoostingClassifier(random_state=0)
        self.RF_model = RandomForestClassifier(random_state=0)
        
        self.X_train = None
        self.Y_train = None
        self.X_test = None
        self.Y_test = None
        
        self.accuracy_LR_model = 0
        self.accuracy_DT_model = 0
        self.accuracy_GB_model = 0
        self.accuracy_RF_model = 0
        
        self.predLR = None
        self.predDT = None
        self.predGB = None
        self.predRF = None
        
    def feedData(self, X_train, Y_train, X_test, Y_test):
        self.X_train = X_train
        self.Y_train = Y_train
        self.X_test = X_test
        self.Y_test = Y_test
        
    def fit(self):
        self.LR_model.fit(self.X_train, self.Y_train)
        self.DT_model.fit(self.X_train, self.Y_train)
        self.GB_model.fit(self.X_train, self.Y_train)
        self.RF_model.fit(self.X_train, self.Y_train)
        
    def predict(self):
        self.predLR = self.LR_model.predict(self.X_test)
        self.predDT = self.DT_model.predict(self.X_test)
        self.predGB = self.GB_model.predict(self.X_test)
        self.predRF = self.RF_model.predict(self.X_test)
        
    def selectModel(self):
        self.accuracy_LR_model = self.LR_model.score(self.X_test, self.Y_test)
        print("accuracy_LR_model: ", self.accuracy_LR_model)
        self.accuracy_DT_model = self.DT_model.score(self.X_test, self.Y_test)
        print("accuracy_DT_model: ", self.accuracy_DT_model)
        self.accuracy_GB_model = self.GB_model.score(self.X_test, self.Y_test)
        print("accuracy_GB_model: ", self.accuracy_GB_model)
        self.accuracy_RF_model = self.RF_model.score(self.X_test, self.Y_test)
        print("accuracy_RF_model: ", self.accuracy_RF_model)
        
        if self.accuracy_LR_model > self.accuracy_DT_model and self.accuracy_LR_model > self.accuracy_GB_model and self.accuracy_LR_model > self.accuracy_RF_model:
            self.model = self.LR_model
        elif self.accuracy_DT_model > self.accuracy_LR_model and self.accuracy_DT_model > self.accuracy_GB_model and self.accuracy_DT_model > self.accuracy_RF_model:
            self.model = self.DT_model
        elif self.accuracy_GB_model > self.accuracy_LR_model and self.accuracy_GB_model > self.accuracy_DT_model and self.accuracy_DB_model > self.accuracy_RF_model:
            self.model = self.GB_model
        else:
            self.model = self.RF_model
            
    def giveModel(self):
        return self.model
        
        
        
        