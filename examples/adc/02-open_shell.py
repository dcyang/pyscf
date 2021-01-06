#!/usr/bin/env python

'''
IP/EA-UADC calculations for open-shell OH
'''

from pyscf import gto, scf, adc

mol = gto.Mole()
r = 0.969286393
mol.atom = [
    ['O', ( 0., 0.    , -r/2   )],
    ['H', ( 0., 0.    ,  r/2)],]
mol.basis = {'O':'aug-cc-pvdz',
             'H':'aug-cc-pvdz'}
mol.verbose = 0
mol.symmetry = False
mol.spin  = 1
mol.build()

mf = scf.UHF(mol)
mf.conv_tol = 1e-12
mf.kernel()

myadc = adc.ADC(mf)

#IP-UADC(2) for 4 roots
myadc.verbose = 4
eip,vip,pip,xip_a,xip_b = myadc.kernel(nroots=4)

#IP-UADC(2)-x for 4 roots
myadc.method = "adc(2)-x"
myadc.method_type = "ip"
eip,vip,pip,xip_a,xip_b = myadc.kernel(nroots=4)

#EA-UADC(3) for 4 roots
myadc.method = "adc(3)"
myadc.method_type = "ea"
eea,vea,pea,xea_a,xea_b = myadc.kernel(nroots=4)
myadc.analyze()
