from secrets import choice,SystemRandom

def key(symbols='𒀀𒀁𒀂𒀃𒀄𒀅𒀆𒀇𒀈𒀉𒀊𒀋𒀌𒀍𒀎𒀏𒀐𒀑𒀒𒀓𒀔𒀕𒀖𒀗𒀘𒀙𒀚𒀛𒀜𒀝𒀞𒀟𒀠𒀡𒀢𒀣𒀤𒀥𒀦𒀧𒀨𒀩𒀪𒀫𒀬𒀭𒀮𒀯𒀰𒀱𒀲𒀳𒀴𒀵𒀶𒀷𒀸𒀹𒀺𒀻𒀼𒀽𒀾𒀿𒁀𒁁𒁂𒁃𒁄𒁅𒁆𒁇𒁈𒁉𒁊𒁋𒁌𒁍𒁎𒁏𒁐𒁑𒁒𒁓𒁔𒁕𒁖𒁗𒁘𒁙𒁚𒁛𒁜𒁝𒁞𒁟𒁠𒁡𒁢𒁣𒁤𒁥𒁦𒁧𒁨𒁩𒁪𒁫𒁬𒁭𒁮𒁯𒁰𒁱𒁲𒁳𒁴𒁵𒁶𒁷𒁸𒁹𒁺𒁻𒁼𒁽𒁾𒁿𒂀𒂁𒂂𒂃𒂄𒂅𒂆𒂇𒂈𒂉𒂊𒂋𒂌𒂍𒂎𒂏𒂐𒂑𒂒𒂓𒂔𒂕𒂖𒂗𒂘𒂙𒂚𒂛𒂜𒂝𒂞𒂟𒂠𒂡𒂢𒂣𒂤𒂥𒂦𒂧𒂨𒂩𒂪𒂫𒂬𒂭𒂮𒂯𒂰𒂱𒂲𒂳𒂴𒂵𒂶𒂷𒂸𒂹𒂺𒂻𒂼𒂽𒂾𒂿𒃀𒃁𒃂𒃃𒃄𒃅𒃆𒃇𒃈𒃉𒃊𒃋𒃌𒃍𒃎𒃏𒃐𒃑𒃒𒃓𒃔𒃕𒃖𒃗𒃘𒃙𒃚𒃛𒃜𒃝𒃞𒃟𒃠𒃡𒃢𒃣𒃤𒃥𒃦𒃧𒃨𒃩𒃪𒃫𒃬𒃭𒃮𒃯𒃰𒃱𒃲𒃳𒃴𒃵𒃶𒃷𒃸𒃹𒃺𒃻𒃼𒃽𒃾𒃿𒄀𒄁𒄂𒄃𒄄𒄅𒄆𒄇𒄈𒄉𒄊𒄋𒄌𒄍𒄎𒄏𒄐𒄑𒄒𒄓𒄔𒄕𒄖𒄗𒄘𒄙𒄚𒄛𒄜𒄝𒄞𒄟𒄠𒄡𒄢𒄣𒄤𒄥𒄦𒄧𒄨𒄩𒄪𒄫𒄬𒄭𒄮𒄯𒄰𒄱𒄲𒄳𒄴𒄵𒄶𒄷𒄸𒄹𒄺𒄻𒄼𒄽𒄾𒄿𒅀𒅁𒅂𒅃𒅄𒅅𒅆𒅇𒅈𒅉𒅊𒅋𒅌𒅍𒅎𒅏𒅐𒅑𒅒𒅓𒅔𒅕𒅖𒅗𒅘𒅙𒅚𒅛𒅜𒅝𒅞𒅟𒅠𒅡𒅢𒅣𒅤𒅥𒅦𒅧𒅨𒅩𒅪𒅫𒅬𒅭𒅮𒅯𒅰𒅱𒅲𒅳𒅴𒅵𒅶𒅷𒅸𒅹𒅺𒅻𒅼𒅽𒅾𒅿𒆀𒆁𒆂𒆃𒆄𒆅𒆆𒆇𒆈𒆉𒆊𒆋𒆌𒆍𒆎𒆏𒆐𒆑𒆒𒆓𒆔𒆕𒆖𒆗𒆘𒆙𒆚𒆛𒆜𒆝𒆞𒆟𒆠𒆡𒆢𒆣𒆤𒆥𒆦𒆧𒆨𒆩𒆪𒆫𒆬𒆭𒆮𒆯𒆰𒆱𒆲𒆳𒆴𒆵𒆶𒆷𒆸𒆹𒆺𒆻𒆼𒆽𒆾𒆿𒇀𒇁𒇂𒇃𒇄𒇅𒇆𒇇𒇈𒇉𒇊𒇋𒇌𒇍𒇎𒇏𒇐𒇑𒇒𒇓𒇔𒇕𒇖𒇗𒇘𒇙𒇚𒇛𒇜𒇝𒇞𒇟𒇠𒇡𒇢𒇣𒇤𒇥𒇦𒇧𒇨𒇩𒇪𒇫𒇬𒇭𒇮𒇯𒇰𒇱𒇲𒇳𒇴𒇵𒇶𒇷𒇸𒇹𒇺𒇻𒇼𒇽𒇾𒇿𒈀𒈁𒈂𒈃𒈄𒈅𒈆𒈇𒈈𒈉𒈊𒈋𒈌𒈍𒈎𒈏𒈐𒈑𒈒𒈓𒈔𒈕𒈖𒈗𒈘𒈙𒈚𒈛𒈜𒈝𒈞𒈟𒈠𒈡𒈢𒈣𒈤𒈥𒈦𒈧𒈨𒈩𒈪𒈫𒈬𒈭𒈮𒈯𒈰𒈱𒈲𒈳𒈴𒈵𒈶𒈷𒈸𒈹𒈺𒈻𒈼𒈽𒈾𒈿𒉀𒉁𒉂𒉃𒉄𒉅𒉆𒉇𒉈𒉉𒉊𒉋𒉌𒉍𒉎𒉏𒉐𒉑𒉒𒉓𒉔𒉕𒉖𒉗𒉘𒉙𒉚𒉛𒉜𒉝𒉞𒉟𒉠𒉡𒉢𒉣𒉤𒉥𒉦𒉧𒉨𒉩𒉪𒉫𒉬𒉭𒉮𒉯𒉰𒉱𒉲𒉳𒉴𒉵𒉶𒉷𒉸𒉹𒉺𒉻𒉼𒉽𒉾𒉿𒊀𒊁𒊂𒊃𒊄𒊅𒊆𒊇𒊈𒊉𒊊𒊋𒊌𒊍𒊎𒊏𒊐𒊑𒊒𒊓𒊔𒊕𒊖𒊗𒊘𒊙𒊚𒊛𒊜𒊝𒊞𒊟𒊠𒊡𒊢𒊣𒊤𒊥𒊦𒊧𒊨𒊩𒊪𒊫𒊬𒊭𒊮𒊯𒊰𒊱𒊲𒊳𒊴𒊵𒊶𒊷𒊸𒊹𒊺𒊻𒊼𒊽𒊾𒊿𒋀𒋁𒋂𒋃𒋄𒋅𒋆𒋇𒋈𒋉𒋊𒋋𒋌𒋍𒋎𒋏𒋐𒋑𒋒𒋓𒋔𒋕𒋖𒋗𒋘𒋙𒋚𒋛𒋜𒋝𒋞𒋟𒋠𒋡𒋢𒋣𒋤𒋥𒋦𒋧𒋨𒋩𒋪𒋫𒋬𒋭𒋮𒋯𒋰𒋱𒋲𒋳𒋴𒋵𒋶𒋷𒋸𒋹𒋺𒋻𒋼𒋽𒋾𒋿𒌀𒌁𒌂𒌃𒌄𒌅𒌆𒌇𒌈𒌉𒌊𒌋𒌌𒌍𒌎𒌏𒌐𒌑𒌒𒌓𒌔𒌕𒌖𒌗𒌘𒌙𒌚𒌛𒌜𒌝𒌞𒌟𒌠𒌡𒌢𒌣𒌤𒌥𒌦𒌧𒌨𒌩𒌪𒌫𒌬𒌭𒌮𒌯𒌰𒌱𒌲𒌳𒌴𒌵𒌶𒌷𒌸𒌹𒌺𒌻𒌼𒌽𒌾𒌿𒍀𒍁𒍂𒍃𒍄𒍅𒍆𒍇𒍈𒍉𒍊𒍋𒍌𒍍𒍎𒍏𒍐𒍑𒍒𒍓𒍔𒍕𒍖𒍗𒍘𒍙𒍚𒍛𒍜𒍝𒍞𒍟𒍠𒍡𒍢𒍣𒍤𒍥𒍦𒍧𒍨𒍩𒍪𒍫𒍬𒍭𒍮𒍯𒍰𒍱𒍲𒍳𒍴𒍵𒍶𒍷𒍸𒍹𒍺𒍻𒍼𒍽𒍾𒍿𒎀𒎁𒎂𒎃𒎄𒎅𒎆𒎇𒎈𒎉𒎊𒎋𒎌𒎍𒎎𒎏𒎐𒎑𒎒𒎓𒎔𒎕𒎖𒎗𒎘𒎙',start=2,stop=4):
 SR=SystemRandom()
 a=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 b=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 c=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 d=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 e=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 f=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 g=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 h=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 i=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 j=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 k=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 l=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 m=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 n=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 o=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 p=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 q=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 r=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 s=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 t=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 u=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 v=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 w=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 x=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 y=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 z=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 A=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 B=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 C=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 D=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 E=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 F=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 G=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 H=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 I=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 J=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 K=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 L=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 M=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 N=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 O=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 P=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 Q=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 S=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 T=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 U=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 V=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 W=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 X=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 Y=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 Z=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 N1=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 N2=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 N3=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 N4=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 N5=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 N6=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 N7=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 N8=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 N9=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 N0=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 S1=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 S2=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 S3=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 S4=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 S5=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 S6=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 S7=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 S8=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 S9=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 S10=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 S11=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 S12=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 S13=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 S14=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 S15=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 S16=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 S17=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 S18=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 S19=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 S20=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 S21=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 S22=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 S23=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 S24=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 S25=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 S26=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 S27=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 S28=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 S29=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 S30=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 S31=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 S32=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 S33=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R1=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R2=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R3=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R4=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R5=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R6=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R7=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R8=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R9=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R10=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R11=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R12=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R13=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R14=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R15=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R16=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R17=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R18=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R19=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R20=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R21=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R22=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R23=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R24=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R25=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R26=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R27=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R28=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R29=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R30=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R31=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R32=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R33=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R34=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R35=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R36=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R37=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R38=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R39=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 R40=''.join(choice(symbols)for i in range(SR.randint(start,stop)))
 with open('key.py','w',encoding='utf8')as _f:_f.write("a='"+a+"';b='"+b+"';c='"+c+"';d='"+d+"';e='"+e+"';f='"+f+"';g='"+g+"';h='"+h+"';i='"+i+"';j='"+j+"';k='"+k+"';l='"+l+"';m='"+m+"';n='"+n+"';o='"+o+"';p='"+p+"';q='"+q+"';r='"+r+"';s='"+s+"';t='"+t+"';u='"+u+"';v='"+v+"';w='"+w+"';x='"+x+"';y='"+y+"';z='"+z+"';A='"+A+"';B='"+B+"';C='"+C+"';D='"+D+"';E='"+E+"';F='"+F+"';G='"+G+"';H='"+H+"';I='"+I+"';J='"+J+"';K='"+K+"';L='"+L+"';M='"+M+"';N='"+N+"';O='"+O+"';P='"+P+"';Q='"+Q+"';R='"+R+"';S='"+S+"';T='"+T+"';U='"+U+"';V='"+V+"';W='"+W+"';X='"+X+"';Y='"+Y+"';Z='"+Z+"';N1='"+N1+"';N2='"+N2+"';N3='"+N3+"';N4='"+N4+"';N5='"+N5+"';N6='"+N6+"';N7='"+N7+"';N8='"+N8+"';N9='"+N9+"';N0='"+N0+"';S1='"+S1+"';S2='"+S2+"';S3='"+S3+"';S4='"+S4+"';S5='"+S5+"';S6='"+S6+"';S7='"+S7+"';S8='"+S8+"';S9='"+S9+"';S10='"+S10+"';S11='"+S11+"';S12='"+S12+"';S13='"+S13+"';S14='"+S14+"';S15='"+S15+"';S16='"+S16+"';S17='"+S17+"';S18='"+S18+"';S19='"+S19+"';S20='"+S20+"';S21='"+S21+"';S22='"+S22+"';S23='"+S23+"';S24='"+S24+"';S25='"+S25+"';S26='"+S26+"';S27='"+S27+"';S28='"+S28+"';S29='"+S29+"';S30='"+S30+"';S31='"+S31+"';S32='"+S32+"';S33='"+S33+"';R1='"+R1+"';R2='"+R2+"';R3='"+R3+"';R4='"+R4+"';R5='"+R5+"';R6='"+R6+"';R7='"+R7+"';R8='"+R8+"';R9='"+R9+"';R10='"+R10+"';R11='"+R11+"';R12='"+R12+"';R13='"+R13+"';R14='"+R14+"';R15='"+R15+"';R16='"+R16+"';R17='"+R17+"';R18='"+R18+"';R19='"+R19+"';R20='"+R20+"';R21='"+R21+"';R22='"+R22+"';R23='"+R23+"';R24='"+R24+"';R25='"+R25+"';R26='"+R26+"';R27='"+R27+"';R28='"+R28+"';R29='"+R29+"';R30='"+R30+"';R31='"+R31+"';R32='"+R32+"';R33='"+R33+"';R34='"+R34+"';R35='"+R35+"';R36='"+R36+"';R37='"+R37+"';R38='"+R38+"';R39='"+R39+"';R40='"+R40+"'")

key()
from key import*

class Symmetric:
 def encrypt(self,plaintext):print(plaintext.replace('a',R1+a+R2).replace('b',R3+b+R4).replace('c',R5+c+R6).replace('d',R7+d+R8).replace('e',R9+e+R10).replace('f',R11+f+R12).replace('g',R13+g+R14).replace('h',R15+h+R16).replace('i',R17+i+R18).replace('j',R19+j+R20).replace('k',R21+k+R22).replace('l',R23+l+R24).replace('m',R25+m+R26).replace('n',R27+n+R28).replace('o',R29+o+R30).replace('p',R31+p+R32).replace('q',R33+q+R34).replace('r',R35+r+R36).replace('s',R37+s+R38).replace('t',R39+t+R40).replace('u',u).replace('v',v).replace('w',w).replace('x',x).replace('y',y).replace('z',z).replace('A',A).replace('B',B).replace('C',C).replace('D',D).replace('E',E).replace('F',F).replace('G',G).replace('H',H).replace('I',I).replace('J',J).replace('K',K).replace('L',L).replace('M',M).replace('N',N).replace('O',O).replace('P',P).replace('Q',Q).replace('R',R).replace('S',S).replace('T',T).replace('U',U).replace('V',V).replace('W',W).replace('X',X).replace('Y',Y).replace('Z',Z).replace('1',N1).replace('2',N2).replace('3',N3).replace('4',N4).replace('5',N5).replace('6',N6).replace('7',N7).replace('8',N8).replace('9',N9).replace('0',N0).replace('`',S1).replace('~',S2).replace('!',S3).replace('@',S4).replace('#',S5).replace('$',S6).replace('%',S7).replace('^',S8).replace('&',S9).replace('*',S10).replace('(',S11).replace(')',S12).replace('-',S13).replace('_',S14).replace('=',S15).replace('+',S16).replace('[',S17).replace('{',S18).replace(']',S19).replace('}',S20).replace('\\',S21).replace('|',S22).replace(';',S23).replace(':',S24).replace("'",S25).replace('"',S26).replace(',',S27).replace('<',S28).replace('.',S29).replace('>',S30).replace('/',S31).replace('?',S32).replace(' ',S33))
 def decrypt(self,ciphertext):print(ciphertext.replace(R1,'').replace(R2,'').replace(R3,'').replace(R4,'').replace(R5,'').replace(R6,'').replace(R7,'').replace(R8,'').replace(R9,'').replace(R10,'').replace(R11,'').replace(R12,'').replace(R13,'').replace(R14,'').replace(R15,'').replace(R16,'').replace(R17,'').replace(R18,'').replace(R19,'').replace(R20,'').replace(R21,'').replace(R22,'').replace(R23,'').replace(R24,'').replace(R25,'').replace(R26,'').replace(R27,'').replace(R28,'').replace(R29,'').replace(R30,'').replace(R31,'').replace(R32,'').replace(R33,'').replace(R34,'').replace(R35,'').replace(R36,'').replace(R37,'').replace(R38,'').replace(R39,'').replace(R40,'').replace(a,'a').replace(b,'b').replace(c,'c').replace(d,'d').replace(e,'e').replace(f,'f').replace(g,'g').replace(h,'h').replace(i,'i').replace(j,'j').replace(k,'k').replace(l,'l').replace(m,'m').replace(n,'n').replace(o,'o').replace(p,'p').replace(q,'q').replace(r,'r').replace(s,'s').replace(t,'t').replace(u,'u').replace(v,'v').replace(w,'w').replace(x,'x').replace(y,'y').replace(z,'z').replace(A,'A').replace(B,'B').replace(C,'C').replace(D,'D').replace(E,'E').replace(F,'F').replace(G,'G').replace(H,'H').replace(I,'I').replace(J,'J').replace(K,'K').replace(L,'L').replace(M,'M').replace(N,'N').replace(O,'O').replace(P,'P').replace(Q,'Q').replace(R,'R').replace(S,'S').replace(T,'T').replace(U,'U').replace(V,'V').replace(W,'W').replace(X,'X').replace(Y,'Y').replace(Z,'Z').replace(N1,'1').replace(N2,'2').replace(N3,'3').replace(N4,'4').replace(N5,'5').replace(N6,'6').replace(N7,'7').replace(N8,'8').replace(N9,'9').replace(N0,'0').replace(S1,'`').replace(S2,'~').replace(S3,'!').replace(S4,'@').replace(S5,'#').replace(S6,'$').replace(S7,'%').replace(S8,'^').replace(S9,'&').replace(S10,'*').replace(S11,'(').replace(S12,')').replace(S13,'-').replace(S14,'_').replace(S15,'=').replace(S16,'+').replace(S17,'[').replace(S18,'{').replace(S19,']').replace(S20,'}').replace(S21,'\\').replace(S22,'|').replace(S23,';').replace(S24,':').replace(S25,"'").replace(S26,'"').replace(S27,',').replace(S28,'<').replace(S29,'.').replace(S30,'>').replace(S31,'/').replace(S32,'?').replace(S33,' '))