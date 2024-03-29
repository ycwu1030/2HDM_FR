#!/Applications/Mathematica.app/Contents/MacOS/wolframscript -script

$FeynRulesPath=SetDirectory["/Users/ycwu/Workingspace/FeynRules/feynrules-2.3.49"];
<<FeynRules`


SetDirectory["/Users/ycwu/Library/CloudStorage/OneDrive-Personal/Projects/000.Codings/FeynRules/ModelBuilding/2HDM_FR"];
LoadModel["2HDMCPC.fr"];
YukawaTypeList={"Type-I","Type-II","Type-LS","Type-FL"};
RUNNLOSWITCH={False,True};


type=ToExpression[$ScriptCommandLine[[2]]];
nlo=ToExpression[$ScriptCommandLine[[3]]];


YukawaType=YukawaTypeList[[type]];
RUNNLO=RUNNLOSWITCH[[nlo]];


If[!RUNNLO,
FeynmanGauge=True;
DirName=StringReplace[M$ModelName <> "_" <> YukawaType <> "_cba_UFO", {" " -> "_"}];
WriteUFO[L2HDM,Output -> DirName];
DeleteDirectory["UFOs/"<>YukawaType<>"/"<>DirName,DeleteContents->True];
CopyDirectory[DirName,"UFOs/"<>YukawaType<>"/"<>DirName];
DeleteDirectory[DirName,DeleteContents->True];
CopyFile["restrict_default.dat","UFOs/"<>YukawaType<>"/"<>DirName<>"/restrict_default.dat"]; (* For LO UFO, using the restriction file *)
]


If[RUNNLO,
LoadRestriction["Massless.rst", "Cabibbo.rst"]; (* For NLO UFO, directly applying Massless constraints for light fermions *)
Get["NLOCT/THDM_"<>YukawaType<>"_QCDreno.nlo"];
DirName=StringReplace[M$ModelName <> "_" <> YukawaType <> "_NLO_cba_UFO", {" " -> "_"}];
WriteUFO[L2HDM, UVCounterterms -> UV$vertlist, R2Vertices -> R2$vertlist, Output -> DirName];
DeleteDirectory["UFOs/"<>YukawaType<>"/"<>DirName,DeleteContents->True];
CopyDirectory[DirName,"UFOs/"<>YukawaType<>"/"<>DirName];
DeleteDirectory[DirName,DeleteContents->True];
]
