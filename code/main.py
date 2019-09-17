#!/usr/bin/env python3

import os
import sys

import fileHandler
from Drink import Drink
from Person import Person
from Round import Round

from prettytable import PrettyTable

resize = lambda: os.system("printf '\e[8;100;200t'")

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

    [P] Get a list of people
    [D] Get a list of drinks
    [P+] Add person
    [D+] Add drink
    [P-] Remove person
    [D-] Remove drink
    [R] Start Round
    [LR] Load last round
    [X] Exit
"""




def run_session(mode, drinks, people):
    clear()
    if mode == "P":
        show_people(people)
    elif mode == "D":
        show_drinks(drinks)
    elif mode == "P+":
        people = add_person(people, drinks)
    elif mode == "D+":
        drinks = add_drink(drinks)
    elif mode == "P-":
        people = remove_person(people)
    elif mode == "D-":
        drinks = remove_drink(drinks, people)
    elif mode == "R":
        start_round(people)
    elif mode == "LR":
        load_round("store/lastround")
    elif mode == "X":
        end_sessions()
    elif mode == "DEVITO":
        resize()
        print(danny)
    else:
        reject_input()

    return [drinks, people]


def end_sessions():
    exit()


def start_round(people):
    show_people(people)
    try:
        maker_id = int(input("Please enter the UID of the round's maker: "))
    except ValueError:
        print("This is not a number")
        return
    people_id_list = input("Please enter the ids of the people who want a drink, separated by comma: ").strip().split(',')
    people_list = []
    for people_id in people_id_list:
        people_list.append(get_person(people, int(people_id)))
    new_round = Round(get_person(people,maker_id),people_list)
    new_round.print_round()
    fileHandler.pickle_variable("store/lastround",new_round)

def load_round(path):
    return fileHandler.unpickle(path)

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
            show_people()
        elif mode == "get-drinks":
            show_drinks()
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


def pretty_print_table(header, data):
    x = PrettyTable()

    x.field_names = header
    for row in data:
        x.add_row(row)

    print(x)


def show_people(people):
    header = ["UID", "Name", "Favourite Drink"]
    data = []
    for index, person in enumerate(people):
        data.append([index, person.get_name(), person.get_favourite()])
    pretty_print_table(header, data)


def show_drinks(drinks):
    header = ["UID", "Name", "Temperature"]
    data = []
    for index, drink in enumerate(drinks):
        data.append([index, drink.get_name(), drink.get_temperature()])
    pretty_print_table(header, data)


def get_person(people, uid):
    return people[uid]


def get_drink(drinks, uid):
    if drinks[uid]:
        return drinks[uid]
    else:
        return None


def add_person(people, drinks):
    if len(drinks) == 0:
        print("Please enter a drink first")
    show_people(people)
    first_name = input("Please enter the new person's first name: ")
    surname = input("Please enter the new person's surname: ")
    show_drinks(drinks)
    favourite = int(input("Please enter the ID of their preferred drink: "))

    new_person = Person(first_name, surname, get_drink(drinks, favourite))

    people.append(new_person)
    fileHandler.pickle_variable("store/people", people)
    return people


def add_drink(drinks):
    show_drinks(drinks)
    name = input("Please enter the new drink name: ")
    temperature = input("Please enter the temperature of the new drink: ")

    new_drink = Drink(name, temperature)
    drinks.append(new_drink)
    fileHandler.pickle_variable("store/drinks", drinks)
    return drinks


def remove_person(people):
    show_people(people)
    uid = int(input("Please enter the UID of the person to be deleted: "))
    person = get_person(people, uid)
    confirm = input(f"This will delete {person}, are you sure you want to continue deletion? [y/n]").upper()

    if confirm == "Y":
        del people[uid]
        return people
    else:
        return


def remove_drink(drinks, people):
    show_drinks(drinks)
    uid = int(input("Please enter the UID of the drink to be deleted: "))
    drink = get_drink(drinks, uid)
    if is_favourite(drink, people):
        print(f"{drink} is someone's favourite drink, please don't delete it.")
    else:
        confirm = input(f"This will delete {drink}, are you sure you want to continue deletion? [y/n]").upper()

        if confirm == "Y":
            del drinks[uid]
    return drinks


def is_favourite(drink, people):
    for person in people:
        if person.get_favourite() == drink:
            return True

    return False

def reject_input():
    print("Invalid input")


def get_help():
    help_text = """
    Comand Line Arguments:
    
    get-people - Prints a list of people stored
    get-drinks - Prints a list of drinks stored
    """


drinks = fileHandler.unpickle("store/drinks")
people = fileHandler.unpickle("store/people")

check_for_CLI_args()
while True:
    clear()
    print(menu_text)
    updated_lists = run_session(input("Enter your selection here: ").upper(),drinks, people)
    drinks = updated_lists[0]
    people = updated_lists[1]
    wait_after_session()
    clear()
