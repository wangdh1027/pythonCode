
#import pandas as pd
#import numpy as np
#from keras.layers.core import Dense, Dropout, Activation, Flatten
#from keras.layers.normalization import BatchNormalization
#from keras.layers import Input
#from keras.utils import np_utils
#from keras.models import Model
#import keras
#import nibabel as nib
#from keras import backend as K
#from keras.datasets import mnist

from tqdm import trange
#from time import sleep
#for i in tqdm(range(1000)):
#    sleep(0.001)

#img_dim = 28
#(x_train, y_train_), (x_test, y_test_) = mnist.load_data()
#
#x_train = x_train.astype('float32') / 255.
#x_test = x_test.astype('float32') / 255.
#
#x_train = x_train.reshape((-1, img_dim, img_dim, 1))
#x_test = x_test.reshape((-1, img_dim, img_dim, 1))
#
#y_train = np_utils.to_categorical(y_train_)
#y_test = np_utils.to_categorical(y_test_)
#x_in = Input(shape=(28,28,1,))
#x = x_in
#x = Flatten()(x)
#x = Dense(100, activation='relu')(x)
#
#x = Dense(10, activation='softmax')(x)
#x_h = x
#model = Model(x_in, x)
#model.compile(loss='categorical_crossentropy',
#              optimizer='adam',
#              metrics=['accuracy'])
#
## 重点来了
#model.metrics_names.append('x_h_norm1')
#model.metrics_tensors.append(K.mean(K.sum(x_h,1)))
#model.metrics_names.append('x_h_norm2')
#model.metrics_tensors.append(K.mean(K.sum(x_h**2,1)))
#model.fit(x_train, y_train,validation_data = (x_test,y_test) ,epochs=5)
#a = model.predict(x_test)
#def addnode(N,List,n,res):
#    print(n)
#    if N==0:
##        print(List)
#        res.append(List)
#    elif n<len(List):
#        if List[n] != None:
#            addnode(N-2,List.copy()+[0,0],n+1,res)
#            addnode(N,List.copy()+[None,None],n+1,res)
#        else:
#            addnode(N,List.copy(),n+1,res)
#def fulltree(N):
#    if N==1:
#        return [0]
#    res = []
#    addnode(N-3,[0,0,0],1,res)
#    
#    return res
#res = fulltree(7)
#print(res)
#
#
#
#
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, discriminant_analysis, model_selection

def load_data():
    diabetes = datasets.load_diabetes()
    return model_selection.train_test_split(diabetes.data, diabetes.target, test_size=0.25, random_state=0)

def test_lasso(*data):
    X_train, X_test, y_train, y_test = data
    lassoRegression = linear_model.Lasso()
    lassoRegression.fit(X_train, y_train)
    print("权重向量:%s, b的值为:%.2f" % (lassoRegression.coef_, lassoRegression.intercept_))
    print("损失函数的值:%.2f" % np.mean((lassoRegression.predict(X_test) - y_test) ** 2))
    print("预测性能得分: %.2f" % lassoRegression.score(X_test, y_test))

#测试不同的α值对预测性能的影响
def test_lasso_alpha(*data):
    X_train, X_test, y_train, y_test = data
    alphas = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
    scores = []
    for i, alpha in enumerate(alphas):
        lassoRegression = linear_model.Lasso(alpha=alpha)
        lassoRegression.fit(X_train, y_train)
        scores.append(lassoRegression.score(X_test, y_test))
    return alphas, scores

def show_plot(alphas, scores):
    figure = plt.figure()
    ax = figure.add_subplot(1, 1, 1)
    ax.plot(alphas, scores)
    ax.set_xlabel(r"$\alpha$")
    ax.set_ylabel(r"score")
    ax.set_xscale("log")
    ax.set_title("Ridge")
    plt.show()

if __name__=='__main__':
    X_train, X_test, y_train, y_test = load_data()
    # 使用默认的alpha
    #test_lasso(X_train, X_test, y_train, y_test)
    # 使用自己设置的alpha
    alphas, scores = test_lasso_alpha(X_train, X_test, y_train, y_test)
    show_plot(alphas, scores)