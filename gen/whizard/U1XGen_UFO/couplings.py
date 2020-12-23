# This file was automatically created by FeynRules 2.3.32
# Mathematica version: 9.0 for Linux x86 (64-bit) (November 20, 2012)
# Date: Thu 27 Dec 2018 15:48:58


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '-G',
                order = {'QCD':1})

GC_7 = Coupling(name = 'GC_7',
                value = 'complex(0,1)*G',
                order = {'QCD':1})

GC_8 = Coupling(name = 'GC_8',
                value = 'complex(0,1)*G**2',
                order = {'QCD':2})

GC_9 = Coupling(name = 'GC_9',
                value = '-(b1*Cp*complex(0,1)*g1p)',
                order = {'QED':1})

GC_10 = Coupling(name = 'GC_10',
                 value = '-6*Ca**3*complex(0,1)*lam1*Sa + 3*Ca**3*complex(0,1)*lam3*Sa + 6*Ca*complex(0,1)*lam2*Sa**3 - 3*Ca*complex(0,1)*lam3*Sa**3',
                 order = {'QED':2})

GC_11 = Coupling(name = 'GC_11',
                 value = '6*Ca**3*complex(0,1)*lam2*Sa - 3*Ca**3*complex(0,1)*lam3*Sa - 6*Ca*complex(0,1)*lam1*Sa**3 + 3*Ca*complex(0,1)*lam3*Sa**3',
                 order = {'QED':2})

GC_12 = Coupling(name = 'GC_12',
                 value = '-6*Ca**4*complex(0,1)*lam2 - 6*Ca**2*complex(0,1)*lam3*Sa**2 - 6*complex(0,1)*lam1*Sa**4',
                 order = {'QED':2})

GC_13 = Coupling(name = 'GC_13',
                 value = '-6*Ca**4*complex(0,1)*lam1 - 6*Ca**2*complex(0,1)*lam3*Sa**2 - 6*complex(0,1)*lam2*Sa**4',
                 order = {'QED':2})

GC_14 = Coupling(name = 'GC_14',
                 value = '-(Ca**4*complex(0,1)*lam3) - 6*Ca**2*complex(0,1)*lam1*Sa**2 - 6*Ca**2*complex(0,1)*lam2*Sa**2 + 4*Ca**2*complex(0,1)*lam3*Sa**2 - complex(0,1)*lam3*Sa**4',
                 order = {'QED':2})

GC_15 = Coupling(name = 'GC_15',
                 value = '2*Ca*cg*complex(0,1)*lam1*Sa*sg + 2*Ca*cg*complex(0,1)*lam2*Sa*sg - 2*Ca*cg*complex(0,1)*lam3*Sa*sg',
                 order = {'QED':2})

GC_16 = Coupling(name = 'GC_16',
                 value = '-2*Ca**2*cg*complex(0,1)*lam2*sg + Ca**2*cg*complex(0,1)*lam3*sg + 2*cg*complex(0,1)*lam1*Sa**2*sg - cg*complex(0,1)*lam3*Sa**2*sg',
                 order = {'QED':2})

GC_17 = Coupling(name = 'GC_17',
                 value = '2*Ca**2*cg*complex(0,1)*lam1*sg - Ca**2*cg*complex(0,1)*lam3*sg - 2*cg*complex(0,1)*lam2*Sa**2*sg + cg*complex(0,1)*lam3*Sa**2*sg',
                 order = {'QED':2})

GC_18 = Coupling(name = 'GC_18',
                 value = '-2*Ca*cg**2*complex(0,1)*lam1*Sa + Ca*cg**2*complex(0,1)*lam3*Sa + 2*Ca*complex(0,1)*lam2*Sa*sg**2 - Ca*complex(0,1)*lam3*Sa*sg**2',
                 order = {'QED':2})

GC_19 = Coupling(name = 'GC_19',
                 value = '2*Ca*cg**2*complex(0,1)*lam2*Sa - Ca*cg**2*complex(0,1)*lam3*Sa - 2*Ca*complex(0,1)*lam1*Sa*sg**2 + Ca*complex(0,1)*lam3*Sa*sg**2',
                 order = {'QED':2})

GC_20 = Coupling(name = 'GC_20',
                 value = '-2*Ca**2*cg**2*complex(0,1)*lam2 - cg**2*complex(0,1)*lam3*Sa**2 - Ca**2*complex(0,1)*lam3*sg**2 - 2*complex(0,1)*lam1*Sa**2*sg**2',
                 order = {'QED':2})

GC_21 = Coupling(name = 'GC_21',
                 value = '-2*Ca**2*cg**2*complex(0,1)*lam1 - cg**2*complex(0,1)*lam3*Sa**2 - Ca**2*complex(0,1)*lam3*sg**2 - 2*complex(0,1)*lam2*Sa**2*sg**2',
                 order = {'QED':2})

GC_22 = Coupling(name = 'GC_22',
                 value = '-(Ca**2*cg**2*complex(0,1)*lam3) - 2*cg**2*complex(0,1)*lam2*Sa**2 - 2*Ca**2*complex(0,1)*lam1*sg**2 - complex(0,1)*lam3*Sa**2*sg**2',
                 order = {'QED':2})

GC_23 = Coupling(name = 'GC_23',
                 value = '-(Ca**2*cg**2*complex(0,1)*lam3) - 2*cg**2*complex(0,1)*lam1*Sa**2 - 2*Ca**2*complex(0,1)*lam2*sg**2 - complex(0,1)*lam3*Sa**2*sg**2',
                 order = {'QED':2})

GC_24 = Coupling(name = 'GC_24',
                 value = '-6*cg**3*complex(0,1)*lam2*sg + 3*cg**3*complex(0,1)*lam3*sg + 6*cg*complex(0,1)*lam1*sg**3 - 3*cg*complex(0,1)*lam3*sg**3',
                 order = {'QED':2})

GC_25 = Coupling(name = 'GC_25',
                 value = '6*cg**3*complex(0,1)*lam1*sg - 3*cg**3*complex(0,1)*lam3*sg - 6*cg*complex(0,1)*lam2*sg**3 + 3*cg*complex(0,1)*lam3*sg**3',
                 order = {'QED':2})

GC_26 = Coupling(name = 'GC_26',
                 value = '-6*cg**4*complex(0,1)*lam2 - 6*cg**2*complex(0,1)*lam3*sg**2 - 6*complex(0,1)*lam1*sg**4',
                 order = {'QED':2})

GC_27 = Coupling(name = 'GC_27',
                 value = '-6*cg**4*complex(0,1)*lam1 - 6*cg**2*complex(0,1)*lam3*sg**2 - 6*complex(0,1)*lam2*sg**4',
                 order = {'QED':2})

GC_28 = Coupling(name = 'GC_28',
                 value = '-(cg**4*complex(0,1)*lam3) - 6*cg**2*complex(0,1)*lam1*sg**2 - 6*cg**2*complex(0,1)*lam2*sg**2 + 4*cg**2*complex(0,1)*lam3*sg**2 - complex(0,1)*lam3*sg**4',
                 order = {'QED':2})

GC_29 = Coupling(name = 'GC_29',
                 value = '-(b1*complex(0,1)*g1p*Sp)',
                 order = {'QED':1})

GC_30 = Coupling(name = 'GC_30',
                 value = '-((ee**2*complex(0,1))/sw**2)',
                 order = {'QED':2})

GC_31 = Coupling(name = 'GC_31',
                 value = '(Ca**2*ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_32 = Coupling(name = 'GC_32',
                 value = '(cg**2*ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_33 = Coupling(name = 'GC_33',
                 value = '(Cp**2*cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_34 = Coupling(name = 'GC_34',
                 value = '(Ca*ee**2*complex(0,1)*Sa)/(2.*sw**2)',
                 order = {'QED':2})

GC_35 = Coupling(name = 'GC_35',
                 value = '(ee**2*complex(0,1)*Sa**2)/(2.*sw**2)',
                 order = {'QED':2})

GC_36 = Coupling(name = 'GC_36',
                 value = '-(cg*ee**2*complex(0,1)*sg)/(2.*sw**2)',
                 order = {'QED':2})

GC_37 = Coupling(name = 'GC_37',
                 value = '(ee**2*complex(0,1)*sg**2)/(2.*sw**2)',
                 order = {'QED':2})

GC_38 = Coupling(name = 'GC_38',
                 value = '-((Cp*cw**2*ee**2*complex(0,1)*Sp)/sw**2)',
                 order = {'QED':2})

GC_39 = Coupling(name = 'GC_39',
                 value = '(cw**2*ee**2*complex(0,1)*Sp**2)/sw**2',
                 order = {'QED':2})

GC_40 = Coupling(name = 'GC_40',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_41 = Coupling(name = 'GC_41',
                 value = '(CKM1x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '(CKM1x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '(CKM1x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '(CKM2x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '(CKM2x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '(CKM2x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '(CKM3x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '(CKM3x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_49 = Coupling(name = 'GC_49',
                 value = '(CKM3x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_50 = Coupling(name = 'GC_50',
                 value = '(Cp*cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_51 = Coupling(name = 'GC_51',
                 value = '(-2*Cp*cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_52 = Coupling(name = 'GC_52',
                 value = '-((cw*ee*complex(0,1)*Sp)/sw)',
                 order = {'QED':1})

GC_53 = Coupling(name = 'GC_53',
                 value = '(2*cw*ee**2*complex(0,1)*Sp)/sw',
                 order = {'QED':2})

GC_54 = Coupling(name = 'GC_54',
                 value = '(a1*complex(0,1)*g1p*Sp)/6. + (b1*complex(0,1)*g1p*Sp)/3. - (Cp*cw*ee*complex(0,1))/(2.*sw) - (Cp*ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_55 = Coupling(name = 'GC_55',
                 value = '(a1*complex(0,1)*g1p*Sp)/6. + (b1*complex(0,1)*g1p*Sp)/3. + (Cp*cw*ee*complex(0,1))/(2.*sw) - (Cp*ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_56 = Coupling(name = 'GC_56',
                 value = '-(a1*complex(0,1)*g1p*Sp)/3. + (b1*complex(0,1)*g1p*Sp)/3. + (Cp*ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_57 = Coupling(name = 'GC_57',
                 value = '-(a1*complex(0,1)*g1p*Sp)/2. - b1*complex(0,1)*g1p*Sp - (Cp*cw*ee*complex(0,1))/(2.*sw) + (Cp*ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_58 = Coupling(name = 'GC_58',
                 value = '-(a1*complex(0,1)*g1p*Sp)/2. - b1*complex(0,1)*g1p*Sp + (Cp*cw*ee*complex(0,1))/(2.*sw) + (Cp*ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_59 = Coupling(name = 'GC_59',
                 value = '(2*a1*complex(0,1)*g1p*Sp)/3. + (b1*complex(0,1)*g1p*Sp)/3. - (2*Cp*ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_60 = Coupling(name = 'GC_60',
                 value = '-(a1*complex(0,1)*g1p*Sp) - b1*complex(0,1)*g1p*Sp + (Cp*ee*complex(0,1)*sw)/cw',
                 order = {'QED':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '(a1*Ca*cg*g1p*Sp)/2. - 2*b1*g1p*Sa*sg*Sp - (Ca*cg*Cp*cw*ee)/(2.*sw) - (Ca*cg*Cp*ee*sw)/(2.*cw)',
                 order = {'QED':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '(a1*cg*g1p*Sa*Sp)/2. + 2*b1*Ca*g1p*sg*Sp - (cg*Cp*cw*ee*Sa)/(2.*sw) - (cg*Cp*ee*Sa*sw)/(2.*cw)',
                 order = {'QED':1})

GC_63 = Coupling(name = 'GC_63',
                 value = '2*b1*cg*g1p*Sa*Sp + (a1*Ca*g1p*sg*Sp)/2. - (Ca*Cp*cw*ee*sg)/(2.*sw) - (Ca*Cp*ee*sg*sw)/(2.*cw)',
                 order = {'QED':1})

GC_64 = Coupling(name = 'GC_64',
                 value = '-2*b1*Ca*cg*g1p*Sp + (a1*g1p*Sa*sg*Sp)/2. - (Cp*cw*ee*Sa*sg)/(2.*sw) - (Cp*ee*Sa*sg*sw)/(2.*cw)',
                 order = {'QED':1})

GC_65 = Coupling(name = 'GC_65',
                 value = '(a1*Cp*complex(0,1)*g1p)/6. + (b1*Cp*complex(0,1)*g1p)/3. - (cw*ee*complex(0,1)*Sp)/(2.*sw) + (ee*complex(0,1)*Sp*sw)/(6.*cw)',
                 order = {'QED':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '(a1*Cp*complex(0,1)*g1p)/6. + (b1*Cp*complex(0,1)*g1p)/3. + (cw*ee*complex(0,1)*Sp)/(2.*sw) + (ee*complex(0,1)*Sp*sw)/(6.*cw)',
                 order = {'QED':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '-(a1*Cp*complex(0,1)*g1p)/3. + (b1*Cp*complex(0,1)*g1p)/3. - (ee*complex(0,1)*Sp*sw)/(3.*cw)',
                 order = {'QED':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '-(a1*Cp*complex(0,1)*g1p)/2. - b1*Cp*complex(0,1)*g1p - (cw*ee*complex(0,1)*Sp)/(2.*sw) - (ee*complex(0,1)*Sp*sw)/(2.*cw)',
                 order = {'QED':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '-(a1*Cp*complex(0,1)*g1p)/2. - b1*Cp*complex(0,1)*g1p + (cw*ee*complex(0,1)*Sp)/(2.*sw) - (ee*complex(0,1)*Sp*sw)/(2.*cw)',
                 order = {'QED':1})

GC_70 = Coupling(name = 'GC_70',
                 value = '(2*a1*Cp*complex(0,1)*g1p)/3. + (b1*Cp*complex(0,1)*g1p)/3. + (2*ee*complex(0,1)*Sp*sw)/(3.*cw)',
                 order = {'QED':1})

GC_71 = Coupling(name = 'GC_71',
                 value = '-(a1*Cp*complex(0,1)*g1p) - b1*Cp*complex(0,1)*g1p - (ee*complex(0,1)*Sp*sw)/cw',
                 order = {'QED':1})

GC_72 = Coupling(name = 'GC_72',
                 value = '(a1*Ca*cg*Cp*g1p)/2. - 2*b1*Cp*g1p*Sa*sg + (Ca*cg*cw*ee*Sp)/(2.*sw) + (Ca*cg*ee*Sp*sw)/(2.*cw)',
                 order = {'QED':1})

GC_73 = Coupling(name = 'GC_73',
                 value = '(a1*cg*Cp*g1p*Sa)/2. + 2*b1*Ca*Cp*g1p*sg + (cg*cw*ee*Sa*Sp)/(2.*sw) + (cg*ee*Sa*Sp*sw)/(2.*cw)',
                 order = {'QED':1})

GC_74 = Coupling(name = 'GC_74',
                 value = '2*b1*cg*Cp*g1p*Sa + (a1*Ca*Cp*g1p*sg)/2. + (Ca*cw*ee*sg*Sp)/(2.*sw) + (Ca*ee*sg*Sp*sw)/(2.*cw)',
                 order = {'QED':1})

GC_75 = Coupling(name = 'GC_75',
                 value = '-2*b1*Ca*cg*Cp*g1p + (a1*Cp*g1p*Sa*sg)/2. + (cw*ee*Sa*sg*Sp)/(2.*sw) + (ee*Sa*sg*Sp*sw)/(2.*cw)',
                 order = {'QED':1})

GC_76 = Coupling(name = 'GC_76',
                 value = 'Ca**2*Cp**2*ee**2*complex(0,1) + (a1**2*Ca**2*complex(0,1)*g1p**2*Sp**2)/2. + 8*b1**2*complex(0,1)*g1p**2*Sa**2*Sp**2 + (Ca**2*Cp**2*cw**2*ee**2*complex(0,1))/(2.*sw**2) - (a1*Ca**2*Cp*cw*ee*complex(0,1)*g1p*Sp)/sw - (a1*Ca**2*Cp*ee*complex(0,1)*g1p*Sp*sw)/cw + (Ca**2*Cp**2*ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_77 = Coupling(name = 'GC_77',
                 value = 'cg**2*Cp**2*ee**2*complex(0,1) + (a1**2*cg**2*complex(0,1)*g1p**2*Sp**2)/2. + 8*b1**2*complex(0,1)*g1p**2*sg**2*Sp**2 + (cg**2*Cp**2*cw**2*ee**2*complex(0,1))/(2.*sw**2) - (a1*cg**2*Cp*cw*ee*complex(0,1)*g1p*Sp)/sw - (a1*cg**2*Cp*ee*complex(0,1)*g1p*Sp*sw)/cw + (cg**2*Cp**2*ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_78 = Coupling(name = 'GC_78',
                 value = 'Ca*Cp**2*ee**2*complex(0,1)*Sa + (a1**2*Ca*complex(0,1)*g1p**2*Sa*Sp**2)/2. - 8*b1**2*Ca*complex(0,1)*g1p**2*Sa*Sp**2 + (Ca*Cp**2*cw**2*ee**2*complex(0,1)*Sa)/(2.*sw**2) - (a1*Ca*Cp*cw*ee*complex(0,1)*g1p*Sa*Sp)/sw - (a1*Ca*Cp*ee*complex(0,1)*g1p*Sa*Sp*sw)/cw + (Ca*Cp**2*ee**2*complex(0,1)*Sa*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_79 = Coupling(name = 'GC_79',
                 value = 'Cp**2*ee**2*complex(0,1)*Sa**2 + 8*b1**2*Ca**2*complex(0,1)*g1p**2*Sp**2 + (a1**2*complex(0,1)*g1p**2*Sa**2*Sp**2)/2. + (Cp**2*cw**2*ee**2*complex(0,1)*Sa**2)/(2.*sw**2) - (a1*Cp*cw*ee*complex(0,1)*g1p*Sa**2*Sp)/sw - (a1*Cp*ee*complex(0,1)*g1p*Sa**2*Sp*sw)/cw + (Cp**2*ee**2*complex(0,1)*Sa**2*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_80 = Coupling(name = 'GC_80',
                 value = '-(cg*Cp**2*ee**2*complex(0,1)*sg) - (a1**2*cg*complex(0,1)*g1p**2*sg*Sp**2)/2. + 8*b1**2*cg*complex(0,1)*g1p**2*sg*Sp**2 - (cg*Cp**2*cw**2*ee**2*complex(0,1)*sg)/(2.*sw**2) + (a1*cg*Cp*cw*ee*complex(0,1)*g1p*sg*Sp)/sw + (a1*cg*Cp*ee*complex(0,1)*g1p*sg*Sp*sw)/cw - (cg*Cp**2*ee**2*complex(0,1)*sg*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_81 = Coupling(name = 'GC_81',
                 value = 'Cp**2*ee**2*complex(0,1)*sg**2 + 8*b1**2*cg**2*complex(0,1)*g1p**2*Sp**2 + (a1**2*complex(0,1)*g1p**2*sg**2*Sp**2)/2. + (Cp**2*cw**2*ee**2*complex(0,1)*sg**2)/(2.*sw**2) - (a1*Cp*cw*ee*complex(0,1)*g1p*sg**2*Sp)/sw - (a1*Cp*ee*complex(0,1)*g1p*sg**2*Sp*sw)/cw + (Cp**2*ee**2*complex(0,1)*sg**2*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_82 = Coupling(name = 'GC_82',
                 value = '-(Ca**2*Cp*ee**2*complex(0,1)*Sp) + (a1**2*Ca**2*Cp*complex(0,1)*g1p**2*Sp)/2. + 8*b1**2*Cp*complex(0,1)*g1p**2*Sa**2*Sp - (Ca**2*Cp*cw**2*ee**2*complex(0,1)*Sp)/(2.*sw**2) - (a1*Ca**2*Cp**2*cw*ee*complex(0,1)*g1p)/(2.*sw) + (a1*Ca**2*cw*ee*complex(0,1)*g1p*Sp**2)/(2.*sw) - (a1*Ca**2*Cp**2*ee*complex(0,1)*g1p*sw)/(2.*cw) + (a1*Ca**2*ee*complex(0,1)*g1p*Sp**2*sw)/(2.*cw) - (Ca**2*Cp*ee**2*complex(0,1)*Sp*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_83 = Coupling(name = 'GC_83',
                 value = '-(cg**2*Cp*ee**2*complex(0,1)*Sp) + (a1**2*cg**2*Cp*complex(0,1)*g1p**2*Sp)/2. + 8*b1**2*Cp*complex(0,1)*g1p**2*sg**2*Sp - (cg**2*Cp*cw**2*ee**2*complex(0,1)*Sp)/(2.*sw**2) - (a1*cg**2*Cp**2*cw*ee*complex(0,1)*g1p)/(2.*sw) + (a1*cg**2*cw*ee*complex(0,1)*g1p*Sp**2)/(2.*sw) - (a1*cg**2*Cp**2*ee*complex(0,1)*g1p*sw)/(2.*cw) + (a1*cg**2*ee*complex(0,1)*g1p*Sp**2*sw)/(2.*cw) - (cg**2*Cp*ee**2*complex(0,1)*Sp*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_84 = Coupling(name = 'GC_84',
                 value = '-(Ca*Cp*ee**2*complex(0,1)*Sa*Sp) + (a1**2*Ca*Cp*complex(0,1)*g1p**2*Sa*Sp)/2. - 8*b1**2*Ca*Cp*complex(0,1)*g1p**2*Sa*Sp - (Ca*Cp*cw**2*ee**2*complex(0,1)*Sa*Sp)/(2.*sw**2) - (a1*Ca*Cp**2*cw*ee*complex(0,1)*g1p*Sa)/(2.*sw) + (a1*Ca*cw*ee*complex(0,1)*g1p*Sa*Sp**2)/(2.*sw) - (a1*Ca*Cp**2*ee*complex(0,1)*g1p*Sa*sw)/(2.*cw) + (a1*Ca*ee*complex(0,1)*g1p*Sa*Sp**2*sw)/(2.*cw) - (Ca*Cp*ee**2*complex(0,1)*Sa*Sp*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_85 = Coupling(name = 'GC_85',
                 value = '8*b1**2*Ca**2*Cp*complex(0,1)*g1p**2*Sp - Cp*ee**2*complex(0,1)*Sa**2*Sp + (a1**2*Cp*complex(0,1)*g1p**2*Sa**2*Sp)/2. - (Cp*cw**2*ee**2*complex(0,1)*Sa**2*Sp)/(2.*sw**2) - (a1*Cp**2*cw*ee*complex(0,1)*g1p*Sa**2)/(2.*sw) + (a1*cw*ee*complex(0,1)*g1p*Sa**2*Sp**2)/(2.*sw) - (a1*Cp**2*ee*complex(0,1)*g1p*Sa**2*sw)/(2.*cw) + (a1*ee*complex(0,1)*g1p*Sa**2*Sp**2*sw)/(2.*cw) - (Cp*ee**2*complex(0,1)*Sa**2*Sp*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_86 = Coupling(name = 'GC_86',
                 value = 'cg*Cp*ee**2*complex(0,1)*sg*Sp - (a1**2*cg*Cp*complex(0,1)*g1p**2*sg*Sp)/2. + 8*b1**2*cg*Cp*complex(0,1)*g1p**2*sg*Sp + (cg*Cp*cw**2*ee**2*complex(0,1)*sg*Sp)/(2.*sw**2) + (a1*cg*Cp**2*cw*ee*complex(0,1)*g1p*sg)/(2.*sw) - (a1*cg*cw*ee*complex(0,1)*g1p*sg*Sp**2)/(2.*sw) + (a1*cg*Cp**2*ee*complex(0,1)*g1p*sg*sw)/(2.*cw) - (a1*cg*ee*complex(0,1)*g1p*sg*Sp**2*sw)/(2.*cw) + (cg*Cp*ee**2*complex(0,1)*sg*Sp*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_87 = Coupling(name = 'GC_87',
                 value = '8*b1**2*cg**2*Cp*complex(0,1)*g1p**2*Sp - Cp*ee**2*complex(0,1)*sg**2*Sp + (a1**2*Cp*complex(0,1)*g1p**2*sg**2*Sp)/2. - (Cp*cw**2*ee**2*complex(0,1)*sg**2*Sp)/(2.*sw**2) - (a1*Cp**2*cw*ee*complex(0,1)*g1p*sg**2)/(2.*sw) + (a1*cw*ee*complex(0,1)*g1p*sg**2*Sp**2)/(2.*sw) - (a1*Cp**2*ee*complex(0,1)*g1p*sg**2*sw)/(2.*cw) + (a1*ee*complex(0,1)*g1p*sg**2*Sp**2*sw)/(2.*cw) - (Cp*ee**2*complex(0,1)*sg**2*Sp*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_88 = Coupling(name = 'GC_88',
                 value = '(a1**2*Ca**2*Cp**2*complex(0,1)*g1p**2)/2. + 8*b1**2*Cp**2*complex(0,1)*g1p**2*Sa**2 + Ca**2*ee**2*complex(0,1)*Sp**2 + (Ca**2*cw**2*ee**2*complex(0,1)*Sp**2)/(2.*sw**2) + (a1*Ca**2*Cp*cw*ee*complex(0,1)*g1p*Sp)/sw + (a1*Ca**2*Cp*ee*complex(0,1)*g1p*Sp*sw)/cw + (Ca**2*ee**2*complex(0,1)*Sp**2*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_89 = Coupling(name = 'GC_89',
                 value = '(a1**2*cg**2*Cp**2*complex(0,1)*g1p**2)/2. + 8*b1**2*Cp**2*complex(0,1)*g1p**2*sg**2 + cg**2*ee**2*complex(0,1)*Sp**2 + (cg**2*cw**2*ee**2*complex(0,1)*Sp**2)/(2.*sw**2) + (a1*cg**2*Cp*cw*ee*complex(0,1)*g1p*Sp)/sw + (a1*cg**2*Cp*ee*complex(0,1)*g1p*Sp*sw)/cw + (cg**2*ee**2*complex(0,1)*Sp**2*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_90 = Coupling(name = 'GC_90',
                 value = '(a1**2*Ca*Cp**2*complex(0,1)*g1p**2*Sa)/2. - 8*b1**2*Ca*Cp**2*complex(0,1)*g1p**2*Sa + Ca*ee**2*complex(0,1)*Sa*Sp**2 + (Ca*cw**2*ee**2*complex(0,1)*Sa*Sp**2)/(2.*sw**2) + (a1*Ca*Cp*cw*ee*complex(0,1)*g1p*Sa*Sp)/sw + (a1*Ca*Cp*ee*complex(0,1)*g1p*Sa*Sp*sw)/cw + (Ca*ee**2*complex(0,1)*Sa*Sp**2*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_91 = Coupling(name = 'GC_91',
                 value = '8*b1**2*Ca**2*Cp**2*complex(0,1)*g1p**2 + (a1**2*Cp**2*complex(0,1)*g1p**2*Sa**2)/2. + ee**2*complex(0,1)*Sa**2*Sp**2 + (cw**2*ee**2*complex(0,1)*Sa**2*Sp**2)/(2.*sw**2) + (a1*Cp*cw*ee*complex(0,1)*g1p*Sa**2*Sp)/sw + (a1*Cp*ee*complex(0,1)*g1p*Sa**2*Sp*sw)/cw + (ee**2*complex(0,1)*Sa**2*Sp**2*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_92 = Coupling(name = 'GC_92',
                 value = '-(a1**2*cg*Cp**2*complex(0,1)*g1p**2*sg)/2. + 8*b1**2*cg*Cp**2*complex(0,1)*g1p**2*sg - cg*ee**2*complex(0,1)*sg*Sp**2 - (cg*cw**2*ee**2*complex(0,1)*sg*Sp**2)/(2.*sw**2) - (a1*cg*Cp*cw*ee*complex(0,1)*g1p*sg*Sp)/sw - (a1*cg*Cp*ee*complex(0,1)*g1p*sg*Sp*sw)/cw - (cg*ee**2*complex(0,1)*sg*Sp**2*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_93 = Coupling(name = 'GC_93',
                 value = '8*b1**2*cg**2*Cp**2*complex(0,1)*g1p**2 + (a1**2*Cp**2*complex(0,1)*g1p**2*sg**2)/2. + ee**2*complex(0,1)*sg**2*Sp**2 + (cw**2*ee**2*complex(0,1)*sg**2*Sp**2)/(2.*sw**2) + (a1*Cp*cw*ee*complex(0,1)*g1p*sg**2*Sp)/sw + (a1*Cp*ee*complex(0,1)*g1p*sg**2*Sp*sw)/cw + (ee**2*complex(0,1)*sg**2*Sp**2*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_94 = Coupling(name = 'GC_94',
                 value = '(Ca*ee**2*complex(0,1)*vev)/(2.*sw**2)',
                 order = {'QED':1})

GC_95 = Coupling(name = 'GC_95',
                 value = '(ee**2*complex(0,1)*Sa*vev)/(2.*sw**2)',
                 order = {'QED':1})

GC_96 = Coupling(name = 'GC_96',
                 value = '(ee*complex(0,1)*VNl1x1)/(2.*sw)',
                 order = {'QED':1})

GC_97 = Coupling(name = 'GC_97',
                 value = '-(Ca*ee*complex(0,1)*MN1*VNl1x1)/(2.*MW*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_98 = Coupling(name = 'GC_98',
                 value = '-(ee*complex(0,1)*MN1*Sa*VNl1x1)/(2.*MW*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_99 = Coupling(name = 'GC_99',
                 value = '-(a1*complex(0,1)*g1p*Sp*VNl1x1)/(2.*cmath.sqrt(2)) - (b1*complex(0,1)*g1p*Sp*VNl1x1)/cmath.sqrt(2) + (Cp*cw*ee*complex(0,1)*VNl1x1)/(2.*sw*cmath.sqrt(2)) + (Cp*ee*complex(0,1)*sw*VNl1x1)/(2.*cw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_100 = Coupling(name = 'GC_100',
                  value = '-(a1*Cp*complex(0,1)*g1p*VNl1x1)/(2.*cmath.sqrt(2)) - (b1*Cp*complex(0,1)*g1p*VNl1x1)/cmath.sqrt(2) - (cw*ee*complex(0,1)*Sp*VNl1x1)/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*Sp*sw*VNl1x1)/(2.*cw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_101 = Coupling(name = 'GC_101',
                  value = '(ee*complex(0,1)*VNl1x2)/(2.*sw)',
                  order = {'QED':1})

GC_102 = Coupling(name = 'GC_102',
                  value = '-(Ca*ee*complex(0,1)*MN1*VNl1x2)/(2.*MW*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_103 = Coupling(name = 'GC_103',
                  value = '-(ee*complex(0,1)*MN1*Sa*VNl1x2)/(2.*MW*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_104 = Coupling(name = 'GC_104',
                  value = '-(a1*complex(0,1)*g1p*Sp*VNl1x2)/(2.*cmath.sqrt(2)) - (b1*complex(0,1)*g1p*Sp*VNl1x2)/cmath.sqrt(2) + (Cp*cw*ee*complex(0,1)*VNl1x2)/(2.*sw*cmath.sqrt(2)) + (Cp*ee*complex(0,1)*sw*VNl1x2)/(2.*cw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_105 = Coupling(name = 'GC_105',
                  value = '-(a1*Cp*complex(0,1)*g1p*VNl1x2)/(2.*cmath.sqrt(2)) - (b1*Cp*complex(0,1)*g1p*VNl1x2)/cmath.sqrt(2) - (cw*ee*complex(0,1)*Sp*VNl1x2)/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*Sp*sw*VNl1x2)/(2.*cw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_106 = Coupling(name = 'GC_106',
                  value = '(ee*complex(0,1)*VNl1x3)/(2.*sw)',
                  order = {'QED':1})

GC_107 = Coupling(name = 'GC_107',
                  value = '-(Ca*ee*complex(0,1)*MN1*VNl1x3)/(2.*MW*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_108 = Coupling(name = 'GC_108',
                  value = '-(ee*complex(0,1)*MN1*Sa*VNl1x3)/(2.*MW*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_109 = Coupling(name = 'GC_109',
                  value = '-(a1*complex(0,1)*g1p*Sp*VNl1x3)/(2.*cmath.sqrt(2)) - (b1*complex(0,1)*g1p*Sp*VNl1x3)/cmath.sqrt(2) + (Cp*cw*ee*complex(0,1)*VNl1x3)/(2.*sw*cmath.sqrt(2)) + (Cp*ee*complex(0,1)*sw*VNl1x3)/(2.*cw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_110 = Coupling(name = 'GC_110',
                  value = '-(a1*Cp*complex(0,1)*g1p*VNl1x3)/(2.*cmath.sqrt(2)) - (b1*Cp*complex(0,1)*g1p*VNl1x3)/cmath.sqrt(2) - (cw*ee*complex(0,1)*Sp*VNl1x3)/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*Sp*sw*VNl1x3)/(2.*cw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_111 = Coupling(name = 'GC_111',
                  value = '(ee*complex(0,1)*VNl2x1)/(2.*sw)',
                  order = {'QED':1})

GC_112 = Coupling(name = 'GC_112',
                  value = '-(Ca*ee*complex(0,1)*MN2*VNl2x1)/(2.*MW*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_113 = Coupling(name = 'GC_113',
                  value = '-(ee*complex(0,1)*MN2*Sa*VNl2x1)/(2.*MW*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_114 = Coupling(name = 'GC_114',
                  value = '-(a1*complex(0,1)*g1p*Sp*VNl2x1)/(2.*cmath.sqrt(2)) - (b1*complex(0,1)*g1p*Sp*VNl2x1)/cmath.sqrt(2) + (Cp*cw*ee*complex(0,1)*VNl2x1)/(2.*sw*cmath.sqrt(2)) + (Cp*ee*complex(0,1)*sw*VNl2x1)/(2.*cw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_115 = Coupling(name = 'GC_115',
                  value = '-(a1*Cp*complex(0,1)*g1p*VNl2x1)/(2.*cmath.sqrt(2)) - (b1*Cp*complex(0,1)*g1p*VNl2x1)/cmath.sqrt(2) - (cw*ee*complex(0,1)*Sp*VNl2x1)/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*Sp*sw*VNl2x1)/(2.*cw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_116 = Coupling(name = 'GC_116',
                  value = '(ee*complex(0,1)*VNl2x2)/(2.*sw)',
                  order = {'QED':1})

GC_117 = Coupling(name = 'GC_117',
                  value = '-(Ca*ee*complex(0,1)*MN2*VNl2x2)/(2.*MW*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_118 = Coupling(name = 'GC_118',
                  value = '-(ee*complex(0,1)*MN2*Sa*VNl2x2)/(2.*MW*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_119 = Coupling(name = 'GC_119',
                  value = '-(a1*complex(0,1)*g1p*Sp*VNl2x2)/(2.*cmath.sqrt(2)) - (b1*complex(0,1)*g1p*Sp*VNl2x2)/cmath.sqrt(2) + (Cp*cw*ee*complex(0,1)*VNl2x2)/(2.*sw*cmath.sqrt(2)) + (Cp*ee*complex(0,1)*sw*VNl2x2)/(2.*cw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_120 = Coupling(name = 'GC_120',
                  value = '-(a1*Cp*complex(0,1)*g1p*VNl2x2)/(2.*cmath.sqrt(2)) - (b1*Cp*complex(0,1)*g1p*VNl2x2)/cmath.sqrt(2) - (cw*ee*complex(0,1)*Sp*VNl2x2)/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*Sp*sw*VNl2x2)/(2.*cw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_121 = Coupling(name = 'GC_121',
                  value = '(ee*complex(0,1)*VNl2x3)/(2.*sw)',
                  order = {'QED':1})

GC_122 = Coupling(name = 'GC_122',
                  value = '-(Ca*ee*complex(0,1)*MN2*VNl2x3)/(2.*MW*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_123 = Coupling(name = 'GC_123',
                  value = '-(ee*complex(0,1)*MN2*Sa*VNl2x3)/(2.*MW*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_124 = Coupling(name = 'GC_124',
                  value = '-(a1*complex(0,1)*g1p*Sp*VNl2x3)/(2.*cmath.sqrt(2)) - (b1*complex(0,1)*g1p*Sp*VNl2x3)/cmath.sqrt(2) + (Cp*cw*ee*complex(0,1)*VNl2x3)/(2.*sw*cmath.sqrt(2)) + (Cp*ee*complex(0,1)*sw*VNl2x3)/(2.*cw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_125 = Coupling(name = 'GC_125',
                  value = '-(a1*Cp*complex(0,1)*g1p*VNl2x3)/(2.*cmath.sqrt(2)) - (b1*Cp*complex(0,1)*g1p*VNl2x3)/cmath.sqrt(2) - (cw*ee*complex(0,1)*Sp*VNl2x3)/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*Sp*sw*VNl2x3)/(2.*cw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_126 = Coupling(name = 'GC_126',
                  value = '(ee*complex(0,1)*VNl3x1)/(2.*sw)',
                  order = {'QED':1})

GC_127 = Coupling(name = 'GC_127',
                  value = '-(Ca*ee*complex(0,1)*MN3*VNl3x1)/(2.*MW*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_128 = Coupling(name = 'GC_128',
                  value = '-(ee*complex(0,1)*MN3*Sa*VNl3x1)/(2.*MW*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_129 = Coupling(name = 'GC_129',
                  value = '-(a1*complex(0,1)*g1p*Sp*VNl3x1)/(2.*cmath.sqrt(2)) - (b1*complex(0,1)*g1p*Sp*VNl3x1)/cmath.sqrt(2) + (Cp*cw*ee*complex(0,1)*VNl3x1)/(2.*sw*cmath.sqrt(2)) + (Cp*ee*complex(0,1)*sw*VNl3x1)/(2.*cw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_130 = Coupling(name = 'GC_130',
                  value = '-(a1*Cp*complex(0,1)*g1p*VNl3x1)/(2.*cmath.sqrt(2)) - (b1*Cp*complex(0,1)*g1p*VNl3x1)/cmath.sqrt(2) - (cw*ee*complex(0,1)*Sp*VNl3x1)/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*Sp*sw*VNl3x1)/(2.*cw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_131 = Coupling(name = 'GC_131',
                  value = '(ee*complex(0,1)*VNl3x2)/(2.*sw)',
                  order = {'QED':1})

GC_132 = Coupling(name = 'GC_132',
                  value = '-(Ca*ee*complex(0,1)*MN3*VNl3x2)/(2.*MW*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_133 = Coupling(name = 'GC_133',
                  value = '-(ee*complex(0,1)*MN3*Sa*VNl3x2)/(2.*MW*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_134 = Coupling(name = 'GC_134',
                  value = '-(a1*complex(0,1)*g1p*Sp*VNl3x2)/(2.*cmath.sqrt(2)) - (b1*complex(0,1)*g1p*Sp*VNl3x2)/cmath.sqrt(2) + (Cp*cw*ee*complex(0,1)*VNl3x2)/(2.*sw*cmath.sqrt(2)) + (Cp*ee*complex(0,1)*sw*VNl3x2)/(2.*cw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_135 = Coupling(name = 'GC_135',
                  value = '-(a1*Cp*complex(0,1)*g1p*VNl3x2)/(2.*cmath.sqrt(2)) - (b1*Cp*complex(0,1)*g1p*VNl3x2)/cmath.sqrt(2) - (cw*ee*complex(0,1)*Sp*VNl3x2)/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*Sp*sw*VNl3x2)/(2.*cw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_136 = Coupling(name = 'GC_136',
                  value = '(ee*complex(0,1)*VNl3x3)/(2.*sw)',
                  order = {'QED':1})

GC_137 = Coupling(name = 'GC_137',
                  value = '-(Ca*ee*complex(0,1)*MN3*VNl3x3)/(2.*MW*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_138 = Coupling(name = 'GC_138',
                  value = '-(ee*complex(0,1)*MN3*Sa*VNl3x3)/(2.*MW*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_139 = Coupling(name = 'GC_139',
                  value = '-(a1*complex(0,1)*g1p*Sp*VNl3x3)/(2.*cmath.sqrt(2)) - (b1*complex(0,1)*g1p*Sp*VNl3x3)/cmath.sqrt(2) + (Cp*cw*ee*complex(0,1)*VNl3x3)/(2.*sw*cmath.sqrt(2)) + (Cp*ee*complex(0,1)*sw*VNl3x3)/(2.*cw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_140 = Coupling(name = 'GC_140',
                  value = '-(a1*Cp*complex(0,1)*g1p*VNl3x3)/(2.*cmath.sqrt(2)) - (b1*Cp*complex(0,1)*g1p*VNl3x3)/cmath.sqrt(2) - (cw*ee*complex(0,1)*Sp*VNl3x3)/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*Sp*sw*VNl3x3)/(2.*cw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_141 = Coupling(name = 'GC_141',
                  value = '-((Ca*complex(0,1)*MN1)/(x*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_142 = Coupling(name = 'GC_142',
                  value = '-((Ca*complex(0,1)*MN2)/(x*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_143 = Coupling(name = 'GC_143',
                  value = '-((Ca*complex(0,1)*MN3)/(x*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_144 = Coupling(name = 'GC_144',
                  value = '(complex(0,1)*MN1*Sa)/(x*cmath.sqrt(2))',
                  order = {'QED':1})

GC_145 = Coupling(name = 'GC_145',
                  value = '(complex(0,1)*MN2*Sa)/(x*cmath.sqrt(2))',
                  order = {'QED':1})

GC_146 = Coupling(name = 'GC_146',
                  value = '(complex(0,1)*MN3*Sa)/(x*cmath.sqrt(2))',
                  order = {'QED':1})

GC_147 = Coupling(name = 'GC_147',
                  value = '(a1**2*Cp**2*complex(0,1)*g1p**2*Sa*vev)/2. + ee**2*complex(0,1)*Sa*Sp**2*vev + (cw**2*ee**2*complex(0,1)*Sa*Sp**2*vev)/(2.*sw**2) + (a1*Cp*cw*ee*complex(0,1)*g1p*Sa*Sp*vev)/sw + (a1*Cp*ee*complex(0,1)*g1p*Sa*Sp*sw*vev)/cw + (ee**2*complex(0,1)*Sa*Sp**2*sw**2*vev)/(2.*cw**2) + 8*b1**2*Ca*Cp**2*complex(0,1)*g1p**2*x',
                  order = {'QED':1})

GC_148 = Coupling(name = 'GC_148',
                  value = '(a1**2*Ca*Cp**2*complex(0,1)*g1p**2*vev)/2. + Ca*ee**2*complex(0,1)*Sp**2*vev + (Ca*cw**2*ee**2*complex(0,1)*Sp**2*vev)/(2.*sw**2) + (a1*Ca*Cp*cw*ee*complex(0,1)*g1p*Sp*vev)/sw + (a1*Ca*Cp*ee*complex(0,1)*g1p*Sp*sw*vev)/cw + (Ca*ee**2*complex(0,1)*Sp**2*sw**2*vev)/(2.*cw**2) - 8*b1**2*Cp**2*complex(0,1)*g1p**2*Sa*x',
                  order = {'QED':1})

GC_149 = Coupling(name = 'GC_149',
                  value = '-6*Ca**2*complex(0,1)*lam1*Sa*vev + 2*Ca**2*complex(0,1)*lam3*Sa*vev - complex(0,1)*lam3*Sa**3*vev - Ca**3*complex(0,1)*lam3*x - 6*Ca*complex(0,1)*lam2*Sa**2*x + 2*Ca*complex(0,1)*lam3*Sa**2*x',
                  order = {'QED':1})

GC_150 = Coupling(name = 'GC_150',
                  value = '-3*Ca**2*complex(0,1)*lam3*Sa*vev - 6*complex(0,1)*lam1*Sa**3*vev - 6*Ca**3*complex(0,1)*lam2*x - 3*Ca*complex(0,1)*lam3*Sa**2*x',
                  order = {'QED':1})

GC_151 = Coupling(name = 'GC_151',
                  value = '-6*Ca**3*complex(0,1)*lam1*vev - 3*Ca*complex(0,1)*lam3*Sa**2*vev + 3*Ca**2*complex(0,1)*lam3*Sa*x + 6*complex(0,1)*lam2*Sa**3*x',
                  order = {'QED':1})

GC_152 = Coupling(name = 'GC_152',
                  value = '-(Ca**3*complex(0,1)*lam3*vev) - 6*Ca*complex(0,1)*lam1*Sa**2*vev + 2*Ca*complex(0,1)*lam3*Sa**2*vev + 6*Ca**2*complex(0,1)*lam2*Sa*x - 2*Ca**2*complex(0,1)*lam3*Sa*x + complex(0,1)*lam3*Sa**3*x',
                  order = {'QED':1})

GC_153 = Coupling(name = 'GC_153',
                  value = '2*cg*complex(0,1)*lam1*Sa*sg*vev - cg*complex(0,1)*lam3*Sa*sg*vev - 2*Ca*cg*complex(0,1)*lam2*sg*x + Ca*cg*complex(0,1)*lam3*sg*x',
                  order = {'QED':1})

GC_154 = Coupling(name = 'GC_154',
                  value = '2*Ca*cg*complex(0,1)*lam1*sg*vev - Ca*cg*complex(0,1)*lam3*sg*vev + 2*cg*complex(0,1)*lam2*Sa*sg*x - cg*complex(0,1)*lam3*Sa*sg*x',
                  order = {'QED':1})

GC_155 = Coupling(name = 'GC_155',
                  value = '-2*cg**2*complex(0,1)*lam1*Sa*vev - complex(0,1)*lam3*Sa*sg**2*vev - Ca*cg**2*complex(0,1)*lam3*x - 2*Ca*complex(0,1)*lam2*sg**2*x',
                  order = {'QED':1})

GC_156 = Coupling(name = 'GC_156',
                  value = '-(cg**2*complex(0,1)*lam3*Sa*vev) - 2*complex(0,1)*lam1*Sa*sg**2*vev - 2*Ca*cg**2*complex(0,1)*lam2*x - Ca*complex(0,1)*lam3*sg**2*x',
                  order = {'QED':1})

GC_157 = Coupling(name = 'GC_157',
                  value = '-2*Ca*cg**2*complex(0,1)*lam1*vev - Ca*complex(0,1)*lam3*sg**2*vev + cg**2*complex(0,1)*lam3*Sa*x + 2*complex(0,1)*lam2*Sa*sg**2*x',
                  order = {'QED':1})

GC_158 = Coupling(name = 'GC_158',
                  value = '-(Ca*cg**2*complex(0,1)*lam3*vev) - 2*Ca*complex(0,1)*lam1*sg**2*vev + 2*cg**2*complex(0,1)*lam2*Sa*x + complex(0,1)*lam3*Sa*sg**2*x',
                  order = {'QED':1})

GC_159 = Coupling(name = 'GC_159',
                  value = '-(Cp*ee**2*complex(0,1)*Sa*Sp*vev) + (a1**2*Cp*complex(0,1)*g1p**2*Sa*Sp*vev)/2. - (Cp*cw**2*ee**2*complex(0,1)*Sa*Sp*vev)/(2.*sw**2) - (a1*Cp**2*cw*ee*complex(0,1)*g1p*Sa*vev)/(2.*sw) + (a1*cw*ee*complex(0,1)*g1p*Sa*Sp**2*vev)/(2.*sw) - (a1*Cp**2*ee*complex(0,1)*g1p*Sa*sw*vev)/(2.*cw) + (a1*ee*complex(0,1)*g1p*Sa*Sp**2*sw*vev)/(2.*cw) - (Cp*ee**2*complex(0,1)*Sa*Sp*sw**2*vev)/(2.*cw**2) + 8*b1**2*Ca*Cp*complex(0,1)*g1p**2*Sp*x',
                  order = {'QED':1})

GC_160 = Coupling(name = 'GC_160',
                  value = '-(Ca*Cp*ee**2*complex(0,1)*Sp*vev) + (a1**2*Ca*Cp*complex(0,1)*g1p**2*Sp*vev)/2. - (Ca*Cp*cw**2*ee**2*complex(0,1)*Sp*vev)/(2.*sw**2) - (a1*Ca*Cp**2*cw*ee*complex(0,1)*g1p*vev)/(2.*sw) + (a1*Ca*cw*ee*complex(0,1)*g1p*Sp**2*vev)/(2.*sw) - (a1*Ca*Cp**2*ee*complex(0,1)*g1p*sw*vev)/(2.*cw) + (a1*Ca*ee*complex(0,1)*g1p*Sp**2*sw*vev)/(2.*cw) - (Ca*Cp*ee**2*complex(0,1)*Sp*sw**2*vev)/(2.*cw**2) - 8*b1**2*Cp*complex(0,1)*g1p**2*Sa*Sp*x',
                  order = {'QED':1})

GC_161 = Coupling(name = 'GC_161',
                  value = 'Cp**2*ee**2*complex(0,1)*Sa*vev + (a1**2*complex(0,1)*g1p**2*Sa*Sp**2*vev)/2. + (Cp**2*cw**2*ee**2*complex(0,1)*Sa*vev)/(2.*sw**2) - (a1*Cp*cw*ee*complex(0,1)*g1p*Sa*Sp*vev)/sw - (a1*Cp*ee*complex(0,1)*g1p*Sa*Sp*sw*vev)/cw + (Cp**2*ee**2*complex(0,1)*Sa*sw**2*vev)/(2.*cw**2) + 8*b1**2*Ca*complex(0,1)*g1p**2*Sp**2*x',
                  order = {'QED':1})

GC_162 = Coupling(name = 'GC_162',
                  value = 'Ca*Cp**2*ee**2*complex(0,1)*vev + (a1**2*Ca*complex(0,1)*g1p**2*Sp**2*vev)/2. + (Ca*Cp**2*cw**2*ee**2*complex(0,1)*vev)/(2.*sw**2) - (a1*Ca*Cp*cw*ee*complex(0,1)*g1p*Sp*vev)/sw - (a1*Ca*Cp*ee*complex(0,1)*g1p*Sp*sw*vev)/cw + (Ca*Cp**2*ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2) - 8*b1**2*complex(0,1)*g1p**2*Sa*Sp**2*x',
                  order = {'QED':1})

GC_163 = Coupling(name = 'GC_163',
                  value = '-((Ca*complex(0,1)*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_164 = Coupling(name = 'GC_164',
                  value = '-((cg*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_165 = Coupling(name = 'GC_165',
                  value = '-((complex(0,1)*Sa*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_166 = Coupling(name = 'GC_166',
                  value = '(sg*yb)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_167 = Coupling(name = 'GC_167',
                  value = '-((Ca*complex(0,1)*yc)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_168 = Coupling(name = 'GC_168',
                  value = '(cg*yc)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_169 = Coupling(name = 'GC_169',
                  value = '-((complex(0,1)*Sa*yc)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_170 = Coupling(name = 'GC_170',
                  value = '-((sg*yc)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_171 = Coupling(name = 'GC_171',
                  value = '-((Ca*complex(0,1)*ydo)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_172 = Coupling(name = 'GC_172',
                  value = '-((cg*ydo)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_173 = Coupling(name = 'GC_173',
                  value = '-((complex(0,1)*Sa*ydo)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_174 = Coupling(name = 'GC_174',
                  value = '(sg*ydo)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_175 = Coupling(name = 'GC_175',
                  value = '-((Ca*complex(0,1)*ye)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_176 = Coupling(name = 'GC_176',
                  value = '-((cg*ye)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_177 = Coupling(name = 'GC_177',
                  value = '-((complex(0,1)*Sa*ye)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_178 = Coupling(name = 'GC_178',
                  value = '(sg*ye)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_179 = Coupling(name = 'GC_179',
                  value = '-((Ca*complex(0,1)*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_180 = Coupling(name = 'GC_180',
                  value = '-((cg*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_181 = Coupling(name = 'GC_181',
                  value = '-((complex(0,1)*Sa*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_182 = Coupling(name = 'GC_182',
                  value = '(sg*ym)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_183 = Coupling(name = 'GC_183',
                  value = '-((Ca*complex(0,1)*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_184 = Coupling(name = 'GC_184',
                  value = '-((cg*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_185 = Coupling(name = 'GC_185',
                  value = '-((complex(0,1)*Sa*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_186 = Coupling(name = 'GC_186',
                  value = '(sg*ys)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_187 = Coupling(name = 'GC_187',
                  value = '-((Ca*complex(0,1)*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_188 = Coupling(name = 'GC_188',
                  value = '(cg*yt)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_189 = Coupling(name = 'GC_189',
                  value = '-((complex(0,1)*Sa*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_190 = Coupling(name = 'GC_190',
                  value = '-((sg*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_191 = Coupling(name = 'GC_191',
                  value = '-((Ca*complex(0,1)*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_192 = Coupling(name = 'GC_192',
                  value = '-((cg*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_193 = Coupling(name = 'GC_193',
                  value = '-((complex(0,1)*Sa*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_194 = Coupling(name = 'GC_194',
                  value = '(sg*ytau)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_195 = Coupling(name = 'GC_195',
                  value = '-((Ca*complex(0,1)*yup)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_196 = Coupling(name = 'GC_196',
                  value = '(cg*yup)/cmath.sqrt(2)',
                  order = {'QED':1})

GC_197 = Coupling(name = 'GC_197',
                  value = '-((complex(0,1)*Sa*yup)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_198 = Coupling(name = 'GC_198',
                  value = '-((sg*yup)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_199 = Coupling(name = 'GC_199',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_200 = Coupling(name = 'GC_200',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_201 = Coupling(name = 'GC_201',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_202 = Coupling(name = 'GC_202',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_203 = Coupling(name = 'GC_203',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_204 = Coupling(name = 'GC_204',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_205 = Coupling(name = 'GC_205',
                  value = '(ee*complex(0,1)*complexconjugate(CKM3x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_206 = Coupling(name = 'GC_206',
                  value = '(ee*complex(0,1)*complexconjugate(CKM3x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_207 = Coupling(name = 'GC_207',
                  value = '(ee*complex(0,1)*complexconjugate(CKM3x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

