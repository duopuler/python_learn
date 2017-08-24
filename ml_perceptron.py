# encoding:utf-8
# 简单感知器
import numpy as np


class Perceptron(object):
    """
    eta :学习率
    n_iter:权重向量训练次数
    w_:神经元分叉权重向量
    errors_:记录神经元判断出错次数
    """

    def __int__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter
        pass

    def fit(self, x, y):
        """
        输入训练数据,训练神经元,x输入样本向量,y对应样本分类
        :param x: shape[n_samples,n_features]
        x: [[1,2,3],[4,5,6]]
        n_samples: 2
        n_features: 3
        :param y: [1,-1]
        :return: 
        """

        # 初始化权重向量为0,加1为w0项,即阈值
        self.w_ = np.zeros(1 + x.shape[1])
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0
            """
            x: [[1,2,3],[4,5,6]]
            y: [1,-1]
            zip(x,y) = [[1,2,3,1],[4,5,6,-1]]
            
            """

            for xi, target in zip(x, y):
                '''
                update = μ*(y-y')
                '''
                update = self.eta*(target - self.predict())
                # xi是一个向量,update*等价于:
                #更新权重 ▽w(1) = x[1]*update......
                self.w_[1:] += update * xi
                self.w_[0] = update

                errors += int(update != 0.0)
                self.errors_.append(errors)
                pass
            pass

        def net_input(self, x):
            '''
            z = w0*1 + w1*x1 + ...wn*xn
            :param self: 
            :param x: 
            :return: 
            '''
            return np.dot(x,self.w_[1:]) + self.w_[0]
            pass

        def predict(self,x):
            return np.where(self.net_input(x) >= 0.0 , 1, -1)   # 假如某个值大于0,则转换成1,否则用-1代替
            pass
        pass


