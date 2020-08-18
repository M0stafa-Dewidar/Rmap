import nmap_script
import xml.etree.ElementTree as ET
import pandas as pd
import os

host_list = []
outputfnpath = os.path.dirname(os.path.realpath(__file__)) + "/data/"
outputfnprefix = 'scanresults__'
time_stamp = nmap_script.time_stamp
outputfn = outputfnpath + outputfnprefix + time_stamp + '.csv'
inputfn = outputfnpath + outputfnprefix + time_stamp + '.xml'

tree = ET.parse(inputfn)
root = tree.getroot()

for host in root.iter('host'):
	host_info = {}
	for child in host:
		if child.tag == 'hostname':
			host_info['hostname'] = child.attrib['name']
		if child.tag == 'address' and child.attrib['addrtype'] == 'ipv4':
			host_info['IP Address'] = child.attrib['addr']
		if child.tag == 'address' and child.attrib['addrtype'] == 'mac':
			host_info['MAC address'] = child.attrib['addr']
			if child.attrib.get('vendor'):
				host_info['Vendor'] = child.attrib['vendor']
		if child.tag == 'os':
			for oschild in child:
				if oschild.tag == 'osmatch':
					host_info['OS'] = oschild.attrib['name']
					break
	host_list.append(host_info)

df = pd.DataFrame(host_list)
df.to_csv(outputfn)

