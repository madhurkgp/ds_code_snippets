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
