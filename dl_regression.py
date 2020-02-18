#adaboost
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor
ada_2 = AdaBoostRegressor(DecisionTreeRegressor(max_depth=22), n_estimators=300, loss='exponential')
ada_2.fit(X2, y2)
yp2 = ada_2.predict(Xv2)


#catboost
from catboost import CatBoostClassifier
cb_model = CatBoostClassifier(iterations=1000,
                              learning_rate=0.083,
                              #depth=7,
                              l2_leaf_reg=5,
                              bootstrap_type='Bernoulli',
                              subsample=0.4,
                              #scale_pos_weight=4,
                              eval_metric='AUC',
                              metric_period=50,
                              od_type='Iter',
                              od_wait=45,
                              random_seed=17,
                              allow_writing_files=False)

cb_model.fit(train_early_x, train_early_y,
             eval_set=(valid_early_x, valid_early_y),
             #cat_features=ohe_cols,
             use_best_model=True,
             #verbose=True
             )

# fea_imp = pd.DataFrame({'imp': cb_model.feature_importances_, 'col': cols})
# fea_imp = fea_imp.sort_values(['imp', 'col'], ascending=[True, False]).iloc[-30:]
print('AUC:', roc_auc_score(valid_early_y, cb_model.predict_proba(valid_early_x)[:, 1]))
y_preds = cb_model.predict_proba(test_df[features])[:, 1]
