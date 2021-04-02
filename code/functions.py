from sklearn.metrics import plot_confusion_matrix,\
    precision_score, recall_score, accuracy_score, f1_score, log_loss,\
    roc_curve, roc_auc_score, classification_report, plot_roc_curve
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV,\
    cross_val_score, StratifiedKFold
from sklearn.preprocessing import RobustScaler
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

def csv_write(ticker, df, start, end, intra = ''):
    '''Given a target filepath and a list of fields,
    create a new CSV file and set Headers
    '''
    df.columns = ['open', 'high', 'low', 'close', 'change', 'volume']
    if intra == 'y':
        intra = 'intra'
    csv_filepath = f'data/{ticker}_{intra}_{start}_{end}.csv'
    df.to_csv(csv_filepath, mode='w')

def model_stats(features, model, model_type, X_test, y_test):
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)
    print('Classifier: ', model_type)
    print('Num features: ', features.size)
    print('Model score: ', model.score(X_test, y_test))
    print('Accuracy score: ', accuracy_score(y_test, y_pred))
    print('Model F1 (micro): ', f1_score(y_test, y_pred, average='micro'))
    print('Model F1 (macro): ', f1_score(y_test, y_pred, average='macro'))
    print('Model F1 (weighted): ', f1_score(y_test, y_pred, average='weighted'))
    print('Cross validation score: ', cross_val_score(model, X_test, y_test, cv=5) )
    print('Classification Report:')
    print(classification_report(y_test, y_pred))
    fig, ax = plt.subplots(figsize = [6,5])
    plot_confusion_matrix(model, X_test, y_test, ax = ax)
#     plot_roc_curve(model, X_test_sc, y_test, ax = ax[1])
    ax.set_title(f'{model_type} Confusion Matrix', fontdict = {'fontsize': 14})
    # ax.set_xlabel(xlabel, fontdict = {'fontsize': 12})
    # ax.set_ylabel(f'{model_type} Confusion Matrix', fontdict = {'fontsize': 12})
    macro_roc_auc_ovo = roc_auc_score(y_test, y_prob, multi_class="ovo",
                                  average="macro")
    weighted_roc_auc_ovo = roc_auc_score(y_test, y_prob, multi_class="ovo",
                                         average="weighted")
    macro_roc_auc_ovr = roc_auc_score(y_test, y_prob, multi_class="ovr",
                                      average="macro")
    weighted_roc_auc_ovr = roc_auc_score(y_test, y_prob, multi_class="ovr",
                                         average="weighted")
    print("One-vs-One ROC AUC scores:\n{:.6f} (macro),\n{:.6f} "
          "(weighted by prevalence)"
          .format(macro_roc_auc_ovo, weighted_roc_auc_ovo))
    print("One-vs-Rest ROC AUC scores:\n{:.6f} (macro),\n{:.6f} "
          "(weighted by prevalence)"
          .format(macro_roc_auc_ovr, weighted_roc_auc_ovr))

def dummy_transform_scale(X, y, to_dummy, rs = 729):
    # to_dummy = ['edu', 'hus_edu', 'chil', 'hus_ocu', 'sol']
    X_with_dums = pd.get_dummies(X, columns=to_dummy, drop_first=True)
    # X_with_dums.shape
    X_train, X_test, y_train, y_test = train_test_split(
        X_with_dums, y, test_size = .25,
        random_state = rs)
    # X_train.shape
    rs = RobustScaler()
    rs.fit(X_train)
    X_train = rs.transform(X_train)
    X_test = rs.transform(X_test)
    return X_with_dums, X_train, X_test, y_train, y_test
