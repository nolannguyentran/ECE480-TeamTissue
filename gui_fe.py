import wx
from datetime import datetime
length = 800
width = 480
current_date_time = datetime.now()
now = current_date_time.strftime("%A, %B %d, %Y %I:%M %p")



def onClick(event):
    print("Button Pressed")

class MyFrame(wx.Frame):
       def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title, size=(length, width))

        panel_1 = wx.Panel(self, -1, style=wx.BORDER_RAISED)
        panel_2 = wx.Panel(self, -1, style=wx.BORDER_RAISED)
        panel_3 = wx.Panel(self, -1, style=wx.BORDER_RAISED)
        panel_4 = wx.Panel(self, -1, style=wx.BORDER_RAISED)
    
        panel_1.SetBackgroundColour((53, 62, 108))        #For housing name, date, and time
        panel_2.SetBackgroundColour((33, 37, 41))         #For housing live-view display
        panel_3.SetBackgroundColour((33, 37, 41))         #For housing buttons
        panel_4.SetBackgroundColour((53, 62, 108))        #For housing navigation buttons

        button_a = wx.Button(panel_3, wx.ID_ANY, 'Motor A')
        button_b = wx.Button(panel_3, wx.ID_ANY, 'Motor B')
        button_c = wx.Button(panel_3, wx.ID_ANY, 'Motor C')
        button_d = wx.Button(panel_3, wx.ID_ANY, 'Motor D')

        button_home = wx.Button(panel_4, wx.ID_ANY, 'Dashboard')
        button_jobs = wx.Button(panel_4, wx.ID_ANY, 'Jobs')
        button_settings = wx.Button(panel_4, wx.ID_ANY, 'Settings')

        button_a.SetBackgroundColour((89, 99, 182))
        button_b.SetBackgroundColour((89, 99, 182))
        button_c.SetBackgroundColour((89, 99, 182))
        button_d.SetBackgroundColour((89, 99, 182))
        button_home.SetBackgroundColour((0, 0, 0))
        button_jobs.SetBackgroundColour((0, 0, 0))
        button_settings.SetBackgroundColour((0, 0, 0))

        text_1 = wx.StaticText(panel_1, label = now, style=wx.ALIGN_RIGHT)
        text_1.SetForegroundColour((255, 255, 255))
   
        window_sizer = wx.BoxSizer(wx.VERTICAL)           #For housing entire application window 
        middle_sizer = wx.BoxSizer(wx.HORIZONTAL)         #For housing middle panel
        motor_grid_sizer = wx.GridSizer(2, 2, 10, 10)     #For housing the four motor buttons
        navigation_grid_sizer = wx.GridSizer(1, 3, 5, 5)  #For housig the three navigation buttons

        middle_sizer.Add(panel_2, 1, wx.EXPAND)
        middle_sizer.Add(panel_3, 1, wx.EXPAND)

        motor_grid_sizer.Add(button_a, 0, wx.EXPAND)
        motor_grid_sizer.Add(button_b, 0, wx.EXPAND)
        motor_grid_sizer.Add(button_c, 0, wx.EXPAND)
        motor_grid_sizer.Add(button_d, 0, wx.EXPAND)

        navigation_grid_sizer.Add(button_home, 0, wx.EXPAND)
        navigation_grid_sizer.Add(button_jobs, 0, wx.EXPAND)
        navigation_grid_sizer.Add(button_settings, 0, wx.EXPAND)
        

        panel_3.SetSizer(motor_grid_sizer)
        panel_4.SetSizer(navigation_grid_sizer)

        window_sizer.Add(panel_1, 1, wx.EXPAND)
        window_sizer.Add(middle_sizer, 10, wx.EXPAND)
        window_sizer.Add(panel_4, 2, wx.EXPAND)

   
        self.SetAutoLayout(True)
        self.SetSizer(window_sizer)
        self.Layout()
   
   
app = wx.App(False)
frame = MyFrame(None, -1, "BioReactor")
frame.Show()
app.MainLoop()