#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 22:42:42 2021

@author: linda
"""
#metadata
metadata = {'protocolName': '96 to 96 well plate','author': 'Linda','description': '96 to 96 well plate,'apiLevel': '2.10'}
col_list = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "A11", "A12"] #0-12
def run(protocol):
    # creadt own function the transfer and change tip in between
   def transfer_modify(pipette, volume, num_col, sorce, des):
        col_list = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "A11", "A12"] #0-12
        for i in range (num_col):
            pipette.pick_up_tip()
            pipette.aspirate(volume, sorce[col_list[i]])
            pipette.air_gap(0.6)
            pipette.dispense(volume+5, des[col_list[i]].top(-6))
            pipette.blow_out()
            pipette.blow_out()
            pipette.blow_out()
            pipette.touch_tip() 
            pipette.drop_tip()    
    # labware
   tiprack20 = [protocol.load_labware('opentrons_96_tiprack_20ul', slot)for slot in ['1', '4', '7']]  
   source_plate1 = protocol.load_labware('elutionplatewithmagnet_96_wellplate_200ul', 2) 
   source_plate2 = protocol.load_labware('elutionplatewithmagnet_96_wellplate_200ul', 5)
   source_plate3 = protocol.load_labware('elutionplatewithmagnet_96_wellplate_200ul', 8)
   des_plate1 = protocol.load_labware('regplateholder_96_wellplate_200ul', 3)
   des_plate2 = protocol.load_labware('regplateholder_96_wellplate_200ul', 6)
   des_plate3 = protocol.load_labware('regplateholder_96_wellplate_200ul', 9)
    # pipettes
   p20_multi = protocol.load_instrument('p20_multi_gen2', 'left', tip_racks=tiprack20)
   
  #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~PCR plate column number ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   source_plate1_col = 7   # number of columns in plate1 in slot 2
   source_plate2_col = 0 # number of columns in plate2 in slot 5
   source_plate3_col = 0 # number of columns in pla te3 in slot 8   
   DNA_vol = 2 
   #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   # 1st plate code
   p20_multi.flow_rate.dispense = 6
# 1st plate code
   p20_multi.flow_rate.aspirate = 6
   
   if source_plate1_col > 0: 
        transfer_modify(p20_multi, DNA_vol, source_plate1_col, source_plate1, des_plate1)
# 2nd plate code
   if source_plate2_col > 0:
        transfer_modify(p20_multi, DNA_vol, source_plate2_col, source_plate2, des_plate2)
# # 3rd plate code
   if source_plate3_col > 0: 
        transfer_modify(p20_multi, DNA_vol, source_plate3_col, source_plate3, des_plate3)