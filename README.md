# Death_Note
(AutoPwn) 
Script which uses YML to attempt to remote into machines and sends *Punishements* if able

An example YML file can be seen in the YML folder, YML file that will be used is called death_note.yml

Modular, Modules should be put into either exploit_cl, shell_cl, or payload_cl and should inherit from the parent class
in that file

Exploit is the method to get into the machine

Shell is the shell produced by the exploit

Payload is the payload to be deployed on the machine

To see what modules are available for each, check each of the corresponding classes.

The names used in the YML file should correspond to the class name of the modules being used

Check YML file for examples.


