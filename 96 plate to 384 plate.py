#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 22:09:58 2021

@author: linda
"""
import math
#metadata
metadata = {'protocolName': 'Genotyping_384','author': 'Linda <linda.tanlam@gmail.com','description': 'Genotyping 384','apiLevel': '2.10'}

def run(protocol):
    # labware
   tiprack20 = [protocol.load_labware('opentrons_96_tiprack_20ul', slot)for slot in ['1', '4', '7', '10']]  
   source_plate1 = protocol.load_labware('elutionplatewithmagnet_96_wellplate_200ul', 2) 
   source_plate2 = protocol.load_labware('elutionplatewithmagnet_96_wellplate_200ul', 5)
   source_plate3 = protocol.load_labware('elutionplatewithmagnet_96_wellplate_200ul', 8)
   source_plate4 = protocol.load_labware('elutionplatewithmagnet_96_wellplate_200ul', 11) 
    
   destination_plate = protocol.load_labware('corning_384_wellplate_112ul_flat', 3)
    # pipettes
   left_pipette = protocol.load_instrument('p20_multi_gen2', 'left', tip_racks=tiprack20)
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~DNA plate column number~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   source_plate1_col = 12 # number of columns in plate1 in slot 2
   source_plate2_col = 7 # number of columns in plate2 in slot 5
   source_plate3_col = 10 # number of columns in plate3 in slot 8
   source_plate4_col = 12 # number of columns in plate4 in slot 11
   
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Plate1 source plate~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
   for i in range (1, source_plate1_col+1):
       source_plate_wellname = "A" + str(i)
       destination_well_number = math.ceil(i/2)
       if (i % 2) == 1 : #odd number-1, 3, 5
           left_pipette.pick_up_tip()
           # Aspirate 96well
           left_pipette.aspirate(2, source_plate1[source_plate_wellname])
           # Dispense in wells A, C, E, G, I, K, M, and O
           destination_well = "A" + str(destination_well_number)
           left_pipette.dispense(2, destination_plate[destination_well])
           left_pipette.blow_out()
           left_pipette.drop_tip()
       
       else: # even number - 2 , 4, 6
           left_pipette.pick_up_tip()
           # Aspirate 96well
           left_pipette.aspirate(2, source_plate1[source_plate_wellname])
           # Dispense in wells B, D, F, H, J, L, N, and P
           destination_well = "B" + str(destination_well_number)
           left_pipette.dispense(2, destination_plate[destination_well])
           left_pipette.blow_out()
           left_pipette.drop_tip()
           
           
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Plate2 source plate~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   
   #protocol.pause('Change plate')   
   for i in range (1, source_plate2_col+1):
       source_plate_wellname = "A" + str(i)
       destination_well_number = math.ceil(i/2)+6
       if (i % 2) == 1 : #odd number-1, 3, 5
           left_pipette.pick_up_tip()
           # Aspirate 96well
           left_pipette.aspirate(2, source_plate2[source_plate_wellname])
           # Dispense in wells A, C, E, G, I, K, M, and O
           destination_well = "A" + str(destination_well_number)
           left_pipette.dispense(2, destination_plate[destination_well])
           left_pipette.blow_out()
           left_pipette.drop_tip()
       
       else: # even number - 2 , 4, 6
           left_pipette.pick_up_tip()
           # Aspirate 96well
           left_pipette.aspirate(2, source_plate2[source_plate_wellname])
           # Dispense in wells B, D, F, H, J, L, N, and P
           destination_well = "B" + str(destination_well_number)
           left_pipette.dispense(2, destination_plate[destination_well])
           left_pipette.blow_out()
           left_pipette.drop_tip()
           
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Plate3 source plate~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   #protocol.pause('Change plate')
   for i in range (1, source_plate3_col+1):
       source_plate_wellname = "A" + str(i)
       destination_well_number = math.ceil(i/2)+12
       if (i % 2) == 1 : #odd number-1, 3, 5
           left_pipette.pick_up_tip()
           # Aspirate 96well
           left_pipette.aspirate(2, source_plate3[source_plate_wellname])
           # Dispense in wells A, C, E, G, I, K, M, and O
           destination_well = "A" + str(destination_well_number)
           left_pipette.dispense(2, destination_plate[destination_well])
           left_pipette.blow_out()
           left_pipette.drop_tip()
       
       else: # even number - 2 , 4, 6
           left_pipette.pick_up_tip()
           # Aspirate 96well
           left_pipette.aspirate(2, source_plate3[source_plate_wellname])
           # Dispense in wells B, D, F, H, J, L, N, and P
           destination_well = "B" + str(destination_well_number)
           left_pipette.dispense(2, destination_plate[destination_well])
           left_pipette.blow_out()
           left_pipette.drop_tip()
           
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Plate4 source plate~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   #protocol.pause('Change plate')
   for i in range (1, source_plate4_col+1):
       source_plate_wellname = "A" + str(i)
       destination_well_number = math.ceil(i/2)+18
       if (i % 2) == 1 : #odd number-1, 3, 5
           left_pipette.pick_up_tip()
           # Aspirate 96well
           left_pipette.aspirate(2, source_plate4[source_plate_wellname])
           # Dispense in wells A, C, E, G, I, K, M, and O
           destination_well = "A" + str(destination_well_number)
           left_pipette.dispense(2, destination_plate[destination_well])
           left_pipette.blow_out()
           left_pipette.drop_tip()
       
       else: # even number - 2 , 4, 6
           left_pipette.pick_up_tip()
           # Aspirate 96well
           left_pipette.aspirate(2, source_plate4[source_plate_wellname])
           # Dispense in wells B, D, F, H, J, L, N, and P
           destination_well = "B" + str(destination_well_number)
           left_pipette.dispense(2, destination_plate[destination_well])
           left_pipette.blow_out()
           left_pipette.drop_tip()
