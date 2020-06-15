#------------Encoding categorical-----------
#OHE encoding
ohe_cols = ['State_ID',
            'branch_id',
            'manufacturer_id',
            #'PERFORM_CNS.SCORE.DESCRIPTION',

            ]

df_all = pd.get_dummies(df_all, columns=ohe_cols)

#----------------------------------
#text classification , tf-idf vecotrizer , sgdclassifier, one vs rest classifier
https://github.com/chetanambi/Innoplexus-Online-Hiring-Hackathon-Sentiment-Analysis/blob/master/Sentiment%20Analysis_Final%20Solution_0.5230949840.ipynb

#date time to unix - i.e. datetime to seconds, date features segregation - 
https://github.com/AnilBetta/AV_JantaHack-IOT-Timeseries-/blob/master/XGBOOST.ipynb

# groupby transform - 
https://github.com/Abhinav-97/JanataHack-Mobility-analytics/blob/master/janataHack-mobility-analytics.ipynb

labelencoder - https://github.com/Sufi737/ecommerce-hackathon/blob/master/code.ipynb



