# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 18:46:12 2018

@author: gawandm
"""

import js
from js import *
from LBA import * 
from jsHuman import * 
import jmStaticStrength

#def Initialize():
#    
#
##    jmStaticStrength.Use(hum)
##    weight = 10.0*u.kg
##    jmStaticStrength.Inst.SetWeight('right_palm.palmcenter',weight)
#    
##    hum.Pose('kneel_one_knee')
#    
##    h = CreateFemale()
##    h.Pose('crawl')
##    
#    return hum


#def Walk():
#    h = CreateMale()
#    h.Pose('crawl')
#    return h
#    


def reach():
    print("Start demo")
    jk = CreateMale()
    jk.Pose("seated_erect")
    cd("C:\Users\gawandm\BASE")
    LoadFile("base.env")
    hum = scene.Find("human",Figure)
    jk.SetLocation(hum)
    
    print
    
    reach = jk.ReachHold("right",goal=scene.middle.seg0.S0,jfrom="shoulder",endeff="palm",reach_duration=5, duration = 10, start = 1,style=EaseInEaseOut)
    
    UseHuman(hum)
        
    print("Get L4/L5 Force")
    force = GetResults(L4L5_FORCE)
        
        
    print("Get LBA Result Dict for L4L5 Moments")
    moment = GetResults(L4L5_MOMENT)
        
    print
    print 
    print "What are the L4L5 Moments Keys?"
    print moment
    
       # What is the L4L5 Moments
    print
    print 
    print "What are the L4L5 Moments ?"
    keys = moment.keys()
        
    
    
#    h = Walk()
#    
#    UseHuman(h)
#    print("Get L4/L5 Force")
#    force = GetResults(L4L5_FORCE)
#    
#    
#    print("Get LBA Result Dict for L4L5 Moments")
#    moment = GetResults(L4L5_MOMENT)
#    
#    print
#    print 
#    print "What are the L4L5 Moments Keys?"
#    print moment
    

##    for i in keys:
#    while i <= 2:
##        hum.Walk((200, 0, 200), duration=5)
#        
##        h = hum.Pose('kneel_one_knee')
##        UseHuman(h)
#        moment = GetResults(L4L5_MOMENT)
#       
##        print "Moment key %s" % (i)
#        print "Moment value %s" % (moment)
#        
#        i = i + 1 
#
#    print
#    print 
#    print "Done with Demo"
    
    
# check if running as a program
if __name__ == '__main__':
    # yes, a program
    reach()
