import threading

import wx
from  socket  import *
class  MyServer(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, id=102, title='服务端端界面' , pos=wx.DefaultPosition, size=(800, 800))
        pl = wx.Panel(self)  # 在窗口中初始化一个面板

        box = wx.BoxSizer(wx.VERTICAL)  # 在窗口中创建一个盒子，垂直方向自动排版

        g1 = wx.FlexGridSizer(wx.HORIZONTAL)  # 在窗口中创建一个面板，水平方向自动布局

        startserver_button = wx.Button(pl, size=(266, 90), label='连接')  # 创建一个连接按钮
        record_save_button = wx.Button(pl, size=(267, 90), label="断开连接")  # 创建一个断开按钮
        stopserver_button = wx.Button(pl, size=(267, 90), label="断开连接")  # 创建一个断开按钮
        g1.Add(startserver_button, 1, wx.TOP  )  # 把连接按钮放到水平框的左上角
        g1.Add(record_save_button, 1, wx.TOP )  # 把断开连接放到水平框的右上角
        g1.Add(stopserver_button, 1, wx.TOP  )  # 把断开连接放到水平框的右上角

        box.Add(g1, 1, wx.ALIGN_CENTRE)  # 把水平框放到盒子里
        # 聊天内容文本框,并放到盒子里,水平布局
        self.text = wx.TextCtrl(pl, size=(800, 710), style=wx.TE_MULTILINE)
        box.Add(self.text, 1, wx.ALIGN_CENTRE)
        #把box盒子放到面板里
        pl.SetSizer(box)
        """
        以上界面代码结束
        为服务器准备执行属性
        """
        self.isOn=False  #判断服务器启动
        self.host_port=('',8888) #允许所有ip连接，监听本机8888端口
        self.server_socket=socket ( AF_INET,SOCK_STREAM)#tcp协议的套节字
        self.server_socket.bind(self.host_port)
        self.server_socket.listen(10) #允许十个客户端等待连接
        self.session_thread_map={}#存放服务器的会话线程，客户端为key，会话线程为value

        """
        给所有按钮绑定动作
        """
        self.Bind(wx.EVT_BUTTON,self.start_server,startserver_button)

    def  start_server(self,event):
        print("服务器开始启动")
        if not  self.isOn:
            self.isOn=True
            main_thread=threading.Thread(target=self.do_work)
            main_thread.setDaemon(True)
            main_thread.start()

    def do_work(self):
        print("服务器开始工作")
        while self.isOn:
            session_socket,client_add=self.server_socket.accept()
            #客户端发送连接请求第一条消息为客户端的名字
            username=seesion_socket.recv(1024).decode('UTF-8')
            #创建一个会话线程

            session_thread=SessionThread(session_socket,username,self)
            slef.session_thread_map[username]=session_thread
            session_thread.start()


#服务器端会话线程的类
class SessionThread(threading.Thread):
    def __init__(self,socket,username,server):
        threading.Thread.__init__(self)
        self.user_socket=socket
        self.username=username
        self.server=server

    def  run(self):
        pass










if __name__ == '__main__':
    app=wx.App()
    MyServer().Show()
    app.MainLoop()