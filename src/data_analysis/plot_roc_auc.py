from sklearn.metrics import auc, roc_curve, roc_auc_score, precision_recall_curve, f1_score, average_precision_score
from matplotlib import pyplot


def plot_roc(y_test, probs):
    
    #y_test = Test labels
    #probs =probabilites generated for the test dataset
    
    auc = roc_auc_score(y_test, probs)
    
    print('AUC: %.3f' % auc)
    
    fpr, tpr, _ = roc_curve(y_test, probs)
    pyplot.plot([0, 1], [0, 1], linestyle='--')
    pyplot.plot(fpr, tpr, marker='.')
    pyplot.show()
    
#     fpr, tpr, _ = roc_curve(y_test, y_pred)
#     roc_auc = auc(fpr, tpr)        
#       
#     plt.figure()
#     plt.plot(fpr, tpr, color='blue', lw=1, label='ROC curve (area = %0.2f)' % roc_auc)
#     plt.plot([0, 1], [0, 1], color='navy', lw = 1, linestyle='--')
#     plt.xlim([0.0, 1.0])
#     plt.ylim([0.0, 1.05])
#     plt.xlabel('False Positive Rate')
#     plt.ylabel('True Positive Rate')
#     plt.title('Receiver operating characteristic')
#     plt.legend(loc="lower right")
#     plt.show()

def plot_precision_recall(y_test, y_pred, probs):
    
    precision, recall, _ = precision_recall_curve(y_test, probs)
    f1 = f1_score(y_test, y_pred)
    ares_under_curve = auc(recall, precision)
    ap = average_precision_score(y_test, probs)
    print('f1=%.3f auc=%.3f ap=%.3f' % (f1, ares_under_curve, ap))
    pyplot.plot([0, 1], [0.5, 0.5], linestyle='--')
    pyplot.plot(recall, precision, marker='.')
    pyplot.show()



