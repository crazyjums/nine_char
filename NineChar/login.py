import tkinter as tk
from tkinter import messagebox
import queryDB
import mainWindow
import Applications
import string

class LoginWindow():
    #构造方法
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x380+350+50")
        self.root.title("九型人格测试系统v1.0-登录")
        self.root.resizable(width=False, height=False)

        self.submit_uname = False
        self.submit_pwd = False
        self.submit_confirm_pwd = False
        self.submit_tel = False
        self.submit_nickname = False


    #登录的窗口显示
    def showLoginWindow(self):
        # 显示图片
        self.canvas = tk.Canvas(self.root, bg="green", width=500, height=198)
        self.image_file = tk.PhotoImage(file=r"g:\software\pycharm\files\NineChar\login2.png")
        image = self.canvas.create_image(0, 0, image=self.image_file, anchor="nw")
        self.canvas.pack(side="top")

        #定义一个矩形容器  用来放用户名和密码的label和输入框========================
        self.frame_input = tk.Frame(self.root)
        self.frame_input.pack()
        # login
        # 用户名
        self.user_name = tk.StringVar()
        label_username = tk.Label(self.frame_input, text="用户名:", width=30, height=2, justify="left").grid(row=1, column=0)
        entry_username = tk.Entry(self.frame_input, text="username", textvariable=self.user_name, width=30).grid(row=1, column=1)
        # 密码
        self.passwd = tk.StringVar()
        label_password = tk.Label(self.frame_input, text="密  码:", width=30, height=2, justify="left").grid(row=2, column=0)
        entry_password = tk.Entry(self.frame_input, text="password", textvariable=self.passwd, show="*", width=30)
        entry_password.bind("<Return>",self.loginEnter)#绑定enter键   按下enter键就可以触发登录事件
        entry_password.grid(row=2,column=1)
        #=======================================
        #用来放错误提示
        self.label_error_info_login = tk.Label(self.root,text="",width=90,height=1,fg="red")
        self.label_error_info_login.pack()
        #======================================

        #该容器用来盛放登录和注册按钮==============
        self.frame_button = tk.Frame(self.root)
        self.frame_button.pack()
        # 登录按钮
        button_login = tk.Button(self.frame_button, text="登   录", command=self.login, width=15, height=1, activebackground="#20b2aa",
                                 activeforeground="white")
        button_login.pack(side="left", pady=20,padx=20)
        # 注册按钮
        button_signup = tk.Button(self.frame_button, text="注   册", command=self.signUpWindow, width=15, height=1,
                                  activebackground="#20b2aa", activeforeground="white")
        button_signup.pack(side="right", pady=20,padx=20)
        #====================================
        #让窗口开始循环监听
        self.root.mainloop()

    ##触发登录事件 # 如果点按下了Enter键 触发该事件
    def loginEnter(self,event):
        uname = self.user_name.get()
        pwd= self.passwd.get()
        self.app = Applications.App(self.root, uname)
        # messagebox.showinfo(title="login",message=uname + "你点了login一下")
        querySQL = queryDB.queryDB()
        if not uname and not pwd:#用户名和密码没写全
            self.label_error_info_login["text"] = "废物，【用户名】和【密码】空着呢，我怎么登录啊"
            # messagebox.showwarning(title="登录警告",message="对不起，用户名或密码不能为空")
        elif not uname and pwd:
            self.label_error_info_login["text"] = "废物，【用户名】还空着呢，我怎么登录啊"
        elif not pwd and uname:
            self.label_error_info_login["text"] = "废物，【密码】空着呢，我怎么登录啊"
        else:#用户民和密码都已填写  判断对错
            if querySQL.duplicate_check(uname):#如果该户注册了
                if querySQL.checkUser(uname=uname,pwd=pwd):#用户名和密码都输入正确
                    # self.root.destroy()  # 登录成功之后 登录界面消失
                    # self.root.quit()
                    self.root.withdraw()
                    self.root.destroy()
                    # root = tk.Tk()  #因为self.root界面已经消失了  所以这里再创建一个主窗口 参数在函数内部设定
                    mainWindow.MainWindow(uname=uname,pwd=pwd).show()

                else:#用户名或者密码输入有误
                    self.label_error_info_login["text"] = "废物，用户名或者密码输错了"
                    # messagebox.showinfo(title="登录错误", message="用户名或密码错误，请重新输入")
            else:#改用户没有注册
                self.label_error_info_login["text"] = "废物，该用户还没有注册呢，赶紧注册"
                # messagebox.showerror(title="登录错误", message="对不起，该用户还没有注册")

    ##触发登录事件 # 如果点按下了登录按钮 触发该事件
    def login(self):
            uname = self.user_name.get()
            pwd = self.passwd.get()
            self.app = Applications.App(self.root, uname)
            # messagebox.showinfo(title="login",message=uname + "你点了login一下")
            querySQL = queryDB.queryDB()
            if not uname and not pwd:  # 用户名和密码没写全
                self.label_error_info_login["text"] = "废物，【用户名】和【密码】空着呢，我怎么登录啊"
                # messagebox.showwarning(title="登录警告",message="对不起，用户名或密码不能为空")
            elif not uname and pwd:
                self.label_error_info_login["text"] = "废物，【用户名】还空着呢，我怎么登录啊"
            elif not pwd and uname:
                self.label_error_info_login["text"] = "废物，【密码】空着呢，我怎么登录啊"
            else:  # 用户民和密码都已填写  判断对错
                if querySQL.duplicate_check(uname):  # 如果该户注册了
                    if querySQL.checkUser(uname=uname, pwd=pwd):  # 用户名和密码都输入正确
                        # self.root.destroy()  # 登录成功之后 登录界面消失
                        # self.root.quit()
                        self.root.withdraw()
                        self.root.destroy()
                        # root = tk.Tk()  #因为self.root界面已经消失了  所以这里再创建一个主窗口 参数在函数内部设定
                        mainWindow.MainWindow(uname=uname, pwd=pwd).show()

                    else:  # 用户名或者密码输入有误
                        self.label_error_info_login["text"] = "对不起，用户名或者密码输错了"
                        # messagebox.showinfo(title="登录错误", message="用户名或密码错误，请重新输入")
                else:  # 改用户没有注册
                    self.label_error_info_login["text"] = "对不起，该用户还没有注册，请先注册"
                    # messagebox.showerror(title="登录错误", message="对不起，该用户还没有注册")


    #注册账号的窗口
    def signUpWindow(self):

        top_window = tk.Toplevel(self.root)
        top_window.geometry("550x600+360+50")
        top_window.title("九型人格测试系统v.10-注册账号")
        top_window.resizable(width=False,height=False)
        #定义一个容器 用来放label
        title_frame = tk.Frame(top_window,bg="red",width=550,height=5,)
        title_frame.pack(side="top",fill="x")

        #设置背景图片
        # bg_p = tk.PhotoImage(file="login.gif")
        show_info = tk.StringVar()
        title_label = tk.Label(title_frame,text="注册账号",width=550,height=2,bg="#40e0d0",font=("Arial",24))
        title_label.pack()

        #该容器用来放用户输入的数据  比如：用户名和密码等
        top_frame = tk.Frame(top_window,)
        top_frame.pack()
        def usernameEvent(event):
            print("在用户名事件中")
            uname = self.new_name.get()
            letter = string.ascii_letters + string.digits
            if not uname:
                label_username_error['fg'] = "red"
                label_username_error["text"] = "用户名不能为空"
                self.submit_uname = False
            else:
                num_allow = 0
                for i in uname:
                    if i not in letter:
                        num_allow += 1
                if num_allow > 0:
                    label_username_error['fg'] = "red"
                    label_username_error["text"] = "含有非法字符"
                    self.submit_uname = False
                else:
                    querySQL = queryDB.queryDB()
                    if querySQL.duplicate_check(uname):
                        label_username_error['fg'] = "red"
                        label_username_error["text"] = "该用户被注册过了"
                        self.submit_uname = False
                    else:
                        label_username_error['fg'] = "green"
                        label_username_error["text"] = "合法用户名"
                        self.submit_uname = True
        def nicknameEvent(event):
            print("在nickname事件中")
            if not self.nick_name.get():
                label_nickname_error["fg"] = "red"
                label_nickname_error["text"] = "昵称不能为空"
                self.submit_nickname = False
                print(self.submit_nickname)
            else:
                label_nickname_error["fg"] = "green"
                label_nickname_error["text"] = "合法昵称"

                self.submit_nickname = True
                print(self.submit_nickname)
        def passwordEvent(event):
            print("在password事件中")
            password = self.new_pwd.get()
            dig = string.digits
            letter = string.ascii_letters
            printable = string.printable
            punctuation = string.punctuation #标点符号
            if len(password) < 8:
                if not password:
                    label_new_pwd_error["fg"] = "red"
                    label_new_pwd_error["text"] = "密码不能为空"
                    self.submit_pwd = False
                else:
                    label_new_pwd_error["fg"] = "red"
                    label_new_pwd_error["text"] = "密码至少8位"
                    self.submit_pwd = False
            else:#不空且大于8位
                num_dig = 0
                num_letter = 0
                num_punc = 0
                for i in password:
                    if i in dig:
                        num_dig += 1
                    elif i in letter:
                        num_letter += 1
                    elif i in punctuation:
                        num_punc += 1
                if int(num_dig) == len(password) or int(num_letter) == len(password) or int(num_punc) == len(password):
                    label_new_pwd_error["fg"] = "orangered"
                    label_new_pwd_error["text"] = "安全等级-低"
                    self.submit_pwd = True
                elif int(num_dig) + int(num_letter) == len(password) or int(num_dig) + int(num_punc) == len(password) or int(num_punc) + int(num_dig) == len(password):
                    label_new_pwd_error["fg"] = "cyan"
                    label_new_pwd_error["text"] = "安全等级-中"
                    self.submit_pwd = True
                elif int(num_dig) + int(num_punc) + int(num_letter) == len(password):
                    label_new_pwd_error["fg"] = "green"
                    label_new_pwd_error["text"] = "安全等级-高"
                    self.submit_pwd = True
                else:
                    label_new_pwd_error["fg"] = "red"
                    label_new_pwd_error["text"] = "含有非法字符"
                    self.submit_pwd = False
        def confirmpPwdEvent(event):
            print("在confirmpwd事件中")
            confirm_pwd = self.confirm_pwd.get()
            pwd = self.new_pwd.get()
            if self.new_pwd.get():
                if not confirm_pwd:
                    label_confirm_pwd_error['fg'] = "red"
                    label_confirm_pwd_error["text"] = "确认密码不能为空"
                    self.submit_confirm_pwd = False
                elif confirm_pwd != pwd and confirm_pwd:
                    label_confirm_pwd_error["fg"] = "red"
                    label_confirm_pwd_error["text"] = "两次密码不一致"
                    self.submit_confirm_pwd = False
                else:
                    label_confirm_pwd_error["fg"] = "green"
                    label_confirm_pwd_error["text"] = "合法确认密码"
                    self.submit_confirm_pwd = True
        def telEvent(event):
            print("在tel事件中")
            tel = self.tel.get()
            if len(tel) != 11:
                if  len(tel) == 0:
                    label_tel_error["fg"] = "red"
                    label_tel_error["text"] = "电话不能为空"
                    self.submit_tel = False
                else:
                    label_tel_error["fg"] = "red"
                    label_tel_error["text"] = "电话号码得11位"
                    self.submit_tel = False
            else:
                num_not_dig = 0
                for i in tel:
                    if i not in string.digits:
                        num_not_dig += 1
                if num_not_dig > 0:
                    label_tel_error["fg"] = "red"
                    label_tel_error["text"] = "含有非数字字符"
                    self.submit_tel = False
                else:
                    label_tel_error["fg"] = "green"
                    label_tel_error["text"] = "合法电话"
                    self.submit_tel = True
        # def checkNone(evnet):
        #     if not self.user_name:

        #用户名 登录账号
        self.new_name = tk.StringVar()
        label_username = tk.Label(top_frame, text="用户名:", width=30, height=2, justify="left").grid(row=0,column=0)
        entry_username = tk.Entry(top_frame, text="username",
                                  textvariable=self.new_name, width=30)
        label_username_error = tk.Label(top_frame,text="",fg="red",width=15,)
        label_username_error.grid(row=0,column=2)
        entry_username.bind("<FocusOut>", usernameEvent)
        entry_username.grid(row=0, column=1)
        #昵称
        self.nick_name = tk.StringVar()
        label_nick_name = tk.Label(top_frame, text="昵   称:", width=30, height=2, justify="left").grid(row=1, column=0)
        entry_nick_name = tk.Entry(top_frame, text="nickname", textvariable=self.nick_name, width=30)
        entry_nick_name.bind("<FocusOut>",nicknameEvent)
        entry_nick_name.grid(row=1,column=1)
        label_nickname_error = tk.Label(top_frame, text="", fg="red", width=15, )
        label_nickname_error.grid(row=1, column=2)
        #密码
        self.new_pwd = tk.StringVar()
        label_pwd = tk.Label(top_frame, text="密   码:", width=30, height=2, justify="left").grid(row=2,column=0)
        entry_pwd = tk.Entry(top_frame, text="password", textvariable=self.new_pwd, width=30,show="*")
        entry_pwd.bind("<FocusOut>",passwordEvent)
        entry_pwd.grid(row=2, column=1)
        label_new_pwd_error = tk.Label(top_frame, text="", fg="red", width=15, )
        label_new_pwd_error.grid(row=2, column=2)
        #确认密码
        self.confirm_pwd = tk.StringVar()
        label_pwd_confirm = tk.Label(top_frame, text="确认密码:", width=30, height=2, justify="left").grid(row=3, column=0)
        entry_pwd_confirm = tk.Entry(top_frame, text="confirm_password", textvariable=self.confirm_pwd, width=30,show="*")
        entry_pwd_confirm.bind("<FocusOut>",confirmpPwdEvent)
        entry_pwd_confirm.grid(row=3, column=1)
        label_confirm_pwd_error = tk.Label(top_frame, text="", fg="red", width=15, )
        label_confirm_pwd_error.grid(row=3, column=2)
        #手机号码
        self.tel = tk.StringVar()
        label_tel = tk.Label(top_frame, text="手   机:", width=30, height=2, justify="left").grid(row=4, column=0)
        entry_tel = tk.Entry(top_frame, text="tel", textvariable=self.tel, width=30,)
        entry_tel.bind("<FocusOut>",telEvent)
        entry_tel.grid(row=4, column=1)
        label_tel_error = tk.Label(top_frame, text="", fg="red", width=15, )
        label_tel_error.grid(row=4,column=2)
        # 备注
        self.back = tk.StringVar()
        label_back = tk.Label(top_frame, text="备   注:", width=30, height=2, justify="left").grid(row=5, column=0)
        entry_back = tk.Text(top_frame,   width=30,height=5 )
        entry_back.grid(row=5, column=1)
        #该容器用来放错误信息
        info_frame = tk.Frame(top_window)
        info_frame.pack()
        lebel_error_info_signup = tk.Label(info_frame,text="",width=90,height=2,fg="red")
        lebel_error_info_signup.pack(pady=10)

        def clear():
            self.new_pwd.set("")
            self.new_name.set("")
            self.confirm_pwd.set("")
            self.nick_name.set("")
            self.tel.set("")
            # self.tel.get()
            entry_back.delete("0.0","end")

        def submit():
            _new_name = self.new_name.get()
            _pwd = self.new_pwd.get()
            _confirm_pwd = self.confirm_pwd.get()
            _nick_name = self.nick_name.get()
            _back = entry_back.get("0.0","end")
            _back = _back.strip()
            _tel = self.tel.get()
            submit_list = [self.submit_uname,self.submit_nickname,self.submit_pwd,self.submit_confirm_pwd,self.submit_tel]
            submit_name = ['用户名','昵称','密码','确认密码','电话']
            print(submit_list)
            if self.submit_confirm_pwd and self.submit_pwd and self.submit_uname and self.submit_tel and self.submit_nickname:
                if _pwd != _confirm_pwd:
                    lebel_error_info_signup["text"] = "您两次密码输入不一致，请确认注册。"
                else:
                    if queryDB.queryDB().duplicate_check(_new_name):
                        lebel_error_info_signup["text"] = "该用户名已经被注册过，请重新输入一个新的用户名。"
                        # messagebox.showwarning(title="注册错误",message="该用户名已经被注册过，请重新输入一个新的用户名。")
                    else:
                        qu = queryDB.queryDB()
                        answer = qu.insertUser(uname=_new_name,pwd=_pwd,tel=_tel,back=_back,nickname=_nick_name)
                        if answer:
                            if messagebox.askokcancel(title="确认取消",message="您确认注册该账号吗？"):
                                messagebox.showinfo(title="注册成功", message="注册成功，您的账号为：" + _new_name + ",密码：" + _pwd)
                                top_window.destroy()
            else:
                num_error = []
                for i in range(len(submit_list)):
                    if submit_list[i] == False:
                        num_error.append(i)
                if len(num_error) == 1:
                    lebel_error_info_signup['text'] = "【{0}】中不符合要求。".format(submit_name[num_error.pop()])
                elif len(num_error) == 2:
                    lebel_error_info_signup['text'] = "【{0}】|【{1}】中不符合要求。".format(submit_name[num_error.pop()],submit_name[num_error.pop()])
                elif len(num_error) == 3:
                    lebel_error_info_signup['text'] = "【{0}】|【{1}】|【{2}】中不符合要求。".format(
                        submit_name[num_error.pop()],submit_name[num_error.pop()],submit_name[num_error.pop()])
                elif len(num_error) == 4:
                    lebel_error_info_signup['text'] = "【{0}】|【{1}】|【{2}】|【{3}】中不符合要求。".format(
                        submit_name[num_error.pop()],submit_name[num_error.pop()],submit_name[num_error.pop()],submit_name[num_error.pop()])
                elif len(num_error) == 5:
                    lebel_error_info_signup['text'] = "【{0}】|【{1}】|【{2}】|【{3}】|【{4}】中不符合要求。".format(
                        submit_name[num_error.pop()],submit_name[num_error.pop()],submit_name[num_error.pop()],submit_name[num_error.pop()],submit_name[num_error.pop()])


        #按钮
        button_register = tk.Button(top_window, text="注   册", command=submit,width=15,height=1,
                                  activebackground="#20b2aa",activeforeground="white")
        # button_register.bind("<FocusIn>",checkNone)
        button_register.place(x=120,y=430)
        tk.Button(top_window, text="清   空", command=clear, width=15, height=1,
                                  activebackground="#20b2aa", activeforeground="white").place(x=300,y=430)




#程序的入口
if __name__ == '__main__':
    LoginWindow().showLoginWindow()