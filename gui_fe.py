import wx

def onButton(event):
    print ("button pressed")

app = wx.App()
frame = wx.Frame(None, -1, 'win.py')
frame.SetDimensions(0,0,200,50)

panel = wx.Panel(frame, wx.ID_ANY)
button = wx.Button(panel, wx.ID_ANY, 'Test', (10, 10))
button.Bind(wx.EVT_BUTTON, onButton)

frame.Show()
frame.Centre()
app.MainLoop()