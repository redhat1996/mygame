import  wx
#客户端继承wx.Frame,拥有窗口界面
class MyClientui(wx.Frame):
    def __init__(self,c_name):
        wx.Frame.__init__(self,None,id=101,title='%s的客户端界面'%c_name,pos=wx.DefaultPosition,size=(800,800))
        pl=wx.Panel(self)#在窗口中初始化一个面板

        box = wx.BoxSizer(wx.VERTICAL)#在窗口中创建一个盒子，垂直方向自动排版

        g1=wx.FlexGridSizer(wx.HORIZONTAL)#在窗口中创建一个面板，水平方向自动布局

        conn_button=wx.Button(pl,size=(400,80),label='连接') #创建一个连接按钮
        dis_conn_button=wx.Button(pl,size=(400,80),label="断开连接")#创建一个断开按钮
        g1.Add(conn_button,1,wx.TOP|wx.LEFT) #把连接按钮放到水平框的左上角
        g1.Add(dis_conn_button,1,wx.TOP|wx.RIGHT)  #把断开连接放到水平框的右上角

        box.Add(g1,1,wx.ALIGN_CENTRE)# 把水平框放到盒子里
        #聊天内容文本框,并放到盒子里,水平布局
        self.text = wx.TextCtrl(pl,size=(800,380),style=wx.TE_MULTILINE)
        box.Add(self.text,1,wx.ALIGN_CENTRE)

        #聊天输入框，放到盒子里
        self.input_text=wx.TextCtrl(pl,size=(800,230),style=wx.TE_MULTILINE)
        box.Add(self.input_text,1,wx.ALIGN_CENTRE)
        #创建面板g2,水平布局
        g2=wx.FlexGridSizer(wx.HORIZONTAL)
        clear_button=wx.Button(pl,size=(400,80),label="重置")
        send_button=wx.Button(pl,size=(400,80),label="发送")
        g2.Add(clear_button,1,wx.TOP|wx.LEFT)
        g2.Add(send_button,1,wx.TOP|wx.RIGHT)
        box.Add(g2,1,wx.ALIGN_CENTRE)

        pl.SetSizer(box)#把盒子放到面板里





if __name__ == '__main__':
    app=wx.App()
    MyClientui('梓雯').Show()
    app.MainLoop()