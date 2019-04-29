from tkinter import *
import view
import Applications
import queryDB
from tkinter import ttk
import logging

class MainWindow():
    def __init__(self,uname,pwd):
        self.uname = uname
        self.pwd = pwd
        self.root = Tk()
        self.app = Applications.App(self.root, self.uname)
        self.root.geometry("550x400+200+50")
        self.root["borderwidth"] = 5
        # self.root["pady"] = 5
        self.root["padx"] = 5
        # self.root.resizable(width=False,height=False)
        self.root.title("九型人格测试系统V1.0(当前账户：" + self.uname + ")")
        # Applications.App().showMenu(self.root)
        #显示菜单栏
        view.ShowMenu(self.root,self.app).showMenu()

    def freshTime(self):
        querySQL = queryDB.queryDB()
        tuple_info = querySQL.selectUsers(self.uname, self.pwd)
        cur_time = querySQL.getTestTimeAndType(self.uname)[0]
        self.label_time['text'] = cur_time

    def show(self):
        try:
            if  queryDB.queryDB().selectUsers(self.uname,self.pwd):
                # while True:
                querySQL = queryDB.queryDB()
                tuple_info = querySQL.selectUsers(self.uname,self.pwd)
                cur_time = querySQL.getTestTimeAndType(self.uname)[0]
                print("这是mainwindow")
                print(tuple_info)

                # time.sleep(60)
                # 定义了一个可以分隔显示的区域
                tab_control = ttk.Notebook(self.root)

                tab_user_info = ttk.Frame(tab_control)
                tab_control.add(text="用户信息", child=tab_user_info)
                tab_frame = Frame(tab_user_info, width=480, height=380)
                tab_frame.place(x=0, y=9)
                Label(tab_frame, text="用户名：", width=15, height=2, bg="skyblue", justify="left").place(x=0, y=0)
                Label(tab_frame, text=tuple_info[1], width=20, height=2, bg="lightgreen", justify="left").place(x=120, y=0)

                Label(tab_frame, text="昵  称：", width=15, height=2, bg="skyblue", justify="left").place(x=0, y=45)
                Label(tab_frame, text=tuple_info[3], width=20, height=2, bg="lightgreen", justify="left").place(x=120, y=45)

                Label(tab_frame, text="电  话：", width=15, height=2, bg="skyblue", justify="left").place(x=0, y=90)
                Label(tab_frame, text=tuple_info[4], width=20, height=2, bg="lightgreen", justify="left").place(x=120, y=90)

                Label(tab_frame, text="测试次数：", width=15, height=2, bg="skyblue", justify="left").place(x=0, y=135)
                Label(tab_frame, text=tuple_info[6], width=20, height=2, bg="lightgreen", justify="left").place(x=120,y=135)
                self.label_time = Label(tab_frame, text=cur_time, width=23, height=2, bg="palegreen", justify="left")
                self.label_time.place(x=275,y=135)
                Button(tab_frame,text="刷新",width=14,height=1,bg="lightgreen").place(x=480,y=135)

                Label(tab_frame, text="备  注：", width=15, height=2, bg="skyblue", justify="left").place(x=0, y=180)
                Label(tab_frame, text=tuple_info[5], width=20, height=2, bg="lightgreen", justify="left").place(x=120,y=180)

                Button(tab_frame, text="刷新", width=14, height=1, bg="lightgreen",command=self.freshTime).place(x=120, y=225)
                # ==============================================================================================================
                tab_character_info = ttk.Frame(tab_control)
                tab_control.add(text="性格信息", child=tab_character_info)
                # ==============================================================================================================
                tab_test_info = ttk.Frame(tab_control)
                tab_control.add(text="测试信息", child=tab_test_info)

                # ==============================================================================================================
                Label(self.root, text="九型人格测试系统V1.0", font=("", 26)).pack()
                tab_control.pack(expand=1, fill="both", pady=5)
        except Exception as e:
            print("这是error")
            logging.error(e)
        finally:
            self.root.mainloop()

if __name__ == '__main__':
    uname = "jums"
    pwd = "jums"
    # root = Tk()
    # app = Applications.App(root,uname)
    MainWindow(uname,pwd).show()