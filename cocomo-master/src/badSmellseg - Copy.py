from __future__ import division,print_function
import sys,random
sys.dont_write_bytecode = True

"""

# Test Cases for COCOMO

"""
from cocomo import *
from badSmells import *
 
 
PROJECTS  = [osp]
#Change the treatment name depending on the practice task
TREATMENTS= [doNothing, newTreatment2]
             
 
@go
def _badSmells():
  sample(projects=PROJECTS,score=badSmell)
   
@go
def _whatStinks():
    rseed(1)
    for project in PROJECTS:
        print("\n",project.__name__)
        stinks = whatStinks(project)
        worst = stinks[0][0]
        for stink,what in stinks:
            if stink > worst*0.5:
                print('stink = ',stink,' when ',what)

@go
def _badSmellsTreated():
  rseed(1)
  for project in [anything]:
    print("\n#### ",project.__name__," ","#"*50,"\n")
    sample(projects=[project],treatments=TREATMENTS,score=badSmell)

 
 

 