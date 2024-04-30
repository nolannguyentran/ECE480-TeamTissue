import wx
import gui_be as gui_be

length = 800
width = 480

#--------------------------------------------------------------------------HOME SCREEN---------------------------------------------
# This is where the user can select which capsule they want to perform tests on; serves as the 'home screen' or dashboard

class HomeFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, size=(length, width))

        dashboard_img = wx.Bitmap("./pictures/dashboard.png")
        jobs_img = wx.Bitmap("./pictures/jobs.png")
        settings_img = wx.Bitmap("./pictures/settings.png")
        logo_img = wx.Image("./pictures/logo.PNG", wx.BITMAP_TYPE_ANY)
        logo_img = logo_img.Scale(300, 100, wx.IMAGE_QUALITY_HIGH)

        panel_1 = wx.Panel(self, -1,)       #For housing name, date, and time
        panel_2 = wx.Panel(self, -1,)       #For housing live-view display
        panel_3 = wx.Panel(self, -1,)       #For housing buttons
        panel_4 = wx.Panel(self, -1,)       #For housing navigation buttons
    
        panel_1.SetBackgroundColour((53, 62, 108))        
        panel_2.SetBackgroundColour((28, 28, 59))         
        panel_3.SetBackgroundColour((28, 28, 59))         
        panel_4.SetBackgroundColour((53, 62, 108))  

        font_1 = wx.Font(10, wx.DECORATIVE, wx.ITALIC, wx.NORMAL) 
        font_2 = wx.Font(12, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)  

        t_1 = wx.StaticText(panel_2, label = "Biomaterial && Musculoskeletal Engineering Lab")
        t_1.SetFont(font_1)
        t_1.SetForegroundColour((255, 255, 255))  

        logo = wx.StaticBitmap(panel_2, wx.ID_ANY, wx.Bitmap(logo_img))
        global button_a
        global button_b
        global button_c
        global button_d
        button_a = wx.Button(panel_3, wx.ID_ANY, 'Capsule: A')
        button_b = wx.Button(panel_3, wx.ID_ANY, 'Capsule: B')
        button_c = wx.Button(panel_3, wx.ID_ANY, 'Capsule: C')
        button_d = wx.Button(panel_3, wx.ID_ANY, 'Capsule: D')

        button_home = wx.BitmapButton(panel_4, wx.ID_ANY, bitmap = dashboard_img)
        button_jobs = wx.BitmapButton(panel_4, wx.ID_ANY, bitmap = jobs_img)
        button_settings = wx.BitmapButton(panel_4, wx.ID_ANY, bitmap = settings_img)
        button_exit = wx.Button(panel_1, wx.ID_ANY, 'X')
       
        button_home.Disable()
        button_jobs.Bind(wx.EVT_BUTTON, lambda event: gui_be.on_jobs_click(event, self.__class__.__name__))
        button_settings.Bind(wx.EVT_BUTTON, lambda event: gui_be.on_settings_click(event, self.__class__.__name__))

        button_exit.SetBackgroundColour((53, 62, 108))
        button_exit.SetForegroundColour((255, 255, 255))
        button_a.SetBackgroundColour((89, 99, 182))
        button_a.SetForegroundColour((255, 255, 255))
        button_b.SetBackgroundColour((89, 99, 182))
        button_b.SetForegroundColour((255, 255, 255))
        button_c.SetBackgroundColour((89, 99, 182))
        button_c.SetForegroundColour((255, 255, 255))
        button_d.SetBackgroundColour((89, 99, 182))
        button_d.SetForegroundColour((255, 255, 255))
        button_home.SetBackgroundColour((28, 28, 59))
        button_jobs.SetBackgroundColour((28, 28, 59))
        button_settings.SetBackgroundColour((28, 28, 59))
       
        button_exit.Bind(wx.EVT_BUTTON, gui_be.exit_application)
        button_a.Bind(wx.EVT_BUTTON, gui_be.on_motor_click)
        button_b.Bind(wx.EVT_BUTTON, gui_be.on_motor_click)
        button_c.Bind(wx.EVT_BUTTON, gui_be.on_motor_click)
        button_d.Bind(wx.EVT_BUTTON, gui_be.on_motor_click)

        text_sizer_1 = wx.BoxSizer(wx.HORIZONTAL)     #Aligning date and time right
        text_sizer_1.Add((0,0), 2, wx.ALIGN_CENTER)
        text_sizer_1.Add(button_exit, 0, wx.EXPAND)

        window_sizer = wx.BoxSizer(wx.VERTICAL)           #For housing entire application window 
        middle_sizer = wx.BoxSizer(wx.HORIZONTAL)         #For housing middle panel
        left_middle_sizer = wx.BoxSizer(wx.VERTICAL)      #For housing the logo and name of application and text instruction
        motor_grid_sizer = wx.GridSizer(2, 2, 10, 10)     #For housing the four motor buttons
        navigation_grid_sizer = wx.GridSizer(1, 3, 0, 0)  #For housig the three navigation buttons

        middle_sizer.Add(panel_2, 1, wx.EXPAND)
        middle_sizer.Add(panel_3, 1, wx.EXPAND)

        left_middle_sizer.Add((0,0), 1, wx.ALIGN_CENTER)
        left_middle_sizer.Add(logo, 1, wx.ALIGN_CENTER)
        left_middle_sizer.Add(t_1, 1, wx.ALIGN_CENTER)
    
        motor_grid_sizer.Add(button_a, 0, wx.EXPAND)
        motor_grid_sizer.Add(button_b, 0, wx.EXPAND)
        motor_grid_sizer.Add(button_c, 0, wx.EXPAND)
        motor_grid_sizer.Add(button_d, 0, wx.EXPAND)

        navigation_grid_sizer.Add(button_home, 0, wx.EXPAND)
        navigation_grid_sizer.Add(button_jobs, 0, wx.EXPAND)
        navigation_grid_sizer.Add(button_settings, 0, wx.EXPAND)
        
        panel_1.SetSizer(text_sizer_1)
        panel_2.SetSizer(left_middle_sizer)
        panel_3.SetSizer(motor_grid_sizer)
        panel_4.SetSizer(navigation_grid_sizer)

        window_sizer.Add(panel_1, 1, wx.EXPAND)
        window_sizer.Add(middle_sizer, 10, wx.EXPAND)
        window_sizer.Add(panel_4, 2, wx.EXPAND)
   
        self.SetAutoLayout(True)
        self.SetSizer(window_sizer)
        self.Layout()
    def is_running(event, motor_name):       #if capsule is being tested, disable respective button and change color to red to indicate test is being ran
        match motor_name[-1]:
            case 'A':
                button_a.Disable()
                button_a.SetBackgroundColour((190, 37, 66))
            case 'B':
                button_b.Disable()
                button_b.SetBackgroundColour((190, 37, 66))
            case 'C':
                button_c.Disable()
                button_c.SetBackgroundColour((190, 37, 66))
            case 'D':
                button_d.Disable()
                button_d.SetBackgroundColour((190, 37, 66))
        
    def done_running(event, motor_name):     #after test is finished, re-enabled button and change color back to default
         match motor_name[-1]:
            case 'A':
                button_a.Enable()
                button_a.SetBackgroundColour((89,99,182))
            case 'B':
                button_b.Enable()
                button_b.SetBackgroundColour((89,99,182))
            case 'C':
                button_c.Enable()
                button_c.SetBackgroundColour((89,99,182))
            case 'D':
                button_d.Enable()
                button_d.SetBackgroundColour((89,99,182))
    
