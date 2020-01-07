# applicationStarter

This is a python application that takes a list of programs and opens them. It saves the previous configuration to facilitate workflow.

The app allows the user to select the ".desktop" files they would like to open at once, and collects them in a list. The user can then start all the applications at once. When the user closes the application, a "save.txt" file is created which contains a list of the apps used in the previous configuration and if that file exists the next time the application is started, the list will be automatically loaded.

Note: For now, in order to clear the list, the "save.txt" file should be deleted. I plan on revamping the GUI and adding an option to clear the list. 