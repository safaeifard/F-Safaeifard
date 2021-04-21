# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 07:34:16 2021

@author: user
"""
import cobra
from cobra import Model, Reaction, Metabolite

from pysb import  Parameter



model = Model('example_model')
# from kineticmodel import model as kineticmodel


# Parameter('Enz1', 15e-3)
# Parameter('Enz2', 15e-3)
# Parameter('Enz3', 15e-3)
# Parameter('Enz4', 15e-3)
# Parameter('Enz5', 15e-3)
# Parameter('Enz6', 15e-3)
# Parameter('Enz7', 15e-3)
# Parameter('Enz8', 15e-3)
# Parameter('Enz9', 15e-3)
# Parameter('Enz10', 15e-3)
# Parameter('Enz11', 15e-3)
# Parameter('Enz12', 15e-3)
# Parameter('Enz13', 15e-3)
# Parameter('Enz14', 15e-3)
# Parameter('Enz15', 15e-3)
# Parameter('Enz16', 15e-3)
# Parameter('Enz17', 15e-3)
# Parameter('Enz18', 15e-3)


Parameter('kcat1', 1000.0)
Parameter('kcat2', 830) 
Parameter('kcat3', 1.3) 
Parameter('kcat4', 1.0e-3)
Parameter('kcat5', 3.3e-6)
Parameter('kcat6', 2.3)
Parameter('kcat7', 1.0e-3)
Parameter('kcat8', 8.3e-6)
Parameter('kcat9', 1.3)

#Rates for 2-AG and COX2 interactions at catalytic site
Parameter('kcat10', 1000.0)
Parameter('kcat11', 760.0) 
Parameter('kcat12', 1.2) 
Parameter('kcat13', 1.0e-3)
Parameter('kcat14', 4.8e-4)
Parameter('kcat15', 1.0e-3)
Parameter('kcat16', 1.9e-6)
Parameter('kcat17', 0.21)
Parameter('kcat18', 0.21)

reaction1 = Reaction('R_1')
reaction2 = Reaction('R_2')
reaction3 = Reaction('R_3')
reaction4 = Reaction('R_4')
reaction5 = Reaction('R_5')
reaction6 = Reaction('R_6')
reaction7 = Reaction('R_7')
reaction8 = Reaction('R_8')
reaction9 = Reaction('R_9')
reaction10 = Reaction('R_10')
reaction11 = Reaction('R_11')
reaction12 = Reaction('R_12')
reaction13 = Reaction('R_13')
reaction14 = Reaction('R_14')
reaction15 = Reaction('R_15')
reaction16 = Reaction('R_16')
reaction17 = Reaction('R_17')
reaction18 = Reaction('R_18')



for rxn in model.reactions:
    rxn.subsystem='Cell Envelope Biosynthesis'


Met_1 = Metabolite(
    'M1',
    compartment='c')
Met_2 = Metabolite(
    'M2',
    compartment='c')
Met_3 = Metabolite(
    'M3',
    compartment='c')
Met_4 = Metabolite(
    'M4',
    compartment='c')
Met_5 = Metabolite(
    'M5',
    compartment='c')
Met_6 = Metabolite(
    'M6',
    compartment='c')
Met_7 = Metabolite(
    'M7',
    compartment='c')
Met_8 = Metabolite(
    'M8',
    compartment='c')
Met_9 = Metabolite(
    'M9',
    compartment='c')
Met_10 = Metabolite(
    'M10',
    compartment='c')
Met_11 = Metabolite(
    'M11',
    compartment='c')
Met_12 = Metabolite(
    'M12',
    compartment='c')


reaction1.add_metabolites({
Met_1 : -1,
Met_2 : -1,
Met_3 : 0,
Met_4 : 0,
Met_5 : 1,
Met_6 : 0,
Met_7  : 0,
Met_8   : 0,
Met_9 : 0,
Met_10: 0,
Met_11 : 0,
Met_12 : 0,
})

reaction2.add_metabolites({
Met_1 : -1,
Met_2 : -1,
Met_3 : 0,
Met_4 : 0,
Met_5: 1,
Met_6 : 0,
Met_7  : 0,
Met_8   : 0,
Met_9 : 0,
Met_10: 0,
Met_11 : 0,
Met_12 : 0,
})

reaction3.add_metabolites({
Met_1 : -1,
Met_2 : -1,
Met_3 : 0,
Met_4 : 0,
Met_5: 1,
Met_6 : 0,
Met_7  : 0,
Met_8   : 0,
Met_9 : 0,
Met_10: 0,
Met_11 : 0,
Met_12 : 0,
})

reaction4.add_metabolites({
Met_1 : -1,
Met_2 : -1,
Met_3 : 0,
Met_4 : 0,
Met_5: 1,
Met_6 : 0,
Met_7  : 0,
Met_8   : 0,
Met_9 : 0,
Met_10: 0,
Met_11 : 0,
Met_12 : 0,
})

reaction5.add_metabolites({
Met_1 : -1,
Met_2 : -1,
Met_3 : 0,
Met_4 : 0,
Met_5: 1,
Met_6 : 0,
Met_7  : 0,
Met_8   : 0,
Met_9 : 0,
Met_10: 0,
Met_11 : 1,
Met_12 : 0,
})

reaction6.add_metabolites({
Met_1 : -1,
Met_2 : -1,
Met_3 : 0,
Met_4 : 0,
Met_5: 1,
Met_6 : 0,
Met_7  : 0,
Met_8   : 0,
Met_9 : 0,
Met_10: 0,
Met_11 : 0,
Met_12 : 0,
})

reaction7.add_metabolites({
Met_1 : -1,
Met_2 : -1,
Met_3 : 0,
Met_4 : 0,
Met_5: 1,
Met_6 : 0,
Met_7  : 0,
Met_8   : 0,
Met_9 : 0,
Met_10: 0,
Met_11 : 0,
Met_12 : 0,
})

reaction8.add_metabolites({
Met_1 : -1,
Met_2 : -1,
Met_3 : 0,
Met_4 : 0,
Met_5: 1,
Met_6 : 0,
Met_7  : 0,
Met_8   : 0,
Met_9 : 0,
Met_10: 0,
Met_11 : 1,
Met_12 : 0,
})

reaction9.add_metabolites({
Met_1 : -1,
Met_2 : -1,
Met_3 : 0,
Met_4 : 0,
Met_5: 1,
Met_6 : 0,
Met_7  : 0,
Met_8   : 0,
Met_9 : 0,
Met_10: 0,
Met_11 : 0,
Met_12 : 0,
})

reaction10.add_metabolites({
Met_1 : -1,
Met_2 : -1,
Met_3 : 0,
Met_4 : 0,
Met_5: 1,
Met_6 : 0,
Met_7  : 0,
Met_8   : 0,
Met_9 : 0,
Met_10: 0,
Met_11 : 0,
Met_12 : 1,
})

reaction11.add_metabolites({
Met_1 : -1,
Met_2 : -1,
Met_3 : 0,
Met_4 : 0,
Met_5: 1,
Met_6 : 0,
Met_7  : 0,
Met_8   : 0,
Met_9 : 0,
Met_10: 0,
Met_11 : 0,
Met_12 : 1,
})

reaction12.add_metabolites({
Met_1 : -1,
Met_2 : -1,
Met_3 : 0,
Met_4 : 0,
Met_5: 1,
Met_6 : 0,
Met_7  : 0,
Met_8   : 0,
Met_9 : 0,
Met_10: 0,
Met_11 : 0,
Met_12 : 0,
})

reaction13.add_metabolites({
Met_1 : -1,
Met_2 : -1,
Met_3 : 0,
Met_4 : 0,
Met_5: 1,
Met_6 : 0,
Met_7  : 0,
Met_8   : 0,
Met_9 : 0,
Met_10: 0,
Met_11 : 0,
Met_12 : 0,
})

reaction14.add_metabolites({
Met_1 : -1,
Met_2 : -1,
Met_3 : 0,
Met_4 : 1,
Met_5: 1,
Met_6 : 0,
Met_7  : 1,
Met_8   : 0,
Met_9 : 0,
Met_10: 0,
Met_11 : 0,
Met_12 : 0,
})

reaction15.add_metabolites({
Met_1 : -1,
Met_2 : -1,
Met_3 : 0,
Met_4 : 1,
Met_5: 1,
Met_6 : 0,
Met_7  : 1,
Met_8   : 0,
Met_9 : 0,
Met_10: 0,
Met_11 : -1,
Met_12 : 0,
})

reaction16.add_metabolites({
Met_1 : -1,
Met_2 : -1,
Met_3 : 0,
Met_4 : 1,
Met_5: 1,
Met_6 : 0,
Met_7  : 1,
Met_8   : 0,
Met_9 : 0,
Met_10: 0,
Met_11 : 0,
Met_12 : 0,
})

reaction17.add_metabolites({
Met_1 : -1,
Met_2 : -1,
Met_3 : 0,
Met_4 : 1,
Met_5: 1,
Met_6 : 0,
Met_7  : 1,
Met_8   : 0,
Met_9 : 0,
Met_10: 0,
Met_11 : 0,
Met_12 : 0,
})

reaction18.add_metabolites({
Met_1 : -1,
Met_2 : -1,
Met_3 : 0,
Met_4 : 1,
Met_5: 1,
Met_6 : 0,
Met_7  : 1,
Met_8   : 0,
Met_9 : 0,
Met_10: 0,
Met_11 : 0,
Met_12 : -1,
})

 # string representation of the reactions

for rxn in model.reactions:
    rxn.reaction

model.add_reactions([reaction1,reaction2,reaction3,reaction4,reaction5,reaction6,reaction7,
                     reaction8,reaction9,reaction10,reaction11,reaction12,reaction13,reaction14
                     ,reaction15,reaction16,reaction17,reaction18])

# Iterate through the the objects in the model
print("Reactions")
print("---------")
for rxn in model.reactions:
    print("%s : %s" % (rxn.id, rxn.reaction))

print("")
print("Metabolites")
print("-----------")
for met in model.metabolites:
    print('%9s : %s' % (met.id, met.formula))

print("")
print("Genes")
print("-----")
for x in model.genes:
    associated_ids = (i.id for i in x.reactions)
    print("%s is associated with reactions: %s" %
          (x.id, "{" + ", ".join(associated_ids) + "}"))
model.objective ="R_3"
# The upper bound should be 1000, so that we get
# the actual optimal value
model.reactions.get_by_id("R_3").upper_bound = 1000.
model.objective





#Kcat={'kcat1': 1000.0, 'kcat2': 830, 'kcat3': 1.3,'kcat4': 1.0e-3,'kcat5':3.3e-6 ,'kcat6':2.3 ,'kcat7': 1.0e-3,'kcat8': 8.3e-6,'kcat9': 1.3,'kcat10': 1000,'kcat11': 760,'kcat12': 1.0e-3,'kcat13': 1.0e-3,'kcat14': 4.8e-4,'kcat15': 1.0e-3,'kcat16': 1.9e-6,'kcat17': 0.21,'kcat18': 0.21}
Kcat=[1000.0, 830, 1.3, 1.0e-3,3.3e-6 ,2.3 ,1.0e-3,8.3e-6, 1.3,1000,760,1.0e-3,1.0e-3, 4.8e-4,1.0e-3, 1.9e-6, 0.21, 0.21]

# Kcat=[kcat1, kcat2, kcat3,kcat4,kcat5,kcat6,kcat7,kcat8,kcat9,kcat10,kcat11,kcat12,kcat13,kcat14,kcat15,kcat16,kcat17,kcat18]
# N=[n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18]
# R_kinetics={'R_1': '3.07', 'R_2': 'Kcat1*n2', 'R_3': 'Kcat1*n3', 'R_4': 'Kcat1*n4', 'R_5': 'Kcat1*n5', 'R_6': 'Kcat1*n6', 'R_7': 'Kcat1*n7' , 'R_8': 'Kcat1*n8', 'R_9': 'Kcat1*n9', 'R_10': 'Kcat1*n10', 'R_11': 'Kcat1*n11', 'R_12': 'Kcat1*n12', 'R_13': 'Kcat1*n13', 'R_14' : 'Kcat1*n14', 'R_15' : 'Kcat1*n15', 'R_16': 'Kcat1*n16', 'R_17': 'Kcat1*n17', 'R_18': 'Kcat1*n18'}

# for rxn in model.reactions:
#     constraint = model.problem.Constraint(0, lb=0, ub=R_kinetics[rxn])
#     model.add_cons_vars(constraint)
    
for i in range (17) :     #shoud be assigned to reactions
      constraint = model.problem.Constraint(0, lb=0, ub=Kcat[i]*50 )
      model.add_cons_vars(constraint)

print(model.objective.expression)
print(model.objective.direction)


import tempfile
from pprint import pprint
from cobra.io import write_sbml_model, validate_sbml_model
with tempfile.NamedTemporaryFile(suffix='.xml') as f_sbml:
   
   # write_sbml_model(model, filename=f_sbml.name)
   # report = validate_sbml_model(filename=f_sbml.name)
      
    write_sbml_model(model, 'Toy_Model')
    report = validate_sbml_model('Toy_Model')
   
pprint(report)



