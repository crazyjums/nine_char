import tkinter as tk
from tkinter import messagebox
import random

import doTest
import view
import login


'''
定义菜单事件
'''
class App():
    def __init__(self,root,uname=""):
        self.uname = uname
        # self.questions_dict = itemContent.questions_dict
        self.root = root


    #退出程序即关闭窗口的方法
    def quitSystem(self):
        if messagebox.askokcancel(title="确认取消",message="您确定退出吗？"):
            self.root.quit()
            # self.root.destroy()
            exit()

    def myTestResult(self):
        view.ViewMyTestResult(self.root, self.uname ).show()

    def accountCenter(self):
        view.ViewAccountCenter(self.root, self.uname ).show()

    def viewTestQuestions_108(self):
        view.ViewItemContent_108(root=self.root,uname=self.uname).show()

    def viewTestQuestions_144(self):
        view.ViewItemContent_144(root=self.root,uname=self.uname).show()

    def openFile(self):
        view.ViewOpenFile(self.root, self.uname ).show()

    def saveFile(self):
        view.ViewSaveFile(self.root, self.uname).show()

    def testQuestion_108(self):
        doTest.DoTest_108(self.root,self.uname).show()

    def testQuestion_144(self):
        doTest.DoTest_144(self.root,self.uname).show()

    def aboutAuthor(self):
        view.ViewAboutAuthor(self.root, self.uname).show()

    def aboutHowToTest(self):
        view.ViewHowToTest(self.root, self.uname).show()

    def aboutNineCharacter(self):
        view.ViewNineCharacter(self.root, self.uname).show()
        # login.LoginWindow().showLoginWindow()

    def logout(self, root):
        # print("运行到了logout方法")
        root.destroy()

        # self.root.withdraw()#将当前的Tk()对象销毁 一个程序只允许有一个Tk()
        login.LoginWindow().showLoginWindow()
        print("运行到了logout方法")





'''
菜单事件定义结束
'''



def loginSuccess(uname):

    root = tk.Tk()
    # 定义主窗口功能
    # App(uname, itemContent.questions_dict)
    # anseer_dicy = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
    doTest.DoTest_144(root, "测试者").show()



if __name__ == '__main__':
    loginSuccess("测试")
