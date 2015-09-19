## -*- encoding: utf-8 -*-
# This file was *autogenerated* from the file civil.sagetex.sage
from sage.all_cmdline import *   # import sage library
_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_8 = Integer(8); _sage_const_88 = Integer(88); _sage_const_89 = Integer(89); _sage_const_85 = Integer(85); _sage_const_86 = Integer(86); _sage_const_87 = Integer(87); _sage_const_80 = Integer(80); _sage_const_82 = Integer(82); _sage_const_12 = Integer(12); _sage_const_14 = Integer(14); _sage_const_18 = Integer(18); _sage_const_100 = Integer(100); _sage_const_92 = Integer(92); _sage_const_91 = Integer(91); _sage_const_90 = Integer(90)## This file (civil.sagetex.sage) was *autogenerated* from civil.tex with sagetex.sty version 2012/01/16 v2.3.3-69dcb0eb93de.
import sagetex
_st_ = sagetex.SageTeXProcessor('civil', version='2012/01/16 v2.3.3-69dcb0eb93de', version_check=True)
_st_.blockbegin()
try:
  load('input.sage')
  latex.matrix_delimiters("[","]")
  '''for storey_i in range(Number_of_storeys):
   Stiffness_matrix(storey_i, storey_i) = Stiffness_storey(storey_i)
   if (storey_i < Number_of_storeys ):
   Stiffness_matrix(storey_i, storey_i) = Stiffness_matrix(storey_i, storey_i) + Stiffness_storey(storey_i + 1)
   Stiffness_matrix(storey_i, storey_i + 1) = - Stiffness_storey(storey_i + 1)
   Stiffness_matrix(storey_i + 1, storey_i) = Stiffness_matrix(storey_i, storey_i + 1)
  '''
 
 
  Stiffness_matrix=matrix([[_sage_const_18 ,-_sage_const_8 ,_sage_const_0 ,_sage_const_0 ],[-_sage_const_8 ,_sage_const_14 ,-_sage_const_6 ,_sage_const_0 ],[_sage_const_0 ,-_sage_const_6 ,_sage_const_12 ,-_sage_const_6 ],[_sage_const_0 ,_sage_const_0 ,-_sage_const_6 ,_sage_const_6 ]])
  w=var('w')
  q=Stiffness_matrix-(w**_sage_const_2 )*Mass
  A=Stiffness_matrix*Mass.inverse()
  Omega_square=A.eigenvalues()
  Time_period=list()
  for i in range( Number_of_storeys):
   q=sqrt(Omega_square[i])
   Time_period.append(n(_sage_const_2 *pi)/q)
  Frequency=list()
  for storey_i in range(Number_of_storeys):
   Frequency.append(sqrt(Omega_square[storey_i]))
  z=A.eigenvectors_left()
  J=list()
  for x in range(Number_of_storeys):
   q=matrix(z[x][_sage_const_1 ][_sage_const_0 ])
   J.append(q*Mass*q.transpose())
  X=list()
  for x in range(Number_of_storeys):
   q=matrix(z[x][_sage_const_1 ][_sage_const_0 ])
   X.append(q/sqrt(abs(J[x])))
  Modal_participation_factor=list()
  Modal_mass=list()
  sum_modal_mass=_sage_const_0 
  for j in range(Number_of_storeys):
         P1,P2=_sage_const_0 ,_sage_const_0 
         m=matrix(X[j])
         for i in range(Number_of_storeys):
             P1=P1+Mass[i][i]*m[_sage_const_0 ][i]
             P2=P2+Mass[i][i]*(m[_sage_const_0 ][i])**_sage_const_2 
         Modal_participation_factor.append(P1/P2)
         Modal_mass.append((P1)**_sage_const_2 /(P2))
         sum_modal_mass = sum_modal_mass + Modal_mass[j]
  print(sum_modal_mass)
  Modal_contribution=list()
  for i in range(Number_of_storeys):
   Modal_contribution.append(_sage_const_100  / sum_modal_mass *Modal_mass[i])
 
 
 
 
 
except:
 _st_.goboom(_sage_const_80 )
_st_.blockend()
try:
 _st_.inline(_sage_const_0 , latex(q))
except:
 _st_.goboom(_sage_const_82 )
try:
 _st_.inline(_sage_const_1 , latex(Stiffness_matrix))
except:
 _st_.goboom(_sage_const_85 )
try:
 _st_.inline(_sage_const_2 , latex(Mass))
except:
 _st_.goboom(_sage_const_86 )
try:
 _st_.inline(_sage_const_3 , latex(Omega_square))
except:
 _st_.goboom(_sage_const_87 )
try:
 _st_.inline(_sage_const_4 , latex(Time_period))
except:
 _st_.goboom(_sage_const_88 )
try:
 _st_.inline(_sage_const_5 , latex(X))
except:
 _st_.goboom(_sage_const_89 )
try:
 _st_.inline(_sage_const_6 , latex(Modal_participation_factor))
except:
 _st_.goboom(_sage_const_90 )
try:
 _st_.inline(_sage_const_7 , latex(Modal_mass))
except:
 _st_.goboom(_sage_const_91 )
try:
 _st_.inline(_sage_const_8 , latex(Modal_contribution))
except:
 _st_.goboom(_sage_const_92 )
_st_.endofdoc()
