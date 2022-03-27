# Dockerize
Takes a folder and creates an initial DockerFile for the python files found in that folder. 

You provide the folder name as well as the container name through the standard python ```input()```. Inside a folder, the a crude Dockerfile appears that tries to install everything that was found to be imported. Some libraries can indeed be installed in this way as sklearn in the example. Some libraries may need renaming, as for example opencv or many others. And lastly, some libraries need not be installed like any standard libraries that the code might have imported. 

Apart from the libraries, what will also generally need attention is which file is to be ran. If there is more than one file in the specified folder it's not possible to tell which one to select and so, CMD just takes the firt python file that comes up as a placeholder and the user should alter that too. 

## Example

There is a sample in the DokerizerSample folder. Which is ran by running the ```main.py``` python code, specifying the DokerizerSample folder as the used folder, and specifying an arbitrary solution name. After running, there Dockerfile will be appropriately updated. The Docker is then built and ran by running "the build_and_run.cmd". If everything worked correctly the cmd should print ```[0 1 2 3 4]```.
