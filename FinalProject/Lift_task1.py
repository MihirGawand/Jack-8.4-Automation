# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 09:03:39 2018

@author: gawandm
"""

import js
from js import *
from LBA import * 
from jsHuman import * 
import jmStaticStrength
from math import *




def Initialize():
    print("Create Human")
    
    jack = CreateMale()
    return jack



def lift1():
    print("Start Demo")
    
    moments = []
    
    cd("C:\Users\gawandm\BASE")
    LoadFile("lift2.env")
    hum = Initialize()

    
    Anthro = [[152,50],[175,78],[185,98]]
    
    moments_list = []

    
    for row in Anthro:
        stature,weight = row

        print(stature,weight)
        myHum = scene.human
        myHumAS = myHum._human.initAnthroscale('CDN_LF_97')
        myHumAS.scaleHeightNweight(stature,weight)
        
        UseHuman(hum)
        w = 10.0*u.kg
        jmStaticStrength.Use(hum)
        jmStaticStrength.Inst.SetWeight('right_palm.palmcenter',w)
    
        DoInOrder(
        hum.Pose("stand_straight"),
        hum.Walk((75,0,0),duration=5),
        hum.Lift(scene.solid,goal_height=4*u.ft,duration=5,start=1,style=EaseInEaseOut))
        
        
        
        print
        print 
        print "Get LBA Result Dict for L4L5 Forces"
        force = GetResults(L4L5_FORCE)
            # To Get a LBA Dict for a specified LBA Result Type
        print
        print 
        print "Get LBA Result Dict for L4L5 Moments"
        moment = GetResults(L4L5_MOMENT)
        print(moment.values())
        
        moments = moment.values()
            
        total_moment = 0
            
        for i in moments:
            total_moment = total_moment  + abs(i)
                
        print(total_moment)
        
        row.append(total_moment)
        
        
    print(Anthro)
    stature, weight, value = min(Anthro, key=lambda item: item[2])
    print("Minimum Moment:",value)
    print("Best Anthropometry:")
    print("Stature %s" % (stature)) 
    print("Weight %s" % (weight))
    
        
        
if __name__ == '__main__':
    lift1()