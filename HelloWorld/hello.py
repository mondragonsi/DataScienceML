#print hello world
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
print("Hello World")

res = input("Enter your name: ")

print("Hello " + res)

print("voltando pra main")

#convert dataframe column to float

#import matplotlib.pyplot as plt


disp = confusion_matrix(classifier, X_test, y_test, display_labels=class_names)
