import pandas as pd
import xgboost as xgb
from typing import Tuple, Union, List

class DelayModel:

    def __init__(self):
        self._model = None

    def preprocess(self, data: pd.DataFrame, target_column: str = None) -> Union[Tuple[pd.DataFrame, pd.DataFrame], pd.DataFrame]:
        """
        Prepare raw data for training or predict.

        Args:
            data (pd.DataFrame): raw data.
            target_column (str, optional): if set, the target is returned.

        Returns:
            Tuple[pd.DataFrame, pd.DataFrame]: features and target.
            or
            pd.DataFrame: features.
        """
        # Assuming that the data DataFrame contains the same structure as the CSV file
        if target_column:
            features = data.drop(columns=[target_column])
            target = data[target_column]
            return features, target
        else:
            return data

    def fit(self, features: pd.DataFrame, target: pd.Series) -> None:
        """
        Fit model with preprocessed data.

        Args:
            features (pd.DataFrame): preprocessed data.
            target (pd.Series): target.
        """
        # Initialize and fit the XGBoost model
        self._model = xgb.XGBClassifier(random_state=1, learning_rate=0.01)
        self._model.fit(features, target)

    def predict(self, features: pd.DataFrame) -> List[int]:
        """
        Predict delays for new flights.

        Args:
            features (pd.DataFrame): preprocessed data.

        Returns:
            List[int]: predicted targets.
        """
        if self._model is None:
            raise ValueError("The model has not been trained. Please call 'fit' method first.")

        # Make predictions using the trained model
        predictions = self._model.predict(features)
        return predictions

# Example usage:
if __name__ == "__main__":
    # Load your data from '../data/data.csv'
    data = pd.read_csv('../data/data.csv')

    # Initialize the DelayModel instance
    model = DelayModel()

    # Preprocess the data
    features, target = model.preprocess(data, target_column='delay')

    # Fit the model
    model.fit(features, target)

    # Make predictions for new flights
    new_data = pd.DataFrame(...)  # Replace with your new data
    predictions = model.predict(new_data)
