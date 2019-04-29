import pymysql
import logging
import time

class queryDB():
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "root"
        self.database = "ninechar"
        self.charset = "utf8mb4"
        self.port = 3306

    def DB(self):
        return pymysql.connect(self.host,self.user, self.password, self.database, self.port, charset=self.charset)

    #检查用户名和密码
    def checkUser(self,uname,pwd):
        mysqlDB = self.DB()
        sql = "select * from user where username=\'{0}\' and password=\'{1}\'".format(uname,pwd)
        print(sql)
        try:
            with mysqlDB.cursor() as cursor:
                cursor.execute(sql)
                if cursor.rowcount >= 1:
                    print("checkAll")
                    print(cursor.fetchall())
                    print(cursor.rowcount)
                    return True
                else:
                    return False
        except Exception as e:
            logging.error(e)
        finally:
            mysqlDB.close()

    #查重  用户名不能一样
    def duplicate_check(self,uname):
        mysqlDB = self.DB()
        sql = "select * from user where username=\'{0}\' ".format(uname)
        print(sql)
        try:
            with mysqlDB.cursor() as cursor:
                info = cursor.execute(sql)
                if info >= 1:
                    #表示用户名重复了
                    return True
                else:
                    #表示用户名没有重复
                    return False
        except Exception as e:
            logging.error(e)
        finally:
            mysqlDB.close()

    #得到一条完整的用户记录信息 在用户登录以后使用
    def selectUsersInfo(self, uname):
        mysqlDB = self.DB()
        sql = "select * from user where username=\'{0}\' ".format(uname)
        print(sql)
        try:
            with mysqlDB.cursor() as cursor:

                info = cursor.execute(sql)
                if info >= 1:
                    print("selectAllInfo")
                    tuple_info = cursor.fetchall()[0]
                    print(tuple_info)
                    print(cursor.rowcount)
                    return tuple_info
                else:
                    return False
        except Exception as e:
            logging.error(e)
        finally:
            mysqlDB.close()

    # 得到一条完整的用户记录信息
    def selectUsers(self, uname, pwd):
        mysqlDB = self.DB()
        sql = "select * from user where username=\'{0}\' and password=\'{1}\'".format(uname, pwd)
        print(sql)
        try:
            with mysqlDB.cursor() as cursor:

                info = cursor.execute(sql)
                if info >= 1:
                    print("selectAll")
                    tuple_info = cursor.fetchall()[0]
                    print(tuple_info)
                    print(cursor.rowcount)
                    return tuple_info
                else:
                    return False
        except Exception as e:
            logging.error(e)
        finally:
            mysqlDB.close()

    def getNickname(self,uname, pwd):
        nickname = ""
        mysqlDB = self.DB()
        sql = "select nickname from user where username=\'{0}\' and password=\'{1}\'".format(uname, pwd)
        print(sql)
        try:
            with mysqlDB.cursor() as cursor:
                cursor.execute(sql)
                if cursor.rowcount >= 1:
                    print("getNickname")
                    print(cursor.fetchall())
                    print(cursor.rowcount)
                    return True
                else:
                    return False
        except Exception as e:
            logging.error(e)
        finally:
            mysqlDB.close()

        return nickname

    # #检查该用户是否注册了
    # def checkUsername(self, uname):
    #     mysqlDB = self.DB()
    #     sql = "select * from user where username=\'{0}\'".format(uname)
    #     print(sql)
    #     try:
    #         with mysqlDB.cursor() as cursor:
    #             cursor.execute(sql)
    #             if cursor.rowcount >= 1:
    #                 print("checkUsername()")
    #                 # unmae =
    #                 print(type(cursor.fetchall()))
    #                 print(cursor.rowcount)
    #                 return True
    #             else:
    #                 return False
    #     except Exception as e:
    #         logging.error(e)
    #     finally:
    #         mysqlDB.close()

    def insertUser(self,uname, pwd, tel, back, nickname):
        sql = "insert into user(username,password,tel,back,nickname) " \
              "VALUES(\'{0}\',\'{1}\',\'{2}\',\'{3}\',\'{4}\')".format(uname, pwd, tel, back, nickname)
        print(sql)
        mysqlDB = self.DB()
        try:
            with mysqlDB.cursor() as cursor:
                cursor.execute(sql)
                mysqlDB.commit()
                if cursor.rowcount >= 1:
                    print("insert()")
                    print(cursor.fetchall())
                    print(cursor.rowcount)
                    return True
                else:
                    return False
        except Exception as e:
            logging.error(e)
        finally:
            mysqlDB.close()


    def updateUserInfo(self,uname, pwd, tel, back, nickname):
        sql = "update  user set username=\'{0}\',password=\'{1}\',tel=\'{2}\',back=\'{3}',nickname=\'{4}\'" \
              " where username=\'{0}\'".format(uname, pwd, tel, back, nickname)
        print(sql)
        mysqlDB = self.DB()
        try:
            with mysqlDB.cursor() as cursor:
                cursor.execute(sql)
                mysqlDB.commit()
                if cursor.rowcount >= 1:
                    print("update()")
                    print(cursor.fetchall())
                    print(cursor.rowcount)
                    return True
                else:
                    return False
        except Exception as e:
            logging.error(e)
        finally:
            mysqlDB.close()

    def updateTestTime(self, uname,times):
        sql = "update user set times=\'{0}\' where username=\'{1}\'".format(times,uname)
        print(sql)
        mysqlDB = self.DB()
        try:
            with mysqlDB.cursor() as cursor:
                cursor.execute(sql)
                mysqlDB.commit()
                if cursor.rowcount >= 1:
                    print("update()")
                    print(cursor.fetchall())
                    print(cursor.rowcount)
                    return True
                else:
                    return False
        except Exception as e:
            logging.error(e)
        finally:
            mysqlDB.close()

    #插入用户的测试结果
    def insertTestResult(self,id, uname, test_result,test_type):
        localtime = time.localtime()
        cur_time = "%s-%s-%s %s:%s:%s" % (localtime.tm_year,localtime.tm_mon,localtime.tm_mday,localtime.tm_hour,localtime.tm_min,localtime.tm_sec)
        sql = "insert into test_result(user_id,username,NO_1,NO_2,NO_3,NO_4,NO_5,NO_6,NO_7,NO_8,NO_9,test_time,test_type) " \
              "VALUES(\'{0}\',\'{1}\',\'{2}\',\'{3}\',\'{4}\',\'{5}\',\'{6}\',\'{7}\'," \
              "\'{8}\',\'{9}\',\'{10}\',\'{11}\',\'{12}\')".format(id, uname,test_result['1'],test_result['2'],test_result['3'],
                                        test_result['4'],test_result['5'],test_result['6'],test_result['7'],
                                        test_result['8'],test_result['9'],cur_time,test_type)
        print(sql)
        mysqlDB = self.DB()
        try:
            with mysqlDB.cursor() as cursor:
                cursor.execute(sql)
                mysqlDB.commit()
                if cursor.rowcount >= 1:
                    print("insertTestResult()")
                    print(cursor.fetchall())
                    print(cursor.rowcount)
                    return True
                else:
                    return False
        except Exception as e:
            logging.error(e)
        finally:
            mysqlDB.close()

    # 得到一条完整的用户记录信息
    def selectUsers(self, uname, pwd):
        mysqlDB = self.DB()
        sql = "select * from user where username=\'{0}\' and password=\'{1}\'".format(uname, pwd)
        print(sql)
        try:
            with mysqlDB.cursor() as cursor:

                info = cursor.execute(sql)
                if info >= 1:
                    print("selectAll")
                    tuple_info = cursor.fetchall()[0]
                    print(tuple_info)
                    print(cursor.rowcount)
                    return tuple_info
                else:
                    return False
        except Exception as e:
            logging.error(e)
        finally:
            mysqlDB.close()

    #得到一条完整的用户测试记录信息  最近一次的测试完整信息
    def selectTestResult(self, uname, user_id):
        mysqlDB = self.DB()
        sql = "select * from test_result where username=\'{0}\' and user_id=\'{1}\' order by test_time desc".format(uname, user_id)
        print(sql)
        try:
            with mysqlDB.cursor() as cursor:
                info = cursor.execute(sql)
                print(info)
                if info == 1:
                    print("selectTestResult")
                    tuple_info = cursor.fetchall()[0]
                    print(tuple_info)
                    print(cursor.rowcount)
                    return tuple_info
                elif info > 1:
                    print("zheli")
                    tuple_info = cursor.fetchall()
                    print("一共有%s条测试数据"%len(tuple_info))
                    print(tuple_info[0])
                    return tuple_info[0]
                else:
                    return False
        except Exception as e:
            logging.error(e)
        finally:
            mysqlDB.close()

    # 得到某用户最近一次的测试时间
    def getTestTimeAndType(self, uname):
        mysqlDB = self.DB()
        sql = "select test_time,test_type from test_result where username=\'{0}\' order by test_time desc".format(uname)
        print(sql)
        try:
            with mysqlDB.cursor() as cursor:
                info = cursor.execute(sql)
                print(info)
                if info == 1:
                    print("这是getTestTimeAndType info==1")
                    tuple_info = cursor.fetchall()[0]
                    print(tuple_info)
                    print(cursor.rowcount)
                    return tuple_info[0],tuple_info[1]
                elif info > 1:
                    print("这是getTestTimeAndType info > 1")
                    tuple_info = cursor.fetchall()
                    print("一共有%s条测试数据" % len(tuple_info))
                    print(tuple_info[0][0],tuple_info[0][1])
                    return tuple_info[0][0],tuple_info[0][1]
                else:
                    return False
        except Exception as e:
            logging.error(e)
        finally:
            mysqlDB.close()


    # 得到某用户一共测试了多少次
    def getTestTimes(self, uname):
        sql = "select test_time from test_result where username=\'{0}\'".format(uname)
        print(sql)
        mysqlDB = self.DB()
        try:
            with mysqlDB.cursor() as cursor:
                cursor.execute(sql)
                # mysqlDB.commit()
                if cursor.rowcount == 1:
                    print("getTestTimes- == 1")
                    tuple_info = cursor.fetchall()
                    print(cursor.fetchall())
                    print(cursor.rowcount)
                    print(tuple_info)
                    return 1
                elif cursor.rowcount > 1:
                    print("getTestTimes- >1")
                    tuple_info = cursor.fetchall()
                    print(cursor.fetchall())
                    print(cursor.rowcount)
                    print(tuple_info)
                    return len(tuple_info)
                else:
                    print(0)
                    return 0
        except Exception as e:
            logging.error(e)
        finally:
            mysqlDB.close()

    # # 得到某用户一共测试了多少次
    # def getTestType(self, uname):
    #     sql = "select test_type from test_result where username=\'{0}\'".format(uname)
    #     print(sql)
    #     mysqlDB = self.DB()
    #     try:
    #         with mysqlDB.cursor() as cursor:
    #             cursor.execute(sql)
    #             # mysqlDB.commit()
    #             if cursor.rowcount == 1:
    #                 print("getTestTimes- == 1")
    #                 tuple_info = cursor.fetchall()
    #                 print(cursor.fetchall())
    #                 print(cursor.rowcount)
    #                 print(tuple_info)
    #                 return 1
    #             elif cursor.rowcount > 1:
    #                 print("getTestTimes- >1")
    #                 tuple_info = cursor.fetchall()
    #                 print(cursor.fetchall())
    #                 print(cursor.rowcount)
    #                 print(tuple_info)
    #                 return len(tuple_info)
    #             else:
    #                 print(0)
    #                 return 0
    #     except Exception as e:
    #         logging.error(e)
    #     finally:
    #         mysqlDB.close()

    def getUserId(self,uname):
        mysqlDB = self.DB()
        sql = "select user_id from user where username=\'{0}\'".format(uname, )
        print(sql)
        try:
            with mysqlDB.cursor() as cursor:

                info = cursor.execute(sql)
                if info >= 1:
                    print("selectAll")
                    myid = cursor.fetchall()[0]
                    print("id:"+str(myid[0]))
                    print(cursor.rowcount)
                    return myid[0]
                else:
                    return False
        except Exception as e:
            logging.error(e)
        finally:
            mysqlDB.close()

    def getFreshTime(self):
        while True:
            times, type = queryDB().getTestTimeAndType(uname="admin")
            # print("------")
            return (times, type)
            import time
            time.sleep(5)


if __name__ == '__main__':
    # while True:
    #     time,type = queryDB().getTestTimeAndType(uname="admin")
    #     print("------")
    #     print(time, type)
    #     import time
    #     time.sleep(5)
    time,type = queryDB().getFreshTime()
    print("-------------------")
    print(time,type)
