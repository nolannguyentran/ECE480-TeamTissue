import wx
from datetime import datetime
length = 800
width = 480
current_date_time = datetime.now()
now = current_date_time.strftime("%A, %B %d, %Y %I:%M %p")

def get_last_letter(string):            # Get capsule identifier
    words = list(string.split(" "))
    words_length = len(words)

    return words[words_length-1]

def on_motor_click(event):
    identity = event.GetEventObject().GetLabel()
    capsule_name = get_last_letter(identity)
    #print(name)
    #print(identity + " is selected!")
    frame = MySecondFrame(capsule_name)
    frame.Show()

class MyFrame(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title, size=(length, width))

        dashboard_img = wx.Bitmap("./pictures/dashboard.png")
        jobs_img = wx.Bitmap("./pictures/jobs.png")
        settings_img = wx.Bitmap("./pictures/settings.png")

        panel_1 = wx.Panel(self, -1,)       #For housing name, date, and time
        panel_2 = wx.Panel(self, -1,)       #For housing live-view display
        panel_3 = wx.Panel(self, -1,)       #For housing buttons
        panel_4 = wx.Panel(self, -1,)       #For housing navigation buttons
    
        panel_1.SetBackgroundColour((53, 62, 108))        
        panel_2.SetBackgroundColour((33, 37, 41))         
        panel_3.SetBackgroundColour((33, 37, 41))         
        panel_4.SetBackgroundColour((53, 62, 108))       

        button_a = wx.Button(panel_3, wx.ID_ANY, 'Motor A')
        button_b = wx.Button(panel_3, wx.ID_ANY, 'Motor B')
        button_c = wx.Button(panel_3, wx.ID_ANY, 'Motor C')
        button_d = wx.Button(panel_3, wx.ID_ANY, 'Motor D')


        button_home = wx.BitmapButton(panel_4, wx.ID_ANY, bitmap = dashboard_img)
        button_jobs = wx.BitmapButton(panel_4, wx.ID_ANY, bitmap = jobs_img)
        button_settings = wx.BitmapButton(panel_4, wx.ID_ANY, bitmap = settings_img)

        button_a.SetBackgroundColour((89, 99, 182))
        button_b.SetBackgroundColour((89, 99, 182))
        button_c.SetBackgroundColour((89, 99, 182))
        button_d.SetBackgroundColour((89, 99, 182))
        button_home.SetBackgroundColour((0, 0, 0))
        button_jobs.SetBackgroundColour((0, 0, 0))
        button_settings.SetBackgroundColour((0, 0, 0))

        button_a.Bind(wx.EVT_BUTTON, on_motor_click)
        button_b.Bind(wx.EVT_BUTTON, on_motor_click)
        button_c.Bind(wx.EVT_BUTTON, on_motor_click)
        button_d.Bind(wx.EVT_BUTTON, on_motor_click)

        text_1 = wx.StaticText(panel_1, label = now, style=wx.ALIGN_RIGHT)
        text_1.SetForegroundColour((255, 255, 255))
   
        window_sizer = wx.BoxSizer(wx.VERTICAL)           #For housing entire application window 
        middle_sizer = wx.BoxSizer(wx.HORIZONTAL)         #For housing middle panel
        motor_grid_sizer = wx.GridSizer(2, 2, 10, 10)     #For housing the four motor buttons
        navigation_grid_sizer = wx.GridSizer(1, 3, 0, 0)  #For housig the three navigation buttons

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

class MySecondFrame(wx.Frame):
       def __init__(self, name):
        wx.Frame.__init__(self, None, size=(length, width))

        self.name = name
        dashboard_img = wx.Bitmap("./pictures/dashboard.png")
        jobs_img = wx.Bitmap("./pictures/jobs.png")
        settings_img = wx.Bitmap("./pictures/settings.png")

        panel_1 = wx.Panel(self, -1,)       #For housing name, date, and time
        panel_2 = wx.Panel(self, -1,)       #For housing Motor name
        panel_3 = wx.Panel(self, -1,)       #For housing buttons
        panel_4 = wx.Panel(self, -1,)       #For housing instructions
        panel_5 = wx.Panel(self, -1,)       #For housing navigation buttons
    
        panel_1.SetBackgroundColour((53, 62, 108))        
        panel_2.SetBackgroundColour((33, 37, 41))         
        panel_3.SetBackgroundColour((33, 37, 41))
        panel_4.SetBackgroundColour((33, 37, 41))               
        panel_5.SetBackgroundColour((53, 62, 108))

        font = wx.Font(20, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        font_2 = wx.Font(20, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        t_1 = wx.StaticText(panel_2, label = "Capsule: "+self.name, style = wx.ALIGN_CENTER) 
        t_1.SetFont(font)
        t_2 = wx.StaticText(panel_4, label = "Please select which type of test to conduct with Capsule: "+self.name, style = wx.ALIGN_CENTER)
        t_2.SetFont(font_2)
      
        text_sizer_2 = wx.BoxSizer(wx.VERTICAL)
        text_sizer_2.Add(t_1,0,wx.ALIGN_CENTER)

        text_sizer_3 = wx.BoxSizer(wx.VERTICAL)
        text_sizer_3.Add(t_2,0,wx.ALIGN_CENTER)

        button_compression = wx.Button(panel_3, wx.ID_ANY, 'Compression Test')
        button_tensile = wx.Button(panel_3, wx.ID_ANY, 'Tensile Test')

        button_compression.SetSize((100,50))
        button_tensile.SetSize((100,50))

        button_compression.SetBackgroundColour((89, 99, 182))
        button_tensile.SetBackgroundColour((89, 99, 182))   

        button_home = wx.BitmapButton(panel_5, wx.ID_ANY, bitmap = dashboard_img)
        button_jobs = wx.BitmapButton(panel_5, wx.ID_ANY, bitmap = jobs_img)
        button_settings = wx.BitmapButton(panel_5, wx.ID_ANY, bitmap = settings_img)

        
        button_home.SetBackgroundColour((0, 0, 0))
        button_jobs.SetBackgroundColour((0, 0, 0))
        button_settings.SetBackgroundColour((0, 0, 0))

        text_1 = wx.StaticText(panel_1, label = now, style=wx.ALIGN_RIGHT)
        text_1.SetForegroundColour((255, 255, 255))
   
        window_sizer = wx.BoxSizer(wx.VERTICAL)           #For housing entire application window 
        middle_sizer = wx.GridSizer(1, 2, 20, 20)         #For housing middle panel
       
        navigation_grid_sizer = wx.GridSizer(1, 3, 0, 0)  #For housig the three navigation buttons

        middle_sizer.Add(button_compression, 0, wx.EXPAND)
        middle_sizer.Add(button_tensile, 0, wx.EXPAND)
        
        navigation_grid_sizer.Add(button_home, 0, wx.EXPAND)
        navigation_grid_sizer.Add(button_jobs, 0, wx.EXPAND)
        navigation_grid_sizer.Add(button_settings, 0, wx.EXPAND)
        
        panel_2.SetSizer(text_sizer_2)
        panel_3.SetSizer(middle_sizer)
        panel_4.SetSizer(text_sizer_3)
        panel_5.SetSizer(navigation_grid_sizer)


        window_sizer.Add(panel_1, 1, wx.EXPAND)
        window_sizer.Add(panel_2, 2, wx.EXPAND)
        window_sizer.Add(panel_3, 6, wx.EXPAND)
        window_sizer.Add(panel_4, 2, wx.EXPAND)
        window_sizer.Add(panel_5, 2, wx.EXPAND)
   
        self.SetAutoLayout(True)
        self.SetSizer(window_sizer)
        self.Layout()
   
app = wx.App(False)
frame = MyFrame(None, -1, "BioReactor")
frame.Show()
app.MainLoop()