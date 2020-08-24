import pandas as pd
import numpy as np

bp = pd.read_pickle('Features/features_bp.pkl')
cc = pd.read_pickle('Features/features_cc.pkl')
mf = pd.read_pickle('Features/features_mf.pkl')
none = pd.read_pickle('Features/features_None.pkl')

acc = bp['accession']
bp_features = bp['features']
cc_features = cc['features']
mf_features = mf['features']
none_features = none['features']

features = []

for i in range(len(acc)):
    features.append(np.concatenate((
        bp_features[i], 
        cc_features[i],
        mf_features[i],
        none_features[i]), axis=None))

res_df = pd.DataFrame({'accession': acc,'features':features})
res_df.to_pickle('all_features.pkl')