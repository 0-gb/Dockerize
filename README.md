# Dockerize
Takes a folder and creates an initial DockerFile for the python files found in that folder. 

You provide the folder name as well as the container name through the standard python ```input()```. Inside a folder, the a crude Dockerfile appears that tries to install everything that was found to be imported. Some libraries can indeed be installed in this way as sklearn in the example. Some libraries may need renaming, as for example opencv or many others. And lastly, some libraries need not be installed like any standard libraried that the code might have imported. 

Apart from the libraries, what will also generally need attention is which file is to be ran. There is no logic built to decide and CMD just takes the firt python file that comes ups so that one should be appropriately altered too. 
