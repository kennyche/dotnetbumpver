#!/usr/bin/python
# Author: Kenny Cheung
# Date: 23/08/2018

import sys, getopt, xml.etree.ElementTree, subprocess

def main(argv):
   inputfile = 'scratch.xml'
   type = 'MajorVersion'
   release = 'SNAPSHOT'
   try:
      opts, args = getopt.getopt(argv,"hi:t:r:",["ifile=","type=", "release="])
   except getopt.GetoptError:
      print('test.py -i <inputfile> -t <type> -r <release>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('test.py -i <inputfile> -t <type> -r <release>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-t", "--type"):
         type = arg
      elif opt in ("-r", "--release"):
         release = arg
   print('Input file is :', inputfile)
   print('VersionType is :', type)
   print('ReleaseType is :', release)

   e = xml.etree.ElementTree.parse(inputfile)

   if type == 'MajorVersion':
       for atype in e.findall('MajorVersion'):
           major = str(int(atype.text) + 1)
           atype.text = str((int(atype.text) + 1))
       for atype in e.findall('MinorVersion'):
           minor = str(int(0))
           atype.text = str(int(0))
       for atype in e.findall('PatchVersion'):
           patch = str(int(0))
           atype.text = str(int(0))
       print(major + "." + minor + "." + patch + "-" + release)
   if type == 'MinorVersion':
       for atype in e.findall('MajorVersion'):
           major = str(int(atype.text))
       for atype in e.findall('MinorVersion'):
           minor = str(int(atype.text) + 1)
           atype.text = str((int(atype.text) + 1))
       for atype in e.findall('PatchVersion'):
           patch = str(int(atype.text))
       print(major + "." + minor + "." + patch + "-" + release)
   if type == 'PatchVersion':
       for atype in e.findall('MajorVersion'):
           major = str(int(atype.text))
       for atype in e.findall('MinorVersion'):
           minor = str(int(atype.text))
       for atype in e.findall('PatchVersion'):
           patch = str(int(atype.text) + 1)
           atype.text = str((int(atype.text) + 1))
       print(major + "." + minor + "." + patch + "-" + release)
   if release == 'RELEASE' or release == 'SNAPSHOT':
       for atype in e.findall('ReleaseVersion'):
           atype.text=release

   e.write('scratch.xml')
  # p = subprocess.Popen(['powershell.exe', 'Write-Host ##vso[task.setvariable variable=GitVersionTag;]$VersionString'],
  #                      stdout=sys.stdout)

if __name__ == "__main__":
   main(sys.argv[1:])
