Collaborators:
  Hernandez, Jose
  Soledad, Alejandro

Supervisor:
  Megret, Remi

Research Group:
  Megret Labs

This project attempts to track, identify, and reidentify bees confined in a testube durring an assay.In particulr the research-
ers intended to understand the behavior of the animal as exposed to ethanol vapor.

To this end we employed DeepLabCut --github.com/DeepLabCut-- to do pose identification. The resulting pose data-- (x,y,t) cordi-
nates--  are segmented using the horizantal axes to identify the bees do to there confinement. This can be done manually or em-
ploying K-means on the videos horizantal axis.

The resulting data is placed in a dataframe indexed by individual and time frame from which we can generate readable graphs and
treshold for certan behaviors such as knock out-- effectively bellow y_KO for t_KO or more frames. 

I am in the process of migrating the CoLab to Git so that all refrences to Google Drive instad refrence folders in the lab. Fur-
ther cleaning and organizing of the data is required. In the future I seek to covert this to a desktop app.
