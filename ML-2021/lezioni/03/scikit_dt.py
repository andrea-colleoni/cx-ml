from sklearn import tree
from sklearn.model_selection import train_test_split

import graphviz 
from IPython.display import Image  
import matplotlib.pyplot as plt

X=[[165,19],[175,32],[136,35],[174,65],[141,28],[176,15]
,[131,32],[166,6],[128,32],[179,10],[136,34],[186,2],[126,25],[176,28],[112,38],
[169,9],[171,36],[116,25],[196,25], [196,38], [126,40], [197,20], [150,25], [140,32],[136,35]]


Y=['Man','Woman','Woman','Man','Woman','Man','Woman','Man','Woman','Man','Woman','Man','Woman',
'Woman','Woman','Man','Woman','Woman','Man', 'Woman', 'Woman', 'Man', 'Man', 'Woman', 'Woman']

data_feature_names = ['height','length of hair']

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.3, random_state = 1)
DTclf = tree.DecisionTreeClassifier()
DTclf = DTclf.fit(X,Y)
prediction = DTclf.predict([[135,2]])
print(prediction)

text_representation = tree.export_text(DTclf)
print(text_representation)

tree.plot_tree(DTclf)

dot_data = tree.export_graphviz(DTclf, out_file='tree.dot', 
                     feature_names=data_feature_names,  
                     class_names=['Man','Woman'],  
                     filled=True, rounded=True,  
                     special_characters=True)  

graph = graphviz.Source(dot_data)  
Image(graph.create_png())