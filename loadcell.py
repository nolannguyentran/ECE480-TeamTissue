import wx
from datetime import datetime
length = 800
width = 480
current_date_time = datetime.now()
now = current_date_time.strftime("%A, %B %d, %Y %I:%M %p")

def on_click(event):
    identity = event.GetEventObject().GetLabel()
    print(identity + " is selected!")

class HomePanel(wx.Panel):
       def __init__(self, parent):

        wx.Panel.__init__(self, parent=parent)
        
        panel_2 = wx.Panel(self, -1,)       #For housing live-view display
        panel_3 = wx.Panel(self, -1,)       #For housing buttons
          
        panel_2.SetBackgroundColour((33, 37, 41))         
        panel_3.SetBackgroundColour((33, 37, 41))         
             
        button_a = wx.Button(panel_3, wx.ID_ANY, 'Motor A')
        button_b = wx.Button(panel_3, wx.ID_ANY, 'Motor B')
        button_c = wx.Button(panel_3, wx.ID_ANY, 'Motor C')
        button_d = wx.Button(panel_3, wx.ID_ANY, 'Motor D')

        button_a.SetBackgroundColour((89, 99, 182))
        button_b.SetBackgroundColour((89, 99, 182))
        button_c.SetBackgroundColour((89, 99, 182))
        button_d.SetBackgroundColour((89, 99, 182))

        button_a.Bind(wx.EVT_BUTTON, on_click)
        button_b.Bind(wx.EVT_BUTTON, on_click)
        button_c.Bind(wx.EVT_BUTTON, on_click)
        button_d.Bind(wx.EVT_BUTTON, on_click)
   
        window_sizer = wx.BoxSizer(wx.VERTICAL)           #For housing entire application window 
        middle_sizer = wx.BoxSizer(wx.HORIZONTAL)         #For housing middle panel
        motor_grid_sizer = wx.GridSizer(2, 2, 10, 10)     #For housing the four motor buttons
       
        middle_sizer.Add(panel_2, 1, wx.EXPAND)
        middle_sizer.Add(panel_3, 1, wx.EXPAND)

        motor_grid_sizer.Add(button_a, 0, wx.EXPAND)
        motor_grid_sizer.Add(button_b, 0, wx.EXPAND)
        motor_grid_sizer.Add(button_c, 0, wx.EXPAND)
        motor_grid_sizer.Add(button_d, 0, wx.EXPAND)

        panel_3.SetSizer(motor_grid_sizer)
        
        window_sizer.Add(middle_sizer, 10, wx.EXPAND)
       
        self.SetAutoLayout(True)
        self.SetSizer(window_sizer)

class JobsPanel(wx.Panel):
       def __init__(self, parent):

        wx.Panel.__init__(self, parent=parent)
          
        panel_2 = wx.Panel(self, -1,)       #For housing live-view display
        panel_3 = wx.Panel(self, -1,)       #For housing buttons
      
        panel_2.SetBackgroundColour((33, 37, 41))         
        panel_3.SetBackgroundColour((33, 37, 41))         
         
        window_sizer = wx.BoxSizer(wx.VERTICAL)           #For housing entire application window 
        middle_sizer = wx.BoxSizer(wx.HORIZONTAL)         #For housing middle panel
    
        middle_sizer.Add(panel_2, 1, wx.EXPAND)
        middle_sizer.Add(panel_3, 1, wx.EXPAND)

        window_sizer.Add(middle_sizer, 10, wx.EXPAND)
       
        self.SetAutoLayout(True)
        self.SetSizer(window_sizer)
        
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, 
                          "Panel Switcher Tutorial", size=(length, width))

        self.Home = HomePanel(self)
        self.Jobs = JobsPanel(self)
        self.Jobs.Hide()

        
        dashboard_img = wx.Bitmap("./pictures/dashboard.png")
        jobs_img = wx.Bitmap("./pictures/jobs.png")
        settings_img = wx.Bitmap("./pictures/settings.png")

        panel_1 = wx.Panel(self, -1,)
        panel_4 = wx.Panel(self, -1,)

        panel_1.SetBackgroundColour((53, 62, 108))
        panel_4.SetBackgroundColour((53, 62, 108))

        self.button_home = wx.BitmapButton(panel_4, wx.ID_ANY, bitmap = dashboard_img)
        self.button_jobs = wx.BitmapButton(panel_4, wx.ID_ANY, bitmap = jobs_img)
        button_settings = wx.BitmapButton(panel_4, wx.ID_ANY, bitmap = settings_img)       

        self.button_home.SetBackgroundColour((33, 37, 41))
        self.button_jobs.SetBackgroundColour((0, 0, 0))
        button_settings.SetBackgroundColour((0, 0, 0))

        text_1 = wx.StaticText(panel_1, label = now, style=wx.ALIGN_RIGHT)
        text_1.SetForegroundColour((255, 255, 255))

        self.button_jobs.Bind(wx.EVT_BUTTON, self.on_Jobs)
        self.button_home.Bind(wx.EVT_BUTTON, self.on_Home)
        

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        navigation_grid_sizer = wx.GridSizer(1, 3, 0, 0)

        navigation_grid_sizer.Add(self.button_home, 0, wx.EXPAND)
        navigation_grid_sizer.Add(self.button_jobs, 0, wx.EXPAND)
        navigation_grid_sizer.Add(button_settings, 0, wx.EXPAND)

        panel_4.SetSizer(navigation_grid_sizer)

        self.sizer.Add(panel_1, 1, wx.EXPAND)
        self.sizer.Add(self.Home, 10, wx.EXPAND)
        self.sizer.Add(self.Jobs, 10, wx.EXPAND)
        self.sizer.Add(panel_4, 2, wx.EXPAND)

        self.SetAutoLayout(True)
        self.SetSizer(self.sizer)
        self.Layout()


    def on_Jobs(self, event):
      
        if self.Home.IsShown():
            
            self.Home.Hide()
            self.Jobs.Show()
            self.button_jobs.SetBackgroundColour((33, 37, 41))
            self.button_jobs.Disable()
            self.button_home.SetBackgroundColour((0, 0, 0))
            self.button_home.Enable()
       
        self.Layout()
    
    def on_Home(self, event):

        if self.Jobs.IsShown():
            self.Jobs.Hide()
            self.Home.Show()
            self.button_home.SetBackgroundColour((33, 37, 41))
            self.button_home.Disable()
            self.button_jobs.SetBackgroundColour((0, 0, 0))
            self.button_jobs.Enable()
        
        self.Layout()
app = wx.App(False)
frame = MyFrame()
frame.Show()
app.MainLoop()