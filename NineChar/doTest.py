import itemContent
import Applications
import queryDB
from tkinter import *
from tkinter import messagebox

class DoTest_108():
    # scrollregion 定义canvas可以滚动的范围
    def __init__(self, root,uname):
        self.uname = uname
        self.questions_dict = itemContent.questions_dict_108
        # 定义画布
        self.root = root
        self.toplevel = Toplevel(self.root)
        self.toplevel.geometry("720x480+100+30")
        self.toplevel.title("正在做测试108题版(当前账户：" + self.uname + ")")
        self.toplevel.resizable(0,0)
        # self.root["borderwidth"] = 5
        self.app = Applications.App(self.root, self.uname)
        # view.ShowMenu(root=self.root, app=self.app).showMenu()

        self.canvas = Canvas(self.toplevel, width=720, height=480, scrollregion=(0, 0, 29500, 29500), )  # 创建canvas
        self.canvas.pack()  # 放置canvas的位置
        # 定义框架矩形  一个容器
        self.frame = Frame(self.canvas, )  # 把frame放在canvas里
        self.frame.pack()  # frame的长宽，和canvas差不多的
        # 定义一个滚动条
        self.vbar = Scrollbar(self.canvas)  # 竖直滚动条
        self.vbar.place(x=700, width=20, height=480)
        self.vbar.configure(command=self.canvas.yview)
        # 连接画布和滚动条
        self.canvas.config(yscrollcommand=self.vbar.set)  # 设置
        self.canvas.create_window((0, 0), anchor=NW, window=self.frame)  # create_window

        # self.qu_dict = itemContent.questions_dict  # 题目的字典
        self.answer_dict = {}  # 用来存放用户的答案
        self.names = locals()  # 定义了一个产生动态变量名的小函数

        # self.length = len(itemContent.questions_dict)+1
        self.names = locals()

        self.length = len(self.questions_dict)
        # self.yes_no = IntVar()
        self.di = {}#用来放用户已经选择的问题的答案的一个字典

    def selectED(self):
        for i in range(1, self.length+1):
            self.di[self.names["qu%s" % i].get()] = self.names["yes_no%s" % i].get()
        print(self.di)

    def submit(self):
        not_yet_list = []
        answer_list = []
        anaylse = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}
        for value,i in zip(self.di.values(),range(1,self.length+1)):
            if value == -1:
                not_yet_list.append(i)
            elif value == 1 or value == 0:
                answer_list.append(i)
        print(self.di)
        print(not_yet_list)
        if len(answer_list) != 108 and len(not_yet_list) == 0:
            self.label_info["text"] = "你还没开始，怎么就结束了呢。还是答完题再交卷吧"
            # messagebox.showwarning(title="题目没做完",message="你还没开始，怎么就结束了呢。还是答完题在结束吧")
        elif len(not_yet_list)> 0:
            if len(not_yet_list) < 10:
                self.label_info["text"] = "还有%s道题目没有做完%s,不能交卷,"%(str(len(not_yet_list)),str(not_yet_list))
            else:
                self.label_info["text"] = "您还有超过10道以上的题目没有做，请接着做完再交卷吧。"
            # messagebox.showwarning(title='题目没做完',message="还有%s道题目没有做完%s,不能交卷,"%(str(len(not_yet_list)),str(not_yet_list)))
        else:#正式提交
            for ques_item,value in self.di.items():#前者是题目 后者是答案
                char = self.questions_dict[ques_item] #该题目所属于的性格类型
                print(char)
                if value == 1:
                    anaylse[char] += 1
            querySQL = queryDB.queryDB()
            user_id = querySQL.getUserId(uname=self.uname)
            querySQL.insertTestResult(id=user_id,uname=self.uname,test_result=anaylse,test_type="108")
            times = querySQL.getTestTimes(uname=self.uname)
            querySQL.updateTestTime(uname=self.uname,times=times)
            self.label_info["text"] = "检测结果：您更有可能是%s号性格。"% list(anaylse.keys())[list(anaylse.values()).index(sorted(anaylse.values())[-1])]

    def getSpace(self, s):
        if len(s) <= 44:
            # if len(s) % 2 == 0:#偶数
            #     return 50 - (len(s))
            # else:#奇数
            return 40 - (len(s))
        else:
            return 0


    def show(self):
        # 标题
        lable_title = Label(self.frame, text="九型人格测试（108题版）", bg="cyan", width=92, height=3, font=("Arial,36"))
        lable_title.pack()
        ############防止视力疲劳 用不同的颜色显示
        COLOR_1 = "SKYBLUE"
        COLOR_2 = "LIGHTBLUE"
        changeColor = lambda x: COLOR_1 if x % 2 == 0 else COLOR_2
        ############################
        for i in range(1, self.length + 1):
            self.names["yes_no%s" % i] = IntVar()
            self.names["yes_no%s" % i].set(-1)#给题目选项设置一个默认值 0表示否  1表示是  -1表示不选择
            self.names["qu%s" % i] = StringVar()
            self.names["qu%s" % i].set(list(self.questions_dict.keys())[i - 1])
            #本标签用来显示题目
            Label(self.frame, text="%s、%s%s" % (i, self.names["qu%s" % i].get(),"  "*self.getSpace(self.names["qu%s" % i].get())),width=92,height=2,bg=changeColor(i),font=("",12)).pack(pady=5)
            Radiobutton(self.frame, text="是", width=15, height=1, variable=self.names["yes_no%s" % i],
                        value=1, command=self.selectED,bg=changeColor(i)).pack(pady=2)
            Radiobutton(self.frame, text="否", width=15, height=1, variable=self.names["yes_no%s" % i],
                        value=0, command=self.selectED,bg=changeColor(i)).pack(pady=2)
            label_null = Label(self.frame, width=105, height=9).pack()#本标签用来显示一个空白区域
        Button(self.frame, text="交  卷", command=self.submit,width=15,height=1,bg="green",font=("",24)).pack()
        self.label_info = Label(self.frame,text="",fg="red",width=60,height=4,font=("",18))
        self.label_info.pack()

        self.root.mainloop()


class DoTest_144():
    # scrollregion 定义canvas可以滚动的范围
    def __init__(self, root,uname):
        self.uname = uname
        self.questions_dict = itemContent.questions_dict_144
        # 定义画布
        self.root = root
        self.toplevel = Toplevel(self.root)
        self.toplevel.geometry("720x480+100+30")
        self.toplevel.title("正在做测试144题版(当前账户：" + self.uname + ")")
        self.toplevel.resizable(0,0)
        # self.root["borderwidth"] = 5
        self.app = Applications.App(self.root, self.uname)
        # view.ShowMenu(root=self.toplevel, app=self.app).showMenu()

        self.canvas = Canvas(self.toplevel, width=720, height=480, scrollregion=(0, 0, 30500, 30500) )  # 创建canvas
        self.canvas.pack()  # 放置canvas的位置
        # 定义框架矩形  一个容器
        self.frame = Frame(self.canvas ,height=100000 )  # 把frame放在canvas里
        self.frame.pack()  # frame的长宽，和canvas差不多的
        # 定义一个滚动条
        self.vbar = Scrollbar(self.canvas)  # 竖直滚动条
        self.vbar.place(x=700, width=20, height=480)
        self.vbar.configure(command=self.canvas.yview)
        # 连接画布和滚动条
        self.canvas.config(yscrollcommand=self.vbar.set)  # 设置
        self.canvas.create_window((0, 0), anchor=NW, window=self.frame)  # create_window

        # self.qu_dict = itemContent.questions_dict  # 题目的字典
        self.answer_dict = {}  # 用来存放用户的答案
        self.names = locals()  # 定义了一个产生动态变量名的小函数

        # self.length = len(itemContent.questions_dict)+1
        self.length = 6
        self.names = locals()

        self.length = len(self.questions_dict)
        self.yes_no = IntVar()
        self.di = {}

    def getAnswerNum(self,i):
        if str(i / 2).split(".")[-1] != '0':
            # print(i - 1)
            return (i-1)
        else:
            # print(i)
            return i

    def selectED(self):

        print("运行到选择答案")
        for i in range(144):
            # print(self.getAnswerNum(i))
            # self.di[self.questions_dict[int(str(self.names["qu_%s" % i]).split("_")[-1])][self.names["yes_no%s" % i].get()]] = self.names["yes_no%s" % i].get()
            self.di["第%s题答案"% (i+1)] = self.names["yes_no%s" % i].get()
        print(self.di)

    def submit(self):
        answer_dict = itemContent.answer_dict_144 #用来校对答案的一个列表 里面放的是同样的题目和题目所属性格类型，就是格式不一样
        not_yet_list = []
        answer_list = []
        anaylse = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}
        for value, i in zip(self.di.values(), range(1, self.length + 1)):
            if value == -1:
                not_yet_list.append(i)
            elif value ==0 or value == 1:
                answer_list.append(i)
        print(not_yet_list)
        print(answer_list)
        if len(not_yet_list) == 0 and len(answer_list) != 144:
            self.label_info["text"] = "你还没开始，怎么就结束了呢。还是答完题再交卷吧"
            # messagebox.showwarning(title="题目没做完",message="你还没开始，怎么就结束了呢。还是答完题在结束吧")
        elif len(not_yet_list) > 0:
            if len(not_yet_list) < 10:
                self.label_info["text"] = "还有%s道题目没有做完%s,不能交卷," % (str(len(not_yet_list)), str(not_yet_list))
            else:
                self.label_info["text"] = "您还有超过10道以上的题目没有做，请接着做完再交卷吧。"
            # messagebox.showwarning(title='题目没做完',message="还有%s道题目没有做完%s,不能交卷,"%(str(len(not_yet_list)),str(not_yet_list)))
        else:
            for answer_title, answer_num in zip(answer_dict, self.di.values()):
                anaylse[list(answer_title[answer_num].values())[0]] += 1
            querySQL = queryDB.queryDB()
            user_id = querySQL.getUserId(uname=self.uname)
            querySQL.insertTestResult(id=user_id, uname=self.uname, test_result=anaylse, test_type="144")
            times = querySQL.getTestTimes(uname=self.uname)
            querySQL.updateTestTime(uname=self.uname, times=times)
            self.label_info["text"] = "检测结果：您更有可能是%s号性格。" % list(anaylse.keys())[
                list(anaylse.values()).index(sorted(anaylse.values())[-1])]
            print(anaylse)

    def getSpace(self, s):
        if len(s) <= 44:
            # if len(s) % 2 == 0:#偶数
            #     return 50 - (len(s))
            # else:#奇数
            return 38 - (len(s))
        else:
            return 0

    def show(self):
        # 标题
        lable_title = Label(self.frame, text="九型人格测试（144题版）", bg="cyan", width=92, height=3, font=("Arial,36"))
        lable_title.pack()
        ############防止视力疲劳 用不同的颜色显示
        COLOR_1 = "SKYBLUE"
        COLOR_2 = "LIGHTBLUE"
        changeColor = lambda x: COLOR_1 if x % 2 == 0 else COLOR_2
        print("长度:%s"%self.length)
        i = 0
        j = 0
        num = 1
        xia_biao = -1  # 下标 用来取字典中的题目
        while i < 288 and j < 144:
            self.names["yes_no%s" % j] = IntVar()
            self.names["yes_no%s" % j].set(-1)
            self.names["qu_%s" % i] = StringVar()
            self.names["qu_%s" % int(i+1)] = StringVar()
            xia_biao += 1 #全局显示的下标
            # self.names["qu_%s" % i].set(list(self.questions_dict[i][0].keys())[0])
            self.names["qu_%s" % i].set(list(self.questions_dict.keys())[i])
            xia_biao += 1
            # self.names["qu_%s" % int(i+1)].set(list(self.questions_dict[i][1].keys())[0])
            self.names["qu_%s" % int(i + 1)].set(list(self.questions_dict.keys())[i + 1])

            Label(self.frame, text="第%s题:%s" % (num," "*76), width=45, height=2, font=("Arial",18)).pack(pady=2)
            num += 1
            Radiobutton(self.frame, text="%s%s" % ( self.names["qu_%s" % i].get(),"  "*self.getSpace(self.names["qu_%s" % i].get())),value=0,variable=self.names["yes_no%s" % j],
                        width=85,height=2,bg=COLOR_1,command=self.selectED,font=("",12)).pack(pady=1)
            # co_row += 1
            Radiobutton(self.frame, text="%s%s" % (self.names["qu_%s" % int(i+1)].get(),"  "*self.getSpace(self.names["qu_%s" % int(i+1)].get())), value=1,variable=self.names["yes_no%s" % j],
                        width=85, height=2, bg=COLOR_2, command=self.selectED,font=("",12)).pack(pady=1)
            i += 2
            j += 1
            # xia_biao += 2
            Label(self.frame, text="", width=105, height=3, ).pack()
        print(i)
        Label(self.frame, text="", width=105, height=8, ).pack()
        Button(self.frame,text="交  卷",width=15,height=1,font=("",24),bg="green",command=self.submit).pack()
        self.label_info = Label(self.frame, text="", fg="red",font=("",18),width=60, height=4, )
        self.label_info.pack()

        self.root.mainloop()




if __name__ == '__main__':
    root = Tk()

    DoTest_144(root=root,uname="jums").show()





