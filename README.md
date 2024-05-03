# ECE480-TeamTissue
# Software Code for Enhanced Mechanically Active Bioreactor

With the complimentary electrical system for the mechanically bioreactor built, we now provide a glimpse into the software integration. The coding will help accommodate the communication between the various components such as the stepper motors and load cell outputs with the SBC. This will serve as the backend for our graphical user interface. The frontend will contain the buttons, display, and controls that the user will interact with. With all the coding being done in Python, we have divided each section into their individual Python modules as seen below:

## gui_fe.py
front-end of the GUI containing buttons and displaying various graphs and charts where the user will interact with
## gui_be.py 
back-end of the GUI containing all functions pertinent in stepper motor control, reading load cell outputs, mathematical manipulation of results, displaying results into visual elements such as graphs, and exporting data to a .csv file
## motor_config.py
code that configures and assign all four physical stepper motors from their respective GPIO pin locations
## loadcell_config.py 
code that configures and assign all four load cells through their respective ADC board’s GPIO pin locations
frames folder
contains all landing pages of the GUI such as those for displaying the home screen, current jobs running, settings page, test selection and input, etc.

With Python modules, a module can be imported into another module, carrying all the functions and code with it. This organization helps create modular code which not only satisfies one of the project’s needs but also conducive to best software development practices such as encapsulation and abstraction.
