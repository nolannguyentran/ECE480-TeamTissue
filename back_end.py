from test_selection_frame import TestSelectionFrame
from strain_input_type_frame import StrainInputTypeFrame
from constant_strain_input_frame import ConstantStrainTestInput
from randomized_strain_input_frame import RandomizedStrainTestInput
from wave_strain_input_frame import WaveStrainTestInput
from settings_frame import Settings
from test_output_frame import TestOutput
from loadcell_calibration_frame import Calibration

def get_current_frame(frame_name):                       #determines which frame user is currently in, assign to existing global frame name class
    global current_frame
    match frame_name:
        case 'TestSelectionFrame':
            current_frame = test_selection_frame
        case 'StrainInputTypeFrame':
            current_frame = strain_input_type_frame
        case 'ConstantStrainTestInput':
            current_frame = constant_strain_test_frame
        case 'RandomizedStrainTestInput':
            current_frame = randomized_strain_test_frame
        case 'WaveStrainTestInput':
            current_frame = square_wave_strain_test_frame
        case 'Settings':
            current_frame = settings_frame
        case 'Calibration':
            current_frame = loadcell_calibration_frame
        #case 'TestOutput':
        #    current_frame = live_test_frame


#TODO: Add functions for grabing max,min,and rate from each of the different strain type input tests




def on_motor_click(event):
    identity = event.GetEventObject().GetLabel()    #Returns which capsule selected
    global test_selection_frame
    test_selection_frame = TestSelectionFrame(identity)
    test_selection_frame.Show()

def on_compression_test_click(event, motor_name):
    identity = event.GetEventObject().GetLabel()    #Returns which test selected
    test_selection_frame.Destroy()
    global strain_input_type_frame
    strain_input_type_frame = StrainInputTypeFrame(motor_name, identity)
    strain_input_type_frame.Show()
    #global strain_rate_frame
    #strain_rate_frame = TestInput(motor_name, identity)
    #strain_rate_frame.Show()

def on_tensile_test_click(event, motor_name):
    identity = event.GetEventObject().GetLabel()    #Returns which test selected
    test_selection_frame.Destroy()
    global strain_input_type_frame
    strain_input_type_frame = StrainInputTypeFrame(motor_name, identity)
    strain_input_type_frame.Show()
    #global strain_rate_frame
    #strain_rate_frame = TestInput(motor_name, identity)
    #strain_rate_frame.Show()

def on_constant_test_click(event, motor_name, test_type):       #[strain input test selection page]
    strain_type = event.GetEventObject().GetLabel()    #Returns which strain input type selected (constant rate)
    strain_input_type_frame.Destroy()
    global constant_strain_test_frame
    constant_strain_test_frame = ConstantStrainTestInput(motor_name, test_type, strain_type)
    constant_strain_test_frame.Show()

def on_random_test_click(event, motor_name, test_type):         #[strain input test selection page]
    strain_type = event.GetEventObject().GetLabel()    #Returns which strain input type selected (constant rate)
    strain_input_type_frame.Destroy()
    global randomized_strain_test_frame
    randomized_strain_test_frame = RandomizedStrainTestInput(motor_name, test_type, strain_type)
    randomized_strain_test_frame.Show()

def on_square_wave_test_click(event, motor_name, test_type):    #[strain input test selection page]
    strain_type = event.GetEventObject().GetLabel()    #Returns which strain input type selected (constant rate)
    strain_input_type_frame.Destroy()
    global square_wave_strain_test_frame
    square_wave_strain_test_frame = WaveStrainTestInput(motor_name, test_type, strain_type)
    square_wave_strain_test_frame.Show()

def on_settings_click(event, frame_name):
    get_current_frame(frame_name)
    current_frame.Destroy()
    global settings_frame
    settings_frame = Settings()
    settings_frame.Show()

def on_calibration_click(event):
    identity = event.GetEventObject().GetLabel()
    settings_frame.Destroy()
    global loadcell_calibration_frame
    loadcell_calibration_frame = Calibration(identity)
    loadcell_calibration_frame.Show()

#def on_start_test_click(event, motor_name, test_name):          
#    identity = event.GetEventObject().GetLabel()
#    constant_strain_test_frame.Destroy()
#    global live_test_frame
#    live_test_frame = TestOutput(motor_name, test_name)
#    live_test_frame.Show()

def on_home_click(event, frame_name):
    get_current_frame(frame_name)
    current_frame.Destroy()
    #HomeFrame.test()

#def test(event):
#    gui_be.randomized_strain(10,100)











