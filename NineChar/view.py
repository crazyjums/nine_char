from tkinter import *
import random,logging
import Applications
import itemContent
import queryDB
import string
from tkinter import messagebox

#查看测试题 105
class ViewItemContent_108():
    #scrollregion 定义canvas可以滚动的范围
    def __init__(self,root,uname):
        #定义画布
        self.root = root
        self.top_level = Toplevel(self.root)
        self.top_level.title("查看试题-108题(当前账户：" + uname + ")")
        self.top_level.geometry("720x480+100+30")
        self.questions_dict = itemContent.questions_dict_108
        self.canvas=Canvas(self.top_level,width=720,height=480,scrollregion=(0,0,10000,10000),) #创建canvas
        self.canvas.pack() #放置canvas的位置
        #定义框架矩形  一个容器
        self.frame=Frame(self.canvas) #把frame放在canvas里
        self.frame.pack() #frame的长宽，和canvas差不多的
        #定义一个滚动条
        self.vbar=Scrollbar(self.canvas) #竖直滚动条
        self.vbar.place(x = 700,width=20,height=480)
        self.vbar.configure(command=self.canvas.yview)
        #连接画布和滚动条
        self.canvas.config(yscrollcommand=self.vbar.set) #设置
        self.canvas.create_window((0,0),anchor=NW, window=self.frame)  #create_window

        self.answer_dict = {} #用来存放用户的答案
        self.names = locals()#定义了一个产生动态变量名的小函数

    def getSpace(self, s):
        if len(s) <= 44:
            # if len(s) % 2 == 0:#偶数
            #     return 43 - (len(s)-1)
            # else:#奇数
            return 44 - (len(s)-1)
        else:
            return 0

    #显示题目
    def show(self):
        #标题
        lable_title = Label(self.frame,text="九型人格测试题（108题）%s"%(" "*20),bg="cyan",width=105,height=3,font=("Arial,36"))
        lable_title.pack()
        #定义动态变量名
        names = locals()
        i = 0
        li = list(self.questions_dict.keys())
        COLOR_1 = "skyblue"
        COLOR_2 = "lightblue"
        changeColor = lambda x:COLOR_1 if x % 2 == 0 else COLOR_2
        while len(li):
            # qu_frame = Frame(frame,width=720,height=400,bg="black")
            i += 1

            self.names["qu%s" % i] = li.pop(random.randint(0,len(li)-1))
            self.names["ques%s" % i] = StringVar()
            self.names["ques%s" % i].set(self.names["qu%s" % i] )
            Label(self.frame,text="%s、%s%s"% (str(i),self.names["qu%s" % i],"  "*self.getSpace(self.names["qu%s" % i])) ,width=105,height=2,bg=changeColor(i),justify=RIGHT,font=("",12)).pack(pady=7)
            Label(self.frame,height=2).pack()

#查看测试题 144
class ViewItemContent_144():
    # scrollregion 定义canvas可以滚动的范围
    def __init__(self, root, uname):
        self.uname = uname
        self.questions_dict = itemContent.questions_dict_144
        # 定义画布
        self.root = root
        self.toplevel = Toplevel(self.root)
        self.toplevel.geometry("720x480+100+30")
        self.toplevel.title("查看试题-144题(当前账户：" + self.uname + ")")
        self.toplevel.resizable(0, 0)
        # self.root["borderwidth"] = 5
        self.app = Applications.App(self.root, self.uname)
        # view.ShowMenu(root=self.toplevel, app=self.app).showMenu()

        self.canvas = Canvas(self.toplevel, width=720, height=480, scrollregion=(0, 0, 29000, 29000))  # 创建canvas
        self.canvas.pack()  # 放置canvas的位置
        # 定义框架矩形  一个容器
        self.frame = Frame(self.canvas, height=100000)  # 把frame放在canvas里
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
        lable_title = Label(self.frame, text="九型人格测试题（144题）", bg="cyan", width=92, height=3, font=("Arial,36"))
        lable_title.pack()
        ############防止视力疲劳 用不同的颜色显示
        COLOR_1 = "SKYBLUE"
        COLOR_2 = "LIGHTBLUE"
        changeColor = lambda x: COLOR_1 if x % 2 == 0 else COLOR_2
        print("长度:%s" % self.length)
        i = 0
        j = 0
        num = 1
        xia_biao = -1  # 下标 用来取字典中的题目
        while i < 288 :
            self.names["qu_%s" % i] = StringVar()
            self.names["qu_%s" % int(i + 1)] = StringVar()
            self.names["qu_%s" % i].set(list(self.questions_dict.keys())[i])
            self.names["qu_%s" % int(i + 1)].set(list(self.questions_dict.keys())[i + 1])

            Label(self.frame, text="第%s题:%s" % (num, " " * 76), width=45, height=2, font=("Arial", 18)).pack(pady=2)
            num += 1
            Label(self.frame, text="%s%s" % (self.names["qu_%s" % i].get(), "  " * self.getSpace(self.names["qu_%s" % i].get())),
                        width=85, height=2, bg=COLOR_1,  font=("", 12)).pack(pady=1)
            # co_row += 1
            Label(self.frame, text="%s%s" % (self.names["qu_%s" % int(i + 1)].get(), "  " * self.getSpace(self.names["qu_%s" % int(i + 1)].get())),
                        width=85, height=2, bg=COLOR_2,  font=("", 12)).pack(pady=1)
            i += 2
            Label(self.frame, text="", width=105, height=3, ).pack()

        self.root.mainloop()


#显示关于作者的简介
class ViewAboutAuthor():
    def __init__(self, root, uname):
        self.root = root
        self.uname = uname
        self.top_level = Toplevel(self.root)
        self.top_level.geometry("720x600+160+40")
        self.top_level.resizable(0, 0)
        self.top_level.title("作者简介(当前账户：" + uname + ")")
        self.canvas = Canvas(self.top_level, width=720, height=600, scrollregion=(0, 0, 2000, 2000), )  # 创建canvas
        self.canvas.pack()  # 放置canvas的位置

        self.frame = Frame(self.top_level)
        self.frame.pack()

        # 定义一个滚动条
        self.vbar = Scrollbar(self.canvas)  # 竖直滚动条
        self.vbar.place(x=700, width=20, height=600)
        self.vbar.configure(command=self.canvas.yview)
        # 连接画布和滚动条
        self.canvas.config(yscrollcommand=self.vbar.set)  # 设置
        self.canvas.create_window((0, 0), anchor=NW, window=self.frame)  # create_window

    def show(self):
        about_author = "  作者是一名在校研究生，专业是计算机专业，2018级。由于兴趣，\n" \
                       "自己就写了这么一个程序，其实这个程序也不是很难。只是说由于\n" \
                       "稍微繁杂了一些，逻辑思路很清晰，如果您也想学，可以加我微信\n" \
                       "和我联系。您的鼓励和支持，我将感激不尽！"
        Label(self.frame, text=about_author, bg="snow", width=85, height=5, font=("Arial,36"), justify="left").pack(
            pady=5)
        # 标题
        lable_title = Label(self.frame, text="作者微信", bg="deeppink", fg="white", width=85, height=3, font=("Arial,36"))
        lable_title.pack(padx=5, pady=5)
        self.canvas_wechat = Canvas(self.frame, width=464, height=466, )
        image_wechat = PhotoImage(file=r"g:\software\pycharm\files\NineChar\wechat.png")
        image = self.canvas_wechat.create_image(0, 0, image=image_wechat, anchor="nw")
        self.canvas_wechat.pack()

        lable_alipay = Label(self.frame, text="作者支付宝", bg="skyblue", fg="white", width=85, height=3, font=("Arial,36"))
        lable_alipay.pack(padx=5, pady=5)
        self.canvas_alipay = Canvas(self.frame, width=453, height=453, )
        image_alipay = PhotoImage(file=r"g:\software\pycharm\files\NineChar\alipay.png")
        image = self.canvas_alipay.create_image(0, 0, image=image_alipay, anchor="nw")
        self.canvas_alipay.pack()

        lable_wechatpay = Label(self.frame, text="作者微信收款", bg="lightgreen", fg="white", width=85, height=3,
                                font=("Arial,36"))
        lable_wechatpay.pack(padx=5, pady=5)
        self.canvas_alipay = Canvas(self.frame, width=415, height=415, )
        image_wechatpay = PhotoImage(file=r"g:\software\pycharm\files\NineChar\wechatpay.png")
        image = self.canvas_alipay.create_image(0, 0, image=image_wechatpay, anchor="nw")
        self.canvas_alipay.pack()

        self.root.mainloop()

#显示如何进行测试
class ViewHowToTest():
    #scrollregion 定义canvas可以滚动的范围
    def __init__(self,root,uname):
        #定义画布
        self.root = root
        self.top_level = Toplevel(self.root)
        self.top_level.title("如何测试(当前账户：" + uname + ")")
        self.top_level.geometry("730x380+100+30")
        self.top_level.resizable(0,0)
        self.canvas=Canvas(self.top_level,width=730,height=480,scrollregion=(0,0,500,500)) #创建canvas
        self.canvas.pack() #放置canvas的位置
        #定义框架矩形  一个容器
        self.frame=Frame(self.canvas,height=100) #把frame放在canvas里
        self.frame.pack() #frame的长宽，和canvas差不多的
        #定义一个滚动条
        self.vbar=Scrollbar(self.canvas) #竖直滚动条
        self.vbar.place(x = 710,width=20,height=380)
        self.vbar.configure(command=self.canvas.yview)
        #连接画布和滚动条
        self.canvas.config(yscrollcommand=self.vbar.set) #设置
        self.canvas.create_window((0,0),anchor=NW, window=self.frame)  #create_window

    #显示题目
    def show(self):
        #标题
        lable_title = Label(self.frame,text="如何使用该系统",bg="silver",width=92,height=3,font=("隶书,40"))
        lable_title.grid(row=0,column=0)

        content = '''
        声明：
        1.本系统是一个九型人格测试系统，测试结果仅供参考，不能作为对个人
        的直接评价，具体的性格分析，需要咨询专业的心里医生
        2.本系统会保管好您的个人信息，并且保证不会将您的个人进行非法买卖
        使用方法：
        1.点击测试菜单->108测试或者144测试即可，题目如果没有做完，将不会提交
        2.提交结果之后，分析结果会在菜单关于->测试结果分析中查看
        '''
        s1 = '''1.本系统是一个九型人格测试系统，测试结果仅供参考，不能作为对个人的直接评价，
        具体的性格分析，需要咨询专业的心里医生                                         '''
        s2 = "2.本系统会保管好您的个人信息，并且保证不会将您的个人进行非法买卖            "
        s3 = "1.点击测试菜单->108测试或者144测试即可，题目如果没有做完，将不会提交        "
        s4 = "2.提交结果之后，可以在账户->我的测试结果中查看自己的测试结果                "
        Label(self.frame, text="声明：%s" % (" "*80), width=92, height=2, font=("Arial,24")).grid(row=1,column=0)

        Label(self.frame, text=s1, width=90, height=2, font=("Arial,24")).grid(row=2,column=0)
        Label(self.frame, text=s2, width=90, height=2, font=("Arial,24")).grid(row=3, column=0)

        Label(self.frame, text="使用方法：%s" % (" "*76), width=92, height=2,  font=("Arial,24")).grid(row=4, column=0)
        Label(self.frame, text=s3, width=90, height=2, font=("Arial,24")).grid(row=5, column=0)
        Label(self.frame, text=s4, width=90, height=2, font=("Arial,24")).grid(row=6, column=0)


        # self.frame_content = Label(self.frame,text="asdfdsafasd",bg="blue",width=740,height=10).pack()
        # Label(self.frame,text="新的容器",width=92,height=3,bg="#009900",font=("Arial,24")).pack()


#显示九种性格特征
class ViewNineCharacter():
    #scrollregion 定义canvas可以滚动的范围
    def __init__(self,root,uname):
        #定义画布
        self.root = root
        self.top_level = Toplevel(self.root)
        self.top_level.title("九种性格特征(当前账户：" + uname + ")")
        self.top_level.geometry("730x480+100+30")
        self.top_level.resizable(0,0)
        self.canvas=Canvas(self.top_level,width=730,height=480,scrollregion=(0,0,5200,5200),) #创建canvas
        self.canvas.pack() #放置canvas的位置
        #定义框架矩形  一个容器
        self.frame=Frame(self.canvas) #把frame放在canvas里
        self.frame.pack() #frame的长宽，和canvas差不多的
        #定义一个滚动条
        self.vbar=Scrollbar(self.canvas) #竖直滚动条
        self.vbar.place(x = 710,width=20,height=480)
        self.vbar.configure(command=self.canvas.yview)
        #连接画布和滚动条
        self.canvas.config(yscrollcommand=self.vbar.set) #设置
        self.canvas.create_window((0,0),anchor=NW, window=self.frame)  #create_window

        self.answer_dict = {} #用来存放用户的答案
        self.names = locals()#定义了一个产生动态变量名的小函数

        self.color = "rosybrown"

    def getSpace(self,s):
        if len(s) <= 44:
            if len(s.split(".")[0]) == 1:
                return 43 - (len(s) - 1)
            else:
                return 44 - (len(s) - 1)
        else:
            return 0

    def showOne(self):

        # ======================================1号性格=================================================================
        s1 = "1.内向、被动、批判关注错误，纠正错误、持续监测，喜欢每件事都井井有条，顺序编排；%s" % (
                "  " * self.getSpace("1.内向、被动、批判关注错误，纠正错误、持续监测，喜欢每件事都井井有条，顺序编排；"))
        s2 = "2.急于把事情办好，努力完美；%s" % ("  " * self.getSpace("2.急于把事情办好，努力完美；"))
        s3 = "3.有理性、独立、勤奋工作有责任、成熟、有目标、且看中效率；%s" % ("  " * self.getSpace("3.有理性、独立、勤奋工作有责任、成熟、有目标、且看中效率；"))
        s4 = "4.对自己和他人都很喜欢批评、没耐性、吹毛求疵；先工作，后享乐；%s" % ("  " * self.getSpace("4.对自己和他人都很喜欢批评、没耐性、吹毛求疵；先工作，后享乐；"))
        s5 = "5.压抑冲动和渴望；过度刚性；将高尚作为自己的报酬；%s" % ("  " * self.getSpace("5.压抑冲动和渴望；过度刚性；将高尚作为自己的报酬；"))
        s6 = "6.嘴边常挂着『应该怎样做』这句话；%s" % ("  " * self.getSpace("6.嘴边常挂着『应该怎样做』这句话；"))
        s7 = "7.一向坚持自己的原则，很难容忍其他不同意见；%s" % ("  " * self.getSpace("7.一向坚持自己的原则，很难容忍其他不同意见；"))
        s8 = "8.个性严谨，严格没有笑容，不拘言笑；%s" % ("  " * self.getSpace("8.个性严谨，严格没有笑容，不拘言笑；"))
        s9 = "9.很少顾及家人，喜欢鸡蛋里挑骨头，常埋怨和生气他人做事不够好；%s" % ("  " * self.getSpace("9.很少顾及家人，喜欢鸡蛋里挑骨头，常埋怨和生气他人做事不够好；"))
        s10 = "10.是一个合理、实际、脚踏实地的人。%s" % ("  " * self.getSpace("10.是一个合理、实际、脚踏实地的人。"))

        title_1 = "1号性格(完美主义者）：%s" % ("  " * self.getSpace("1号性格(完美主义者）："))
        Label(self.frame, text=title_1, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=1,
                                                                                                          column=0,
                                                                                                          pady=4)
        Label(self.frame, text=s1, width=92, height=2, font=("Arial,24")).grid(row=2, column=0)
        Label(self.frame, text=s2, width=92, height=2, font=("Arial,24")).grid(row=3, column=0)
        Label(self.frame, text=s3, width=92, height=2, font=("Arial,24")).grid(row=4, column=0)
        Label(self.frame, text=s4, width=92, height=2, font=("Arial,24")).grid(row=5, column=0)
        Label(self.frame, text=s5, width=92, height=2, font=("Arial,24")).grid(row=6, column=0)
        Label(self.frame, text=s6, width=92, height=2, font=("Arial,24")).grid(row=7, column=0)
        Label(self.frame, text=s7, width=92, height=2, font=("Arial,24")).grid(row=8, column=0)
        Label(self.frame, text=s8, width=92, height=2, font=("Arial,24")).grid(row=9, column=0)
        Label(self.frame, text=s9, width=92, height=2, font=("Arial,24")).grid(row=10, column=0)
        Label(self.frame, text=s10, width=92, height=2, font=("Arial,24")).grid(row=11, column=0)

    def showTwo(self):
        # ======================================2号性格=================================================================
        a1 = "1.外向、主动、感情丰富；%s" % ("  " * self.getSpace("1.外向、主动、感情丰富；"))  # 12个中文字符  一个85个英文字符
        a2 = "2.关注去满足重要的其他人；%s" % ("  " * self.getSpace("2.关注去满足重要的其他人；"))
        a3 = "3.乐于付出，努力满足他人的需要；%s" % ("  " * self.getSpace("3.乐于付出，努力满足他人的需要；"))
        a4 = "4.想成为他人不可缺少的；%s" % ("  " * self.getSpace("4.想成为他人不可缺少的；"))
        a5 = "5.压抑或疏忽自己的感受；%s" % ("  " * self.getSpace("5.压抑或疏忽自己的感受；"))
        a6 = "6.有时会有强烈的寂寞感觉；%s" % ("  " * self.getSpace("6.有时会有强烈的寂寞感觉；"))
        a7 = "7.不直接表达自己人感受；%s" % ("  " * self.getSpace("7.不直接表达自己人感受；"))
        a8 = "8.缺乏自主和想法；%s" % ("  " * self.getSpace("8.缺乏自主和想法；"))
        a9 = "9.很希望被他人接受、并获得他人的认同、尊重、爱护及钦佩；%s" % ("  " * self.getSpace("9.很希望被他人接受、并获得他人的认同、尊重、爱护及钦佩；"))
        a10 = "10.喜欢朋友并乐于倾听他们的事情；%s" % ("  " * self.getSpace("10.喜欢朋友并乐于倾听他们的事情；"))
        a11 = "11.对人热情、友善、有爱心和有耐心；%s" % ("  " * self.getSpace("11.对人热情、友善、有爱心和有耐心；"))
        a12 = "12.借着对别人的付出来表现自己；%s" % ("  " * self.getSpace("12.借着对别人的付出来表现自己；"))
        a13 = "13.重视人际关系；%s" % ("  " * self.getSpace("13.重视人际关系；"))
        a14 = "14.不会直接向某人表达自己不满的情绪，但可能会向其他人抱怨；%s" % ("  " * self.getSpace("14.不会直接向某人表达自己不满的情绪，但可能会向其他人抱怨；"))
        a15 = "15.会掩饰或不去触自己的焦虑；%s" % ("  " * self.getSpace("15.会掩饰或不去触自己的焦虑；"))
        a16 = "16.很难拒绝有求于自己的人，即使拨不出时间，也会牺牲自己成全他人；%s" % ("  " * self.getSpace("16.很难拒绝有求于自己的人，即使拨不出时间，也会牺牲自己成全他人；"))
        a17 = "17.是一个关怀、乐于助人、慷慨的人；%s" % ("  " * self.getSpace("17.是一个关怀、乐于助人、慷慨的人；"))

        title_2 = "2号性格(给予者）：%s" % ("  " * self.getSpace("2号性格(给予者）："))
        Label(self.frame, text=title_2, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=12,
                                                                                                               column=0,
                                                                                                               pady=4)
        Label(self.frame, text=a1, width=92, height=2, font=("Arial,24")).grid(row=13, column=0)
        Label(self.frame, text=a2, width=92, height=2, font=("Arial,24")).grid(row=14, column=0)
        Label(self.frame, text=a3, width=92, height=2, font=("Arial,24")).grid(row=15, column=0)
        Label(self.frame, text=a4, width=92, height=2, font=("Arial,24")).grid(row=16, column=0)
        Label(self.frame, text=a5, width=92, height=2, font=("Arial,24")).grid(row=17, column=0)
        Label(self.frame, text=a6, width=92, height=2, font=("Arial,24")).grid(row=18, column=0)
        Label(self.frame, text=a7, width=92, height=2, font=("Arial,24")).grid(row=19, column=0)
        Label(self.frame, text=a8, width=92, height=2, font=("Arial,24")).grid(row=20, column=0)
        Label(self.frame, text=a9, width=92, height=2, font=("Arial,24")).grid(row=21, column=0)
        Label(self.frame, text=a10, width=92, height=2, font=("Arial,24")).grid(row=22, column=0)
        Label(self.frame, text=a11, width=92, height=2, font=("Arial,24")).grid(row=23, column=0)
        Label(self.frame, text=a12, width=92, height=2, font=("Arial,24")).grid(row=24, column=0)
        Label(self.frame, text=a13, width=92, height=2, font=("Arial,24")).grid(row=25, column=0)
        Label(self.frame, text=a14, width=92, height=2, font=("Arial,24")).grid(row=26, column=0)
        Label(self.frame, text=a15, width=92, height=2, font=("Arial,24")).grid(row=27, column=0)
        Label(self.frame, text=a16, width=92, height=2, font=("Arial,24")).grid(row=28, column=0)
        Label(self.frame, text=a17, width=92, height=2, font=("Arial,24")).grid(row=29, column=0)

    def showThree(self):
        # ======================================3号性格=================================================================
        b1 = "1.外向、主动、擅于交际；%s" % ("  " * self.getSpace("1.外向、主动、擅于交际；"))
        b2 = "2.关注任务（包括休息时间）；%s" % ("  " * self.getSpace("2.关注任务（包括休息时间）；"))
        b3 = "3.相信世上无难事，只怕有心人；%s" % ("  " * self.getSpace("3.相信世上无难事，只怕有心人；"))
        b4 = "4.别人会觉得自己是一很有野心的人；%s" % ("  " * self.getSpace("4.别人会觉得自己是一很有野心的人；"))
        b5 = "5.执行、做、争先；%s" % ("  " * self.getSpace("5.执行、做、争先；"))
        b6 = "6.注意力集中在结果，而非意义；%s" % ("  " * self.getSpace("6.注意力集中在结果，而非意义；"))
        b7 = "7.基于成绩，得到认可和接受；%s" % ("  " * self.getSpace("7.基于成绩，得到认可和接受；"))
        b8 = "8.疏忽自己的感受；%s" % ("  " * self.getSpace("8.疏忽自己的感受；"))
        b9 = "9.喜欢与人竞争，借由超越他人来建立自己的优越感；%s" % ("  " * self.getSpace("9.喜欢与人竞争，借由超越他人来建立自己的优越感；"))
        b10 = "10.坚持自己的目标，达不到目标就恼火；效率高，有时会为了求效率而牺牲完美走捷径；%s" % (
                "  " * self.getSpace("10.坚持自己的目标，达不到目标就恼火；效率高，有时会为了求效率而牺牲完美走捷径；"))
        b11 = "11.精力充沛、热爱工作、奋力追求成功、以获得地位和赞赏；%s" % ("  " * self.getSpace("11.精力充沛、热爱工作、奋力追求成功、以获得地位和赞赏；"))
        b12 = "12.为了事业成功、声望、财富，有时牺牲情感、婚姻、家庭或朋友；%s" % ("  " * self.getSpace("12.为了事业成功、声望、财富，有时牺牲情感、婚姻、家庭或朋友；"))
        b13 = "13.是一个受人欣赏、有能力、出众的人；%s" % ("  " * self.getSpace("13.是一个受人欣赏、有能力、出众的人；"))

        title_3 = "3号性格(实干者）：%s" % ("  " * self.getSpace("3号性格(实干者）："))
        Label(self.frame, text=title_3, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=30,
                                                                                                               column=0,
                                                                                                               pady=4)
        Label(self.frame, text=b1, width=92, height=2, font=("Arial,24")).grid(row=31, column=0)
        Label(self.frame, text=b2, width=92, height=2, font=("Arial,24")).grid(row=32, column=0)
        Label(self.frame, text=b3, width=92, height=2, font=("Arial,24")).grid(row=33, column=0)
        Label(self.frame, text=b4, width=92, height=2, font=("Arial,24")).grid(row=34, column=0)
        Label(self.frame, text=b5, width=92, height=2, font=("Arial,24")).grid(row=35, column=0)
        Label(self.frame, text=b6, width=92, height=2, font=("Arial,24")).grid(row=36, column=0)
        Label(self.frame, text=b7, width=92, height=2, font=("Arial,24")).grid(row=37, column=0)
        Label(self.frame, text=b8, width=92, height=2, font=("Arial,24")).grid(row=38, column=0)
        Label(self.frame, text=b9, width=92, height=2, font=("Arial,24")).grid(row=39, column=0)
        Label(self.frame, text=b10, width=92, height=2, font=("Arial,24")).grid(row=40, column=0)
        Label(self.frame, text=b11, width=92, height=2, font=("Arial,24")).grid(row=41, column=0)
        Label(self.frame, text=b12, width=92, height=2, font=("Arial,24")).grid(row=42, column=0)
        Label(self.frame, text=b13, width=92, height=2, font=("Arial,24")).grid(row=43, column=0)

    def showFour(self):
        # ======================================4号性格=================================================================
        c1 = "1.内向，被动，多愁善感、感情丰富；%s" % ("  " * self.getSpace("1.内向，被动，多愁善感、感情丰富；"))
        c2 = "2.关注什么是重大损失；%s" % ("  " * self.getSpace("2.关注什么是重大损失；"))
        c3 = "3.特别被人生哀愁、悲剧所触动；%s" % ("  " * self.getSpace("3.特别被人生哀愁、悲剧所触动；"))
        c4 = "4.认为被他人误解是一件特别痛苦的事；%s" % ("  " * self.getSpace("4.认为被他人误解是一件特别痛苦的事；"))
        c5 = "5.把焦点放在关系和感觉上；%s" % ("  " * self.getSpace("5.把焦点放在关系和感觉上；"))
        c6 = "6.和不熟的人交往时，会表现沉默和冷淡；%s" % ("  " * self.getSpace("6.和不熟的人交往时，会表现沉默和冷淡；"))
        c7 = "7.不开心时，喜欢独自一人来处理不开心的情绪；%s" % ("  " * self.getSpace("7.不开心时，喜欢独自一人来处理不开心的情绪；"))
        c8 = "8.对不符合自己心意的人，会表出拒人以千里之外的态度；%s" % ("  " * self.getSpace("8.对不符合自己心意的人，会表出拒人以千里之外的态度；"))
        c9 = "9.对别人的痛苦具有深层且天赋的同情心，会立刻抛开自己的烦恼，去支持帮助在痛苦中的人；%s" % (
                "  " * self.getSpace("9.对别人的痛苦具有深层且天赋的同情心，会立刻抛开自己的烦恼，去支持帮助在痛苦中的人；"))
        c10 = "10.创造力、热情和丰富的感情很多时吸引了其他人；%s" % ("  " * self.getSpace("10.创造力、热情和丰富的感情很多时吸引了其他人；"))
        c11 = "11.当遭到拒绝、挫折时，便会退缩，变得沉默、害羞；%s" % ("  " * self.getSpace("11.当遭到拒绝、挫折时，便会退缩，变得沉默、害羞；"))
        c12 = "12.有时会感到忧郁，心中有很多梦想和理想，可总是很难实现他们；%s" % ("  " * self.getSpace("12.有时会感到忧郁，心中有很多梦想和理想，可总是很难实现他们；"))
        c13 = "13.比一般人感受更深并怀疑那些总是很快乐的人；%s" % ("  " * self.getSpace("13.比一般人感受更深并怀疑那些总是很快乐的人；"))
        c14 = "14.是一个直觉、敏感、有创造力及理想化的人；%s" % ("  " * self.getSpace("14.是一个直觉、敏感、有创造力及理想化的人；"))

        title_4 = "4号性格(悲情浪漫者）：%s" % ("  " * self.getSpace("4号性格(悲情浪漫者）："))
        Label(self.frame, text=title_4, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=44,
                                                                                                               column=0,
                                                                                                               pady=4)
        Label(self.frame, text=c1, width=92, height=2, font=("Arial,24")).grid(row=45, column=0)
        Label(self.frame, text=c2, width=92, height=2, font=("Arial,24")).grid(row=46, column=0)
        Label(self.frame, text=c3, width=92, height=2, font=("Arial,24")).grid(row=47, column=0)
        Label(self.frame, text=c4, width=92, height=2, font=("Arial,24")).grid(row=48, column=0)
        Label(self.frame, text=c5, width=92, height=2, font=("Arial,24")).grid(row=49, column=0)
        Label(self.frame, text=c6, width=92, height=2, font=("Arial,24")).grid(row=50, column=0)
        Label(self.frame, text=c7, width=92, height=2, font=("Arial,24")).grid(row=51, column=0)
        Label(self.frame, text=c8, width=92, height=2, font=("Arial,24")).grid(row=52, column=0)
        Label(self.frame, text=c9, width=92, height=2, font=("Arial,24")).grid(row=53, column=0)
        Label(self.frame, text=c10, width=92, height=2, font=("Arial,24")).grid(row=54, column=0)
        Label(self.frame, text=c11, width=92, height=2, font=("Arial,24")).grid(row=55, column=0)
        Label(self.frame, text=c12, width=92, height=2, font=("Arial,24")).grid(row=56, column=0)
        Label(self.frame, text=c13, width=92, height=2, font=("Arial,24")).grid(row=57, column=0)
        Label(self.frame, text=c14, width=92, height=2, font=("Arial,24")).grid(row=58, column=0)

    def showFive(self):
        # ======================================5号性格=================================================================
        d1 = "1.内向，被动，自我，喜欢思考；%s" % ("  " * self.getSpace("1.内向，被动，自我，喜欢思考；"))
        d2 = "2.关注探究，思考代替行动；%s" % ("  " * self.getSpace("2.关注探究，思考代替行动；"))
        d3 = "3.与感觉相分离，讨厌情绪激动；%s" % ("  " * self.getSpace("3.与感觉相分离，讨厌情绪激动；"))
        d4 = "4.自我满足和简单化；%s" % ("  " * self.getSpace("4.自我满足和简单化；"))
        d5 = "5.贪求或积攒时间、空间、知识；%s" % ("  " * self.getSpace("5.贪求或积攒时间、空间、知识；"))
        d6 = "6.不擅长对他人说好听的话；%s" % ("  " * self.getSpace("6.不擅长对他人说好听的话；"))
        d7 = "7.喜欢别人扮演自己的学问和知识；%s" % ("  " * self.getSpace("7.喜欢别人扮演自己的学问和知识；"))
        d8 = "8.很难表达自己心中的感受；%s" % ("  " * self.getSpace("8.很难表达自己心中的感受；"))
        d9 = "9.不喜欢娱乐活动，在人际关系上显得比较木讷和保持理性的状态；%s" % ("  " * self.getSpace("9.不喜欢娱乐活动，在人际关系上显得比较木讷和保持理性的状态；"))
        d10 = "10.寻求独自感觉，不喜欢自己的空间受到骚扰；%s" % ("  " * self.getSpace("10.寻求独自感觉，不喜欢自己的空间受到骚扰；"))
        d11 = "11.喜欢自己解决问题或制定计划并执行一项计划；%s" % ("  " * self.getSpace("11.喜欢自己解决问题或制定计划并执行一项计划；"))
        d12 = "12.不喜欢过度计划的生活和每周一次的例会；%s" % ("  " * self.getSpace("12.不喜欢过度计划的生活和每周一次的例会；"))
        d13 = "13.是一个理解力强、重分析、好奇心强、有洞察力的人；%s" % ("  " * self.getSpace("13.是一个理解力强、重分析、好奇心强、有洞察力的人；"))

        title_5 = "5号性格(观察者）：%s" % ("  " * self.getSpace("5号性格(观察者）："))
        Label(self.frame, text=title_5, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=59,
                                                                                                               column=0,
                                                                                                               pady=4)
        Label(self.frame, text=d1, width=92, height=2, font=("Arial,24")).grid(row=60, column=0)
        Label(self.frame, text=d2, width=92, height=2, font=("Arial,24")).grid(row=61, column=0)
        Label(self.frame, text=d3, width=92, height=2, font=("Arial,24")).grid(row=62, column=0)
        Label(self.frame, text=d4, width=92, height=2, font=("Arial,24")).grid(row=63, column=0)
        Label(self.frame, text=d5, width=92, height=2, font=("Arial,24")).grid(row=64, column=0)
        Label(self.frame, text=d6, width=92, height=2, font=("Arial,24")).grid(row=65, column=0)
        Label(self.frame, text=d7, width=92, height=2, font=("Arial,24")).grid(row=66, column=0)
        Label(self.frame, text=d8, width=92, height=2, font=("Arial,24")).grid(row=67, column=0)
        Label(self.frame, text=d9, width=92, height=2, font=("Arial,24")).grid(row=68, column=0)
        Label(self.frame, text=d10, width=92, height=2, font=("Arial,24")).grid(row=69, column=0)
        Label(self.frame, text=d11, width=92, height=2, font=("Arial,24")).grid(row=70, column=0)
        Label(self.frame, text=d12, width=92, height=2, font=("Arial,24")).grid(row=71, column=0)
        Label(self.frame, text=d13, width=92, height=2, font=("Arial,24")).grid(row=72, column=0)

    def showSix(self):
        # ======================================6号性格=================================================================
        e1 = "1.内向、主动、保守、忠诚；关注潜在的伤害、危险、威胁；%s" % ("  " * self.getSpace("1.内向、主动、保守、忠诚；关注潜在的伤害、危险、威胁；"))
        e2 = "2.关注潜在的伤害、危险、威胁；%s" % ("  " * self.getSpace("2.关注潜在的伤害、危险、威胁；"))
        e3 = "3.积极想像：放大危险、灾害；质疑并反向思维；%s" % ("  " * self.getSpace("3.积极想像：放大危险、灾害；质疑并反向思维；"))
        e4 = "4.延迟是因为担心成果不安全；%s" % ("  " * self.getSpace("4.延迟是因为担心成果不安全；"))
        e5 = "5.不会轻易相信别人，但内心深处希望得到别人欣赏和肯定；%s" % ("  " * self.getSpace("5.不会轻易相信别人，但内心深处希望得到别人欣赏和肯定；"))
        e6 = "6.经常犹豫不决，对事情通常想的太认真，很在意配偶及伙伴的想法；%s" % ("  " * self.getSpace("6.经常犹豫不决，对事情通常想的太认真，很在意配偶及伙伴的想法；"))
        e7 = "7.常充满矛盾，希望寻求权威的庇护，但又不相信权威，渴望别人喜欢，但又怀疑别人；%s" % (
                "  " * self.getSpace("7.常充满矛盾，希望寻求权威的庇护，但又不相信权威，渴望别人喜欢，但又怀疑别人；"))
        e8 = "8.期望公平，要求付出和所得是相匹配的，别人会觉得斤斤计较；%s" % ("  " * self.getSpace("8.期望公平，要求付出和所得是相匹配的，别人会觉得斤斤计较；"))
        e9 = "9.会常常提防别人陷害和利用，所以常和人保持一种安全距离，因此别人也觉得自己不容易相处；%s" % (
                "  " * self.getSpace("9.会常常提防别人陷害和利用，所以常和人保持一种安全距离，因此别人也觉得自己不容易相处；"))
        e10 = "10.常问自己是否有做错事，因为害怕错误而被责备；%s" % ("  " * self.getSpace("10.常问自己是否有做错事，因为害怕错误而被责备；"))
        e11 = "11.一个忠诚、值得信赖、勤奋的人；%s" % ("  " * self.getSpace("11.一个忠诚、值得信赖、勤奋的人；"))

        title_6 = "6号性格(怀疑论者）：%s" % ("  " * self.getSpace("6号性格(怀疑论者）："))
        Label(self.frame, text=title_6, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=73,
                                                                                                               column=0,
                                                                                                               pady=4)
        Label(self.frame, text=e1, width=92, height=2, font=("Arial,24")).grid(row=74, column=0)
        Label(self.frame, text=e2, width=92, height=2, font=("Arial,24")).grid(row=75, column=0)
        Label(self.frame, text=e3, width=92, height=2, font=("Arial,24")).grid(row=76, column=0)
        Label(self.frame, text=e4, width=92, height=2, font=("Arial,24")).grid(row=77, column=0)
        Label(self.frame, text=e5, width=92, height=2, font=("Arial,24")).grid(row=78, column=0)
        Label(self.frame, text=e6, width=92, height=2, font=("Arial,24")).grid(row=79, column=0)
        Label(self.frame, text=e7, width=92, height=2, font=("Arial,24")).grid(row=80, column=0)
        Label(self.frame, text=e8, width=92, height=2, font=("Arial,24")).grid(row=81, column=0)
        Label(self.frame, text=e9, width=92, height=2, font=("Arial,24")).grid(row=82, column=0)
        Label(self.frame, text=e10, width=92, height=2, font=("Arial,24")).grid(row=83, column=0)
        Label(self.frame, text=e11, width=92, height=2, font=("Arial,24")).grid(row=84, column=0)

    def showSeven(self):
        # ======================================7号性格=================================================================
        f1 = "1.外向、主动、乐观、贪玩；%s" % ("  " * self.getSpace("1.外向、主动、乐观、贪玩；"))
        f2 = "2.关注什么是未来可能的；%s" % ("  " * self.getSpace("2.关注什么是未来可能的；"))
        f3 = "3.乐于探索，多种选择；%s" % ("  " * self.getSpace("3.乐于探索，多种选择；"))
        f4 = "4.不喜欢接受规范，不想被约束；%s" % ("  " * self.getSpace("4.不喜欢接受规范，不想被约束；"))
        f5 = "5.对有兴趣的事很入迷；不善于处理繁琐和细节的任务；%s" % ("  " * self.getSpace("5.对有兴趣的事很入迷；不善于处理繁琐和细节的任务；"))
        f6 = "6.贪图经历和享受，经历比成功更重要；%s" % ("  " * self.getSpace("6.贪图经历和享受，经历比成功更重要；"))
        f7 = "7.头脑灵活，变通快，多计，勇于尝试，富有冒险精神；%s" % ("  " * self.getSpace("7.头脑灵活，变通快，多计，勇于尝试，富有冒险精神；"))
        f8 = "8.总是放任自己，喜欢我行我素，认为『只要我喜欢，有什么不可以。』%s" % ("  " * self.getSpace("8.总是放任自己，喜欢我行我素，认为『只要我喜欢，有什么不可以。』"))
        f9 = "9.讨厌无聊，喜欢尽可能忙碌，认识很多朋友，每天活动都排得满满的；%s" % ("  " * self.getSpace("9.讨厌无聊，喜欢尽可能忙碌，认识很多朋友，每天活动都排得满满的；"))
        f10 = "10.喜欢刺激和紧张的关系，而不喜欢稳定和依赖的关系；%s" % ("  " * self.getSpace("10.喜欢刺激和紧张的关系，而不喜欢稳定和依赖的关系；"))
        f11 = "11.很少用心去聆听别人的感受，所以很难了解别人的内心感受；%s" % ("  " * self.getSpace("11.很少用心去聆听别人的感受，所以很难了解别人的内心感受；"))
        f12 = "12.喜欢上餐馆、娱乐、旅行或同朋友谈天说地的美好享受；%s" % ("  " * self.getSpace("12.喜欢上餐馆、娱乐、旅行或同朋友谈天说地的美好享受；"))
        f13 = "13.是一个快乐、热心、思想正面的人；%s" % ("  " * self.getSpace("13.是一个快乐、热心、思想正面的人；"))

        title_7 = "7号性格(享乐主义者）：%s" % ("  " * self.getSpace("7号性格(享乐主义者）："))
        Label(self.frame, text=title_7, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=85,
                                                                                                               column=0,
                                                                                                               pady=4)
        Label(self.frame, text=f1, width=92, height=2, font=("Arial,24")).grid(row=86, column=0)
        Label(self.frame, text=f2, width=92, height=2, font=("Arial,24")).grid(row=87, column=0)
        Label(self.frame, text=f3, width=92, height=2, font=("Arial,24")).grid(row=88, column=0)
        Label(self.frame, text=f4, width=92, height=2, font=("Arial,24")).grid(row=89, column=0)
        Label(self.frame, text=f5, width=92, height=2, font=("Arial,24")).grid(row=90, column=0)
        Label(self.frame, text=f6, width=92, height=2, font=("Arial,24")).grid(row=91, column=0)
        Label(self.frame, text=f7, width=92, height=2, font=("Arial,24")).grid(row=92, column=0)
        Label(self.frame, text=f8, width=92, height=2, font=("Arial,24")).grid(row=93, column=0)
        Label(self.frame, text=f9, width=92, height=2, font=("Arial,24")).grid(row=94, column=0)
        Label(self.frame, text=f10, width=92, height=2, font=("Arial,24")).grid(row=95, column=0)
        Label(self.frame, text=f11, width=92, height=2, font=("Arial,24")).grid(row=96, column=0)
        Label(self.frame, text=f12, width=92, height=2, font=("Arial,24")).grid(row=97, column=0)
        Label(self.frame, text=f13, width=92, height=2, font=("Arial,24")).grid(row=98, column=0)

    def showEight(self):
        # ======================================8号性格=================================================================
        g1 = "1.外向、主动、乐观、冲动、专制、有正义感；%s" % ("  " * self.getSpace("1.外向、主动、乐观、冲动、专制、有正义感；"))
        g2 = "2.关注权力、独断，并且控制空间和领域；%s" % ("  " * self.getSpace("2.关注权力、独断，并且控制空间和领域；"))
        g3 = "3.充满活力，讨厌虚伪，喜欢危险和冒险的刺激感；%s" % ("  " * self.getSpace("3.充满活力，讨厌虚伪，喜欢危险和冒险的刺激感；"))
        g4 = "4.愤怒爆发直接、面对面、硬碰硬；%s" % ("  " * self.getSpace("4.愤怒爆发直接、面对面、硬碰硬；"))
        g5 = "5.很难听从别人的意见；%s" % ("  " * self.getSpace("5.很难听从别人的意见；"))
        g6 = "6.相信“强权就是公理”，别人会觉得专横霸道；%s" % ("  " * self.getSpace("6.相信“强权就是公理”，别人会觉得专横霸道；"))
        g7 = "7.喜欢被人尊重而不是被人喜爱；%s" % ("  " * self.getSpace("7.喜欢被人尊重而不是被人喜爱；"))
        g8 = "8.通常会支持比较弱势或不利的一方；%s" % ("  " * self.getSpace("8.通常会支持比较弱势或不利的一方；"))
        g9 = "9.会保护、支持自己的朋友、家人和下属；%s" % ("  " * self.getSpace("9.会保护、支持自己的朋友、家人和下属；"))
        g10 = "10.喜欢控制大局和授权给别人的乐趣，但却不喜欢被控制；%s" % ("  " * self.getSpace("10.喜欢控制大局和授权给别人的乐趣，但却不喜欢被控制；"))
        g11 = "11.有坚强的意志力，相信自己能战胜一切挑战和困境而会有突破；%s" % ("  " * self.getSpace("11.有坚强的意志力，相信自己能战胜一切挑战和困境而会有突破；"))
        g12 = "12.不喜欢求人，觉得求人不如求自己，所以不停地增值自己的能力；%s" % ("  " * self.getSpace("12.不喜欢求人，觉得求人不如求自己，所以不停地增值自己的能力；"))
        g13 = "13.对家人粗心大意，缺乏温柔及很难站在对方的立场来思考。%s" % ("  " * self.getSpace("13.对家人粗心大意，缺乏温柔及很难站在对方的立场来思考。"))
        g14 = "14.但是一个负责任的好丈夫、好妻子；%s" % ("  " * self.getSpace("14.但是一个负责任的好丈夫、好妻子；"))
        g15 = "15.是一个坚强、自信、果断和会马上采取行动去解决问题的人；%s" % ("  " * self.getSpace("15.是一个坚强、自信、果断和会马上采取行动去解决问题的人；"))

        title_8 = "8号性格(保护者）：%s" % ("  " * self.getSpace("8号性格(保护者）："))
        Label(self.frame, text=title_8, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=99,
                                                                                                               column=0,
                                                                                                               pady=4)
        Label(self.frame, text=g1, width=92, height=2, font=("Arial,24")).grid(row=100, column=0)
        Label(self.frame, text=g2, width=92, height=2, font=("Arial,24")).grid(row=101, column=0)
        Label(self.frame, text=g3, width=92, height=2, font=("Arial,24")).grid(row=102, column=0)
        Label(self.frame, text=g4, width=92, height=2, font=("Arial,24")).grid(row=103, column=0)
        Label(self.frame, text=g5, width=92, height=2, font=("Arial,24")).grid(row=104, column=0)
        Label(self.frame, text=g6, width=92, height=2, font=("Arial,24")).grid(row=105, column=0)
        Label(self.frame, text=g7, width=92, height=2, font=("Arial,24")).grid(row=106, column=0)
        Label(self.frame, text=g8, width=92, height=2, font=("Arial,24")).grid(row=107, column=0)
        Label(self.frame, text=g9, width=92, height=2, font=("Arial,24")).grid(row=108, column=0)
        Label(self.frame, text=g10, width=92, height=2, font=("Arial,24")).grid(row=109, column=0)
        Label(self.frame, text=g11, width=92, height=2, font=("Arial,24")).grid(row=110, column=0)
        Label(self.frame, text=g12, width=92, height=2, font=("Arial,24")).grid(row=111, column=0)
        Label(self.frame, text=g13, width=92, height=2, font=("Arial,24")).grid(row=112, column=0)
        Label(self.frame, text=g14, width=92, height=2, font=("Arial,24")).grid(row=113, column=0)
        Label(self.frame, text=g15, width=92, height=2, font=("Arial,24")).grid(row=114, column=0)

    def showNine(self):
        # ======================================9号性格=================================================================
        i1 = "1.内向、被动、乐观、随和；%s" % ("  " * self.getSpace("1.内向、被动、乐观、随和；"))
        i2 = "2.关注周围对其的抱怨；%s" % ("  " * self.getSpace("2.关注周围对其的抱怨；"))
        i3 = "3.顺从、服务、很难说不；%s" % ("  " * self.getSpace("3.顺从、服务、很难说不；"))
        i4 = "4.向往相容和熟悉，避免冲突；%s" % ("  " * self.getSpace("4.向往相容和熟悉，避免冲突；"))
        i5 = "5.拙于排列事情的优先顺序；%s" % ("  " * self.getSpace("5.拙于排列事情的优先顺序；"))
        i6 = "6.不像其他人那样关注名誉及地位；%s" % ("  " * self.getSpace("6.不像其他人那样关注名誉及地位；"))
        i7 = "7.别人会觉得自己动作很慢、经常拖延而不去行动；%s" % ("  " * self.getSpace("7.别人会觉得自己动作很慢、经常拖延而不去行动；"))
        i8 = "8.时常因为问题而懒脑但却不去解决，特别喜欢睡觉和看电视容易耽误事情，别人会觉得其%s" % (
                "  " * self.getSpace("8.时常因为问题而懒脑但却不去解决，特别喜欢睡觉和看电视容易耽误事情，别人会觉得其"))
        i9 = "      被动和优柔寡断；%s" % ("  " * self.getSpace("被动和优柔寡断；"))
        i10 = "9.不喜欢命令别人，但当别人命令自己时，会反感和变得倔强对于不同观点的分歧和争论，%s" % ("  " * self.getSpace("9.不喜欢命令别人，但当别人命令自己时，会反感和变得倔强对于不同观点的分歧和争论，"))
        i11 = "      能看到其方方面面是一个和平、友善、随和、包容和忍耐的人。%s" % ("  " * self.getSpace("能看到其方方面面是一个和平、友善、随和、包容和忍耐的人。"))
        # i10 = "   9.不喜欢命令别人，但当别人命令自己时，会反感和变得倔强对于不同观点的分歧%s" % (
        #         "  " * self.getSpace("9不喜欢命令别人，但当别人命令自己时，会反感和变得倔强对于不同观点的分歧"))
        # i11 = "和争论，能看到其方方面面是一个和平、友善、随和、包容和忍耐的人。%s" % (
        #         "  " * self.getSpace("和争论，能看到其方方面面是一个和平、友善、随和、包容和忍耐的人。"))

        title_9 = "9号性格(调停者）：%s" % ("  " * self.getSpace("9号性格(调停者）："))
        Label(self.frame, text=title_9, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=115,
                                                                                                               column=0,
                                                                                                               pady=4)
        Label(self.frame, text=i1, width=92, height=2, font=("Arial,24")).grid(row=116, column=0)
        Label(self.frame, text=i2, width=92, height=2, font=("Arial,24")).grid(row=117, column=0)
        Label(self.frame, text=i3, width=92, height=2, font=("Arial,24")).grid(row=118, column=0)
        Label(self.frame, text=i4, width=92, height=2, font=("Arial,24")).grid(row=119, column=0)
        Label(self.frame, text=i5, width=92, height=2, font=("Arial,24")).grid(row=120, column=0)
        Label(self.frame, text=i6, width=92, height=2, font=("Arial,24")).grid(row=121, column=0)
        Label(self.frame, text=i7, width=92, height=2, font=("Arial,24")).grid(row=122, column=0)
        Label(self.frame, text=i8, width=92, height=2, font=("Arial,24")).grid(row=123, column=0)
        Label(self.frame, text=i9, width=92, height=2, font=("Arial,24")).grid(row=124, column=0)
        Label(self.frame, text=i10, width=92, height=2, font=("Arial,24")).grid(row=125, column=0)
        Label(self.frame, text=i11, width=92, height=2, font=("Arial,24")).grid(row=126, column=0)

    #显示题目
    def show(self):
        #标题
        lable_title = Label(self.frame,text="九种性格特征",fg="white",bg="silver",width=92,height=3,font=("Arial,36"))
        lable_title.grid(row=0,column=0)
        self.showOne()
        self.showTwo()
        self.showThree()
        self.showFour()
        self.showFive()
        self.showSix()
        self.showSeven()
        self.showEight()
        self.showNine()


#打开文件
class ViewOpenFile():
    #scrollregion 定义canvas可以滚动的范围
    def __init__(self,root,uname):
        #定义画布
        self.root = root
        self.top_level = Toplevel(self.root)
        self.top_level.title("打开文件(当前账户：" + uname + ")")
        self.top_level.geometry("720x480+100+30")
        self.canvas=Canvas(self.top_level,width=720,height=480,scrollregion=(0,0,6000,6000),) #创建canvas
        self.canvas.pack() #放置canvas的位置
        #定义框架矩形  一个容器
        self.frame=Frame(self.canvas) #把frame放在canvas里
        self.frame.pack() #frame的长宽，和canvas差不多的
        #定义一个滚动条
        self.vbar=Scrollbar(self.canvas) #竖直滚动条
        self.vbar.place(x = 700,width=20,height=480)
        self.vbar.configure(command=self.canvas.yview)
        #连接画布和滚动条
        self.canvas.config(yscrollcommand=self.vbar.set) #设置
        self.canvas.create_window((0,0),anchor=NW, window=self.frame)  #create_window

        self.answer_dict = {} #用来存放用户的答案
        self.names = locals()#定义了一个产生动态变量名的小函数

    #显示题目
    def show(self):
        #标题
        lable_title = Label(self.frame,text="打开文件",bg="hotpink",width=92,height=3,font=("Arial,36"))
        lable_title.pack(pady=9)

        lable_author = Label(self.frame, text="显示打开文件", bg="hotpink", width=92, height=3, font=("Arial,24"))
        lable_author.pack()

#保存文件
class ViewSaveFile():
    #scrollregion 定义canvas可以滚动的范围
    def __init__(self,root,uname):
        #定义画布
        self.root = root
        self.top_level = Toplevel(self.root)
        self.top_level.title("保存文件(当前账户：" + uname + ")")
        self.top_level.geometry("720x480+100+30")
        self.canvas=Canvas(self.top_level,width=720,height=480,scrollregion=(0,0,6000,6000),) #创建canvas
        self.canvas.pack() #放置canvas的位置
        #定义框架矩形  一个容器
        self.frame=Frame(self.canvas) #把frame放在canvas里
        self.frame.pack() #frame的长宽，和canvas差不多的
        #定义一个滚动条
        self.vbar=Scrollbar(self.canvas) #竖直滚动条
        self.vbar.place(x = 700,width=20,height=480)
        self.vbar.configure(command=self.canvas.yview)
        #连接画布和滚动条
        self.canvas.config(yscrollcommand=self.vbar.set) #设置
        self.canvas.create_window((0,0),anchor=NW, window=self.frame)  #create_window

        self.answer_dict = {} #用来存放用户的答案
        self.names = locals()#定义了一个产生动态变量名的小函数

    #显示题目
    def show(self):
        #标题
        lable_title = Label(self.frame,text="保存文件",bg="hotpink",width=92,height=3,font=("Arial,36"))
        lable_title.pack(pady=9)

        lable_author = Label(self.frame, text="显示保存文件", bg="hotpink", width=92, height=3, font=("Arial,24"))
        lable_author.pack()

#账号中心
class ViewAccountCenter():
    #scrollregion 定义canvas可以滚动的范围
    def __init__(self,root,uname):
        #定义画布
        self.root = root
        self.uname = uname
        self.top_level = Toplevel(self.root)
        self.top_level.title("账号中心(当前账户：" + uname + ")")
        self.top_level.geometry("740x480+100+30")
        self.top_level.resizable(0,0)
        self.canvas=Canvas(self.top_level,width=740,height=480,scrollregion=(0,0,600,600),) #创建canvas
        self.canvas.pack() #放置canvas的位置
        #定义框架矩形  一个容器
        self.frame=Frame(self.canvas) #把frame放在canvas里
        self.frame.pack() #frame的长宽，和canvas差不多的
        #定义一个滚动条
        self.vbar=Scrollbar(self.canvas) #竖直滚动条
        self.vbar.place(x = 720,width=20,height=480)
        self.vbar.configure(command=self.canvas.yview)
        #连接画布和滚动条
        self.canvas.config(yscrollcommand=self.vbar.set) #设置
        self.canvas.create_window((0,0),anchor=NW, window=self.frame)  #create_window
        self.submit_nickname = False
        self.submit_pwd = False
        self.submit_confirm_pwd = False
        self.seubmit_tel = False

    def submit(self):
        if messagebox.askokcancel(title="确认取消",message="您确定修改吗？"):
            if self.seubmit_tel and self.submit_confirm_pwd and self.submit_pwd and self.submit_nickname:
                uname = self.username.get()
                nickname = self.nickname.get()
                pwd = self.pwd.get()
                confirm_pwd = self.confirm_pwd.get()
                tel = self.tel.get()
                back = self.entry_back.get("0.0","end")
                queryDB.queryDB().updateUserInfo(uname=uname,pwd=pwd,tel=tel,back=back,nickname=nickname)
                self.label_error_update["text"] = "更新成功"
                self.label_error_confirm_pwd['text'] = ""
                self.label_error_pwd["text"] = ""
                self.label_error_tel["text"] = ""
                self.label_error_nickname["text"] = ""
            else:
                messagebox.showerror(title="更新错误",message="输入的信息有误，请更正后在提交。")

    def nicknameEvent(self,event):
        print("在nickname事件中")
        if not self.nickname.get():
            self.label_error_nickname["fg"] = "red"
            self.label_error_nickname["text"] = "昵称不能为空"
            self.submit_nickname = False
        else:
            self.label_error_nickname["fg"] = "green"
            self.label_error_nickname["text"] = "合法昵称"
            self.submit_nickname = True

    def passwordEvent(self,event):
        print("在password事件中")
        password = self.pwd.get()
        dig = string.digits
        letter = string.ascii_letters
        printable = string.printable
        punctuation = string.punctuation  # 标点符号
        if len(password) < 8:
            if not password:
                self.label_error_pwd["fg"] = "red"
                self.label_error_pwd["text"] = "密码不能为空"
                self.submit_pwd = False
            else:
                self.label_error_pwd["fg"] = "red"
                self.label_error_pwd["text"] = "密码至少8位"
                self.submit_pwd = False
        else:  # 不空且大于8位
            num_ill = 0
            for i in password:
                if i not in printable:
                    num_ill += 1
            num_dig = 0
            for i in password:
                if i in dig:
                    num_dig += 1
            num_letter = 0
            for i in password:
                if i in letter:
                    num_letter += 1
            num_punctuation = 0
            for i in password:
                if i in punctuation:
                    num_punctuation += 1
            if num_ill > 0:
                self.label_error_pwd["fg"] = "red"
                self.label_error_pwd["text"] = "含有非法字符"
                self.submit_pwd = False
            elif num_dig == len(password) or num_letter == len(password):
                self.label_error_pwd["fg"] = "orangered"
                self.label_error_pwd["text"] = "安全等级较低"
                self.submit_pwd = True
            elif num_dig != 0 and num_letter != 0 and num_punctuation == 0:
                self.label_error_pwd["fg"] = "cyan"
                self.label_error_pwd["text"] = "安全等级一般"
                self.submit_pwd = True
            elif num_dig != 0 and num_letter != 0 and num_punctuation != 0:
                self.label_error_pwd["fg"] = "green"
                self.label_error_pwd["text"] = "安全等级高"
                self.submit_pwd = True

    def confirmpPwdEvent(self,event):
        print("在confirmpwd事件中")
        confirm_pwd = self.confirm_pwd.get()
        pwd = self.pwd.get()
        if self.confirm_pwd.get():
            if not confirm_pwd:
                self.label_error_confirm_pwd['fg'] = "red"
                self.label_error_confirm_pwd["text"] = "确认密码不能为空"
                self.submit_confirm_pwd = False
            elif confirm_pwd != pwd and confirm_pwd:
                self.label_error_confirm_pwd["fg"] = "red"
                self.label_error_confirm_pwd["text"] = "两次密码不一致"
                self.submit_confirm_pwd = False
                # label_new_pwd_error["text"] = ""
            else:
                self.label_error_confirm_pwd["fg"] = "green"
                self.label_error_confirm_pwd["text"] = "合法确认密码"
                self.submit_confirm_pwd = True

    def telEvent(self,event):
        print("在tel事件中")
        tel = self.tel.get()
        if len(tel) != 11:
            if len(tel) == 0:
                self.label_error_tel["fg"] = "red"
                self.label_error_tel["text"] = "电话不能为空"
                self.seubmit_tel = False
            else:
                self.label_error_tel["fg"] = "red"
                self.label_error_tel["text"] = "电话号码得11位"
                self.seubmit_tel = False
        else:
            num_not_dig = 0
            for i in tel:
                if i not in string.digits:
                    num_not_dig += 1
            if num_not_dig > 0:
                self.label_error_tel["fg"] = "red"
                self.label_error_tel["text"] = "含有非数字字符"
                self.seubmit_tel = False
            else:
                self.label_error_tel["fg"] = "green"
                self.label_error_tel["text"] = "合法电话"
                self.seubmit_tel = True
    #显示题目
    def show(self):
        #标题
        lable_title = Label(self.frame,text="我的账号中心",bg="silver",fg="white",width=92,height=3,font=("Arial,36"))
        lable_title.grid(row=0,column=0,columnspan=3,pady=5)
        try:
            user_info = queryDB.queryDB().selectUsersInfo(uname=self.uname)
            uname = user_info[1]
            pwd = user_info[2]
            nickname = user_info[3]
            tel = user_info[4]
            times = user_info[6]
            print("times:%s"%times)
        except Exception as e:
            logging.error(e)
        # back = user_info[4]
        back = "fsdfhkasdhodjfhoaskdjfhaosdkjf"
        self.username = StringVar()
        self.username.set(uname)
        Label(self.frame, text="用 户 名:", width=30, height=2,font=("",12) ).grid(row=2, column=0)
        entry_username = Entry(self.frame, text="username", width=30,textvariable=self.username)
        entry_username.grid(row=2,column=1)
        # entry_username.insert(0,uname)#从第0号索引下标处插入数据
        entry_username["state"] = "readonly"

        self.pwd = StringVar()
        self.pwd.set(pwd)
        Label(self.frame, text="密    码:", width=30, height=2, font=("",12)).grid(row=3, column=0)
        entry_password = Entry(self.frame, text="password", width=30, textvariable=self.pwd)
        # entry_password.insert(0, pwd)  # 从第0号索引下标处插入数据
        entry_password.bind("<FocusOut>",self.passwordEvent)
        entry_password.grid(row=3, column=1)
        self.label_error_pwd = Label(self.frame, text="", fg="red", width=15, height=2,font=("", 12))
        self.label_error_pwd.grid(row=3, column=2)

        self.confirm_pwd = StringVar()
        Label(self.frame, text="确认密码:", width=30, height=2,font=("",12) ).grid(row=4, column=0)
        entry_confirm_password = Entry(self.frame, text="confirm_password", width=30,textvariable=self.confirm_pwd )
        # entry_confirm_password.insert(0, pwd)  # 从第0号索引下标处插入数据
        entry_confirm_password.bind("<FocusOut>",self.confirmpPwdEvent)
        entry_confirm_password.grid(row=4, column=1)
        self.label_error_confirm_pwd = Label(self.frame, text="", fg="red", width=15, height=2, font=("", 12))
        self.label_error_confirm_pwd.grid(row=4, column=2)

        self.nickname = StringVar()
        self.nickname.set(nickname)
        Label(self.frame, text="昵    称:", width=30, height=2,font=("",12) ).grid(row=5, column=0)
        entry_nickname = Entry(self.frame, text="nickname", width=30, textvariable=self.nickname)
        # entry_nickname.insert(0, nickname)  # 从第0号索引下标处插入数据
        entry_nickname.bind("<FocusOut>",self.nicknameEvent)
        entry_nickname.grid(row=5, column=1)
        self.label_error_nickname = Label(self.frame, text="",fg="red", width=15, height=2, font=("", 12))
        self.label_error_nickname.grid(row=5, column=2,)

        self.tel = StringVar()
        # self.tel.set(tel)
        Label(self.frame, text="电    话:", width=30, height=2,font=("",12) ).grid(row=6, column=0)
        entry_tel = Entry(self.frame, text="tel", width=30,textvariable=self.tel )
        entry_tel.insert(0, tel)  # 从第0号索引下标处插入数据
        entry_tel.bind("<FocusOut>",self.telEvent)
        entry_tel.grid(row=6, column=1)
        self.label_error_tel = Label(self.frame, text="",fg="red", width=15, height=2, font=("", 12))
        self.label_error_tel.grid(row=6, column=2)

        Label(self.frame, text="测试次数:", width=30, height=2, font=("", 12)).grid(row=7, column=0)
        entry_times = Entry(self.frame, text="time", width=30, )
        entry_times.insert(0, times)  # 从第0号索引下标处插入数据
        entry_times["state"] = "readonly"
        entry_times.grid(row=7, column=1)

        # self.back.set(back)
        Label(self.frame, text="备    注:", width=30, height=2, font=("", 12)).grid(row=8, column=0)
        self.entry_back = Text(self.frame, height=7, width=30,bg="whitesmoke", )
        self.entry_back.insert("end", back)  # 从第0号索引下标处插入数据
        self.entry_back.grid(row=8, column=1)

        Button(self.frame,text="提交修改",width=20,height=1,bg="springgreen",command=self.submit).grid(row=9,column=1,pady=20)
        self.label_error_update = Label(self.frame, text="", width=20, height=1, fg="green",)
        self.label_error_update.grid(row=9, column=0,pady=20)


#显示我的测试结果
class ViewMyTestResult():
    #scrollregion 定义canvas可以滚动的范围
    def __init__(self,root,uname):
        self.uname = uname
        #定义画布
        self.root = root
        self.top_level = Toplevel(self.root)
        self.top_level.title("我的测试结果(当前账户：" + uname + ")")
        self.top_level.geometry("810x480+100+30")
        self.top_level.resizable(0,0)
        self.canvas=Canvas(self.top_level,width=810,height=480,scrollregion=(0,0,3000,3000),) #创建canvas
        self.canvas.pack() #放置canvas的位置
        #定义框架矩形  一个容器
        self.frame=Frame(self.canvas) #把frame放在canvas里
        self.frame.pack() #frame的长宽，和canvas差不多的

        #定义一个滚动条
        self.vbar=Scrollbar(self.canvas) #竖直滚动条
        self.vbar.place(x = 790,width=20,height=480)
        self.vbar.configure(command=self.canvas.yview)
        #连接画布和滚动条
        self.canvas.configure(yscrollcommand=self.vbar.set) #设置
        self.canvas.create_window((0,0),anchor=NW, window=self.frame)  #create_window
        self.color = "SKYBLUE"


    def displaySquare(self,score):
        print("■"*score)
        return "■"*score

    def displayMainSquare(self,score):
        print("★"*score)
        return "★"*score


    def displaySpace(self,score):
        if score >= 10:
            return 90 - score*2 - 7
        else:
            return 90 - score * 2 - 6
    #----------------------------------------------------------------------------------
    def displayLine(self,str_list,start_row,color):

        for _str in str_list:
            if len(_str) > 44 and len(_str) < 88:
                index = 44
                s1 = _str[:int(index)]
                s2 = _str[int(index):]
                new1 = s1 + self.getSpaces(s1)
                new2 = s2 + self.getSpaces(s2)
                Label(self.frame, text=new1, width=92, fg=color,height=2, font=("Arial,24")).grid(row=int(start_row), column=0, columnspan=9)
                Label(self.frame, text=new2, width=92, fg=color,height=2, font=("Arial,24")).grid(row=int(start_row)+1, column=0, columnspan=9)
                start_row += 2
            elif len(_str) >=88 and len(_str) <= 132:
                index = 44
                s1 = _str[:int(index)]
                s2 = _str[int(index):88]
                s3 = _str[88:]
                new1 = s1 + self.getSpaces(s1)
                new2 = s2 + self.getSpaces(s2)
                new3 = s3 + self.getSpaces(s3)
                Label(self.frame, text=new1, width=92, fg=color, height=2, font=("Arial,24")).grid(row=int(start_row),
                                                                                                   column=0,
                                                                                                   columnspan=9)
                Label(self.frame, text=new2, width=92, fg=color, height=2, font=("Arial,24")).grid(
                    row=int(start_row) + 1, column=0, columnspan=9)
                Label(self.frame, text=new3, width=92, fg=color, height=2, font=("Arial,24")).grid(
                    row=int(start_row) + 2, column=0, columnspan=9)
                start_row += 3
            else:
                new = _str + self.getSpaces(_str)
                Label(self.frame, text=new, width=92, fg=color,height=2, font=("Arial,24")).grid(row=int(start_row), column=0, columnspan=9)
                start_row += 1
        return start_row

    def getSpace(self, s):
        if len(s) <= 44:
            if len(s.split(".")[0]) == 1:
                return 43 - (len(s) - 1)
            else:
                return 44 - (len(s) - 1)
        else:
            return 0

    def getSpaces(self, s):
        if len(s) <= 44:
            if len(s.split(".")[0]) == 1:
                return (43 - (len(s) - 1)) * "  "
            else:
                return (44 - (len(s) - 1)) * "  "
        else:
            return 0 * "  "

    def showOne(self):
        # ======================================1号性格=================================================================
        s1 = "1.内向、被动、批判关注错误，纠正错误、持续监测，喜欢每件事都井井有条，顺序编排；%s" % (
                "  " * self.getSpace("1.内向、被动、批判关注错误，纠正错误、持续监测，喜欢每件事都井井有条，顺序编排；"))
        s2 = "2.急于把事情办好，努力完美；%s" % ("  " * self.getSpace("2.急于把事情办好，努力完美；"))
        s3 = "3.有理性、独立、勤奋工作有责任、成熟、有目标、且看中效率；%s" % ("  " * self.getSpace("3.有理性、独立、勤奋工作有责任、成熟、有目标、且看中效率；"))
        s4 = "4.对自己和他人都很喜欢批评、没耐性、吹毛求疵；先工作，后享乐；%s" % ("  " * self.getSpace("4.对自己和他人都很喜欢批评、没耐性、吹毛求疵；先工作，后享乐；"))
        s5 = "5.压抑冲动和渴望；过度刚性；将高尚作为自己的报酬；%s" % ("  " * self.getSpace("5.压抑冲动和渴望；过度刚性；将高尚作为自己的报酬；"))
        s6 = "6.嘴边常挂着『应该怎样做』这句话；%s" % ("  " * self.getSpace("6.嘴边常挂着『应该怎样做』这句话；"))
        s7 = "7.一向坚持自己的原则，很难容忍其他不同意见；%s" % ("  " * self.getSpace("7.一向坚持自己的原则，很难容忍其他不同意见；"))
        s8 = "8.个性严谨，严格没有笑容，不拘言笑；%s" % ("  " * self.getSpace("8.个性严谨，严格没有笑容，不拘言笑；"))
        s9 = "9.很少顾及家人，喜欢鸡蛋里挑骨头，常埋怨和生气他人做事不够好；%s" % ("  " * self.getSpace("9.很少顾及家人，喜欢鸡蛋里挑骨头，常埋怨和生气他人做事不够好；"))
        s10 = "10.是一个合理、实际、脚踏实地的人。%s" % ("  " * self.getSpace("10.是一个合理、实际、脚踏实地的人。"))

        title_1 = "您的参考性格-1号性格(完美主义者）：%s" % ("  " * self.getSpace("您的参考性格-1号性格(完美主义者）："))
        Label(self.frame, text=title_1, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=14,
                                                                                                               column=0,
                                                                                                               pady=4,columnspan=9)
        Label(self.frame, text=s1, width=92, height=2, font=("Arial,24")).grid(row=15, column=0,columnspan=9)
        Label(self.frame, text=s2, width=92, height=2, font=("Arial,24")).grid(row=16, column=0,columnspan=9)
        Label(self.frame, text=s3, width=92, height=2, font=("Arial,24")).grid(row=17, column=0,columnspan=9)
        Label(self.frame, text=s4, width=92, height=2, font=("Arial,24")).grid(row=18, column=0,columnspan=9)
        Label(self.frame, text=s5, width=92, height=2, font=("Arial,24")).grid(row=19, column=0,columnspan=9)
        Label(self.frame, text=s6, width=92, height=2, font=("Arial,24")).grid(row=20, column=0,columnspan=9)
        Label(self.frame, text=s7, width=92, height=2, font=("Arial,24")).grid(row=21, column=0,columnspan=9)
        Label(self.frame, text=s8, width=92, height=2, font=("Arial,24")).grid(row=22, column=0,columnspan=9)
        Label(self.frame, text=s9, width=92, height=2, font=("Arial,24")).grid(row=23, column=0,columnspan=9)
        Label(self.frame, text=s10, width=92, height=2, font=("Arial,24")).grid(row=24, column=0,columnspan=9)
        # ————————————————有利的做法
        font_color = "hotpink"
        title_4_1 = "对您有利的做法：%s" % ("  " * self.getSpace("对您有利的做法："))
        Label(self.frame, text=title_4_1, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=29,
                                                                                                                 column=0,
                                                                                                                 pady=4,
                                                                                                                 columnspan=9)
        s_list1 = ["1.不要强迫自己做事；不要把自己的工作安排的满满当当，以至于没有时间思考真正的需求。",
                   "2.需要对内心的严格标准进行修改。需要对规则剔除质疑。",
                   "3.不要把自己的洞察变成对自己的攻击。‘我怎么会连自己的错误都发现不了？’",
                   "4.到现实中去找答案。如果觉得其他人在对自己品头论足，那就直接找他们问问清楚。如果感到自己的担忧在加剧，就去寻找事实信息来消除不必要的焦虑。",
                   "5.关注其他人思想观念中的价值和一惯性。",
                   "6.知道‘唯一正确性’的思想会限制妥协的机会，或者与其他观点交流的机会。",
                   "7.学会寻找快乐和接受快乐",
                   "8.学会区分‘应该’完成和‘想要’完成之间的差别。",
                   "9.关注你对他人的怒火，很可能他人的所作所为正是你内心渴望的。",
                   "10.注意未被察觉的生气现象：比如内心很生气，表面还故意摆出笑脸；言语很礼貌，但声音很尖刻；或者面带笑容，但动作僵硬。",
                   "11.学会让阴影情绪发泄出来。",
                   "12.运用想象力来化解怒气。想象最糟糕的情况，知道怒气消失。"
                   ]
        start_row = self.displayLine(s_list1, 30, font_color)
        # ————————————————注意的做法
        font_color = "crimson"
        title_4_1 = "您需要注意的做法：%s" % ("  " * self.getSpace("您需要注意的做法："))
        Label(self.frame, text=title_4_1, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=start_row,
                                                                                                                 column=0,
                                                                                                                 pady=4,
                                                                                                                 columnspan=9)
        s_list2 = [
            "1.感到两个自己的存在，一个很快乐，一个很严厉。",
            "2.对个人的希望毫无察觉。",
            "3.因为察觉到自己内心的怒火而感到焦虑，‘我设法不要对别人发脾气。’",
            "4.把时间都占满了，没有给快乐留下时间。",
            "5.犹豫不决。把简单的问题复杂化，不愿做出最后的承诺。",
            "6.被压抑的需求找不到表达途径，导致自身压力不断增大，不满情绪随之增强。",
            "7.需要从环境中找到错误。",
            "8.‘焦土政策’（一种在战争中实行的自我破坏政策）。一旦发现错误，就要求全部返工。无法妥协。因为楼梯的位置不对，就非要把整栋房子都拆掉。",
            "9.为了平衡内心对自身的批评，对他人的抱怨越来越多。",
            "10.注意力僵硬。把所有的注意力都放在生活中需要改进的地方，对其他方面毫不关心。把内心的冲突抛在脑后。",
            "11.无法忍受多样的观点。‘我认为事情只有两种结果，不是正确，就是错误。’",
        ]
        r = self.displayLine(s_list2, start_row+1, font_color)

    def showTwo(self):
        # ======================================2号性格=================================================================
        a1 = "1.外向、主动、感情丰富；%s" % ("  " * self.getSpace("1.外向、主动、感情丰富；"))  # 12个中文字符  一个85个英文字符
        a2 = "2.关注去满足重要的其他人；%s" % ("  " * self.getSpace("2.关注去满足重要的其他人；"))
        a3 = "3.乐于付出，努力满足他人的需要；%s" % ("  " * self.getSpace("3.乐于付出，努力满足他人的需要；"))
        a4 = "4.想成为他人不可缺少的；%s" % ("  " * self.getSpace("4.想成为他人不可缺少的；"))
        a5 = "5.压抑或疏忽自己的感受；%s" % ("  " * self.getSpace("5.压抑或疏忽自己的感受；"))
        a6 = "6.有时会有强烈的寂寞感觉；%s" % ("  " * self.getSpace("6.有时会有强烈的寂寞感觉；"))
        a7 = "7.不直接表达自己人感受；%s" % ("  " * self.getSpace("7.不直接表达自己人感受；"))
        a8 = "8.缺乏自主和想法；%s" % ("  " * self.getSpace("8.缺乏自主和想法；"))
        a9 = "9.很希望被他人接受、并获得他人的认同、尊重、爱护及钦佩；%s" % ("  " * self.getSpace("9.很希望被他人接受、并获得他人的认同、尊重、爱护及钦佩；"))
        a10 = "10.喜欢朋友并乐于倾听他们的事情；%s" % ("  " * self.getSpace("10.喜欢朋友并乐于倾听他们的事情；"))
        a11 = "11.对人热情、友善、有爱心和有耐心；%s" % ("  " * self.getSpace("11.对人热情、友善、有爱心和有耐心；"))
        a12 = "12.借着对别人的付出来表现自己；%s" % ("  " * self.getSpace("12.借着对别人的付出来表现自己；"))
        a13 = "13.重视人际关系；%s" % ("  " * self.getSpace("13.重视人际关系；"))
        a14 = "14.不会直接向某人表达自己不满的情绪，但可能会向其他人抱怨；%s" % ("  " * self.getSpace("14.不会直接向某人表达自己不满的情绪，但可能会向其他人抱怨；"))
        a15 = "15.会掩饰或不去触自己的焦虑；%s" % ("  " * self.getSpace("15.会掩饰或不去触自己的焦虑；"))
        a16 = "16.很难拒绝有求于自己的人，即使拨不出时间，也会牺牲自己成全他人；%s" % ("  " * self.getSpace("16.很难拒绝有求于自己的人，即使拨不出时间，也会牺牲自己成全他人；"))
        a17 = "17.是一个关怀、乐于助人、慷慨的人；%s" % ("  " * self.getSpace("17.是一个关怀、乐于助人、慷慨的人；"))

        title_2 = "您的参考性格-2号性格(给予者）：%s" % ("  " * self.getSpace("您的参考性格-2号性格(给予者）："))
        Label(self.frame, text=title_2, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=14,
                                                                                                               column=0,
                                                                                                               pady=4,columnspan=9)
        Label(self.frame, text=a1, width=92, height=2, font=("Arial,24")).grid(row=15, column=0,columnspan=9)
        Label(self.frame, text=a2, width=92, height=2, font=("Arial,24")).grid(row=16, column=0,columnspan=9)
        Label(self.frame, text=a3, width=92, height=2, font=("Arial,24")).grid(row=17, column=0,columnspan=9)
        Label(self.frame, text=a4, width=92, height=2, font=("Arial,24")).grid(row=18, column=0,columnspan=9)
        Label(self.frame, text=a5, width=92, height=2, font=("Arial,24")).grid(row=19, column=0,columnspan=9)
        Label(self.frame, text=a6, width=92, height=2, font=("Arial,24")).grid(row=20, column=0,columnspan=9)
        Label(self.frame, text=a7, width=92, height=2, font=("Arial,24")).grid(row=21, column=0,columnspan=9)
        Label(self.frame, text=a8, width=92, height=2, font=("Arial,24")).grid(row=22, column=0,columnspan=9)
        Label(self.frame, text=a9, width=92, height=2, font=("Arial,24")).grid(row=23, column=0,columnspan=9)
        Label(self.frame, text=a10, width=92, height=2, font=("Arial,24")).grid(row=24, column=0,columnspan=9)
        Label(self.frame, text=a11, width=92, height=2, font=("Arial,24")).grid(row=25, column=0,columnspan=9)
        Label(self.frame, text=a12, width=92, height=2, font=("Arial,24")).grid(row=26, column=0,columnspan=9)
        Label(self.frame, text=a13, width=92, height=2, font=("Arial,24")).grid(row=27, column=0,columnspan=9)
        Label(self.frame, text=a14, width=92, height=2, font=("Arial,24")).grid(row=28, column=0,columnspan=9)
        Label(self.frame, text=a15, width=92, height=2, font=("Arial,24")).grid(row=29, column=0,columnspan=9)
        Label(self.frame, text=a16, width=92, height=2, font=("Arial,24")).grid(row=30, column=0,columnspan=9)
        Label(self.frame, text=a17, width=92, height=2, font=("Arial,24")).grid(row=31, column=0,columnspan=9)
        # ————————————————有利的做法
        font_color = "hotpink"
        title_4_1 = "对您有利的做法：%s" % ("  " * self.getSpace("对您有利的做法："))
        Label(self.frame, text=title_4_1, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=29,
                                                                                                                 column=0,
                                                                                                                 pady=4,
                                                                                                                 columnspan=9)
        s_list1 = [
            "1.发现自己的控制欲。",
            "2.认识自己对他人的真正价值。既不要过分骄傲，夸大自己的重要性，也不应该表现的过于卑微。",
            "3.认识到奉承很可能导致焦虑增加。",
            "4.不要过于注重最初的情感反应，要注意其他反应，因为最初的反应往往是遮掩自己真正感情的虚伪面具。",
            "5.注意心理疗法的作用，在一个小时的心理练习中集中注意力会受益匪浅。学会与他人讨论自己。",
            "6.在出现下列情况时对自己予以提醒：希望变现的无助，希望心理治疗不会；令人难堪，不愿意提供有损自身形象的内容。",
            "7.认识到保持‘多个自我’与保持统一形象之间的冲突。",
            "8.认识到生气实际上真实感觉的一种暗示，也是对内心冲突的解释。",
            "9.不同通过奉承来拉拢他人，并认识到自己的复仇欲望来自于伤害的骄傲感。",
                   ]
        start_row = self.displayLine(s_list1, 30, font_color)
        # ————————————————注意的做法
        font_color = "crimson"
        title_4_1 = "您需要注意的做法：%s" % ("  " * self.getSpace("您需要注意的做法："))
        Label(self.frame, text=title_4_1, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=start_row,
                                                                                                                 column=0,
                                                                                                                 pady=4,
                                                                                                                 columnspan=9)
        s_list2 = [
            "1.希望扮演另一个人，幻想通过不同的方式得到爱。",
            "2.对多个自己感到困惑‘哪一个是真正的我呢？’",
            "3.在两性关系中不愿选择最好的对象，而倾向于第二位的对象。虽然也想和‘最好的’在一起，但是害怕被拒绝，所以宁愿选择‘爱我更多的那个人’。",
            "4.害怕没有真正的自我，害怕被复制，害怕模仿他人。在冥想的过程中，害怕身体的中心是一个空洞。",
            "5.失去了他人的保护后，就会产生强烈的不安全感，感觉生存受到威胁。",
            "6.相信获得认可与获得爱是同等重要的。相信独立将导致再也得不到爱。",
            "7.当寻求认可的习惯于逐渐浮现的自身需要发生冲突时，会突然大发雷霆。相信是他人在试图限制自己的自由。",
            "8.要求后的无限自由，拒绝对多样的自我做出承诺。",
            "9.被难以得到的关系所吸引。陷入三角恋。对于难以到手的目标，通过不断的追求保持控制权。要求独享真正的亲密。",
            "10.一旦得到了真正的亲密，又没有经验去面对。对于真正的性需求和情感需求并不熟悉。需要花时间找到自己真正的感情，而不受他人影响。需要学会区分逢场作戏的爱情游戏和海誓山盟的真爱。",

        ]
        r = self.displayLine(s_list2, start_row+1, font_color)

    def showThree(self):
        # ======================================3号性格=================================================================
        b1 = "1.外向、主动、擅于交际；%s" % ("  " * self.getSpace("1.外向、主动、擅于交际；"))
        b2 = "2.关注任务（包括休息时间）；%s" % ("  " * self.getSpace("2.关注任务（包括休息时间）；"))
        b3 = "3.相信世上无难事，只怕有心人；%s" % ("  " * self.getSpace("3.相信世上无难事，只怕有心人；"))
        b4 = "4.别人会觉得自己是一很有野心的人；%s" % ("  " * self.getSpace("4.别人会觉得自己是一很有野心的人；"))
        b5 = "5.执行、做、争先；%s" % ("  " * self.getSpace("5.执行、做、争先；"))
        b6 = "6.注意力集中在结果，而非意义；%s" % ("  " * self.getSpace("6.注意力集中在结果，而非意义；"))
        b7 = "7.基于成绩，得到认可和接受；%s" % ("  " * self.getSpace("7.基于成绩，得到认可和接受；"))
        b8 = "8.疏忽自己的感受；%s" % ("  " * self.getSpace("8.疏忽自己的感受；"))
        b9 = "9.喜欢与人竞争，借由超越他人来建立自己的优越感；%s" % ("  " * self.getSpace("9.喜欢与人竞争，借由超越他人来建立自己的优越感；"))
        b10 = "10.坚持自己的目标，达不到目标就恼火；效率高，有时会为了求效率而牺牲完美走捷径；%s" % (
                "  " * self.getSpace("10.坚持自己的目标，达不到目标就恼火；效率高，有时会为了求效率而牺牲完美走捷径；"))
        b11 = "11.精力充沛、热爱工作、奋力追求成功、以获得地位和赞赏；%s" % ("  " * self.getSpace("11.精力充沛、热爱工作、奋力追求成功、以获得地位和赞赏；"))
        b12 = "12.为了事业成功、声望、财富，有时牺牲情感、婚姻、家庭或朋友；%s" % ("  " * self.getSpace("12.为了事业成功、声望、财富，有时牺牲情感、婚姻、家庭或朋友；"))
        b13 = "13.是一个受人欣赏、有能力、出众的人；%s" % ("  " * self.getSpace("13.是一个受人欣赏、有能力、出众的人；"))

        title_3 = "您的参考性格-3号性格(实干者）：%s" % ("  " * self.getSpace("您的参考性格-3号性格(实干者）："))
        Label(self.frame, text=title_3, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=14,
                                                                                                               column=0,
                                                                                                               pady=4,columnspan=9)
        Label(self.frame, text=b1, width=92, height=2, font=("Arial,24")).grid(row=15, column=0,columnspan=9)
        Label(self.frame, text=b2, width=92, height=2, font=("Arial,24")).grid(row=16, column=0,columnspan=9)
        Label(self.frame, text=b3, width=92, height=2, font=("Arial,24")).grid(row=17, column=0,columnspan=9)
        Label(self.frame, text=b4, width=92, height=2, font=("Arial,24")).grid(row=18, column=0,columnspan=9)
        Label(self.frame, text=b5, width=92, height=2, font=("Arial,24")).grid(row=19, column=0,columnspan=9)
        Label(self.frame, text=b6, width=92, height=2, font=("Arial,24")).grid(row=20, column=0,columnspan=9)
        Label(self.frame, text=b7, width=92, height=2, font=("Arial,24")).grid(row=21, column=0,columnspan=9)
        Label(self.frame, text=b8, width=92, height=2, font=("Arial,24")).grid(row=22, column=0,columnspan=9)
        Label(self.frame, text=b9, width=92, height=2, font=("Arial,24")).grid(row=23, column=0,columnspan=9)
        Label(self.frame, text=b10, width=92, height=2, font=("Arial,24")).grid(row=24, column=0,columnspan=9)
        Label(self.frame, text=b11, width=92, height=2, font=("Arial,24")).grid(row=25, column=0,columnspan=9)
        Label(self.frame, text=b12, width=92, height=2, font=("Arial,24")).grid(row=26, column=0,columnspan=9)
        Label(self.frame, text=b13, width=92, height=2, font=("Arial,24")).grid(row=27, column=0,columnspan=9)
        # ————————————————有利的做法
        font_color = "hotpink"
        title_4_1 = "对您有利的做法：%s" % ("  " * self.getSpace("对您有利的做法："))
        Label(self.frame, text=title_4_1, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=29,
                                                                                                                 column=0,
                                                                                                                 pady=4,
                                                                                                                 columnspan=9)
        s_list1 = [
            "1.学会停止。给自己的情感和真实思想留下时间。是什么在驱使自己不停地工作，找到这种担心，并直接面对。",
            "2.不要让自己的行动变成机械化反应。意识到自己成了生产机器，而情感全部搁置。",
            "3.不要让对个人成功的幻想取代了自己的真实能力。",
            "4.遇到困难时，不要通过寻找新的工作来逃避困难，也不要无视失败，或者抱怨批评自己的人。",
            "5.意识到自己常常会吧情感的快乐延迟。‘我完成了下一个推销任务后就会快乐。’",
            "6.认识到真正自我与公众形象的差异。学会从形象中抽离出来。",
            "7.注意自己的欺骗倾向，喜欢表演。‘没有人会发现面具背后的我；他们只会看到我的所作所为。’",
            "8.不要把自己看做离不开的关键人物，把周围的人都看做没有能力的懒汉。",
            "9.注意到自己总是希望成为最完美的心理病人。总是在心理医生面前表现出典型症状，把治疗当成工作，把冥想变成任务。‘我今天静坐了多少分钟？’",
            "10.学会通过身体的感觉来发现自己的感觉。比如，在你无法确定自己的情绪时，你首先说出自己的身体感觉，‘我的脸发热’或者‘我的肚子很紧’。这些身体上的感觉能够帮助你找到自己的真实感受。",

                   ]
        start_row = self.displayLine(s_list1, 30, font_color)
        # ————————————————注意的做法
        font_color = "crimson"
        title_4_1 = "您需要注意的做法：%s" % ("  " * self.getSpace("您需要注意的做法："))
        Label(self.frame, text=title_4_1, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=start_row,
                                                                                                                 column=0,
                                                                                                                 pady=4,
                                                                                                                 columnspan=9)
        s_list2 = [
            "1.对感觉感到困惑。‘我的感觉正确吗？’或者‘哪个感觉是真的？’",
            "2.在过度活跃的幻想中生活。在方法根本行不通，或者出现负面效应时，依然幻想成功。",
            "3.为自己打造虚幻的形象，并且相信这些特质是自己天生具有的。",
            "4.急于求成，用工作取代情感需求，并感觉良好。在心理治疗的成果还没有显现时，就想要退出。",
            "5.需要获得成功的证明。",
            "6.在讨论个人问题时，总是习惯性地避免讨论自身感觉。觉得个人的问题说一说就能解决，无需情感体会。",
            "7.在接受心理治疗时，倾向于选择十分能干而吸引人的心理医师。看重的是心理医师的价值，而不是去发现自己的价值。",
            "8.在冥想的过程中，担心真正的自我根本不存在。",
            "9.当遭遇他人的批评是，感觉自己像个圣人。‘我做出了那么大的贡献，我根本不用理会那些批评。’",
        ]
        r = self.displayLine(s_list2, start_row+1, font_color)

    def showFour(self):
        # ======================================4号性格=================================================================
        c1 = "1.内向，被动，多愁善感、感情丰富；%s" % ("  " * self.getSpace("1.内向，被动，多愁善感、感情丰富；"))
        c2 = "2.关注什么是重大损失；%s" % ("  " * self.getSpace("2.关注什么是重大损失；"))
        c3 = "3.特别被人生哀愁、悲剧所触动；%s" % ("  " * self.getSpace("3.特别被人生哀愁、悲剧所触动；"))
        c4 = "4.认为被他人误解是一件特别痛苦的事；%s" % ("  " * self.getSpace("4.认为被他人误解是一件特别痛苦的事；"))
        c5 = "5.把焦点放在关系和感觉上；%s" % ("  " * self.getSpace("5.把焦点放在关系和感觉上；"))
        c6 = "6.和不熟的人交往时，会表现沉默和冷淡；%s" % ("  " * self.getSpace("6.和不熟的人交往时，会表现沉默和冷淡；"))
        c7 = "7.不开心时，喜欢独自一人来处理不开心的情绪；%s" % ("  " * self.getSpace("7.不开心时，喜欢独自一人来处理不开心的情绪；"))
        c8 = "8.对不符合自己心意的人，会表出拒人以千里之外的态度；%s" % ("  " * self.getSpace("8.对不符合自己心意的人，会表出拒人以千里之外的态度；"))
        c9 = "9.对别人的痛苦具有深层且天赋的同情心，会立刻抛开自己的烦恼，去支持帮助在痛苦中的人；%s" % (
                "  " * self.getSpace("9.对别人的痛苦具有深层且天赋的同情心，会立刻抛开自己的烦恼，去支持帮助在痛苦中的人；"))
        c10 = "10.创造力、热情和丰富的感情很多时吸引了其他人；%s" % ("  " * self.getSpace("10.创造力、热情和丰富的感情很多时吸引了其他人；"))
        c11 = "11.当遭到拒绝、挫折时，便会退缩，变得沉默、害羞；%s" % ("  " * self.getSpace("11.当遭到拒绝、挫折时，便会退缩，变得沉默、害羞；"))
        c12 = "12.有时会感到忧郁，心中有很多梦想和理想，可总是很难实现他们；%s" % ("  " * self.getSpace("12.有时会感到忧郁，心中有很多梦想和理想，可总是很难实现他们；"))
        c13 = "13.比一般人感受更深并怀疑那些总是很快乐的人；%s" % ("  " * self.getSpace("13.比一般人感受更深并怀疑那些总是很快乐的人；"))
        c14 = "14.是一个直觉、敏感、有创造力及理想化的人；%s" % ("  " * self.getSpace("14.是一个直觉、敏感、有创造力及理想化的人；"))

        title_4 = "您的参考性格-4号性格(悲情浪漫者）：%s" % ("  " * self.getSpace("您的参考性格-4号性格(悲情浪漫者）："))
        Label(self.frame, text=title_4, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=14,
                                                                                                               column=0,
                                                                                                               pady=4,columnspan = 9)
        Label(self.frame, text=c1, width=92, height=2, font=("Arial,24")).grid(row=15, column=0,columnspan = 9)
        Label(self.frame, text=c2, width=92, height=2, font=("Arial,24")).grid(row=16, column=0,columnspan = 9)
        Label(self.frame, text=c3, width=92, height=2, font=("Arial,24")).grid(row=17, column=0,columnspan = 9)
        Label(self.frame, text=c4, width=92, height=2, font=("Arial,24")).grid(row=18, column=0,columnspan = 9)
        Label(self.frame, text=c5, width=92, height=2, font=("Arial,24")).grid(row=19, column=0,columnspan = 9)
        Label(self.frame, text=c6, width=92, height=2, font=("Arial,24")).grid(row=20, column=0,columnspan = 9)
        Label(self.frame, text=c7, width=92, height=2, font=("Arial,24")).grid(row=21, column=0,columnspan = 9)
        Label(self.frame, text=c8, width=92, height=2, font=("Arial,24")).grid(row=22, column=0,columnspan = 9)
        Label(self.frame, text=c9, width=92, height=2, font=("Arial,24")).grid(row=23, column=0,columnspan = 9)
        Label(self.frame, text=c10, width=92, height=2, font=("Arial,24")).grid(row=24, column=0,columnspan = 9)
        Label(self.frame, text=c11, width=92, height=2, font=("Arial,24")).grid(row=25, column=0,columnspan = 9)
        Label(self.frame, text=c12, width=92, height=2, font=("Arial,24")).grid(row=26, column=0,columnspan = 9)
        Label(self.frame, text=c13, width=92, height=2, font=("Arial,24")).grid(row=27, column=0,columnspan = 9)
        Label(self.frame, text=c14, width=92, height=2, font=("Arial,24")).grid(row=28, column=0,columnspan = 9)
        #————————————————有利的做法
        font_color = "hotpink"
        title_4_1 = "对您有利的做法：%s" % ("  " * self.getSpace("对您有利的做法："))
        Label(self.frame, text=title_4_1, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=29,
                                                                                                               column=0,
                                                                                                               pady=4,
                                                                                                               columnspan=9)
        s_list1 = ["1.承认自己早期的确实是真的；在悲伤之后，要把它放到一边。",
             "2.注意到当强烈的情感变化发生时，自己会完全投入于其中，把注意力转移到其他事物上，让自己从这种专注中解脱出来。",
             "3.养成善始善终的习惯，把被破坏或者被遗弃的工作当成未完成的工作做完。",
             "4.发现自己身上那些令他人羡慕的特质。",
             "5.与其刻意追求快乐，不如坦然接受伤感。要知道这样的情绪总会过去。",
            "6.让他人知道，过度亲近会遭到你的攻击，请他们不要误会。告诉他们在你生气的时候不要离去，这样你就会确信，即便他们受到攻击，也不会抛弃你。",
             "7.为自己能够感知他人的痛苦感到骄傲，但是要学会自如运用你的注意力。",
             "8.把注意力放在眼前。当注意力转移时，提醒自己。不要仅仅关注眼前的负面因素。",
             "9.培养多样的兴趣，结交各种朋友，把自己的注意力从抑郁的情绪中转移出来。",
             "10.通过身体的运动练习来调节心情。",
             "11.当真实的感觉被强烈的情感掩盖时，要注意到这一点，尤其是当你感到‘一切又会变得很糟糕’时。"
             ]
        start_row = self.displayLine(s_list1, 30, font_color)
        # ————————————————注意的做法
        font_color = "crimson"
        title_4_1 = "您需要注意的做法：%s" % ("  " * self.getSpace("您需要注意的做法："))
        Label(self.frame, text=title_4_1, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=start_row,
                                                                                                                 column=0,
                                                                                                                 pady=4,columnspan=9)
        s_list2 = [
            "1.对摆在眼前的问题想尽各种各种解决方法，尝试各种解决途径，但就是不愿意采取实质行动，推动事情发展。",
            "2.不喜欢被分类，不喜欢别人吧自己的问题看成普通问题。认为他人没有理解情况的独特性和严重性。",
            "3.希望得到解决问题的灵丹妙药。在冥想的过程中，希望‘被带到其他地方’。",
            "4.厌烦平淡的普通情感。希望通过遗失、幻想或艺术来重新巩固自己的情感。",
            "5.总是带着遗憾。‘现在改变已经太晚了’或者‘要是我选择了不同的做法，那该多好啊’。",
            "6.有自杀的想法或举动。渴望得到帮助。‘要是他们能够理解我的感受’或者‘我走了，他们就知道我受的苦了’，这样的想法需要特别注意。",
            "7.渴望奢望的生活，‘洗衣服可不是我该干的’。",
            "8.把自己和他人比较，嫉妒他人的优点。‘她比我漂亮。’或者‘他的衣服比我好’。",
            "9.诱惑和拒绝。在对方拒绝你之前，先找到对方的优点。",
            "10.强烈的自我批评。对自己的形象产生错误的判断，觉得毫无优点。总是觉得自己太胖，常常出现厌食或者易饿的症状。",
            "11.语言尖锐，讽刺让人。觉得是他人的错误导致了你的痛苦。",
            "12.寻求他人的建议，然后拒绝采用。不愿放弃受害者的形象。"
        ]
        r = self.displayLine(s_list2,start_row+1,font_color)

    def showFive(self):
        # ======================================5号性格=================================================================
        d1 = "1.内向，被动，自我，喜欢思考；%s" % ("  " * self.getSpace("1.内向，被动，自我，喜欢思考；"))
        d2 = "2.关注探究，思考代替行动；%s" % ("  " * self.getSpace("2.关注探究，思考代替行动；"))
        d3 = "3.与感觉相分离，讨厌情绪激动；%s" % ("  " * self.getSpace("3.与感觉相分离，讨厌情绪激动；"))
        d4 = "4.自我满足和简单化；%s" % ("  " * self.getSpace("4.自我满足和简单化；"))
        d5 = "5.贪求或积攒时间、空间、知识；%s" % ("  " * self.getSpace("5.贪求或积攒时间、空间、知识；"))
        d6 = "6.不擅长对他人说好听的话；%s" % ("  " * self.getSpace("6.不擅长对他人说好听的话；"))
        d7 = "7.喜欢别人扮演自己的学问和知识；%s" % ("  " * self.getSpace("7.喜欢别人扮演自己的学问和知识；"))
        d8 = "8.很难表达自己心中的感受；%s" % ("  " * self.getSpace("8.很难表达自己心中的感受；"))
        d9 = "9.不喜欢娱乐活动，在人际关系上显得比较木讷和保持理性的状态；%s" % ("  " * self.getSpace("9.不喜欢娱乐活动，在人际关系上显得比较木讷和保持理性的状态；"))
        d10 = "10.寻求独自感觉，不喜欢自己的空间受到骚扰；%s" % ("  " * self.getSpace("10.寻求独自感觉，不喜欢自己的空间受到骚扰；"))
        d11 = "11.喜欢自己解决问题或制定计划并执行一项计划；%s" % ("  " * self.getSpace("11.喜欢自己解决问题或制定计划并执行一项计划；"))
        d12 = "12.不喜欢过度计划的生活和每周一次的例会；%s" % ("  " * self.getSpace("12.不喜欢过度计划的生活和每周一次的例会；"))
        d13 = "13.是一个理解力强、重分析、好奇心强、有洞察力的人；%s" % ("  " * self.getSpace("13.是一个理解力强、重分析、好奇心强、有洞察力的人；"))

        title_5 = "您的参考性格-5号性格(观察者）：%s" % ("  " * self.getSpace("您的参考性格-5号性格(观察者）："))
        Label(self.frame, text=title_5, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=14,
                                                                                                               column=0,
                                                                                                               pady=4,columnspan = 9)
        Label(self.frame, text=d1, width=92, height=2, font=("Arial,24")).grid(row=15, column=0,columnspan = 9)
        Label(self.frame, text=d2, width=92, height=2, font=("Arial,24")).grid(row=16, column=0,columnspan = 9)
        Label(self.frame, text=d3, width=92, height=2, font=("Arial,24")).grid(row=17, column=0,columnspan = 9)
        Label(self.frame, text=d4, width=92, height=2, font=("Arial,24")).grid(row=18, column=0,columnspan = 9)
        Label(self.frame, text=d5, width=92, height=2, font=("Arial,24")).grid(row=19, column=0,columnspan = 9)
        Label(self.frame, text=d6, width=92, height=2, font=("Arial,24")).grid(row=20, column=0,columnspan = 9)
        Label(self.frame, text=d7, width=92, height=2, font=("Arial,24")).grid(row=21, column=0,columnspan = 9)
        Label(self.frame, text=d8, width=92, height=2, font=("Arial,24")).grid(row=22, column=0,columnspan = 9)
        Label(self.frame, text=d9, width=92, height=2, font=("Arial,24")).grid(row=23, column=0,columnspan = 9)
        Label(self.frame, text=d10, width=92, height=2, font=("Arial,24")).grid(row=24, column=0,columnspan = 9)
        Label(self.frame, text=d11, width=92, height=2, font=("Arial,24")).grid(row=25, column=0,columnspan = 9)
        Label(self.frame, text=d12, width=92, height=2, font=("Arial,24")).grid(row=26, column=0,columnspan = 9)
        Label(self.frame, text=d13, width=92, height=2, font=("Arial,24")).grid(row=27, column=0,columnspan = 9)
        # ————————————————有利的做法
        font_color = "hotpink"
        title_4_1 = "对您有利的做法：%s" % ("  " * self.getSpace("对您有利的做法："))
        Label(self.frame, text=title_4_1, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=29,
                                                                                                                 column=0,
                                                                                                                 pady=4,
                                                                                                                 columnspan=9)
        s_list1 = [
            "1.注意到当他人在期待回应时，自己却有刻意保留的欲望。‘我什么时候想做就会做，而不是你让我做我就做。’",
            "2.不要让情感被理性分析所取代，不要让精神构建替代了真实经验。",
            "3.认识到接触情感并不等于受到伤害。",
            "4.认识到自己渴望得到认可，又不想花费力气。",
            "5.认识到自己总是离不开三个陪伴：私密、优越和分离。",
            "6.学会接受突发情况。学会去冒险，去求助，去让私下的梦想变成现实。",
            "7.与他人在一起时，自己能感受到什么，把这种感受与自己独处时的感受进行对比，找到两种感受的差异。",
            "8.学会坚持完成重要的项目，并且把他们公之于众。让自己的成果被他人看见。",
            "9.对最简单的物质生活提出质疑。",
            "10.学会从自己的特殊研究中受益。",
            "11.学会容忍他人的需要和情感。",
            "12.愿意当场表现自己的情感，可以通过格式塔心理学、身体练习或者艺术工作来变现。但是同时要注意，不要在不成熟的情况下，让自己的情感一泻千里。允许延迟的情感反应与直觉发生联系。",

                   ]
        start_row = self.displayLine(s_list1, 30, font_color)
        # ————————————————注意的做法
        font_color = "crimson"
        title_4_1 = "您需要注意的做法：%s" % ("  " * self.getSpace("您需要注意的做法："))
        Label(self.frame, text=title_4_1, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=start_row,
                                                                                                                 column=0,
                                                                                                                 pady=4,
                                                                                                                 columnspan=9)
        s_list2 = [
            "1.让自己离开身体，退缩到内心。",
            "2.希望储藏时间和精力。总是在节省，而不是在付出。",
            "3.难以展现自我。把暴露自我的话从对话中过滤掉。保留信息。",
            "4.不愿给予；感觉被他人的需求所利用。",
            "5.过于自负，不愿依赖他人。‘没你我也可以。’",
            "6.对承诺感到疲惫。不愿与他人分享太多。",
            "7.用思想取代现实体验。不断巩固孤独者的立场。幻想不切实际的生活，而不是面对现实。",
            "8.幻想天上掉馅饼，可以不费力气就得到认可。‘如果上帝想要我，他就会来找我。’",
            "9.把自己隐藏在一个表面的姿态立。让自己的表现适应周围环境，以避免被他人注意。",
            "10.相信自己高人一等，不受感情控制。‘生气是愚蠢者的行为。’，‘他们为什么不能控制自己呢？’",
            "11.害怕欲望而麻痹自己。让自己无法走出去，也无法退出来。",
            "12.脱离情感生活。喜欢私密，没有人知道。",
            "13.无法分清楚什么是精神上的舍弃，什么是情感痛苦的逃避。",
            # "12.愿意当场表现自己的情感，可以通过格式塔心理学、身体练习或者艺术工作来变现。但是同时要注意，不要在不成熟的情况下，让自己的情感一泻千里。允许延迟的情感反应与直觉发生联系。",

        ]
        start_row1 = self.displayLine(s_list2, start_row+1, font_color)

    def showSix(self):
        # ======================================6号性格=================================================================
        e1 = "1.内向、主动、保守、忠诚；关注潜在的伤害、危险、威胁；%s" % ("  " * self.getSpace("1.内向、主动、保守、忠诚；关注潜在的伤害、危险、威胁；"))
        e2 = "2.关注潜在的伤害、危险、威胁；%s" % ("  " * self.getSpace("2.关注潜在的伤害、危险、威胁；"))
        e3 = "3.积极想像：放大危险、灾害；质疑并反向思维；%s" % ("  " * self.getSpace("3.积极想像：放大危险、灾害；质疑并反向思维；"))
        e4 = "4.延迟是因为担心成果不安全；%s" % ("  " * self.getSpace("4.延迟是因为担心成果不安全；"))
        e5 = "5.不会轻易相信别人，但内心深处希望得到别人欣赏和肯定；%s" % ("  " * self.getSpace("5.不会轻易相信别人，但内心深处希望得到别人欣赏和肯定；"))
        e6 = "6.经常犹豫不决，对事情通常想的太认真，很在意配偶及伙伴的想法；%s" % ("  " * self.getSpace("6.经常犹豫不决，对事情通常想的太认真，很在意配偶及伙伴的想法；"))
        e7 = "7.常充满矛盾，希望寻求权威的庇护，但又不相信权威，渴望别人喜欢，但又怀疑别人；%s" % (
                "  " * self.getSpace("7.常充满矛盾，希望寻求权威的庇护，但又不相信权威，渴望别人喜欢，但又怀疑别人；"))
        e8 = "8.期望公平，要求付出和所得是相匹配的，别人会觉得斤斤计较；%s" % ("  " * self.getSpace("8.期望公平，要求付出和所得是相匹配的，别人会觉得斤斤计较；"))
        e9 = "9.会常常提防别人陷害和利用，所以常和人保持一种安全距离，因此别人也觉得自己不容易相处；%s" % (
                "  " * self.getSpace("9.会常常提防别人陷害和利用，所以常和人保持一种安全距离，因此别人也觉得自己不容易相处；"))
        e10 = "10.常问自己是否有做错事，因为害怕错误而被责备；%s" % ("  " * self.getSpace("10.常问自己是否有做错事，因为害怕错误而被责备；"))
        e11 = "11.一个忠诚、值得信赖、勤奋的人；%s" % ("  " * self.getSpace("11.一个忠诚、值得信赖、勤奋的人；"))

        title_6 = "您的参考性格-6号性格(怀疑论者）：%s" % ("  " * self.getSpace("您的参考性格-6号性格(怀疑论者）："))
        Label(self.frame, text=title_6, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=14,
                                                                                                               column=0,
                                                                                                               pady=4,columnspan = 9)
        Label(self.frame, text=e1, width=92, height=2, font=("Arial,24")).grid(row=15, column=0,columnspan = 9)
        Label(self.frame, text=e2, width=92, height=2, font=("Arial,24")).grid(row=16, column=0,columnspan = 9)
        Label(self.frame, text=e3, width=92, height=2, font=("Arial,24")).grid(row=17, column=0,columnspan = 9)
        Label(self.frame, text=e4, width=92, height=2, font=("Arial,24")).grid(row=18, column=0,columnspan = 9)
        Label(self.frame, text=e5, width=92, height=2, font=("Arial,24")).grid(row=19, column=0,columnspan = 9)
        Label(self.frame, text=e6, width=92, height=2, font=("Arial,24")).grid(row=20, column=0,columnspan = 9)
        Label(self.frame, text=e7, width=92, height=2, font=("Arial,24")).grid(row=21, column=0,columnspan = 9)
        Label(self.frame, text=e8, width=92, height=2, font=("Arial,24")).grid(row=22, column=0,columnspan = 9)
        Label(self.frame, text=e9, width=92, height=2, font=("Arial,24")).grid(row=23, column=0,columnspan = 9)
        Label(self.frame, text=e10, width=92, height=2, font=("Arial,24")).grid(row=24, column=0,columnspan = 9)
        Label(self.frame, text=e11, width=92, height=2, font=("Arial,24")).grid(row=25, column=0,columnspan = 9)

        # ————————————————有利的做法
        font_color = "hotpink"
        title_4_1 = "对您有利的做法：%s" % ("  " * self.getSpace("对您有利的做法："))
        Label(self.frame, text=title_4_1, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=29,
                                                                                                                 column=0,
                                                                                                                 pady=4,
                                                                                                                 columnspan=9)
        s_list1 = [
            '1.注意自己有从他人的行为中寻找潜在企图的习惯。当他人表现出敌意时。首先检查自己是否率先表现出了进攻的倾向。',
            '2.不要让怀疑为自己关上帮助的大门。在感情关系中，自己的怀疑破坏了双方信任的基础。他们真的值得信任吗?你总是在大脑中突出对方的弱点。',
            '3.不要总是与他人划清界限。不要总是询问他人的立场。注意到自己总是希望就指导方针与他人达成一致。',
            '4.打断自己对他人的观察，不要总是强调他人是否言行一致。',
            '5.注意到什么时候自己的思维取代了感觉和冲动。',
            "6.不要总是把别人都看作是没有能力或者不值得信任的人。好像其他人都是行动的阻碍。",
            "7.学会保持联系。不要因为害怕而退出，并认为是对方抛弃了自己。",
            '8.注意到自己喜欢怀疑他人的好意和恭维，尤其是在自己放松警惕的时候。“在我毫无准备的时候就会被击中。”',
            "9.承认自己胆量不够。总是需要得到权威的许可才敢行动。",
            "10.注意自己喜欢质疑权威，而不是去寻找双方的共同点。",
            '11.认识到自己往往只会想起糟糕的事情而不是快乐的经历。提醒自己去回忆那些快乐的记忆。6号性格者总是喜欢在负面记忆的轨道上行驶。',
            "12.利用自己的想象力，去想象和表达正面的结果。如果注意力总是集中在糟糕的结果上，那就通过想象力把负面的结果夸大，让自己发现原来现实还不是最糟的。",

                   ]
        start_row = self.displayLine(s_list1, 30, font_color)
        # ————————————————注意的做法
        font_color = "crimson"
        title_4_1 = "您需要注意的做法：%s" % ("  " * self.getSpace("您需要注意的做法："))
        Label(self.frame, text=title_4_1, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=start_row,
                                                                                                                 column=0,
                                                                                                                 pady=4,
                                                                                                                 columnspan=9)
        s_list2 = [
            '1.对潜在的帮助表示怀疑，宁愿自己单干。',
            "2.对成功感到害怕。害怕超越了父母。",
            "3.随着畏惧感的产生，觉得自己变得被动了，觉得自己失去了棱角，开始犹豫不决，不愿再把项目做完。",
            "4.希望自己比那些准备帮助自己的人更出色。",
            "5.碟谍不休。让大脑控制了心灵。让言语和分析取代了实际行为和来自内心的感受。",
            "6.越来越明显的自我怀疑，而且很容易把怀疑投影到他人身上，认为是他人也对自己的能力产生了怀疑。",
            "7.妄自尊大。把改变的过程弄得过于复杂。对结果不切实际的幻想阻碍了完成现实目标的逻辑行动",

        ]
        r = self.displayLine(s_list2, start_row+1, font_color)

    def showSeven(self):
        # ======================================7号性格=================================================================
        f1 = "1.外向、主动、乐观、贪玩；%s" % ("  " * self.getSpace("1.外向、主动、乐观、贪玩；"))
        f2 = "2.关注什么是未来可能的；%s" % ("  " * self.getSpace("2.关注什么是未来可能的；"))
        f3 = "3.乐于探索，多种选择；%s" % ("  " * self.getSpace("3.乐于探索，多种选择；"))
        f4 = "4.不喜欢接受规范，不想被约束；%s" % ("  " * self.getSpace("4.不喜欢接受规范，不想被约束；"))
        f5 = "5.对有兴趣的事很入迷；不善于处理繁琐和细节的任务；%s" % ("  " * self.getSpace("5.对有兴趣的事很入迷；不善于处理繁琐和细节的任务；"))
        f6 = "6.贪图经历和享受，经历比成功更重要；%s" % ("  " * self.getSpace("6.贪图经历和享受，经历比成功更重要；"))
        f7 = "7.头脑灵活，变通快，多计，勇于尝试，富有冒险精神；%s" % ("  " * self.getSpace("7.头脑灵活，变通快，多计，勇于尝试，富有冒险精神；"))
        f8 = "8.总是放任自己，喜欢我行我素，认为『只要我喜欢，有什么不可以。』%s" % ("  " * self.getSpace("8.总是放任自己，喜欢我行我素，认为『只要我喜欢，有什么不可以。』"))
        f9 = "9.讨厌无聊，喜欢尽可能忙碌，认识很多朋友，每天活动都排得满满的；%s" % ("  " * self.getSpace("9.讨厌无聊，喜欢尽可能忙碌，认识很多朋友，每天活动都排得满满的；"))
        f10 = "10.喜欢刺激和紧张的关系，而不喜欢稳定和依赖的关系；%s" % ("  " * self.getSpace("10.喜欢刺激和紧张的关系，而不喜欢稳定和依赖的关系；"))
        f11 = "11.很少用心去聆听别人的感受，所以很难了解别人的内心感受；%s" % ("  " * self.getSpace("11.很少用心去聆听别人的感受，所以很难了解别人的内心感受；"))
        f12 = "12.喜欢上餐馆、娱乐、旅行或同朋友谈天说地的美好享受；%s" % ("  " * self.getSpace("12.喜欢上餐馆、娱乐、旅行或同朋友谈天说地的美好享受；"))
        f13 = "13.是一个快乐、热心、思想正面的人；%s" % ("  " * self.getSpace("13.是一个快乐、热心、思想正面的人；"))

        title_7 = "您的参考性格-7号性格(享乐主义者）：%s" % ("  " * self.getSpace("您的参考性格-7号性格(享乐主义者）："))
        Label(self.frame, text=title_7, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=14,
                                                                                                               column=0,
                                                                                                               pady=4,columnspan = 9)
        Label(self.frame, text=f1, width=92, height=2, font=("Arial,24")).grid(row=15, column=0,columnspan = 9)
        Label(self.frame, text=f2, width=92, height=2, font=("Arial,24")).grid(row=16, column=0,columnspan = 9)
        Label(self.frame, text=f3, width=92, height=2, font=("Arial,24")).grid(row=17, column=0,columnspan = 9)
        Label(self.frame, text=f4, width=92, height=2, font=("Arial,24")).grid(row=18, column=0,columnspan = 9)
        Label(self.frame, text=f5, width=92, height=2, font=("Arial,24")).grid(row=19, column=0,columnspan = 9)
        Label(self.frame, text=f6, width=92, height=2, font=("Arial,24")).grid(row=20, column=0,columnspan = 9)
        Label(self.frame, text=f7, width=92, height=2, font=("Arial,24")).grid(row=21, column=0,columnspan = 9)
        Label(self.frame, text=f8, width=92, height=2, font=("Arial,24")).grid(row=22, column=0,columnspan = 9)
        Label(self.frame, text=f9, width=92, height=2, font=("Arial,24")).grid(row=23, column=0,columnspan = 9)
        Label(self.frame, text=f10, width=92, height=2, font=("Arial,24")).grid(row=24, column=0,columnspan = 9)
        Label(self.frame, text=f11, width=92, height=2, font=("Arial,24")).grid(row=25, column=0,columnspan = 9)
        Label(self.frame, text=f12, width=92, height=2, font=("Arial,24")).grid(row=26, column=0,columnspan = 9)
        Label(self.frame, text=f13, width=92, height=2, font=("Arial,24")).grid(row=27, column=0,columnspan = 9)
        # ————————————————有利的做法
        font_color = "hotpink"
        title_4_1 = "对您有利的做法：%s" % ("  " * self.getSpace("对您有利的做法："))
        Label(self.frame, text=title_4_1, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=29,
                                                                                                                 column=0,
                                                                                                                 pady=4,
                                                                                                                 columnspan=9)
        s_list1 = [
            "1.认识到自己总是被青春和活力所吸引。让自己看到年龄增长和成熟价值。",
            "2.学会让自己面对痛苦，直到发现问题。不要总是觉得：“如果我需要帮助，我就是有缺陷的”。",
            "3.注意到自己出现精神逃避时的情况：过多计划、多项活动、新选择、未来设想。当自己的想法和活动都在高速运转时，7号实际上是在逃避现实。",
            "4.认识到自己喜欢去想象痛苦的感觉，而不是去接受真实的体验。",
            "5.注意到虚幻的快乐和缺乏深度的承诺会让人渴望得到更多的快乐和娱乐。",
            "6.不要沉溺于表面的快乐，而忽视了深层次的体验。",
            "7.不要用虚假或者不成熟的情感发泄取代深层次的情感反应。注意到自己总是害怕做出深入的承诺",
            "8.不要觉得自己总是应该获得特殊待遇。",
            "9.发现真正的责任范围，这往往比七号希望的要更大。",
            "10.当内在的偏执情绪出现时，坚持脚踏实地。",
            "11.发现他人的批评和自我评价之间的差异，学会正确地评估自己。注意到当自我价值遭到质疑时，自己会很害怕，会渴望重新振作起来，重新获得高人一等的感觉。",
            "12.当良好的自我感觉遭到质疑时，尽管十分愤怒，也要学会控制自己的情绪，继续完成工作。当情感出现问题时，不要对爱人产生两极化的看法，要么认为对方全是错的，要么认为对方全是对的。如果事情看上去很糟糕，会接受现实，而不是胡思乱想。",
            "13.认识到自己喜欢把事物美化，喜欢让事情变得更有趣，总是想象得比实际更好。",
            "14.认识到自己喜欢为自己虚构一个故事，以避免受到痛苦的伤害。这种令人愉快的故事与事实关系甚微，但7号会通过类推的办法把痛苦的情绪精 神化，让注意力转移到精神画面上，从而阻止真正的痛苦体验。",
            "15.认识到自己喜欢逃离现实，躲在自己的幻想和虚假情感中。学会生活在现实中，而不是逃避。",
            "16.舍弃没有实现的选择。不必因为失去选择而产生遭到限制的害怕感。",

        ]
        start_row = self.displayLine(s_list1, 30, font_color)
        print(start_row)
        # ————————————————注意的做法
        font_color = "crimson"
        title_4_1 = "您需要注意的做法：%s" % ("  " * self.getSpace("您需要注意的做法："))
        Label(self.frame, text=title_4_1, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=start_row,
                                                                                                                 column=0,
                                                                                                                 pady=4,
                                                                                                                 columnspan=9)
        s_list2 = [
            '1.对心理治疗感到厌倦，开始向心理医生献殷勤，送小礼物，让自己的注意力转移到有趣的精神追求上。',
            "2.觉得自己高人一等。瞧不起温柔的心理医生，认为对方很可笑。瞧不起普通百姓的生活。",
            "3.在遇到困难情况时，会在脑海中联想很多其他情况，让眼前的困难失去威力。",
            "4.当承诺出现问题时，希望加速完成自己的活动。在失去其他选择时，感到焦虑不安。",
            "5.对承诺感到厌烦。“我想要回我的其他选择。”",
            "6.在乎自己的地位。“我站在哪儿？我的位置在哪儿?其他人怎么看我的？”",
            "7.不想当领导，也不想被领导。希望与权威平起平坐，避免受到他们命令。",
            "8.一旦现有问题出现了好转，就想要离开心理治疗。急于恢复健康状态。",
            "9.喜欢改变，喜欢把现有问题赋予更高的含义。",
            "10.对过去的负面经历产生错误的记忆。",
            "11.通过取笑问题，来表达自己的愤怒。认为遇到的问题很可笑。认为他人的担忧都是微不足道，令人发笑的。",


        ]
        start_row2 = self.displayLine(s_list2, start_row+1, font_color)

    def showEight(self):
        # ======================================8号性格=================================================================
        g1 = "1.外向、主动、乐观、冲动、专制、有正义感；%s" % ("  " * self.getSpace("1.外向、主动、乐观、冲动、专制、有正义感；"))
        g2 = "2.关注权力、独断，并且控制空间和领域；%s" % ("  " * self.getSpace("2.关注权力、独断，并且控制空间和领域；"))
        g3 = "3.充满活力，讨厌虚伪，喜欢危险和冒险的刺激感；%s" % ("  " * self.getSpace("3.充满活力，讨厌虚伪，喜欢危险和冒险的刺激感；"))
        g4 = "4.愤怒爆发直接、面对面、硬碰硬；%s" % ("  " * self.getSpace("4.愤怒爆发直接、面对面、硬碰硬；"))
        g5 = "5.很难听从别人的意见；%s" % ("  " * self.getSpace("5.很难听从别人的意见；"))
        g6 = "6.相信“强权就是公理”，别人会觉得专横霸道；%s" % ("  " * self.getSpace("6.相信“强权就是公理”，别人会觉得专横霸道；"))
        g7 = "7.喜欢被人尊重而不是被人喜爱；%s" % ("  " * self.getSpace("7.喜欢被人尊重而不是被人喜爱；"))
        g8 = "8.通常会支持比较弱势或不利的一方；%s" % ("  " * self.getSpace("8.通常会支持比较弱势或不利的一方；"))
        g9 = "9.会保护、支持自己的朋友、家人和下属；%s" % ("  " * self.getSpace("9.会保护、支持自己的朋友、家人和下属；"))
        g10 = "10.喜欢控制大局和授权给别人的乐趣，但却不喜欢被控制；%s" % ("  " * self.getSpace("10.喜欢控制大局和授权给别人的乐趣，但却不喜欢被控制；"))
        g11 = "11.有坚强的意志力，相信自己能战胜一切挑战和困境而会有突破；%s" % ("  " * self.getSpace("11.有坚强的意志力，相信自己能战胜一切挑战和困境而会有突破；"))
        g12 = "12.不喜欢求人，觉得求人不如求自己，所以不停地增值自己的能力；%s" % ("  " * self.getSpace("12.不喜欢求人，觉得求人不如求自己，所以不停地增值自己的能力；"))
        g13 = "13.对家人粗心大意，缺乏温柔及很难站在对方的立场来思考。%s" % ("  " * self.getSpace("13.对家人粗心大意，缺乏温柔及很难站在对方的立场来思考。"))
        g14 = "14.但是一个负责任的好丈夫、好妻子；%s" % ("  " * self.getSpace("14.但是一个负责任的好丈夫、好妻子；"))
        g15 = "15.是一个坚强、自信、果断和会马上采取行动去解决问题的人；%s" % ("  " * self.getSpace("15.是一个坚强、自信、果断和会马上采取行动去解决问题的人；"))

        title_8 = "您的参考性格-8号性格(保护者）：%s" % ("  " * self.getSpace("您的参考性格-8号性格(保护者）："))
        Label(self.frame, text=title_8, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=14,
                                                                                                               column=0,
                                                                                                               pady=4,columnspan = 9)
        Label(self.frame, text=g1, width=92, height=2, font=("Arial,24")).grid(row=15, column=0,columnspan = 9)
        Label(self.frame, text=g2, width=92, height=2, font=("Arial,24")).grid(row=16, column=0,columnspan = 9)
        Label(self.frame, text=g3, width=92, height=2, font=("Arial,24")).grid(row=17, column=0,columnspan = 9)
        Label(self.frame, text=g4, width=92, height=2, font=("Arial,24")).grid(row=18, column=0,columnspan = 9)
        Label(self.frame, text=g5, width=92, height=2, font=("Arial,24")).grid(row=19, column=0,columnspan = 9)
        Label(self.frame, text=g6, width=92, height=2, font=("Arial,24")).grid(row=20, column=0,columnspan = 9)
        Label(self.frame, text=g7, width=92, height=2, font=("Arial,24")).grid(row=21, column=0,columnspan = 9)
        Label(self.frame, text=g8, width=92, height=2, font=("Arial,24")).grid(row=22, column=0,columnspan = 9)
        Label(self.frame, text=g9, width=92, height=2, font=("Arial,24")).grid(row=23, column=0,columnspan = 9)
        Label(self.frame, text=g10, width=92, height=2, font=("Arial,24")).grid(row=24, column=0,columnspan = 9)
        Label(self.frame, text=g11, width=92, height=2, font=("Arial,24")).grid(row=25, column=0,columnspan = 9)
        Label(self.frame, text=g12, width=92, height=2, font=("Arial,24")).grid(row=26, column=0,columnspan = 9)
        Label(self.frame, text=g13, width=92, height=2, font=("Arial,24")).grid(row=27, column=0,columnspan = 9)
        Label(self.frame, text=g14, width=92, height=2, font=("Arial,24")).grid(row=28, column=0,columnspan = 9)
        Label(self.frame, text=g15, width=92, height=2, font=("Arial,24")).grid(row=29, column=0,columnspan = 9)
        # ————————————————有利的做法
        font_color = "hotpink"
        title_4_1 = "对您有利的做法：%s" % ("  " * self.getSpace("对您有利的做法："))
        Label(self.frame, text=title_4_1, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=29,
                                                                                                                 column=0,
                                                                                                                 pady=4,
                                                                                                                 columnspan=9)
        s_list1 = [
            "1.注意到自己总是要求对一段关系予以明确定义。把斗争看作发展信任的一种方式。",
            "2.注意到自己在感情关系或心理治疗中，总是要求建立清楚的规则。但是一旦建立了规则，又渴望破坏规则。",
            "3.注意到自己总是喜欢在身边寻找对手。喜欢把周围的人都划分成两派，不是朋友就是故人。通过挑衅，让对方采取行动",
            "4.认识到自己的厌烦感觉，实际上是在掩盖其他的情。",
            "5.努力发现他人行为的逻辑性和正确性，允许他人坚持不同的观点。",
            "6.认识到真正的感觉往往是从消沉中产生的。把消沉当作一种感情流露的方式，不要逃避负面情绪",
            "7.注意到什么时候对物质的滥用。不要让对他人的控制欲，取代了自己的其实希望。",
            "8.注意到自己对公正的追求和渴望保护他人的想法，常常把周围的人分成了朋灰和敌人两大对立的阵营。",
            "9.把自己的注意力从“你的方式-VS-我的方式”上转移出来，尽量认识到各个观点之间的相互联系",
            "10.记得把自己的想法和感受记录下来，和自己的强追性健忘做斗争。用自己记录下来的想法和感受提醒自己不要强迫拒绝内心的感觉。",
            "11.学会延迟情感的表达。在准备发火之前，先在心里倒数十下。",
            "12.不要总是从外界寻找问题的根源，学会从自己身上找问题。",
            "13.学会承认自己的错误。",

                   ]
        start_row = self.displayLine(s_list1, 30, font_color)
        # ————————————————注意的做法
        font_color = "crimson"
        title_4_1 = "您需要注意的做法：%s" % ("  " * self.getSpace("您需要注意的做法："))
        Label(self.frame, text=title_4_1, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=start_row,
                                                                                                                 column=0,
                                                                                                                 pady=4,
                                                                                                                 columnspan=9)
        s_list2 = [
            "1.把他人的帮助误认为对自己的怜悯。",
            "2.喜欢控制细节。在行动中对一些小事要求苛刻。“除非我找到我最喜欢的那把汤勺，不然宴会到此为”。",
            "3.把潜在的帮助拒之门外。对他人的优点只字不提。行事鲁莽，把人得罪了自己还不知道。",
            "4.忘记自己的目标。沉浸于过度的狂欢、食物、性爱、毒品之中。觉得越多就是越好。吃着碗里的，望着锅里的。",
            "5.对自己看不顺眼的人发出攻击。",
            "6.难以妥协。要么控制，要么离开。不会看到中间立场。",
            "7.不想让自己表现出依赖性。把他人的疏忽看作对诚信的背叛。",
            "8.关闭自己的感觉。有时候会放弃所有事情，什么也不关心。",
            "9.为了掩藏自身的弱点，而谴责他人，从他人身上挑毛病。",
            "10.制定规则，并把规则强加于他人身上。",
            "11.破坏自己的规则，说明自己是权力的掌控者，是不受约束的。",
            "12.失败以后陷入绝望，不能自拔。",

        ]
        self.displayLine(s_list2, start_row+1, font_color)

    def showNine(self):
        # ======================================9号性格=================================================================
        i1 = "1.内向、被动、乐观、随和；%s" % ("  " * self.getSpace("1.内向、被动、乐观、随和；"))
        i2 = "2.关注周围对其的抱怨；%s" % ("  " * self.getSpace("2.关注周围对其的抱怨；"))
        i3 = "3.顺从、服务、很难说不；%s" % ("  " * self.getSpace("3.顺从、服务、很难说不；"))
        i4 = "4.向往相容和熟悉，避免冲突；%s" % ("  " * self.getSpace("4.向往相容和熟悉，避免冲突；"))
        i5 = "5.拙于排列事情的优先顺序；%s" % ("  " * self.getSpace("5.拙于排列事情的优先顺序；"))
        i6 = "6.不像其他人那样关注名誉及地位；%s" % ("  " * self.getSpace("6.不像其他人那样关注名誉及地位；"))
        i7 = "7.别人会觉得自己动作很慢、经常拖延而不去行动；%s" % ("  " * self.getSpace("7.别人会觉得自己动作很慢、经常拖延而不去行动；"))
        i8 = "8.时常因为问题而懒脑但却不去解决，特别喜欢睡觉和看电视容易耽误事情，别人会觉得其%s" % (
                "  " * self.getSpace("8.时常因为问题而懒脑但却不去解决，特别喜欢睡觉和看电视容易耽误事情，别人会觉得其"))
        i9 = "      被动和优柔寡断；%s" % ("  " * self.getSpace("被动和优柔寡断；"))
        i10 = "9.不喜欢命令别人，但当别人命令自己时，会反感和变得倔强对于不同观点的分歧和争论，%s" % (
                "  " * self.getSpace("9.不喜欢命令别人，但当别人命令自己时，会反感和变得倔强对于不同观点的分歧和争论，"))
        i11 = "      能看到其方方面面是一个和平、友善、随和、包容和忍耐的人。%s" % ("  " * self.getSpace("能看到其方方面面是一个和平、友善、随和、包容和忍耐的人。"))
        # i10 = "   9.不喜欢命令别人，但当别人命令自己时，会反感和变得倔强对于不同观点的分歧%s" % (
        #         "  " * self.getSpace("9不喜欢命令别人，但当别人命令自己时，会反感和变得倔强对于不同观点的分歧"))
        # i11 = "和争论，能看到其方方面面是一个和平、友善、随和、包容和忍耐的人。%s" % (
        #         "  " * self.getSpace("和争论，能看到其方方面面是一个和平、友善、随和、包容和忍耐的人。"))

        title_9 = "您的参考性格-9号性格(调停者）：%s" % ("  " * self.getSpace("您的参考性格-9号性格(调停者）："))
        Label(self.frame, text=title_9, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=14,
                                                                                                               column=0,
                                                                                                               pady=4,columnspan = 9)
        Label(self.frame, text=i1, width=92, height=2, font=("Arial,24")).grid(row=15, column=0,columnspan = 9)
        Label(self.frame, text=i2, width=92, height=2, font=("Arial,24")).grid(row=16, column=0,columnspan = 9)
        Label(self.frame, text=i3, width=92, height=2, font=("Arial,24")).grid(row=17, column=0,columnspan = 9)
        Label(self.frame, text=i4, width=92, height=2, font=("Arial,24")).grid(row=18, column=0,columnspan = 9)
        Label(self.frame, text=i5, width=92, height=2, font=("Arial,24")).grid(row=19, column=0,columnspan = 9)
        Label(self.frame, text=i6, width=92, height=2, font=("Arial,24")).grid(row=20, column=0,columnspan = 9)
        Label(self.frame, text=i7, width=92, height=2, font=("Arial,24")).grid(row=21, column=0,columnspan = 9)
        Label(self.frame, text=i8, width=92, height=2, font=("Arial,24")).grid(row=22, column=0,columnspan = 9)
        Label(self.frame, text=i9, width=92, height=2, font=("Arial,24")).grid(row=23, column=0,columnspan = 9)
        Label(self.frame, text=i10, width=92, height=2, font=("Arial,24")).grid(row=24, column=0,columnspan = 9)
        Label(self.frame, text=i11, width=92, height=2, font=("Arial,24")).grid(row=25, column=0,columnspan = 9)
        # ————————————————有利的做法
        font_color = "hotpink"
        title_4_1 = "对您有利的做法：%s" % ("  " * self.getSpace("对您有利的做法："))
        Label(self.frame, text=title_4_1, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=29,
                                                                                                                 column=0,
                                                                                                                 pady=4,
                                                                                                                 columnspan=9)
        s_list1 = [
            "1.注意到自己总是想办法获得他人的积极评价，借此找到自己的位置。",
            "2.注意到自己喜欢把他人变成决定的参照物：“我是同意他，还是反对他？”。",
            "3.不要让举棋不定的困惑取代了自己的真实感觉和愿望。",
            "4.让工作项目有计划地进行，设定最后期限来帮助自己集中精力。",
            "5.不要保留自己的意见，把它说出来。",
            "6.学会一心一意地完成任务，不要被其他事情分心。",
            "7.不要把注意力转移到不必要的替代品上，比如食品或电视。要及时注意到这种情绪的出现。",
            "8.不要向他人去寻求决定的答案。本性格者很清楚自己不想要什么，但是却不知道自己要什么，不过他们可以通过排除法找到答案",
            "9.要练习既能从他人的立场上行动，又能从自己的立场上行动。",
            "10.在注意力分散到不必要的事物上时，学会限制自己。",
            "11.关注眼前的下一步，而不是最终的目标，因为最终的目标需要一步一步地实现。",
            "12.注意到自己面对压力时，会变得顽固。",
            "13.通过想象力来释放自己的愤怒。想象自己说出或做出了最糟糕的事情。",
            "14.直到内心的怒火得到消减。",

                   ]
        start_row = self.displayLine(s_list1, 30, font_color)
        # ————————————————注意的做法
        font_color = "crimson"
        title_4_1 = "您需要注意的做法：%s" % ("  " * self.getSpace("您需要注意的做法："))
        Label(self.frame, text=title_4_1, fg="white", bg=self.color, width=92, height=2, font=("Arial,24")).grid(row=start_row,
                                                                                                                 column=0,
                                                                                                                 pady=4,
                                                                                                                 columnspan=9)
        s_list2 = [
            "1.依赖他人的帮助，不愿与他人分开。",
            "2.责备他人。因为过于在意他人的愿望，一旦出现问题，就会产生“都是他们的错”的想法。",
            "3.变得顽固。感到来自他人的压力。不愿把问题拿到桌面上来。僵持不动，逼着对方首先采取行动",
            "4.急需找到消磨时间和能量的新办法。",
            "5.恍憾。在谈话的时候注意力不集中，同时想着好几件事情。",
            "6.无法注意到真正的需要，让琐事占据了自己的注意力。",
            "7.习惯按部就班，从事机械性的动作。",
            "8.麻木、无动于衷。期望事情自己结束，而不是主动表明态度。不希望听到负面信息。",
            "9.总是需要得到更多的信息，等待他人的解释。",
            "10.工作无法善始善终。感觉受到了骚扰，不想认真对待工作。希望用最小的投入换得最大的收获",
            "11.感觉有很多事情要做。不知道该从哪里做起，不知道从哪里找到能量。",

        ]
        start_row2 = self.displayLine(s_list2, start_row+1, font_color)
    #---------------------------------------------------------------------------------------------
    def displayScoreAndCharacter(self,test_result):
        #######################################图形显示
        mainChar = 0
        self.numChar = 0
        for i in range(3,12):
            if test_result[i] > mainChar:
                mainChar = test_result[i]
                self.numChar = i
        print(mainChar,self.numChar)
        num = ["一","二","三","四","五","六","七","八","九"]
        for i in range(3,12):
            if int(test_result[i]) == mainChar:
                print(num[i - 3])
                text1 = "%s号:%s%s%s" % (
                num[i-3],self.displayMainSquare(test_result[i]), test_result[i], " " * self.displaySpace(score=test_result[i]))
                Label(self.frame, text=text1, width=92, height=2, fg ="green",font=("Arial,24")).grid(row=2+i, column=0, columnspan=9)
            else:
                print(num[i - 3])
                text2 = "%s号:%s%s%s" % (
                num[i-3],self.displaySquare(test_result[i]), test_result[i], " " * self.displaySpace(score=test_result[i]))
                Label(self.frame, text=text2, width=92, height=2, font=("Arial,24")).grid(row=2+i, column=0,columnspan=9)

        #此时row=14 这里row从15开始
        self.numChar -= 2
        if self.numChar == 1:
            self.showOne()
        elif self.numChar == 2 :
            self.showTwo()
        elif self.numChar == 3 :
            self.showThree()
        elif self.numChar == 4:
            self.showFour()
        elif self.numChar == 5:
            self.showFive()
        elif self.numChar == 6:
            self.showSix()
        elif self.numChar == 7:
            self.showSeven()
        elif self.numChar == 8:
            self.showEight()
        else:
            self.showNine()

    def showTable(self,test_result):
        ############防止视力疲劳 用不同的颜色显示
        COLOR_1 = "SKYBLUE"
        COLOR_2 = "LIGHTBLUE"
        Label(self.frame, text="1号", bg=COLOR_1, width=10, height=2, font=("Arial,24")).grid(row=3, column=0,
                                                                                             pady=1,
                                                                                             padx=1)
        Label(self.frame, text=test_result[3], bg=COLOR_2, width=10, height=2, font=("Arial,24")).grid(row=4,
                                                                                                       column=0,
                                                                                                       pady=1,
                                                                                                       padx=1)

        Label(self.frame, text="2号", bg=COLOR_1, width=10, height=2, font=("Arial,24")).grid(row=3, column=1,
                                                                                             pady=1, padx=1)
        Label(self.frame, text=test_result[4], bg=COLOR_2, width=10, height=2, font=("Arial,24")).grid(row=4,
                                                                                                       column=1,
                                                                                                       pady=1,
                                                                                                       padx=1)
        Label(self.frame, text="3号", bg=COLOR_1, width=10, height=2, font=("Arial,24")).grid(row=3, column=2,
                                                                                             pady=1,
                                                                                             padx=1)
        Label(self.frame, text=test_result[5], bg=COLOR_2, width=10, height=2, font=("Arial,24")).grid(row=4,
                                                                                                       column=2,
                                                                                                       pady=1,
                                                                                                       padx=1)
        Label(self.frame, text="4号", bg=COLOR_1, width=10, height=2, font=("Arial,24")).grid(row=3, column=3,
                                                                                             pady=1,
                                                                                             padx=1)
        Label(self.frame, text=test_result[6], bg=COLOR_2, width=10, height=2, font=("Arial,24")).grid(row=4,
                                                                                                       column=3,
                                                                                                       pady=1,
                                                                                                       padx=1)
        Label(self.frame, text="5号", bg=COLOR_1, width=10, height=2, font=("Arial,24")).grid(row=3, column=4,
                                                                                             pady=1,
                                                                                             padx=1)
        Label(self.frame, text=test_result[7], bg=COLOR_2, width=10, height=2, font=("Arial,24")).grid(row=4,
                                                                                                       column=4,
                                                                                                       pady=1,
                                                                                                       padx=1)
        Label(self.frame, text="6号", bg=COLOR_1, width=10, height=2, font=("Arial,24")).grid(row=3, column=5,
                                                                                             pady=1,
                                                                                             padx=1)
        Label(self.frame, text=test_result[8], bg=COLOR_2, width=10, height=2, font=("Arial,24")).grid(row=4,
                                                                                                       column=5,
                                                                                                       pady=1,
                                                                                                       padx=1)
        Label(self.frame, text="7号", bg=COLOR_1, width=10, height=2, font=("Arial,24")).grid(row=3, column=6,
                                                                                             pady=1,
                                                                                             padx=1)
        Label(self.frame, text=test_result[9], bg=COLOR_2, width=10, height=2, font=("Arial,24")).grid(row=4,
                                                                                                       column=6,
                                                                                                       pady=1,
                                                                                                       padx=1)
        Label(self.frame, text="8号", bg=COLOR_1, width=10, height=2, font=("Arial,24")).grid(row=3, column=7,
                                                                                             pady=1,
                                                                                             padx=1)
        Label(self.frame, text=test_result[10], bg=COLOR_2, width=10, height=2, font=("Arial,24")).grid(row=4,
                                                                                                       column=7,
                                                                                                       pady=1,
                                                                                                       padx=1)
        Label(self.frame, text="9号", bg=COLOR_1, width=10, height=2, font=("Arial,24")).grid(row=3, column=8,
                                                                                             pady=1,
                                                                                             padx=1)
        Label(self.frame, text=test_result[11], bg=COLOR_2, width=10, height=2, font=("Arial,24")).grid(row=4,
                                                                                                        column=8,
                                                                                                        pady=1,
                                                                                                        padx=1)

    #显示测试结果
    def show(self):

        #============================108题的测试结果======================================
        #标题
        test_time, test_type = queryDB.queryDB().getTestTimeAndType(uname=self.uname)
        print(test_type,test_time)
        lable_title = Label(self.frame,text="最近一次的测试结果({0})/({1}版)".format(test_time,test_type),bg="silver",fg="white",width=98,height=4,font=("Arial,36"))
        # lable_title.grid(row=0,column=0,pady=9,rowspan=8)
        lable_title.grid(row=0,column=0,columnspan=9)
        lable_author = Label(self.frame, text="108题测试得分情况:%s"%(" "*76), bg="rosybrown", width=98, height=2, font=("Arial,24"))
        lable_author.grid(row=1,column=0,columnspan=9,pady=4)

        try:
            querySQL = queryDB.queryDB()
            my_id = querySQL.getUserId(self.uname)
            test_result = querySQL.selectTestResult(uname=self.uname,user_id=my_id)
            print("这是返回的数据")
            print(test_result)
            if test_result:
                self.showTable(test_result)
                self.displayScoreAndCharacter(test_result)
            else:
                Label(self.frame, text="您暂时还没有测试数据，请您测试完再来查看。", fg="red", width=90, height=4, font=("Arial,30")).grid(row=3,
                                                                                                                column=0,
                                                                                                                pady=1,
                                                                                                                padx=1,
                                                                                                        columnspan=9,rowspan=2)
        except Exception as e:
            print("错误")
            logging.error(e)
            # print(e)

class ShowMenu():
    def __init__(self,root,app):
        self.root = root
        self.app = app

    def showMenu(self):
        # 定义注菜单栏
        self.menubar = Menu(self.root)
        # ----定义子菜单----
        ###账户子菜单
        self.account_menu = Menu(self.menubar)
        self.account_menu.add_command(label="我的测试结果", command=self.app.myTestResult)
        self.account_menu.add_command(label="账户中心", command=self.app.accountCenter)
        self.account_menu.add_separator()  # 添加一条分割线
        self.account_menu.add_command(label="退出", command=lambda: self.app.quitSystem())  # 对事件传入参数
        self.account_menu.add_command(label="注销",command=lambda :self.app.logout(self.root))
        self.menubar.add_cascade(label="账户", menu=self.account_menu)  # 将子菜单和顶级菜单连接
        ###文件子菜单
        self.view_menu = Menu(self.menubar)
        self.view_menu.add_command(label="108试题", command=self.app.viewTestQuestions_108)
        self.view_menu.add_command(label="144试题", command=self.app.viewTestQuestions_144)
        self.menubar.add_cascade(label="查看", menu=self.view_menu)  # 将子菜单和顶级菜单连接
        ### 子菜单  测试
        self.view_menu = Menu(self.menubar)
        self.view_menu.add_command(label="108题版", command=self.app.testQuestion_108)
        self.view_menu.add_command(label="144题版", command=self.app.testQuestion_144)
        self.menubar.add_cascade(label="测试", menu=self.view_menu)  # 将子菜单和顶级菜单连接

        ### 子菜单  关于
        self.about_menu = Menu(self.menubar)
        self.about_menu.add_command(label="作者简介", command=self.app.aboutAuthor)
        self.about_menu.add_separator()
        self.about_menu.add_command(label="如何测试", command=self.app.aboutHowToTest)
        self.about_menu.add_command(label="九种性格特征", command=self.app.aboutNineCharacter)
        self.menubar.add_cascade(label="关于", menu=self.about_menu)  # 将子菜单和顶级菜单连接

        self.root["menu"] = self.menubar  # 将菜单栏添加到根窗口

def main():

    uanme = "jums"
    root = Tk()
    root.geometry("300x300")
    # show_qu = ViewItemContent_105(root,uanme,questions_dict_105)
    # show_qu.show()
    app = Applications.App(root=root, uname=uanme)
    ShowMenu(root,app).showMenu()
    root.mainloop()

if __name__ == '__main__':
    main()


