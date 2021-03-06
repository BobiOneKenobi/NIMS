#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Python script for use with Abaqus 6.12
#====================================================================================================================
# AUTHOR: d.mercier
# DATE: May.26,2015 10:29
# GENERATED WITH: NIMS_2.6 written by D. Mercier
# See https://github.com/DavidMercier/NIMS
# or http://fr.mathworks.com/matlabcentral/fileexchange/43392-davidmercier-nims
# Modelling of indentation experiments with a (sphero-)conical indenter performed on a multilayer system
# To run this procedure Python script, open Abaqus, then ==> File/Run Script
# Units: Displacement in nm, Young's modulus in GPa ==> Load in nN.
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# NEW MODEL
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup

import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import material
import assembly
import step
import interaction
import load
import mesh
if ('12' in version) == True:
    import optimization # Not available in versions released before Abaqus 6.12
import job
import sketch
import visualization
import xyPlot
import displayGroupOdbToolset as dgo
import connectorBehavior

cliCommand("""session.journalOptions.setValues(replayGeometry=COORDINATE, recoverGeometry=COORDINATE)""")
backwardCompatibility.setValues(includeDeprecated=True, reportDeprecated=False)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# PARAMETERS
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
myModel = mdb.Model(name='multilayer_model_2015-05-26')
indenter_used = 'BerkoSaclay'
h_ind = 0.100000
r_ind = 1.611982
a_ind = 70.32
sheet_Size = 3000.000000
step_Load = 'Loading'
ind_h = -200.000000
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# PARTS
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Analytical rigid indenter
s = myModel.ConstrainedSketch(name='__profile__', sheetSize=sheet_Size)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.sketchOptions.setValues(viewStyle=AXISYM)
s.setPrimaryObject(option=STANDALONE)
s.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
s.FixedConstraint(entity=g[2])
s.ArcByCenterEnds(center=(0.0, r_ind), point1=(0.542862 , 0.094159), point2=(0.0, 0.0),direction=CLOCKWISE)
s.Line(point1=(0.542862 , 0.094159), point2=(1412.925095 , 505.244063))
s.TangentConstraint(entity1=g[3], entity2=g[4])
p = myModel.Part(name=indenter_used, dimensionality=AXISYMMETRIC, type=ANALYTIC_RIGID_SURFACE)
p = myModel.parts[indenter_used]
p.AnalyticRigidSurf2DPlanar(sketch=s)
s.unsetPrimaryObject()
p = myModel.parts[indenter_used]
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del myModel.sketches['__profile__']
p = myModel.parts[indenter_used]
v1, e, d1, n = p.vertices, p.edges, p.datums, p.nodes
p.ReferencePoint(point=v1.findAt(coordinates=(0.0, 0.0, 0.0)))
# -------------------------------------------------------------------------------------------------------------------
# Multilayer sample
s = myModel.ConstrainedSketch(name='__profile__', sheetSize=sheet_Size)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.sketchOptions.setValues(viewStyle=AXISYM)
s.setPrimaryObject(option=STANDALONE)
s.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
s.FixedConstraint(entity=g[2])
s.rectangle(point1=(0.0, 0.000000), point2=(3000.000000, -500.000000))
s.CoincidentConstraint(entity1=v[0], entity2=g[2], addUndoState=False)
p = myModel.Part(name='Film_4', dimensionality=AXISYMMETRIC, type=DEFORMABLE_BODY)
p = myModel.parts['Film_4']
p.BaseShell(sketch=s)
s.unsetPrimaryObject()
p = myModel.parts['Film_4']
s = p.edges
side1Edges = s.findAt(((1500.000000, 0.000000, 0.0), ))
p.Surface(side1Edges=side1Edges, name='Surf-Top')
side1Edges = s.findAt(((1500.000000, -500.000000, 0.0), ))
p.Surface(side1Edges=side1Edges, name='Surf-Bottom')
a = myModel.rootAssembly
a.regenerate()
s = myModel.ConstrainedSketch(name='__profile__', sheetSize=sheet_Size)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.sketchOptions.setValues(viewStyle=AXISYM)
s.setPrimaryObject(option=STANDALONE)
s.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
s.FixedConstraint(entity=g[2])
s.rectangle(point1=(0.0, -500.000000), point2=(3000.000000, -1000.000000))
s.CoincidentConstraint(entity1=v[0], entity2=g[2], addUndoState=False)
p = myModel.Part(name='Film_3', dimensionality=AXISYMMETRIC, type=DEFORMABLE_BODY)
p = myModel.parts['Film_3']
p.BaseShell(sketch=s)
s.unsetPrimaryObject()
p = myModel.parts['Film_3']
s = p.edges
side1Edges = s.findAt(((1500.000000, -500.000000, 0.0), ))
p.Surface(side1Edges=side1Edges, name='Surf-Top')
side1Edges = s.findAt(((1500.000000, -1000.000000, 0.0), ))
p.Surface(side1Edges=side1Edges, name='Surf-Bottom')
a = myModel.rootAssembly
a.regenerate()
s = myModel.ConstrainedSketch(name='__profile__', sheetSize=sheet_Size)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.sketchOptions.setValues(viewStyle=AXISYM)
s.setPrimaryObject(option=STANDALONE)
s.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
s.FixedConstraint(entity=g[2])
s.rectangle(point1=(0.0, -1000.000000), point2=(3000.000000, -1500.000000))
s.CoincidentConstraint(entity1=v[0], entity2=g[2], addUndoState=False)
p = myModel.Part(name='Film_2', dimensionality=AXISYMMETRIC, type=DEFORMABLE_BODY)
p = myModel.parts['Film_2']
p.BaseShell(sketch=s)
s.unsetPrimaryObject()
p = myModel.parts['Film_2']
s = p.edges
side1Edges = s.findAt(((1500.000000, -1000.000000, 0.0), ))
p.Surface(side1Edges=side1Edges, name='Surf-Top')
side1Edges = s.findAt(((1500.000000, -1500.000000, 0.0), ))
p.Surface(side1Edges=side1Edges, name='Surf-Bottom')
a = myModel.rootAssembly
a.regenerate()
s = myModel.ConstrainedSketch(name='__profile__', sheetSize=sheet_Size)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.sketchOptions.setValues(viewStyle=AXISYM)
s.setPrimaryObject(option=STANDALONE)
s.ConstructionLine(point1=(0.0, -100.0), point2=(0.0, 100.0))
s.FixedConstraint(entity=g[2])
s.rectangle(point1=(0.0, -1500.000000), point2=(3000.000000, -2500.000000))
s.CoincidentConstraint(entity1=v[0], entity2=g[2], addUndoState=False)
p = myModel.Part(name='Film_1', dimensionality=AXISYMMETRIC, type=DEFORMABLE_BODY)
p = myModel.parts['Film_1']
p.BaseShell(sketch=s)
s.unsetPrimaryObject()
p = myModel.parts['Film_1']
s = p.edges
side1Edges = s.findAt(((1500.000000, -1500.000000, 0.0), ))
p.Surface(side1Edges=side1Edges, name='Surf-Top')
side1Edges = s.findAt(((1500.000000, -2500.000000, 0.0), ))
p.Surface(side1Edges=side1Edges, name='Surf-Bottom')
a = myModel.rootAssembly
a.regenerate()
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# MATERIALS
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
myModel.Material(name='Diamond')
myModel.materials['Diamond'].Density(table=((1.0, ), ))
myModel.materials['Diamond'].Elastic(temperatureDependency=False,table=((1070.000000, 0.070000), ))
myModel.Material(name='Material_1')
myModel.materials['Material_1'].Density(table=((1.0, ), ))
myModel.materials['Material_1'].Elastic(temperatureDependency=False,table=((165.000000, 0.280000), ))
myModel.Material(name='Material_2')
myModel.materials['Material_2'].Density(table=((1.0, ), ))
myModel.materials['Material_2'].Elastic(temperatureDependency=False,table=((60.000000, 0.300000), ))
myModel.Material(name='Material_3')
myModel.materials['Material_3'].Density(table=((1.0, ), ))
myModel.materials['Material_3'].Elastic(temperatureDependency=False,table=((60.000000, 0.300000), ))
myModel.Material(name='Material_4')
myModel.materials['Material_4'].Density(table=((1.0, ), ))
myModel.materials['Material_4'].Elastic(temperatureDependency=False,table=((60.000000, 0.300000), ))
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# SECTIONS
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
mySection = myModel.HomogeneousSolidSection(name='Section_indenter',material='Diamond')
mySection = myModel.HomogeneousSolidSection(name='Section_material_1',material='Material_1')
mySection = myModel.HomogeneousSolidSection(name='Section_material_2',material='Material_2')
mySection = myModel.HomogeneousSolidSection(name='Section_material_3',material='Material_3')
mySection = myModel.HomogeneousSolidSection(name='Section_material_4',material='Material_4')
myModel.rootAssembly.regenerate()
p = myModel.parts['Film_4']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = myModel.parts['Film_4']
f = p.faces
faces = f.findAt(((1500.000000, -250.000000, 0.0), ))
region = p.Set(faces=faces, name='Set_1')
p = myModel.parts['Film_4']
p.SectionAssignment(region=region, sectionName='Section_material_4', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)
p = myModel.parts['Film_3']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = myModel.parts['Film_3']
f = p.faces
faces = f.findAt(((1500.000000, -750.000000, 0.0), ))
region = p.Set(faces=faces, name='Set_1')
p = myModel.parts['Film_3']
p.SectionAssignment(region=region, sectionName='Section_material_3', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)
p = myModel.parts['Film_2']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = myModel.parts['Film_2']
f = p.faces
faces = f.findAt(((1500.000000, -1250.000000, 0.0), ))
region = p.Set(faces=faces, name='Set_1')
p = myModel.parts['Film_2']
p.SectionAssignment(region=region, sectionName='Section_material_2', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)
p = myModel.parts['Film_1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p = myModel.parts['Film_1']
f = p.faces
faces = f.findAt(((1500.000000, -2000.000000, 0.0), ))
region = p.Set(faces=faces, name='Set_1')
p = myModel.parts['Film_1']
p.SectionAssignment(region=region, sectionName='Section_material_1', offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ASSEMBLY
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
myAssembly = myModel.rootAssembly
p = myModel.parts['Film_1']
myAssembly.Instance(name='Film_1', part=p, dependent=OFF)
myAssembly = myModel.rootAssembly
p = myModel.parts['Film_2']
myAssembly.Instance(name='Film_2', part=p, dependent=OFF)
myAssembly = myModel.rootAssembly
p = myModel.parts['Film_3']
myAssembly.Instance(name='Film_3', part=p, dependent=OFF)
myAssembly = myModel.rootAssembly
p = myModel.parts['Film_4']
myAssembly.Instance(name='Film_4', part=p, dependent=OFF)
myAssembly = myModel.rootAssembly
p = myModel.parts[indenter_used]
myAssembly.Instance(name=indenter_used, part=p, dependent=OFF)
myAssembly = myModel.rootAssembly
myAssembly.regenerate()
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# STEPS
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
session.viewports['Viewport: 1'].setValues(displayedObject=myAssembly)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
myModel.StaticStep(name=step_Load, previous='Initial', description='Indentation step', maxNumInc=100000, initialInc=0.0001, minInc=1e-30, maxInc=0.02)
myModel.steps[step_Load].setValues(nlgeom=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step=step_Load)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# MESH
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(meshTechnique=ON)
a = myModel.rootAssembly
e1 = a.instances['Film_4'].edges
pickedEdges = e1.findAt(((0.0, -250.000000, 0.0), ))
a.seedEdgeByNumber(edges=pickedEdges, number=int(20.000000), constraint=FINER)
pickedEdges = e1.findAt(((3000.000000, -250.000000, 0.0), ))
a.seedEdgeByNumber(edges=pickedEdges, number=int(20.000000), constraint=FINER)
pickedEdges = e1.findAt(((1500.000000, 0.000000, 0.0), ))
a.seedEdgeByNumber(edges=pickedEdges, number=int(120.000000), constraint=FINER)
f = a.instances['Film_4'].faces
pickedRegions = f.findAt(((1500.000000, -250.000000, 0.0), ))
a.setMeshControls(regions=pickedRegions, elemShape=QUAD_DOMINATED)
e2 = a.instances['Film_3'].edges
pickedEdges = e2.findAt(((0.0, -750.000000, 0.0), ))
a.seedEdgeByNumber(edges=pickedEdges, number=int(20.000000), constraint=FINER)
pickedEdges = e2.findAt(((3000.000000, -750.000000, 0.0), ))
a.seedEdgeByNumber(edges=pickedEdges, number=int(20.000000), constraint=FINER)
pickedEdges = e2.findAt(((1500.000000, -500.000000, 0.0), ))
a.seedEdgeByNumber(edges=pickedEdges, number=int(120.000000), constraint=FINER)
f = a.instances['Film_3'].faces
pickedRegions = f.findAt(((1500.000000, -750.000000, 0.0), ))
a.setMeshControls(regions=pickedRegions, elemShape=QUAD_DOMINATED)
e3 = a.instances['Film_2'].edges
pickedEdges = e3.findAt(((0.0, -1250.000000, 0.0), ))
a.seedEdgeByNumber(edges=pickedEdges, number=int(20.000000), constraint=FINER)
pickedEdges = e3.findAt(((3000.000000, -1250.000000, 0.0), ))
a.seedEdgeByNumber(edges=pickedEdges, number=int(20.000000), constraint=FINER)
pickedEdges = e3.findAt(((1500.000000, -1000.000000, 0.0), ))
a.seedEdgeByNumber(edges=pickedEdges, number=int(120.000000), constraint=FINER)
f = a.instances['Film_2'].faces
pickedRegions = f.findAt(((1500.000000, -1250.000000, 0.0), ))
a.setMeshControls(regions=pickedRegions, elemShape=QUAD_DOMINATED)
e4 = a.instances['Film_1'].edges
pickedEdges = e4.findAt(((0.0, -2000.000000, 0.0), ))
a.seedEdgeByNumber(edges=pickedEdges, number=int(40.000000), constraint=FINER)
pickedEdges = e4.findAt(((3000.000000, -2000.000000, 0.0), ))
a.seedEdgeByNumber(edges=pickedEdges, number=int(40.000000), constraint=FINER)
pickedEdges = e4.findAt(((1500.000000, -1500.000000, 0.0), ))
a.seedEdgeByNumber(edges=pickedEdges, number=int(120.000000), constraint=FINER)
f = a.instances['Film_1'].faces
pickedRegions = f.findAt(((1500.000000, -2000.000000, 0.0), ))
a.setMeshControls(regions=pickedRegions, elemShape=QUAD_DOMINATED)
pickedEdges = e4.findAt(((1500.000000, -2500.000000, 0.0), ))
a.seedEdgeByNumber(edges=pickedEdges, number=int(120.000000), constraint=FINER)
partInstances =(a.instances['Film_1'], )
a.generateMesh(regions=partInstances)
partInstances =(a.instances['Film_2'], )
a.generateMesh(regions=partInstances)
partInstances =(a.instances['Film_3'], )
a.generateMesh(regions=partInstances)
partInstances =(a.instances['Film_4'], )
a.generateMesh(regions=partInstances)
elemType1 = mesh.ElemType(elemCode=CAX8R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=CAX6M, elemLibrary=STANDARD)
f = a.instances['Film_4'].faces
faces = f.findAt(((1500.000000, -250.000000, 0.0), ))
pickedRegions =(faces, )
a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
f = a.instances['Film_3'].faces
faces = f.findAt(((1500.000000, -750.000000, 0.0), ))
pickedRegions =(faces, )
a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
f = a.instances['Film_2'].faces
faces = f.findAt(((1500.000000, -1250.000000, 0.0), ))
pickedRegions =(faces, )
a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
f = a.instances['Film_1'].faces
faces = f.findAt(((1500.000000, -2000.000000, 0.0), ))
pickedRegions =(faces, )
a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# INTERACTIONS INDENTER-FILM
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
myModel.ContactProperty('Indenter-Film')
myModel.interactionProperties['Indenter-Film'].TangentialBehavior(formulation=FRICTIONLESS)
myModel.interactionProperties['Indenter-Film'].NormalBehavior(pressureOverclosure=HARD, allowSeparation=OFF, constraintEnforcementMethod=DEFAULT)
a = myModel.rootAssembly
s1 = a.instances[indenter_used].edges
side2Edges1 = s1.findAt(((0.542862, 0.094159, 0.0), ))
region1=regionToolset.Region(side2Edges=side2Edges1)
s1 = a.instances['Film_4'].edges
side1Edges1 = s1.findAt(((1500.000000, 0.0, 0.0), ))
region2=regionToolset.Region(side1Edges=side1Edges1)
myModel.SurfaceToSurfaceContactStd(name='Interaction_Indenter-Film', createStepName=step_Load, master=region1, slave=region2, sliding=FINITE, thickness=ON, interactionProperty='Indenter-Film', adjustMethod=NONE, initialClearance=OMIT, datumAxis=None, clearanceRegion=None)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# INTERACTIONS FILM-FILM
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
myModel.ContactProperty('Film-Film')
myModel.interactionProperties['Film-Film'].TangentialBehavior(formulation=ROUGH)
myModel.interactionProperties['Film-Film'].NormalBehavior(pressureOverclosure=HARD, allowSeparation=OFF, constraintEnforcementMethod=DEFAULT)
a = myModel.rootAssembly
region1=a.instances['Film_4'].surfaces['Surf-Bottom']
region2=a.instances['Film_3'].surfaces['Surf-Top']
myModel.SurfaceToSurfaceContactStd(name='Interaction_Film4-Film3', createStepName=step_Load, master=region1, slave=region2, sliding=FINITE, thickness=ON, interactionProperty='Film-Film', adjustMethod=NONE, initialClearance=OMIT, datumAxis=None, clearanceRegion=None)
a = myModel.rootAssembly
region1=a.instances['Film_3'].surfaces['Surf-Bottom']
region2=a.instances['Film_2'].surfaces['Surf-Top']
myModel.SurfaceToSurfaceContactStd(name='Interaction_Film3-Film2', createStepName=step_Load, master=region1, slave=region2, sliding=FINITE, thickness=ON, interactionProperty='Film-Film', adjustMethod=NONE, initialClearance=OMIT, datumAxis=None, clearanceRegion=None)
a = myModel.rootAssembly
region1=a.instances['Film_2'].surfaces['Surf-Bottom']
region2=a.instances['Film_1'].surfaces['Surf-Top']
myModel.SurfaceToSurfaceContactStd(name='Interaction_Film2-Film1', createStepName=step_Load, master=region1, slave=region2, sliding=FINITE, thickness=ON, interactionProperty='Film-Film', adjustMethod=NONE, initialClearance=OMIT, datumAxis=None, clearanceRegion=None)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# BOUNDARIES CONDITIONS
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, predefinedFields=ON, interactions=OFF, constraints=OFF, connectors=ON, engineeringFeatures=OFF)
a = myModel.rootAssembly
e1 = a.instances['Film_4'].edges
edges1 = e1.findAt(((0.0, -250.000000, 0.0), ))
region = regionToolset.Region(edges=edges1)
myModel.DisplacementBC(name='BC_Film_4', createStepName=step_Load, region=region, u1=0.0, u2=UNSET, ur3=UNSET, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=None)
e1 = a.instances['Film_3'].edges
edges1 = e1.findAt(((0.0, -750.000000, 0.0), ))
region = regionToolset.Region(edges=edges1)
myModel.DisplacementBC(name='BC_Film_3', createStepName=step_Load, region=region, u1=0.0, u2=UNSET, ur3=UNSET, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=None)
e1 = a.instances['Film_2'].edges
edges1 = e1.findAt(((0.0, -1250.000000, 0.0), ))
region = regionToolset.Region(edges=edges1)
myModel.DisplacementBC(name='BC_Film_2', createStepName=step_Load, region=region, u1=0.0, u2=UNSET, ur3=UNSET, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=None)
e1 = a.instances['Film_1'].edges
edges1 = e1.findAt(((0.0, -2000.000000, 0.0), ))
region = regionToolset.Region(edges=edges1)
myModel.DisplacementBC(name='BC_Film_1', createStepName=step_Load, region=region, u1=0.0, u2=UNSET, ur3=UNSET, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=None)
e1 = a.instances['Film_1'].edges
edges1 = e1.findAt(((1500.000000, -2500.000000, 0.0), ))
region = regionToolset.Region(edges=edges1)
myModel.DisplacementBC(name='BC_Film_1_2', createStepName=step_Load, region=region, u1=0.0, u2=0.0, ur3=UNSET, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=None)
# -------------------------------------------------------------------------------------------------------------------
# Indentation displacement
r1 = a.instances[indenter_used].referencePoints
refPoints1=(r1[2], )
region = regionToolset.Region(referencePoints=refPoints1)
myModel.DisplacementBC(name='BC_Indentation_step', createStepName=step_Load, region=region, u1=0.0, u2=ind_h, ur3=0.0, amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=None)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# JOB
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, predefinedFields=OFF, connectors=OFF)
mdb.Job(name='Job1', model='multilayer_model_2015-05-26', description='Indentation of multilayer sample', type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='', multiprocessingMode=DEFAULT, numCpus=1, numDomains=2)
