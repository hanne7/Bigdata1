import pandas as pd
from sklearn import svm, metrics

or_data = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

data = []
label = []
for row in or_data:
    p = row[0]
    q = row[1]
    r = row[2]
    data.append([p, q])
    label.append(r)

clf = svm.SVC()
clf.fit(data, label)
pre = clf.predict(data)
print('예측결과:', pre)

ok = 0
total = 0
for idx, answer in enumerate(label):
    p = pre[idx]
    if p == answer:
        ok += 1
    total += 1
print('정답률 : ', ok, '/', total, '=', ok/total)

or_df = pd.DataFrame(or_data)
or_data2 = or_df.ix[:, 0:1]
and_label = or_df.ix[:, 2]

clf = svm.SVC()
clf.fit(or_data2, and_label)
pre = clf.predict(or_data2)

ac_score = metrics.accuracy_score(and_label, pre)
print()
print(pre)
print('정답률 = ', ac_score)