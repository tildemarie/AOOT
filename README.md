This GitHub contains the code used for processing different things related to the project in AOOT (summer 2026).

"Extract_fish_coordinates" uses the output .txt files from LSSS (ListUserFile...) and singles out every fish/school event, and then lumps the ones together that are probably the same event based on values spanning multiple seconds. This can then be used to get the coordinates and depths for each fish. 

"Fish_echogram" is the code used to make simple, single-colored echograms/transects from the LSSS output .txt files.

"Fish_depth_histogram" is the code used to make a histogram of the count of individual fish and schools versus depth from the .csv files (fish_school_events_xxxx). Since the detections were in a relatively narrow area, the intervals are all of only 1 m. This can obviously be changed. 

"tv80_trawl_analysis" is the code for the calculations about the fish density. It uses 2 files: "Havfisken-D20260609-T084257.txt" and "Havfisken-D20260611-T074259.txt" from the HFLog from Havfisken.

"Pycnocline cor" uses Seabird CTD data and fish observations from the echosounder to correlate and compare fish presence with environmental conditions. It looks at day 1 vs day 2 vs day 3, schools vs individuals, and across all variables and days. It includes interpolation  boxplots, summary statistics and various statistical tests.

"CTD & fish" uses Seabird CTD data and fish observations from the echosounder to correlate and compare fish presence with environmental conditions. It oulines the interpolation of CTD data workflow, and summarises physical conditions that fish are experiencing.
