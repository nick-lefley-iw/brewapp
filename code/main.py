import os
import sys
import pickle

from prettytable import PrettyTable

clear = lambda: os.system('clear')

danny = """
XXKKK00OOOOOOOOOO0000KKKKK000000000000000KKKKKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKKKKKKKKKKKKKKKKKKXXXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNX
XXXXXKKKK00000000000KKKKK0000000000000000KKKKKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKKKKKKKKKKKKKKKKKKXXXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
XXXXXXKKKK00000000000KK000000000000000000KKKKKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKKKKKKKKKKKKKKKKKKXXXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
XXXXKKKKKKK000000000000000000000000000000KKKKKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKKKKKKKKKKKKKKKKKXXXXXXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
KKKKKKKKKKK000000000000000000000000000000KKKKKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKKKKKKKKKKKKKKKKXXXXXXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
00000000000000000000000000000000000000000KKKKKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKKKKKKKKKKKKKKKXXXXXXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
00000000000OOOOOO000000000000000000000000KKKKKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKXXXKKKKKKKKKKKKKKKXXXXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
OOOOOOOOOOOOOOOO00000000000000000000000000KKKKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKKXXXXXXXXXXXXKKXXKKKKKKKKKKKKKKKXXXXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
kkkkkkkkOOOOOOO0O000000000000000000OOO0000KKKKXXXXXXXXXXXXXXXXXXXXXXXXXXXXKK0OOkkkkkkkkkkkkkOOO000KKKKXKKKKKKKKKKKKKKKXXXXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
kkkkkkkOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO000KKKXXXXXXXXXXXXXXXXXXXXXXXXXKOkkxxxxxxxxxxxxkkxxxdddxxxxxxkkOOO00KKKKKKKKKKXXXXXXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
kkkkkkkkkkkkkOOOOOOOOOOOOOOOOOOOOOOOOOO000KKKXXXXXXXXXXXXXXXXXXXXXK0kxdddxxxxxxxxxxxxxxkxxxxxxxxxxddddddddxxkO00KKKKKKXXXXXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
xxxxxxxxxxkkkkkkkkkkkkkkkkkkkkOOOOkkOOO000KKKXXXXXXXXXXXXXXXXXXK0kxdoodxxxxxxxxxxkkxxxkkkxxxxddddddddddddddddddxkkO0KKKKKKKXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
ddxxxxxxxxxxxxxxxxxxxxxkkkxxkkkkkkkkOOO00KKKKXXXXXXXXXXXXXXXK0kdddddddxxxxxxxxxxxkkkkkkkkkxxxxxxxxddddddddooooooooodkO00000KKXXXXNXNNNXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
dxxxxxxdddxxxxdddddddddxxxxxxxxkkkkkkOO00KKKKXXXXXXXXXXNNX0kdoooodddddxxxxxxxxxkkkkkkkkkkkkkkxxxxxxxxxxddddoodoooooooodxxkO000KKXXXXXXKKKXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
dxxxxxxxdxxxdddddddddddxxddddxxxxxxkkOO000KKKXXXNXXXXNXKOxoooooddddddddxxdddxxxxxkkkkkkkkkkkkxxxxxxxxxxdddddddoooooooooloodxkO000O00KKKKKKKKKKXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
xxxxxxxxxxxxdddddddddddxxddddxxxxxxkkOO000KKKXXXXNXNNXOdlloooodddddddddxxxxxxxkkkkkkkkkkkkkkkkkkxxxxxxxdddddddddddddooooooooooddddxkkkkkOOO000KKKXXXXXXNNNNNXXNNNNNNNNNNNNNNNNNNNXXXNNNNNNNNNNNNNXXXXXXX
kkkkkkkkkkkkxxxxxxxxxxxxxxxxxxkkkkkkkOO00KKKKXXXXXNX0dlclloooddddddxxxxxxxkkkkkkkkkkkkkkkkkkkkkkkkxxxxxxddddddddddddoooooooolllcccccc::ccloooodxk00KKKXXXXXXXXXXXXXXNNNNNNNNNXXXXXXXXXXXXXXXXXXXXXXXXXXX
OOOOOOOOOOOOOkkkkkkkkkkkOOOOOOOOOOOOO000KKKKKXXXXX0xlccllloddddddddddxxxxxxkkkkkkkkkkkkOkkkkkkkkkkxxkkxxxxxdddddddddooooooooloolc:;,,',;:::::::clodxO00KKKKKKKXXXXXXNNNNNNNNXXXXXXXXXXXXXXXXXXXXXXXXXXXX
00000000000000000000000000000000000000KKKKKKXXXXKklccccllooddddxxxxxxxxxxkkkkkOOOOOOkkOOOOOOkkkkkkkkkkkxxxxxxddddddddoooooooollllc;,'......',;;::cllldxkOOO0KKKKKKKKXXNNNNNXXXXXXXXXKKKKXXXXXXXXKKKKKXXX
KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKOdc:ccclloodddxxxxxxxxxxxxxkkkkkkkkkkkkkkOkkkkkkkkkkkkkkxxkxxxxxxdddddooodddddoollc:;,'...........,:::;:loxkO000000KKKXXXXXXXXKKKKKKKKKKKKKKXXXKKKKKKKKKK
KKXXXXXXXXXXKKKKXXXXXXXXXXXXXXXXXXXXXKKKKKK00Okl:::cccloooddddxxxxxxxxxxkkkkkkkkOOOOOOOOOOkkkkkkkkkkxxxkkkxxxxxxxxddddddddddddoolc:;;,'............';;,,;codxkkO00K00KKKKXKKKKKKK00000000000KKKK00000000
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKK000Okdl::::cccloooddddxxxxxxxxkkkkkkkkkkOOOOOOOOkkkkkkkkkkkkkkkxxxxxxxxxxxxdddddddddddddol:;,,,,'.........  ....',cllldxxkOOO0OO0KKKK0000000OOOOOOOO00000000000O
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKK00Oxollc:::::ccclloodddxxxxxxxxkkkkkkkkkkkkkkkkkOOkkkOOOkkkkkkkkkkkkxxkkkxxxxxdddddddddddool:;;;;,'....           ...,:clloxxkkkkxkO000000OOOOOOOOkkkOOOOOOOOOOOOO
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKOxdl:;;:c:::::ccccloodddxxxxxxxxkkkkkkkkkkkkOOOkkOOOOOOOOOOOOOOOkkkkkkkxxkkkxxxdddddddddddolcccc:;,''....               ..,:lodxxkkxddkO0OOOOOOOkkkkkkkkkkkkOOOOOOOk
XXXXXXXXXXXXXXXXXXXXXXXXNXXXXXXXX0kxo:,',;ccc::::::clooooddxxxxxxxkkkkkkkkkkOOOOOOOOOOOOOOOOOOOOOOOOOkkkkxxxxxxkkxxxdddddddoooolccc::;,,'....          ...    ..;cclddxxdddxkOOOOOOkkkkkkkkkxxxkkkOOkkkk
XXXXXXXXXXXXXXXXXXXXXXXXNXXXXXXK0xooc;,,;clcc::::ccllooddxxxxxxxxxkkOOOkkkkOOOOOOOOOOOkkkxxdddddddxxxxxxxxxxxxxxxxxxddxxxddoooolcc:;,,,,'....           ....   ..';clodddddodxkOOOkkxxdxxxxxxxxxkkkOOOkk
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX0ko:,'',;cclccc:::clloodddxxxxxkxxxxkOOOOkkOOOOOOOkkxxxxdoc:;,;;;;;;:ccccllldxxxxxxxxxxxxxxdddollcc;,',,''....              ....   ..,:lodddddddxkkkkxdddxxkkkkkkkkOOOOOk
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKkl,..',;:cccccccclllloolllooooddddddxkOOkkkOOOOOkkxxxxxxdlc:,'''....'',,,,,,'',,,,;:ccloxkxxddolllc;,,''''.....            ........  ...,;:codddddddddddxxkkkkkkkkkOOOOOk
XXXXXXXXXXXXXXXXXXXXXXXXXXKKKKk:.....';:cccccclolcccc;,''',;::ccloodkkkxxxkkkOkkkkxdlllcc:;,,;:ccloooooooolc:;,'..    .;c;;:llllc:;,,'',,'....              ................';coddolllodxkkkkkkkkkkkkkkk
XXXXXXXXXXXXXXXXXXXXNXXXXKKKOd:'.....,::ccccccllc;'..........',,:clodxxxkkkkkkxoc,..':cclooddxkxxxxkkkkkxxdxxxddl:,.   ..    ..',,,,''','.....               .. .....',::;,,,''';cloooooxkkkkkkkkkkkkkkk
XXXXXXXXXXXXXXXXNXXXNNXNX00kl;,'....',;:cc::;,'.....................',;::cc:;'..  .;ccllcc:::::;;;;;;;;;:clcclcloodc.               ..',.......                 ......',:cc:;;;;,;:llodddkOOkkkkkkkkkkkk
XXXXXXXXXXXXXXXNNXXXXNNXXKOd:;,'. ...''''.......',:ccclllllllcc:,'..            .',,,''',;;;:cclloolcc:;;:;;;:clc;cl'                     ...                   ..........,;:;',;,;cllodxkkOOkkkkkkOOOOk
XXXXXXXXXXXXXXXNXNNXXXNXX0kc:;,....      ..',,;cllllc:;:;;;;:::::;,'.           .,'..';:ccclolllccllloooolc:coddoccl,                                              .........;:,',;,,:ccoxkkOOkkkkkOOOOOO
XXXXXXXXXXXXXXXNXXNXXXXXXKkl:;.  ..    .,,'';::;;;'.....'',,;;;;:;;;.          .::;,,;:cc:;;,'...'....,:;,,;coddollc'                          ..                   ....'....','..'',;:oxkkkkkkkkkOOOOOO
XXXXXXXXXXXXXXXNXXNXXXXXXXkc:'.   .   .,;,'',;,''...';::::;;;;,,,,,,'.         'll:;;;;;;'':c;..'',;;,:c:;:ldolcccc;. ...                                            ....'''. ....''',;ldxxxxxxkkkkOOOOk
XXXXXXXXXXXXXXXXXNNNXXXXXXxc;.    .   .,,'..',,'.',,,,'... ........''.    .''.  .;llcll:;;:lol::lodxxxkkxxdddollccc'  ............              ...'...               .............',,,;coodxxxxkkkkkkkk
XXXXXXXXXXXXXXXNNNXXNXKKK0xo:..   ..  ......';,'''.....''...''...'',;.  .,cooc'  .cddxdoloooooodxxxxxxxxddddxdocclc'.';;:::::::::;,'...        .........              .... ..........,,,;clldxkkkkkkkkkk
XXXXXXXXXXXXXXXNNXXNXKkkOkkx;.    ..  ......';::ccccclllllllooolc:;;;.  .cdxxxo,. .lxxxdoolooooddddooolodxkkkkdoloc..ldllllolccclc:;,'...      .........               ..........  ..',,;ccldxkkOOkkkkxx
XXXXXXXXXXXXXXXXXNNXX0kkO0Od;..   ..  ......';;;;:clddddddoooollc::l:. .;ldxxxxdc..'lxkkkxdlcccccclooodxkkkkOkxodd:.;dxdolllllllllcc;,....    ....'...,'.        .     ...........  .',,:::ldxkkkkkkxxdd
XXXXXXXXXXXXXXXXNNXXXXK00Oxl;,,.   .   ....,;:::::clloooollcc::cllll:. ,odxxxxxxxo,.'lxkkkkkkxddoddxkkkkkkkkkkkkxl''oxxxxxdooooolc:,....... ...';cc;;:l:.        .........',;,..... .','.,:dxxxkxxxxddol
XXXXXXXXXXXXXXXXXXXXXKK0kddlcc;.        .'',;:ccloooddddddoooodddool'.,oddxxxxkkxkx:..cxkkOOkOkkkkkkkkkkkO00O0Oxc',okxxxxkxxddddooc:,..........':lolccol.            .....';ll,......',;:oxkkxkkxxdoollc
XXXXXXXXXXXXXXXXXXXXXK0Oxdolc:'.        ..';:::cloodxxkkkkkxxxxxdol,..cdddxxxxkkkkkxl,.,:lddxkkkkkkxxkkkkkkxol:,':oxxkkkkkkkxdddddoolc:;,''...',:clc:ldl.             ......;c;'',,,';::codxxxxxddollc:;
XXXXXXXXXXXXXXXXXXXXXK0Okxdoc,'..     .. .';:cloodxxkOOOOOkkkkkxoc'..,lddxxxxxkkkkxdool;,''..,;;:;;;;;;;;;;;;;:ldxxxxkkOOkkkkxddddooooooc:;,,'.,:llcccol'              ......';,,;;,;loolooooddollc:;;,'
XXXXXXXXXXXXXXXXXXXXXK0Oxdl:;,;;..    .....,:lloddxxkkkkkkkkkkdc'.':clloddxxkkkkkkxddxkkkxo;......,:cclooxxkOOOOkkkkkxkkOOkkkxdddoodddddolc:cc;';cllllll' ...           .......';;:;:::clolc:ccc:;,''''.
XXXXXXXXXXXXXXXXXXXXK0Okdlclccl:,......','..';cloddddxxxdolc:,...;ddlcclddxxkOOkkxdddxkOOkkdc:ccc::ccloxkkkkkOOOkkkxxxxkkkkkkxxxdooddddddolcldoc:llodooc.                 ... ........,cllc:;;;,,''..'',
XXXXXXXXXXNNNXXXXXXXK0Okoldxdoo:'.''...';::,.....''''''''.......,cllc;;:codddddoooooddddooooccdxxdlc:;;:cldxxxkkkxxxxxxxxkkkkxxxdddxxxkxxddoloollooodxo:.                       ......',,,''''''..''',;;
XXXXXXXXXXXXXXXXXXXXXK0kox0kxxo:'';:;,.'::::;,',,;:::cccc:,,,;;;;,,,'..',:cllllccc:,''...',:coxkkkxxddl:;;:codddxxxxxxxxxkkkkkxxxxxxxxkkxxddoollooooddl'                        ..,;;,''........'',,;;::
XXXXXXXXXXXXXXXXXXXXXKKkoxkkxxo:';:::;',::::::clodddddoc:;:llc::;'........',;:cc:;,'',,,;:coxkkkkkkxxxxdoc;,,:loddddxxxxxkkkkkkxxxxxxxxxxxxdddolldxdol;.                   ...   .,,,,,'.......''',,;::c
XXXXXXXXXXNNXXXXXXXXKK0Oxdxkxxo:,;,,,,;:::::::cllllol:;,;cllcc::::;,,'''.....',,,;:loooodxxxkkkxxxxkkxxdddoc;,,;lodxxxxxxkkkkkkxxxxxxxxxxxxxdddoloxxoc,                     ..   .'''''......'''',,;::cl
XXXXXXXXXXXXXXXXXXXXXK0Oxxkkdo:,;;',colc::::;:cllllc;,,:cllllcc::::::::;;;,'''',:loxxxxxxxxxxxxddddxxkkkxxxddl:;:ldxxxxxxkkOkkkkxxxxxddddxxxxddolloxkd;.                     .   ......''''',,,,;;::ccll
XXXXXXXXXXXXXXXXXXXKK0OkxkOOxoclxd;,cdo:::::;:ccllc;;:ccccllcclccccccc::ccllccloddxxxddddxxxxxdooddxxxxddddddxdlcldxxxxxkkOOOOOkkxxxdddddddxdddoolcldxl'                 ..    .....',;;;:;;;;;::cccccll
XXXXXXXXXXXXXXXXKKKKKXX0OOOkxooxOd:;ldl:::::::cclc:;:lllllllccllcclllccccloollllooooddodddddddddoooooolllooooooooodxxxxxkkkOOOOkkkxxdddoodddddddoolc::;'                 ....   ...';clcclol::cllllc::cc
XXXXXXXXXXXXXXXXXXXXXXXKK000OdoxOxllooc:::::::cllllccclllllc:::c::cllllllloolloododdddooooollccc:::::;:;;,'';;:oddxxxxxkkkkOOOOkkkxxddoooooddxxdoolc;..                  ..... ....':c:;:dxxdddddolc:;;;
XXXXXXXXNNXXXXXXXXNNXXKKKKKXKkxkOOkdoc::cccc::cloddollcc:::;;,,,''','',,,,;:;:cllccccccc:ccc:;;,....  ...';:c:coxxxxxxxkkkkOOOOkkkxddooloodddxdddoll:.                    ......',;cdxxdxOOOOOkxxdol:;,;
XXXXXXXXXXXXXXXXXXXXXXKXXXKKKOO000K0xl::cccc::cloxxxdol:;,......     .''',,,,;::;cllloxkxx0KOOOkxo;...;loddxdlloxxxxxxkkkkkkOOkkkxxdoollldxkxxddoolc:'                     ....';lxkO0KKKKKKK00Okxxolc:c
XXXXXXXXXXXXXXXXXXXXXKXXXXKKKK0K0000Oo::cclc::clodkkkxdol:;'....    .:ddxkkxkO0OkOKXK000kooxdlodxxollodxxxxxxdooxxxxxkkkkkkkOOkkxxddolclodxxxxxddocc:'                       ...;ok0KKKXXXXXXKK0OOkxdddd
XXXXXXXXXXXXXXXXXNXXXXXXXXK0KKK0000K0o::ccllccclloxxkkxxdddl:::;,....:lc:ldxxkkkkkkkdolllc:ccccloddxxxxxxkxxxdxxxxxxxxkkkkkOOOkxxdoolccldxxxxxxddocc:.                    ..... .;kKXXNNNNNXXXKK00OOkkkk
XXXXXXXXXXXXXXXXXXXXXXXXXXKKKXKKKKKK0d:;:cclllcloodxxxxxxxdollllll:::;;,,;cllooddddxdxxkkkkxxxxxxxxxxxxkkkxxxxxkxxxxxxxkkkkkOkkxdoolccloxkkxxxddolc:,.               ..   .:c;..;xXNNNNNNNNNNXXKKKK000OO
XXXXXXXXXXXXXXXXXXXXXXXXXXKKKXXKKKKKKk:,;:::clllooodxxddddddoollllllccclodddxxxxxkkxxxkkkkkkkkxxxxxxxxkkxxxxxkxxxddxxxxkkkkkkkxdoollcloxxxxxxxollc:,.                ...  .cxkxk0XNXNNNNNNNNNNXXXXXKKK00
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXKKKXKX0o,';::cllloooodddddddooooolcccclloooddxxxxxxkkxxkkkkkkkkkkkkxxxkkxxxxkkkkxxdddxxxxkkkkxxdolllcloxxxxxxddolc;,,.                ....,lxO0KKXXXXXXNNNNNNNNNXXXXXKKKK
XXXXNNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXKXXOc'',;:ccllooooodddoooollll:::clllooddxxxxxxkkxxkkkkkkkkxxxxxxxxxxxxkkkkxxxddxxxxxkkkxddollccloxxxxxddool:;,,,.                .  .ok000KXNNXXXXNNNXNNNNXXXXXKKKKK
XXXXXXXXXXXXXXXXXXXXNNNXXXXXXXXXXXXXKKXk;..,;::cllooodoooooooolccc::ccllodddddxxxxkkkkkkkxxkkkxxxxxxddxxxkkkkxxdddxxxxxkkxxdollccclodxxdddooc::;;,,,.                .. .o0KKKOxdl:;:codolllllcc::::;;::
NXXXXXXXNXXXXXXXXXXXXXXXXXXXXXXXXXXXKKXXd'..';;:ccloooolloooooollcc:::cllooodddxxxkkkkkkkkxxxxxxxxxxxxxxxxxxxxxxxxxxxxxkxdollc:::ldxxdddoolc::;,,,,..           .    ..  .:ll:.....  ...................
NXXXXXXXXNNNNNNNNNXXXXXXXXXXXXXXXXXKKKKXKl....';;:clooolccllooooollllllloooddxxxxxkkkkkkkkxxxxxxxxxxxxxxxxxdddxxxxkxxxxddolc::::loddooollc::;,,,,,..            .. .... .....  .........................
NXXNNNNNNXXK0OOO0KXNNNNNNNXXXXXKXXKKKKKXX0c....',;:cloolc:::clllooooollllooddxxxxxxxkkkkxxxxxxxxxxxxxxxxddddddxxxkkkxxdoc::;;clooooollcc:;;,',;;....       .   ...  ....................................
NNX0Okdlc;'......';cclodxkO0KXXXXKKKKXKKKX0l.....',;cclll:;;:cllllooollclodddddddddxxxxkkxxxxxxxxxxxxxxdooddxxkkkxxxddlc:;;:cloolllcc::;;,,;;;'. ..       .... .........................................
xc,...      ..           ...,:oxOKXXKKKKKKXKd'.....',:cccc::;;:cloooollc:loddddxxdxxxxxddxxxxxxddddddddolodxxxkkxxddoc::;:cloooccccc:::::::;'.            ..............................................
.          ...                 ..;lk0KKKXKKXXO:......';::cc:;;;:cllcclllccloodxxddddxkxddxxxddoooodooollodxxxxxxxdol::;:clooolcccccc:ccc:;..         .................  ................................
  ...                              .,lkKXXXXKkc. ......,;;:::::;;;:::::clllloodddoodxxxxdddolclloolc:cldxxxxxxxdooc:::clooolllcclllllc;,..    .     ............. .... .................................
  ..                                  .,:cc;..       ....',;;:::;,,,;;;;::ccccllllloolllcc::::ccc::cloxxxxxxxdollc::clooollclllloolc,...        ..  .... ... .......................................... 
 ..    .                                              .....',;:::;,,'',,,,,,,,;::::::;;;;;;;;;;;;coxxxxxxxxdoolc:ccloooolllooodol:'....... ..   ... ..................................................  
...   ..                                                  ...';;:;:;,''....'''',,,,,,,''''''';:lodxxxxxddddolcc::cloolllloooooc;.............   ... ........ ......................................... .
...  ..    .                                               ....,,;;:::;,'................',:ldxxxddddddolcc:::::cloooloooool:,..........  ......... ..                                 .............. ..
..   .  .                                                  ......',,,;;::::;;,,''''',;:cloddxdddddddoolc::;;,,;:lloooooolc;'.............. ..               ...                    ................ ....
..   .. .                                                  ... .....',,;::cclllllooodddddddddooolllcc::;,,',;:clllllool:,...............                ............  ..      ..........................
..               ..                                          ..........',;;:clllloooooolllllcccc:;,,''...,;clllllllll:'.................     ...      ........................................ .........
.             ...                                             ............',,;;::ccccccc::;;;,,'......',;:cclllccc:,'...................... ...    .......................................... ..........
.                      .                                      .................'',,,,,,,''.........',,;:ccc:::;,'............................   ........................................................
.          .                                                  ..................................',;:::::;,,'................................  .............................................. ...........
            ..                                                  . ..........................'',,,,,,,'..................................................................................................
           ...                                                 ... .....................''',,''............................................................................................ ............
           ..                                                  ......................'''.........',''...................................................................................................
            ...                                                 .'.........................',;:::,'.....................................................................................................
            ...                                                 .',,'.................',;::ccc:,........................................................................................................
            ....                           .                     .,;,,,'....'''''',,;;:::ccc;'..........................................................................................................
             ...                      ...    .     ..            .';;;;;,'..''',,;;:::ccc:,.............................................................................................................
             ..                ..       .            .     .      .;;;;;,,'',,;:::::ccc:,...............................................................................................................
              ...              ..                      .          .;::::::;;,,;;;;:cc:,.................................................................................................................
              ...             .. .                                'clooollc:;;;::::;'....... ...........................................................................................................
               ..                .                                'loodoolc::;;:::,......  .............................................................................................................
                ..               .  .                      ..     .:llolllc:::cc:'......................................................................................................................
               ...                 ..                  ..         .;ccccccccclc,.................................................................................................................. .....
                . .     ..        ... ..           ...  .     ..  .;:::ccccll:'.................  ............................................................................................... ......
                 ...      ..      .. ...  .         ...           .:ccclllol;..............   ................................................................................................... ......
                 ..       .       .  .. ...           ...  ... ....:lollooc'...........     ......................................'............................................................. .......
                  ...     .        .......  ...        ...  ....  .;loooo:...........    . ......... ........................'',,;;;;;;;,,''............................................................
.                 ...              ... ...  ..           ..   ... .;looo:..........    ...................................';:cloddxxxxxxdool:;,'.......................................... .... ... ....
                  ..       ..       .. ..  ..  ..         ...  .. .,lol;........     ........ ........................'',:ldxkkO00000KK0000Okxdoc;''....................................................
                    ...    .  .     . ...  .. ...          ...   ..'cc'.......    ...................................',:odxOO000KKKKKKXXXXXXKK00Oxoc,......................................... .........
                    ..       .     .. .. .......  ..       .....   .,'.....      ........... .......................';coxkO00KKKKKKKKKKXXXXXXNXXKKOxo:''................................................
                    ..       ..    .  .. ..  ...  ..          ...   ......     ................  . ................';coxkOO000KK00000KKKKKXXXNNNXXKOxoc,................................................
.                    ...    .      ....  ..  ..  ... ..        ..   ....    .. ............ ...    ................,:ldkkOOOO00000000000KKKXXXNNNXK0Oxo:'...............................................
.                     ...          .  .  .  ... ... ...           ...       .. .. .... ....... ....................,:ldxkkkkOOOOOOOOOO00KKKXXXXXXKK0Oxoc;''. ...........................................
   .                  .....    .  ..  . ..  ..  ..  ....         ..        ..  .. ...  ... .. .....................';coxxkkkkkkkkkkkOO00KKKKKKK00OOkxdlc,''.............................................
  .                    ....   ..         . ...  ..  .. ...      ..        ... ....... ....... ... ......... .... ...':loxxxxxxxxxxxkkOO0000000Okxdollc:;,,'.............................................
.......                .......    .  .      ..  .. ... ...    .        .   .  ..  ... ....... ... ......... .........;cloddddddddddddxxxxxxxddoolc:::;;,''..............................................
:::;;,,'....        ....''''''.........      .  .  ...  ..            .   ..  ..  ..  .. ........ ...................,:cloddoooollccccclllllllllcc::;;,,,'........................................ .....
ddddddolc:;'...    ...,,;;:::;;;,,'....            ... ..             .   ..  .. .......  ........... ...............';:clooooolc:;,,,,;;::ccclllccc::;,,'........... ........ .........................
kkkOkkkkxdlc;'... ...,;:cclllccc::;,,'.....         ..                ... .. .......................  .... ..........',;:coddddol:;,''',,;;::ccllllcc:;;,'........'. ....................... ...........
kOOOOOOOkkxdl:,.....',;ccllllllllc:::;,''.....   .  ..         .  .  ..................  ..............................';:lodddolc;,''''',,;;:cclllccc:;,'.........  ................................. .
O00KKKKK000kxdc;'...',;;::cc::::ccc:::;;;,..... ... ..  ..        ..................... .......  .. ..... ... ..........',:clooolc;,'....'',,;::cccccc::;,'........ ....................... ............
XXXXXXXXXK000Oxoc;,,;;;;;;;,,,,,,,;;;:::;,,,'.....     ....  .   .......... ............... .... ..  .... ... ...........'',;:cc:;,,''.....'',,;;:::cc:::;,,'.............................. .... .... ..
XXXKKKKXKK0000Oxdlc:::;;,''......''',,;::;;,'....      .......  .......... ....... ... ............  ..  ....................',,,,,,''''''...''',,;:::::::;,'..... .................. .... ..... ..  ...
XXXKKKKK000OOOkxddolc:;;,'..........'',;;;;,''..      ........ ........... ............... .......   ..  ... .....................''''',,,,''..'',,;;::::::;,'''.......................... ........  ...
xxxddoollodxxxdddollc:;,'.............',,;;,,'..      .................... ...... ... ............ .... ....................... ......'',,,,,'''.''',;;:::::;;,'........................ .........  ... 
cc:;'....,;:clllllc::;,''.........''..',;;;;;,'. .   ............ ... ....... ..  ... .......................... ...  ..    ... ........'',,,,,''...'',;;::::;;,'.............. .... ...  ............. 
dool;'',,;:::::::;;;;,,'''..''',,,,,,,,;::::;,'... .......... ... ... .......... ...  ................ ..................  ..        .....',,,,,'......',;;::::;,'.................. ...  ... ........  
Okkdl::cllolllcc:;;::;;;,,,,,;;;;;:::::cccc:;,,..  ......... ............ ...... ... ....... ................................  ..    .. .....'''........',,;::::;,'........... ........  ...  ..........
K00kxddxkkxxxdolc::ccc:::;;;;:::::ccc:ccccc:;,,.  .......... ... ... .... ..... ............ ........ ............................. ..   ......'....  ....',;:::;;,'.......... ...  ...  ...  ... ......

"""
menu_text = """
Welcome to brew app!

          {
       }   }   {
      {   {  }  }
       }   }{  {
      {  }{  }  }
     ( }{ }{  { )
    .-{   }   }-.
   ( ( } { } { } )
   |`-.._____..-'|
   |             ;--.
   |   (__)     (__  \\
   |   (oo)      | )  )
   |    \/       |/  /
   |             /  /    
   |            (  /
   \             y'
    `-.._____..-'


Please select an option:

    [1] Get a list of people
    [2] Get a list of drinks
    [3] Add person
    [4] Add drink
    [5] Show Favourites
    [6] Add Favourite
    [x] Exit
"""


def unpickle(path):
    if os.path.exists(path):
        return pickle.load(open(path, "rb"))
    else:
        return {}


def pickle_dictionary(name, dictionary):
    pickle.dump(dictionary, open(f"store/{name}.pickle", "wb"))


def get_name_from_uid(type, uid):
    if type == "person":
        mapping = uid_to_person
    elif type == "drink":
        mapping = uid_to_drink

    if mapping[uid]:
        return mapping[uid]
    else:
        return False


def run_session():
    mode = input("Enter your selection here: ")
    clear()

    if mode == "1":
        get_people_and_id()
    elif mode == "2":
        get_drinks_and_id()
    elif mode == "3":
        add_person()
    elif mode == "4":
        add_drink()
    elif mode == "5":
        get_favourites()
    elif mode == "6":
        add_favourite()
    elif mode == "x":
        end_sessions()
    elif mode == "DeVito":
        print(danny)
    else:
        reject_input()


def end_sessions():
    exit()

def get_new_uid(dictionary):
    if dictionary.keys():
        return int(max(dictionary.keys())) + 1
    else:
        return 1

def check_for_CLI_args():
    for i in range(1, len(sys.argv)):
        if sys.argv[i]:
            mode = sys.argv[i]
        else:
            if i == 1:
                reject_input()
                exit()
            else:
                exit()

        if mode == "get-people":
            get_people_and_id()
        elif mode == "get-drinks":
            get_drinks_and_id()
        elif mode == "--help":
            get_help()
        else:
            reject_input()

        wait_after_session()


def wait_after_session():
    selection = input("Would you like to continue? [y/n]").upper()

    if selection == "N":
        end_sessions()
    elif selection != "Y":
        reject_input()


def pretty_print_table(headers, data):
    x = PrettyTable()

    x.field_names = headers
    for row in data:
        x.add_row(row)

    print(x)


def add_person():
    get_people_and_id()
    new_entry = input("Please enter the new person's name: ").title()
    new_uid = get_new_uid(uid_to_person)
    uid_to_person[new_uid] = new_entry
    pickle_dictionary("people",uid_to_person)


def get_people_and_id():
    headers = ["People", "UID"]
    data = []
    for uid in uid_to_person:
        name = uid_to_person[uid]
        data.append([name, uid])
    pretty_print_table(headers, data)


def add_drink():
    get_drinks_and_id()
    new_entry = input("Please enter the new drink name: ").title()
    new_uid = get_new_uid(uid_to_drink)
    uid_to_drink[new_uid] = new_entry
    pickle_dictionary("drinks",uid_to_drink)


def get_drinks_and_id():
    headers = ["Drink", "UID"]
    data = []
    for uid in uid_to_drink:
        name = uid_to_drink[uid]
        data.append([name, uid])
    pretty_print_table(headers, data)


def get_favourites():
    headers = ["People", "People UID", "Favourite Drink"]
    data = []
    for uid in uid_to_person:
        name = uid_to_person[uid]
        try:
            data.append([name, uid, get_name_from_uid("drink", favourites[uid])])
        except:
            data.append([name, uid, "N/A"])
    pretty_print_table(headers, data)


def add_favourite():
    get_people_and_id()
    get_drinks_and_id()
    get_favourites()
    print("Adding a favourite")
    uid = int(input("Please enter the UID of the person: "))
    if uid not in uid_to_person.keys():
        reject_favourite()
    drink = int(input("Please enter the UID of their favourite drink: "))
    if drink not in uid_to_drink.keys():
        reject_favourite()

    favourites[uid] = drink
    pickle_dictionary("favourites",favourites)


def reject_favourite():
    print("Invalid input to create a favourite")


def reject_input():
    print("Invalid input")


def get_help():
    help_text = """
    Comand Line Arguments:
    
    get-people - Prints a list of people stored
    get-drinks - Prints a list of drinks stored
    """


uid_to_person = unpickle("store/people.pickle")
uid_to_drink = unpickle("store/drinks.pickle")
favourites = unpickle("store/favourites.pickle")

check_for_CLI_args()
while True:
    clear()
    print(menu_text)
    run_session()
    wait_after_session()
    clear()
