#Session1
#OS.path() 3P lib so that you don't need to pay attention to should use \ in Win and / in Mac
#enter
#import os
#os.path.join('users','zqqi','Desktop') in Terminal of Pycharm *first type Python

#Session2
#Current folder obtain
# enter os.getcwd() in Terminal of Pycharm *first type Python cwd=current working directory
#os.chdir('/Users/zqqi/Desktop') #change working directory

#Session3
#绝对路径与相对路径
#绝对路径是从跟文件夹开始的
#相对路径是相对于程序的当前工作目录的
    #Num_XIAOFEI_Write&Read的绝对路径
    #/Users/qizhang/PycharmProjects/PythonTrainingONPyCharm/Numpy/Numpy_XIAOFEI_Write&Read Files-1.py
    #Leeson-1相对于Lesson-2的相对路径
    #'.'当前文件夹
    #'..'父文件夹
    #Leeson-1../Lesson-2

#返回绝对路径
    #os.path.abspath('.') #先にimport osを忘れず
#返回相对路径
    #os.path.relpath('/Users/qizhang/PycharmProjects/PythonTrainingONPyCharm/Test/Empty-1.py','/Users/qizhang/PycharmProjects/PythonTrainingONPyCharm/Test/Empty-2.py')
        #Result:'../Empty-1.py'
    #os.path.relpath('Users/qizhang/PycharmProjects/PythonTrainingONPyCharm/Numpy/Numpy_XIAOFEI_Write&Read Files-1.py','/Users/qizhang/PycharmProjects/PythonTrainingONPyCharm/Test/Empty-2.py')
        # Result:'../../../../Users/qizhang/PycharmProjects/PythonTrainingONPyCharm/Numpy/Numpy_XIAOFEI_Write&Read Files-1.py'
#返回最后一个斜杠前的所有内容--目录名
    os.path.dirname('/Users/qizhang/PycharmProjects/PythonTrainingONPyCharm/Test/Empty-1.py')
        #Result: '/Users/qizhang/PycharmProjects/PythonTrainingONPyCharm/Test'
#返回最后一个斜杠后的所有内容--文件名
    os.path.basename('/Users/qizhang/PycharmProjects/PythonTrainingONPyCharm/Test/Empty-1.py')
        #Result：'Empty-1.py'
    os.path.basename('/Users/qizhang/PycharmProjects/PythonTrainingONPyCharm/Test/')
        # Result：''
    os.path.basename('/Users/qizhang/PycharmProjects/PythonTrainingONPyCharm/Test')
    # Result：'Test'

#Pycharm function
    #copy path from content root: Test/Empty-1.py
    #copy path from repository root: Test/Empty-1.py
    #copy absolute path: /Users/qizhang/PycharmProjects/PythonTrainingONPyCharm/Test/Empty-1.py