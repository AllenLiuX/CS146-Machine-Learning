from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

import time

if __name__ == '__main__':
    start_time = time.time()
    X_train = np.array([[1,2,3],[4,5,6]])
    X_test = np.array([[7, 8, 10], [4, 5, 6]])

    scaler = StandardScaler()
    X_train_std = scaler.fit_transform(X_train)
    # X_val_std = scaler.fit_transform(X_val)
    # X_test_std = scaler.fit_transform(X_test)
    X_test_std = scaler.transform(X_test)
    print(X_train_std)
    print(X_test_std)
    print('======= Time taken: %f =======' %(time.time() - start_time))