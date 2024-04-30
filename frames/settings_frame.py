import wx
import gui_be as gui_be

length = 800
width = 480

#--------------------------------------------------------------------------SETTINGS SCREEN---------------------------------------------
# This is where the user can select settings options (load cell callibration) they want to configure; serves as the 'Settings'

class Settings(wx.Frame):
       def __init__(self):
        wx.Frame.__init__(self, None, size=(length, width))

        dashboard_img = wx.Bitmap("./pictures/dashboard.png")
        jobs_img = wx.Bitmap("./pictures/jobs.png")
        settings_img = wx.Bitmap("./pictures/settings.png")
        logo_img = wx.Image("./pictures/logo.PNG", wx.BITMAP_TYPE_ANY)
        logo_img = logo_img.Scale(90, 30, wx.IMAGE_QUALITY_HIGH)

        panel_1 = wx.Panel(self, -1,)       #For housing name, date, and time
        panel_2 = wx.Panel(self, -1,)       #For capsule name
        panel_3 = wx.Panel(self, -1,)       #For housing two test selection buttons
        panel_4 = wx.Panel(self, -1,)       #For housing instructions
        panel_5 = wx.Panel(self, -1,)       #For housing navigation buttons
    
        panel_1.SetBackgroundColour((53, 62, 108))        
        panel_2.SetBackgroundColour((28, 28, 59))         
        panel_3.SetBackgroundColour((28, 28, 59))
        panel_4.SetBackgroundColour((28, 28, 59))               
        panel_5.SetBackgroundColour((53, 62, 108))

        logo = wx.StaticBitmap(panel_1, wx.ID_ANY, wx.Bitmap(logo_img))

        font_1 = wx.Font(20, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        font_2 = wx.Font(14, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        
        t_2 = wx.StaticText(panel_2, label = "Settings") 
        t_2.SetFont(font_1)
        t_2.SetForegroundColour((255, 255, 255))
        t_3 = wx.StaticText(panel_4, label = "Please select a Setting to adjust")
        t_3.SetFont(font_2)
        t_3.SetForegroundColour((255, 255, 255))
      
        text_sizer_1 = wx.BoxSizer(wx.HORIZONTAL)     #Aligning date and time right
        text_sizer_1.Add(logo)
        text_sizer_1.Add((0,0), 2, wx.ALIGN_CENTER)

        text_sizer_2 = wx.BoxSizer(wx.HORIZONTAL)   #Aligning Capsule Name in center
        text_sizer_2.Add((0,0), 1, wx.EXPAND)
        text_sizer_2.Add(t_2, 0, wx.ALIGN_CENTER)
        text_sizer_2.Add((0,0), 1, wx.EXPAND)

        text_sizer_3 = wx.BoxSizer(wx.HORIZONTAL)   #Aligning instructions in center
        text_sizer_3.Add((0,0), 1, wx.EXPAND)
        text_sizer_3.Add(t_3,0,wx.ALIGN_CENTER)
        text_sizer_3.Add((0,0), 1, wx.EXPAND)

        button_1 = wx.Button(panel_3, wx.ID_ANY, 'Zero-ed Motors')
        button_calibrate = wx.Button(panel_3, wx.ID_ANY, 'Calibrate Load Cells')
        button_3 = wx.Button(panel_3, wx.ID_ANY, 'Change email address')

        button_1.SetBackgroundColour((89, 99, 182))
        button_1.SetForegroundColour((255,255,255))
        button_calibrate.SetBackgroundColour((89, 99, 182))
        button_calibrate.SetForegroundColour((255,255,255))
        button_3.SetBackgroundColour((89, 99, 182))
        button_3.SetForegroundColour((255,255,255))

        button_home = wx.BitmapButton(panel_5, wx.ID_ANY, bitmap = dashboard_img)
        button_jobs = wx.BitmapButton(panel_5, wx.ID_ANY, bitmap = jobs_img)
        button_settings = wx.BitmapButton(panel_5, wx.ID_ANY, bitmap = settings_img)

        button_1.Disable()
        button_calibrate.Bind(wx.EVT_BUTTON, lambda event: gui_be.on_calibration_click(event, self.__class__.__name__))
        button_3.Disable()

        button_home.Bind(wx.EVT_BUTTON, lambda event: gui_be.on_home_click(event, self.__class__.__name__))
        button_jobs.Bind(wx.EVT_BUTTON, lambda event: gui_be.on_jobs_click(event, self.__class__.__name__))
        button_settings.Disable()
        
        button_home.SetBackgroundColour((28, 28, 59))
        button_jobs.SetBackgroundColour((28, 28, 59))
        button_settings.SetBackgroundColour((28, 28, 59))

        window_sizer = wx.BoxSizer(wx.VERTICAL)           #For housing entire application window 
        middle_sizer = wx.GridSizer(1, 3, 20, 20)         #For housing middle panel
       
        navigation_grid_sizer = wx.GridSizer(1, 3, 0, 0)  #For housig the three navigation buttons

        middle_sizer.Add(button_1, 0, wx.EXPAND)
        middle_sizer.Add(button_calibrate, 0, wx.EXPAND)
        middle_sizer.Add(button_3, 0, wx.EXPAND)
        
        navigation_grid_sizer.Add(button_home, 0, wx.EXPAND)
        navigation_grid_sizer.Add(button_jobs, 0, wx.EXPAND)
        navigation_grid_sizer.Add(button_settings, 0, wx.EXPAND)
        
        panel_1.SetSizer(text_sizer_1)
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