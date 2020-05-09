# -*- coding: utf-8 -*-
import time
from selenium import webdriver
import random
from tkinter import messagebox
import win32gui
import win32con
from selenium.webdriver.common.keys import Keys

#user config
myusername = "XXX"  # 登录一卡通
mypassword = "XXX"  # 登录密码
TimesMax = 5    #由于网络延迟问题导致页面加载缓慢，脚本将反复等待执行点击操作，直到达到最大值TimesMax

#script variables
Flag = False
Times = 0   #由于网络延迟问题导致页面加载缓慢，脚本将反复等待执行点击操作，直到达到最大值TimesMax,times用来记录次数
Status = 0  #记录脚本运行进度，以便于反复执行
Wrong = False   #出错标志
Wrong_Message=""    #出错信息
def action(driver):
    global Status,Times,Wrong,Wrong_Message,myusername,mypassword
    if Wrong == False or Status == 1:
        try:
            # 找到登录框，输入账号密码
            driver.find_element_by_xpath("//input[@id='username']").send_keys(myusername)
            driver.find_element_by_xpath("//input[@id='password']").send_keys(mypassword)
            Times=0
            Wrong = False
        except Exception as e:
            print(e)
            print("登录信息填写失败")
            Wrong_Message = "登录信息填写失败"
            Times = Times + 1
            Status = 1
            Wrong = True
    if Wrong == False or Status == 2:
        try:
            # 模拟点击登录
            driver.find_element_by_xpath("//button[@class='auth_login_btn primary full_width']").click()
            Times=0
            Wrong = False
            time.sleep(5)
        except Exception as e:
            print(e)
            print("登陆失败")
            Wrong_Message = "登陆失败"
            Times = Times + 1
            Status = 2
            Wrong = True
    if Wrong == False or Status == 3:
        try:
            # 模拟登陆后点击新增
            driver.find_element_by_xpath(
                "//button[@class='mint-button geuhjrnk bottom155 mt-btn-primary mint-button--normal']").click()
            Times=0
            Wrong = False
            time.sleep(3)
        except Exception as e:
            print(e)
            print("点击新增失败")
            Wrong_Message = "点击新增失败"
            Times = Times + 1
            Status = 3
            Wrong = True

    temperature = i = str(random.randint(363, 367) / 10)
    if Wrong == False or Status == 4:
        try:
            #输入当天体温并点击确认
            driver.find_element_by_xpath("//input[@placeholder='请输入当天晨检体温']").send_keys(temperature)
            # 模拟点击签到
            driver.find_element_by_xpath("//button[@class='mint-button mt-btn-primary mint-button--large']").click()
            Times=0
            Wrong = False
            time.sleep(2)
        except Exception as e:
            print(e)
            print("上报表填写失败")
            Wrong_Message = "点击新增失败"
            Times = Times + 1
            Status = 4
            Wrong = True
    if Wrong == False or Status == 5:
        try:
            driver.find_element_by_xpath("//button[@class='mint-msgbox-btn mint-msgbox-confirm mt-btn-primary']").click()
            time.sleep(2)
            Times=0
            Wrong = False
            Status=0
            print("签到成功")
        except Exception as e:
            print(e)
            print("点击确认失败")
            Wrong_Message = "点击确认失败"
            Times = Times + 1
            Status = 5
            Wrong = True

def sign_in():
    global Flag,Times,Status,Wrong,TimesMax
    driver = webdriver.Chrome()  # 模拟浏览器打开网站
    driver.get(
        "http://ehall.seu.edu.cn/qljfwapp2/sys/lwReportEpidemicSeu/*default/index.do?from=groupmessage&isappinstalled=0#/dailyReport")
    # driver.maximize_window() #将窗口最大化
    action(driver)
    while Times<TimesMax:
        if Status != 0:
            action(driver)
            Flag = False
        else:
            Flag = True
            break
    driver.quit  # 退出去

class mymessage:
    def __init__(self):
        # 注册一个窗口类
        wc = win32gui.WNDCLASS()
        hinst = wc.hInstance = win32gui.GetModuleHandle(None)
        wc.lpszClassName = "mymessage"
        wc.lpfnWndProc = {win32con.WM_DESTROY: self.OnDestroy, }
        classAtom = win32gui.RegisterClass(wc)
        style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
        self.hwnd = win32gui.CreateWindow(classAtom, "Taskbar Demo", style,
                                          0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT,
                                          0, 0, hinst, None)
        hicon = win32gui.LoadIcon(0, win32con.IDI_APPLICATION)
        nid = (self.hwnd, 0, win32gui.NIF_ICON, win32con.WM_USER + 20, hicon, "Demo")
        win32gui.Shell_NotifyIcon(win32gui.NIM_ADD, nid)

    def showMsg(self, title, msg):
        # 原作者使用Shell_NotifyIconA方法代替包装后的Shell_NotifyIcon方法
        # 据称是不能win32gui structure, 我稀里糊涂搞出来了.
        # 具体对比原代码.
        nid = (self.hwnd,  # 句柄
               0,  # 托盘图标ID
               win32gui.NIF_INFO,  # 标识
               0,  # 回调消息ID
               0,  # 托盘图标句柄
               "TestMessage",  # 图标字符串
               msg,  # 气球提示字符串
               0,  # 提示的显示时间
               title,  # 提示标题
               win32gui.NIIF_INFO  # 提示用到的图标
               )
        win32gui.Shell_NotifyIcon(win32gui.NIM_MODIFY, nid)

    def OnDestroy(self, hwnd, msg, wparam, lparam):
        nid = (self.hwnd, 0)
        win32gui.Shell_NotifyIcon(win32gui.NIM_DELETE, nid)
        win32gui.PostQuitMessage(0)  # Terminate the app.


if __name__ == '__main__':
    t = mymessage()
    sign_in()
    if Flag == False:
        t.showMsg("上报失败", Wrong_Message)
        time.sleep(5)
        win32gui.DestroyWindow(t.hwnd)
    else:
        t.showMsg("上报成功", "东南大学健康上报")
        time.sleep(5)
        win32gui.DestroyWindow(t.hwnd)


