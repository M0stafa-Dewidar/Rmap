import pandas as pd
import os
import xml_parser_for_nmap

dir_path = os.path.dirname(os.path.realpath(__file__))
masterlistfn = dir_path + "/masterlist.csv"
masterlist = pd.read_csv(masterlistfn)
timestamp = xml_parser_for_nmap.nmap_script.time_stamp
testdatafn = dir_path + '/data/' + 'scanresults__' + timestamp + '.csv'

testdata = pd.read_csv(testdatafn)

MasterMACs = masterlist['MAC address']
testdata.fillna("empty", inplace=True)
potential_rogue_systems = []

#MAC Address test
for index, row in testdata.iterrows():
	if row['MAC address'] not in MasterMACs.values and row['MAC address'] != "empty":
		potential_rogue_systems.append(row)
rogue = pd.DataFrame(potential_rogue_systems)
output_rogue_fn = dir_path + "/rogue/" + timestamp + "rogue.csv"
rogue.to_csv(output_rogue_fn)


