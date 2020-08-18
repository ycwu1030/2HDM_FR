#!/Applications/Mathematica.app/Contents/MacOS/MathematicaScript -script

$FeynRulesPath=SetDirectory["/Users/ycwu/Workingspace/FeynRules/feynrules-2.3.36"];
<<FeynRules`


SetDirectory["/Users/ycwu/Workingspace/FeynRules/ModelBuilding/2HDM_FR"];
LoadModel["2HDMCPC.fr"];
YukawaTypeList={"Type-I","Type-II","Type-LS","Type-FL"};
RUNNLOSWITCH={False,True};


type=ToExpression[$ScriptCommandLine[[2]]];
nlo=ToExpression[$ScriptCommandLine[[3]]];


YukawaType=YukawaTypeList[[type]];
RUNNLO=RUNNLOSWITCH[[nlo]];


If[!RUNNLO, 
FeynmanGauge=True;
WriteUFO[L2HDM,Output -> StringReplace["UFOs/"<>YukawaType<>"/"<>M$ModelName <> "_" <> YukawaType <> "_UFO", {" " -> "_"}]];
]


If[RUNNLO, 
Get["NLOCT/THDM_"<>YukawaType<>"_QCDreno.nlo"];
WriteUFO[L2HDM, UVCounterterms -> UV$vertlist, R2Vertices -> R2$vertlist, 
Output -> StringReplace["UFOs/"<>YukawaType<>"/"<>M$ModelName <> "_" <> YukawaType <> "_NLO_UFO", {" " -> "_"}]];
]
