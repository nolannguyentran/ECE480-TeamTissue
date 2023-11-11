import wx
length = 800
width = 480
class MyFrame(wx.Frame):
       def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title, size=(length, width))
    
        panel_1 = wx.Panel(self,-1, style=wx.BORDER_RAISED)
        panel_2 = wx.Panel(self,-1, style=wx.BORDER_RAISED)
        panel_3 = wx.Panel(self,-1, style=wx.BORDER_RAISED)
        panel_4 = wx.Panel(self,-1,style=wx.BORDER_RAISED)
        panel_5 = wx.Panel(self,-1,style=wx.BORDER_RAISED)
    
        panel_1.SetBackgroundColour((53,62,108))
        panel_2.SetBackgroundColour((53,62,108))
        
        panel_3.SetBackgroundColour((33,37,41))
        panel_4.SetBackgroundColour((33,37,41))
   
        window_sizer = wx.BoxSizer(wx.VERTICAL)
        middle_sizer = wx.BoxSizer(wx.HORIZONTAL)       #For housing middle panel

        middle_sizer.Add(panel_3, 1, wx.EXPAND)
        middle_sizer.Add(panel_4, 1, wx.EXPAND)

        window_sizer.Add(panel_1, 1, wx.EXPAND)
        window_sizer.Add(middle_sizer, 10, wx.EXPAND)
        window_sizer.Add(panel_2, 2, wx.EXPAND)

   
        self.SetAutoLayout(True)
        self.SetSizer(window_sizer)
        self.Layout()
   
   
app = wx.App(False)
frame = MyFrame(None, -1, "Sizer Test")
frame.Show()
app.MainLoop()