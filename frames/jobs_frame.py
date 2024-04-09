import wx
import frames.back_end as back_end

length = 800
width = 480

#--------------------------------------------------------------------------JOBS SCREEN---------------------------------------------
# This is where the user is presented all four capsules and whether they are currently being experimented on or not; Green will
# indicate 'currently in testing' no color will means it is available to be experimented

class Jobs(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, size=(length, width))

        dashboard_img = wx.Bitmap("./pictures/dashboard.png")
        jobs_img = wx.Bitmap("./pictures/jobs.png")
        settings_img = wx.Bitmap("./pictures/settings.png")
        logo_img = wx.Image("./pictures/logo.PNG", wx.BITMAP_TYPE_ANY)
        logo_img = logo_img.Scale(90, 30, wx.IMAGE_QUALITY_HIGH)

        panel_1 = wx.Panel(self, -1,)       #For housing name, date, and time
        panel_2 = wx.Panel(self, -1,)       #For capsule name
        panel_3 = wx.Panel(self, -1,)       #For user input strain and percentage
        panel_4 = wx.Panel(self, -1,)       #For 'START' button
        panel_5 = wx.Panel(self, -1,)       #For housing navigation buttons
        panel_6 = wx.Panel(self, -1,)
    
        panel_1.SetBackgroundColour((53, 62, 108))        
        panel_2.SetBackgroundColour((28, 28, 59))         
        panel_3.SetBackgroundColour((28, 28, 59))
        panel_4.SetBackgroundColour((28, 28, 59))               
        panel_5.SetBackgroundColour((28, 28, 59))
        panel_6.SetBackgroundColour((53, 62, 108))

        logo = wx.StaticBitmap(panel_1, wx.ID_ANY, wx.Bitmap(logo_img))

        font_1 = wx.Font(20, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        font_2 = wx.Font(14, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        
        t_2 = wx.StaticText(panel_2, label = "Current Jobs:") 
        t_2.SetFont(font_1)
        t_2.SetForegroundColour((255, 255, 255))
        t_3 = wx.StaticText(panel_5, label = "Please go back to 'Home' to start a new test")
        t_3.SetFont(font_2)
        t_3.SetForegroundColour((255, 255, 255))

        global button_a     #button for each capsule test
        global button_b
        global button_c
        global button_d

        global button_a_stop        #stop button for each capsule test
        global button_b_stop
        global button_c_stop
        global button_d_stop

        button_a = wx.Button(panel_3, wx.ID_ANY, 'Capsule: A -----[STATUS: No Test Selected]', style = wx.BU_LEFT)
        button_b = wx.Button(panel_3, wx.ID_ANY, 'Capsule: B -----[STATUS: No Test Selected]', style = wx.BU_LEFT)
        button_c = wx.Button(panel_3, wx.ID_ANY, 'Capsule: C -----[STATUS: No Test Selected]', style = wx.BU_LEFT)
        button_d = wx.Button(panel_3, wx.ID_ANY, 'Capsule: D -----[STATUS: No Test Selected]', style = wx.BU_LEFT)

        button_a.Disable()              #buttons are disabled by default
        button_b.Disable()
        button_c.Disable()
        button_d.Disable()

        button_a_stop = wx.Button(panel_4, wx.ID_ANY, 'Stop Test')
        button_a_stop.myname = 'A'
        button_b_stop = wx.Button(panel_4, wx.ID_ANY, 'Stop Test')
        button_b_stop.myname = 'B'
        button_c_stop = wx.Button(panel_4, wx.ID_ANY, 'Stop Test')
        button_c_stop.myname = 'C'
        button_d_stop = wx.Button(panel_4, wx.ID_ANY, 'Stop Test')
        button_d_stop.myname = 'D'

        button_a_stop.Disable()
        button_b_stop.Disable()
        button_c_stop.Disable()
        button_d_stop.Disable()

        text_sizer_1 = wx.BoxSizer(wx.HORIZONTAL)     #Aligning date and time right
        text_sizer_1.Add(logo)
        text_sizer_1.Add((0,0), 2, wx.ALIGN_CENTER)

        text_sizer_2 = wx.BoxSizer(wx.HORIZONTAL)   #Aligning Capsule Name and type of test in center
        text_sizer_2.Add((0,0), 1, wx.EXPAND)
        text_sizer_2.Add(t_2, 0, wx.ALIGN_CENTER)
        text_sizer_2.Add((0,0), 1, wx.EXPAND)

        text_sizer_3 = wx.BoxSizer(wx.HORIZONTAL)   #Aligning instructions in center
        text_sizer_3.Add((0,0), 1, wx.EXPAND)
        text_sizer_3.Add(t_3,0,wx.ALIGN_CENTER)
        text_sizer_3.Add((0,0), 1, wx.EXPAND)

        button_home = wx.BitmapButton(panel_6, wx.ID_ANY, bitmap = dashboard_img)
        button_jobs = wx.BitmapButton(panel_6, wx.ID_ANY, bitmap = jobs_img)
        button_settings = wx.BitmapButton(panel_6, wx.ID_ANY, bitmap = settings_img)
        
        button_a.SetBackgroundColour((28, 28, 59))
        button_a.SetForegroundColour((255, 255, 255))
        button_b.SetBackgroundColour((28, 28, 59))
        button_b.SetForegroundColour((255, 255, 255))
        button_c.SetBackgroundColour((28, 28, 59))
        button_c.SetForegroundColour((255, 255, 255))
        button_d.SetBackgroundColour((28, 28, 59))
        button_d.SetForegroundColour((255, 255, 255))

        button_a_stop.SetBackgroundColour((28, 28, 59))
        button_a_stop.SetForegroundColour((255, 255, 255))
        button_b_stop.SetBackgroundColour((28, 28, 59))
        button_b_stop.SetForegroundColour((255, 255, 255))
        button_c_stop.SetBackgroundColour((28, 28, 59))
        button_c_stop.SetForegroundColour((255, 255, 255))
        button_d_stop.SetBackgroundColour((28, 28, 59))
        button_d_stop.SetForegroundColour((255, 255, 255))

        button_a_stop.Bind(wx.EVT_BUTTON, back_end.on_stop_test_click)
        button_b_stop.Bind(wx.EVT_BUTTON, back_end.on_stop_test_click)
        button_c_stop.Bind(wx.EVT_BUTTON, back_end.on_stop_test_click)
        button_d_stop.Bind(wx.EVT_BUTTON, back_end.on_stop_test_click)

        button_home.Bind(wx.EVT_BUTTON, lambda event: back_end.on_home_click(event, self.__class__.__name__))
        button_jobs.Disable()
        button_settings.Bind(wx.EVT_BUTTON, lambda event: back_end.on_settings_click(event, self.__class__.__name__))
       
        button_home.SetBackgroundColour((28, 28, 59))
        button_jobs.SetBackgroundColour((28, 28, 59))
        button_settings.SetBackgroundColour((28, 28, 59))
        
        window_sizer = wx.BoxSizer(wx.VERTICAL)           #For housing entire application window 
        parent_middle_sizer = wx.BoxSizer(wx.HORIZONTAL)

        parent_middle_sizer.Add(panel_3, 10, wx.EXPAND)
        parent_middle_sizer.Add(panel_4, 1, wx.EXPAND)

        lef_middle_sizer = wx.GridSizer(4, 1, 20 , 20)
        right_middle_sizer = wx.GridSizer(4, 1, 20 , 20)
       
        lef_middle_sizer.Add(button_a, 0, wx.EXPAND)
        lef_middle_sizer.Add(button_b, 0, wx.EXPAND)
        lef_middle_sizer.Add(button_c, 0, wx.EXPAND)
        lef_middle_sizer.Add(button_d, 0, wx.EXPAND)

        right_middle_sizer.Add(button_a_stop, 0, wx.EXPAND)
        right_middle_sizer.Add(button_b_stop, 0, wx.EXPAND)
        right_middle_sizer.Add(button_c_stop, 0, wx.EXPAND)
        right_middle_sizer.Add(button_d_stop, 0, wx.EXPAND)
       
        navigation_grid_sizer = wx.GridSizer(1, 3, 0, 0)  #For housig the three navigation buttons
        navigation_grid_sizer.Add(button_home, 0, wx.EXPAND)
        navigation_grid_sizer.Add(button_jobs, 0, wx.EXPAND)
        navigation_grid_sizer.Add(button_settings, 0, wx.EXPAND)
        
        panel_1.SetSizer(text_sizer_1)
        panel_2.SetSizer(text_sizer_2)
        panel_3.SetSizer(lef_middle_sizer)
        panel_4.SetSizer(right_middle_sizer)
        panel_5.SetSizer(text_sizer_3)
        panel_6.SetSizer(navigation_grid_sizer)

        window_sizer.Add(panel_1, 1, wx.EXPAND)
        window_sizer.Add(panel_2, 2, wx.EXPAND)
        window_sizer.Add(parent_middle_sizer, 8, wx.EXPAND)
        window_sizer.Add(panel_5, 2, wx.EXPAND)
        window_sizer.Add(panel_6, 2, wx.EXPAND)
   
        self.SetAutoLayout(True)
        self.SetSizer(window_sizer)
        self.Layout()
    
    def is_running(event, motor_name, test_type, strain_type):       #if capsule is being tested, disable respective button and change color to red to indicate test is being ran
        match motor_name[-1]:
            case 'A':
                button_a.Disable()
                button_a_stop.Enable()
                button_a.SetLabel(motor_name+ " - "+ test_type+": "+ strain_type+"-----[STATUS: Running]")
                button_a.SetBackgroundColour((190, 37, 66))
                button_a_stop.SetBackgroundColour((190, 37, 66))
            case 'B':
                button_b.Disable()
                button_b_stop.Enable()
                button_b.SetLabel(motor_name+ " - "+ test_type+": "+ strain_type+"-----[STATUS: Running]")
                button_b.SetBackgroundColour((190, 37, 66))
                button_b_stop.SetBackgroundColour((190, 37, 66))
            case 'C':
                button_c.Disable()
                button_c_stop.Enable()
                button_c.SetLabel(motor_name+ " - "+ test_type+": "+ strain_type+"-----[STATUS: Running]")
                button_c.SetBackgroundColour((190, 37, 66))
                button_c_stop.SetBackgroundColour((190, 37, 66))
            case 'D':
                button_d.Disable()
                button_d_stop.Enable()
                button_d.SetLabel(motor_name+ " - "+ test_type+": "+ strain_type+"-----[STATUS: Running]")
                button_d.SetBackgroundColour((190, 37, 66))
                button_d_stop.SetBackgroundColour((190, 37, 66))
        
    def done_running(event, motor_name, test_type, strain_type):     #after test is finished, re-enabled button and change color back to default
         match motor_name[-1]:
            case 'A':
                button_a.SetLabel(motor_name+ " - "+ test_type+": "+ strain_type+"-----[STATUS: Finished]")
                button_a.SetBackgroundColour((51,153,51))
                button_a.Enable()
                button_a.Bind(wx.EVT_BUTTON, lambda event: back_end.on_task_click(event, motor_name, test_type, strain_type))
                button_a_stop.Disable()
                button_a_stop.SetBackgroundColour((28, 28, 59))
            case 'B':
                button_b.SetLabel(motor_name+ " - "+ test_type+": "+ strain_type+"-----[STATUS: Finished]")
                button_b.SetBackgroundColour((51,153,51))
                button_b.Enable()
                button_b.Bind(wx.EVT_BUTTON, lambda event: back_end.on_task_click(event, motor_name, test_type, strain_type))
                button_b_stop.Disable()
                button_b_stop.SetBackgroundColour((28, 28, 59))
            case 'C':
                button_c.SetLabel(motor_name+ " - "+ test_type+": "+ strain_type+"-----[STATUS: Finished]")
                button_c.SetBackgroundColour((51,153,51))
                button_c.Enable()
                button_c.Bind(wx.EVT_BUTTON, lambda event: back_end.on_task_click(event, motor_name, test_type, strain_type))
                button_c_stop.Disable()
                button_c_stop.SetBackgroundColour((28, 28, 59))
            case 'D':
                button_d.SetLabel(motor_name+ " - "+ test_type+": "+ strain_type+"-----[STATUS: Finished]")
                button_d.SetBackgroundColour((51,153,51))
                button_d.Enable()
                button_d.Bind(wx.EVT_BUTTON, lambda event: back_end.on_task_click(event, motor_name, test_type, strain_type))
                button_d_stop.Disable()
                button_d_stop.SetBackgroundColour((28, 28, 59))

    def clear_test(event, motor_name):
        match motor_name[-1]:
            case 'A':
                button_a.Disable()
                button_a.SetLabel('Capsule: A -----[STATUS: No Test Selected]')
                button_a.SetBackgroundColour((28, 28, 59))
            case 'B':
                button_b.Disable()
                button_b.SetLabel('Capsule: B -----[STATUS: No Test Selected]')
                button_b.SetBackgroundColour((28, 28, 59))
            case 'C':
                button_c.Disable()
                button_c.SetLabel('Capsule: C -----[STATUS: No Test Selected]')
                button_c.SetBackgroundColour((28, 28, 59))
            case 'D':
                button_d.Disable()
                button_d.SetLabel('Capsule: D -----[STATUS: No Test Selected]')
                button_d.SetBackgroundColour((28, 28, 59))
    
    
            