#['IP', 'DNS', 'NetBIOS', 'OS', 'IP Status', 'QID', 'Title', 'Type', 'Severity', 'Port', 'Protocol', 'FQDN', 'SSL', 'CVE ID', 'Vendor Reference', 'Bugtraq ID', 'CVSS Base', 'CVSS Temporal', 'Threat', 'Impact', 'Solution', 'Exploitability', 'Associated Malware', 'Results', 'PCI Vuln', 'Instance']

#Row 8
#sample usage 1: python qualysparse.py -f qualys.csv -t "Feature Denial of Service"
#sample usage 2: python qualysparse.py -f qualys.csv -s 5
#python qualysparse.py -f qualys.csv -c CVE-2014-0224
# Prajwal Panchmahalkar's script to parse Qualys Reports prajwal@matriux.com


import optparse
import csv
import sys,os
def parse_by_severity(qualysreportfile, severity):
	with open(qualysreportfile) as f:
		for i, line in enumerate(csv.reader(f,delimiter=','),1):
			if i > 9:
				try:
					if(int(line[8])==int(severity)):
						if(line[9]!=None):
							print line[0]+" | "+line[9]+" | "+line[6]
						else:
							print line[0]+" | "+line[6]
				except:
					pass
				continue

def parse_by_cve(qualysreportfile, cveid):
	with open(qualysreportfile) as f:
		for i, line in enumerate(csv.reader(f,delimiter=','),1):
			if i>9:
				try:
					if(str(cveid) in str(line[13])):
						if(line[9]!=None):
							print line[0]+ " | "+line[9]+" | "+line[6]
						else:
							print line[0]+" "+line[6]
				except:
					pass
				continue
def parse_by_title(qualysreportfile, title):
	with open(qualysreportfile) as f:
		for i, line in enumerate(csv.reader(f,delimiter=','),1):
			if i>9:
				try:
					if(str(title) in str(line[6])):
						if(line[9]!=None):
							print line[0]+" | "+line[9]+" | "+line[6]
						else:
							print line[0]+" | "+line[6]
				except:
					pass
				continue

def main():
	parser = optparse.OptionParser('python %prog -f qualys.csv  -s <severity> or -cve <CVEID> or -t <title>')
	parser.add_option('-f', dest = 'tgtfile', metavar = 'FILE', help ='specify the qualys report in csv')
	parser.add_option('-s', dest = 'severity', help ='specify the severity 1-5 report in csv')
	parser.add_option('-c', dest = 'CVEID', help ='eg.,CVE-2014-0224')
	parser.add_option('-t', dest = 'title', help ='NTP monlist feature denial of service')
	(options,args) = parser.parse_args()
	reportfile = options.tgtfile
	severity = options.severity
	cve = options.CVEID
	vulntitle = options.title
	if((reportfile==None) & ((severity==None)|(cve==None)|(vulntitle==None))):
		print parser.usage
		sys.exit(0)
	if(severity!=None):
		if int(severity) in range(1,6):
			parse_by_severity(reportfile,severity)
		else:
			print "[!]Severity must be in range 1 to 5."
			print "[!]Exiting...."
			sys.exit(0)
	if(cve!=None):
		parse_by_cve(reportfile,cve)
	if(vulntitle!=None):
		parse_by_title(reportfile,vulntitle)

if __name__ =="__main__":
    main()