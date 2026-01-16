from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, FunctionTransformer
from sklearn.impute import SimpleImputer

def _clip(X):
    return X.clip(-3, 3)

def build_numeric_preprocess():
    """Prétraitement minimal avec clipping."""
    return Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
        ("clip", FunctionTransformer(_clip)),
    ])
# Temporary comment to enable PR
