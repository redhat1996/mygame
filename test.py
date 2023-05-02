import wx
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='ai聊天框')
        self.SetSize(500, 400)
        # 创建用于读取数据的文本框
        self.read_text = wx.TextCtrl(self, style=wx.TE_MULTILINE|wx.HSCROLL)
        # 创建用于输入数据的文本框
        self.input_text = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        # 创建连接按钮
        self.connect_button = wx.Button(self, label="Connect")
        # 创建断开连接按钮
        self.disconnect_button = wx.Button(self, label="Disconnect")
        # 创建发送按钮
        self.send_button = wx.Button(self, label="Send")
        # 创建清空按钮
        self.clear_button = wx.Button(self, label="Clear")
        # 创建一个垂直方向的布局管理器
        vbox = wx.BoxSizer(wx.VERTICAL)
        # 将读取文本框添加到布局管理器中，并设置它的大小
        vbox.Add(self.read_text, proportion=1, flag=wx.EXPAND|wx.ALL, border=10)
        # 创建一个水平方向的布局管理器，并将输入文本框和发送按钮添加到其中
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.input_text, proportion=1, flag=wx.EXPAND|wx.ALL, border=10)
        hbox.Add(self.send_button, flag=wx.RIGHT|wx.BOTTOM, border=10)
        # 将水平布局管理器添加到垂直布局管理器中
        vbox.Add(hbox, proportion=0, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.BOTTOM, border=10)
        # 创建一个水平方向的布局管理器，并将连接按钮和断开连接按钮添加到其中
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(self.disconnect_button, proportion=1, flag=wx.LEFT, border=10)
        hbox2.Add(self.connect_button, proportion=1, flag=wx.LEFT, border=10)
        # 将连接按钮和断开连接按钮的布局管理器添加到垂直布局管理器中
        vbox.Add(hbox2, proportion=0, flag=wx.TOP|wx.LEFT|wx.RIGHT|wx.BOTTOM, border=10)
        # 创建一个水平方向的布局管理器，并将清空按钮添加到其中
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3.Add(self.clear_button, proportion=1, flag=wx.RIGHT|wx.BOTTOM, border=10)
        # 将清空按钮的布局管理器添加到垂直布局管理器中
        vbox.Add(hbox3, proportion=0, flag=wx.ALIGN_RIGHT|wx.RIGHT|wx.BOTTOM, border=10)
        # 将主布局管理器设置为垂直布局管理器
        self.SetSizer(vbox)
        # 将输入文本框的回车键事件绑定到发送按钮的单击事件上
        self.input_text.Bind(wx.EVT_TEXT_ENTER, self.on_send_button)
    def on_send_button(self, event):
        # 处理发送按钮的单击事件
        pass
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()