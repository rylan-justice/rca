from secrets import choice


def key_file():
    symbols = ('𒒀𒒁𒒂𒒃𒒄𒒅𒒆𒒇𒒈𒒉𒒊𒒋𒒌𒒍𒒎𒒏𒒐𒒑𒒒𒒓𒒔𒒕𒒖𒒗𒒘𒒙𒒚𒒛𒒜𒒝𒒞𒒟𒒠𒒡𒒢𒒣𒒤𒒥𒒦𒒧𒒨𒒩𒒪𒒫𒒬𒒭𒒮𒒯𒒰𒒱𒒲𒒳𒒴𒒵𒒶𒒷𒒸𒒹𒒺𒒻𒒼𒒽𒒾𒒿𒓀𒓁𒓂𒓃𒓄𒓅𒓆𒓇𒓈𒓉𒓊𒓋𒓌𒓍𒓎'
               '𒓏𒓐𒓑𒓒𒓓𒓔𒓕𒓖𒓗𒓘𒓙𒓚𒓛𒓜𒓝𒓞𒓟𒓠𒓡𒓢𒓣𒓤𒓥𒓦𒓧𒓨𒓩𒓪𒓫𒓬𒓭𒓮𒓯𒓰𒓱𒓲𒓳𒓴𒓵𒓶𒓷𒓸𒓹𒓺𒓻𒓼𒓽𒓾𒓿𒔀𒔁𒔂𒔃𒔄𒔅𒔆𒔇𒔈𒔉𒔊𒔋𒔌𒔍𒔎𒔏𒔐𒔑𒔒𒔓𒔔𒔕𒔖𒔗𒔘𒔙𒔚𒔛𒔜𒔝'
               '𒔞𒔟𒔠𒔡𒔢𒔣𒔤𒔥𒔦𒔧𒔨𒔩𒔪𒔫𒔬𒔭𒔮𒔯𒔰𒔱𒔲𒔳𒔴𒔵𒔶𒔷𒔸𒔹𒔺𒔻𒔼𒔽𒔾𒔿𒕀𒕁𒕂𒕃𒀀𒀁𒀂𒀃𒀄𒀅𒀆𒀇𒀈𒀉𒀊𒀋𒀌𒀍𒀎𒀏𒀐𒀑𒀒𒀓𒀔𒀕𒀖𒀗𒀘𒀙𒀚𒀛𒀜𒀝𒀞𒀟𒀠𒀡𒀢𒀣𒀤𒀥𒀦𒀧𒀨'
               '𒀩𒀪𒀫𒀬𒀭𒀮𒀯𒀰𒀱𒀲𒀳𒀴𒀵𒀶𒀷𒀸𒀹𒀺𒀻𒀼𒀽𒀾𒀿𒁀𒁁𒁂𒁃𒁄𒁅𒁆𒁇𒁈𒁉𒁊𒁋𒁌𒁍𒁎𒁏𒁐𒁑𒁒𒁓𒁔𒁕𒁖𒁗𒁘𒁙𒁚𒁛𒁜𒁝𒁞𒁟𒁠𒁡𒁢𒁣𒁤𒁥𒁦𒁧𒁨𒁩𒁪𒁫𒁬𒁭𒁮𒁯𒁰𒁱𒁲𒁳𒁴𒁵𒁶𒁷'
               '𒁸𒁹𒁺𒁻𒁼𒁽𒁾𒁿𒂀𒂁𒂂𒂃𒂄𒂅𒂆𒂇𒂈𒂉𒂊𒂋𒂌𒂍𒂎𒂏𒂐𒂑𒂒𒂓𒂔𒂕𒂖𒂗𒂘𒂙𒂚𒂛𒂜𒂝𒂞𒂟𒂠𒂡𒂢𒂣𒂤𒂥𒂦𒂧𒂨𒂩𒂪𒂫𒂬𒂭𒂮𒂯𒂰𒂱𒂲𒂳𒂴𒂵𒂶𒂷𒂸𒂹𒂺𒂻𒂼𒂽𒂾𒂿𒃀𒃁𒃂𒃃𒃄𒃅𒃆'
               '𒃇𒃈𒃉𒃊𒃋𒃌𒃍𒃎𒃏𒃐𒃑𒃒𒃓𒃔𒃕𒃖𒃗𒃘𒃙𒃚𒃛𒃜𒃝𒃞𒃟𒃠𒃡𒃢𒃣𒃤𒃥𒃦𒃧𒃨𒃩𒃪𒃫𒃬𒃭𒃮𒃯𒃰𒃱𒃲𒃳𒃴𒃵𒃶𒃷𒃸𒃹𒃺𒃻𒃼𒃽𒃾𒃿𒄀𒄁𒄂𒄃𒄄𒄅𒄆𒄇𒄈𒄉𒄊𒄋𒄌𒄍𒄎𒄏𒄐𒄑𒄒𒄓𒄔𒄕'
               '𒄖𒄗𒄘𒄙𒄚𒄛𒄜𒄝𒄞𒄟𒄠𒄡𒄢𒄣𒄤𒄥𒄦𒄧𒄨𒄩𒄪𒄫𒄬𒄭𒄮𒄯𒄰𒄱𒄲𒄳𒄴𒄵𒄶𒄷𒄸𒄹𒄺𒄻𒄼𒄽𒄾𒄿𒅀𒅁𒅂𒅃𒅄𒅅𒅆𒅇𒅈𒅉𒅊𒅋𒅌𒅍𒅎𒅏𒅐𒅑𒅒𒅓𒅔𒅕𒅖𒅗𒅘𒅙𒅚𒅛𒅜𒅝𒅞𒅟𒅠𒅡𒅢𒅣𒅤'
               '𒅥𒅦𒅧𒅨𒅩𒅪𒅫𒅬𒅭𒅮𒅯𒅰𒅱𒅲𒅳𒅴𒅵𒅶𒅷𒅸𒅹𒅺𒅻𒅼𒅽𒅾𒅿𒆀𒆁𒆂𒆃𒆄𒆅𒆆𒆇𒆈𒆉𒆊𒆋𒆌𒆍𒆎𒆏𒆐𒆑𒆒𒆓𒆔𒆕𒆖𒆗𒆘𒆙𒆚𒆛𒆜𒆝𒆞𒆟𒆠𒆡𒆢𒆣𒆤𒆥𒆦𒆧𒆨𒆩𒆪𒆫𒆬𒆭𒆮𒆯𒆰𒆱𒆲𒆳'
               '𒆴𒆵𒆶𒆷𒆸𒆹𒆺𒆻𒆼𒆽𒆾𒆿𒇀𒇁𒇂𒇃𒇄𒇅𒇆𒇇𒇈𒇉𒇊𒇋𒇌𒇍𒇎𒇏𒇐𒇑𒇒𒇓𒇔𒇕𒇖𒇗𒇘𒇙𒇚𒇛𒇜𒇝𒇞𒇟𒇠𒇡𒇢𒇣𒇤𒇥𒇦𒇧𒇨𒇩𒇪𒇫𒇬𒇭𒇮𒇯𒇰𒇱𒇲𒇳𒇴𒇵𒇶𒇷𒇸𒇹𒇺𒇻𒇼𒇽𒇾𒇿𒈀𒈁𒈂'
               '𒈃𒈄𒈅𒈆𒈇𒈈𒈉𒈊𒈋𒈌𒈍𒈎𒈏𒈐𒈑𒈒𒈓𒈔𒈕𒈖𒈗𒈘𒈙𒈚𒈛𒈜𒈝𒈞𒈟𒈠𒈡𒈢𒈣𒈤𒈥𒈦𒈧𒈨𒈩𒈪𒈫𒈬𒈭𒈮𒈯𒈰𒈱𒈲𒈳𒈴𒈵𒈶𒈷𒈸𒈹𒈺𒈻𒈼𒈽𒈾𒈿𒉀𒉁𒉂𒉃𒉄𒉅𒉆𒉇𒉈𒉉𒉊𒉋𒉌𒉍𒉎𒉏𒉐𒉑'
               '𒉒𒉓𒉔𒉕𒉖𒉗𒉘𒉙𒉚𒉛𒉜𒉝𒉞𒉟𒉠𒉡𒉢𒉣𒉤𒉥𒉦𒉧𒉨𒉩𒉪𒉫𒉬𒉭𒉮𒉯𒉰𒉱𒉲𒉳𒉴𒉵𒉶𒉷𒉸𒉹𒉺𒉻𒉼𒉽𒉾𒉿𒊀𒊁𒊂𒊃𒊄𒊅𒊆𒊇𒊈𒊉𒊊𒊋𒊌𒊍𒊎𒊏𒊐𒊑𒊒𒊓𒊔𒊕𒊖𒊗𒊘𒊙𒊚𒊛𒊜𒊝𒊞𒊟𒊠'
               '𒊡𒊢𒊣𒊤𒊥𒊦𒊧𒊨𒊩𒊪𒊫𒊬𒊭𒊮𒊯𒊰𒊱𒊲𒊳𒊴𒊵𒊶𒊷𒊸𒊹𒊺𒊻𒊼𒊽𒊾𒊿𒋀𒋁𒋂𒋃𒋄𒋅𒋆𒋇𒋈𒋉𒋊𒋋𒋌𒋍𒋎𒋏𒋐𒋑𒋒𒋓𒋔𒋕𒋖𒋗𒋘𒋙𒋚𒋛𒋜𒋝𒋞𒋟𒋠𒋡𒋢𒋣𒋤𒋥𒋦𒋧𒋨𒋩𒋪𒋫𒋬𒋭𒋮𒋯'
               '𒋰𒋱𒋲𒋳𒋴𒋵𒋶𒋷𒋸𒋹𒋺𒋻𒋼𒋽𒋾𒋿𒌀𒌁𒌂𒌃𒌄𒌅𒌆𒌇𒌈𒌉𒌊𒌋𒌌𒌍𒌎𒌏𒌐𒌑𒌒𒌓𒌔𒌕𒌖𒌗𒌘𒌙𒌚𒌛𒌜𒌝𒌞𒌟𒌠𒌡𒌢𒌣𒌤𒌥𒌦𒌧𒌨𒌩𒌪𒌫𒌬𒌭𒌮𒌯𒌰𒌱𒌲𒌳𒌴𒌵𒌶𒌷𒌸𒌹𒌺𒌻𒌼𒌽𒌾'
               '𒌿𒍀𒍁𒍂𒍃𒍄𒍅𒍆𒍇𒍈𒍉𒍊𒍋𒍌𒍍𒍎𒍏𒍐𒍑𒍒𒍓𒍔𒍕𒍖𒍗𒍘𒍙𒍚𒍛𒍜𒍝𒍞𒍟𒍠𒍡𒍢𒍣𒍤𒍥𒍦𒍧𒍨𒍩𒍪𒍫𒍬𒍭𒍮𒍯𒍰𒍱𒍲𒍳𒍴𒍵𒍶𒍷𒍸𒍹𒍺𒍻𒍼𒍽𒍾𒍿𒎀𒎁𒎂𒎃𒎄𒎅𒎆𒎇𒎈𒎉𒎊𒎋𒎌𒎍'
               '𒎎𒎏𒎐𒎑𒎒𒎓𒎔𒎕𒎖𒎗𒎘𒎙𒐀𒐁𒐂𒐃𒐄𒐅𒐆𒐇𒐈𒐉𒐊𒐋𒐌𒐍𒐎𒐏𒐐𒐑𒐒𒐓𒐔𒐕𒐖𒐗𒐘𒐙𒐚𒐛𒐜𒐝𒐞𒐟𒐠𒐡𒐢𒐣𒐤𒐥𒐦𒐧𒐨𒐩𒐪𒐫𒐬𒐭𒐮𒐯𒐰𒐱𒐲𒐳𒐴𒐵𒐶𒐷𒐸𒐹𒐺𒐻𒐼𒐽𒐾𒐿𒑀𒑁𒑂'
               '𒑃𒑄𒑅𒑆𒑇𒑈𒑉𒑊𒑋𒑌𒑍𒑎𒑏𒑐𒑑𒑒𒑓𒑔𒑕𒑖𒑗𒑘𒑙𒑚𒑛𒑜𒑝𒑞𒑟𒑠𒑡𒑢𒑣𒑤𒑥𒑦𒑧𒑨𒑩𒑪𒑫𒑬𒑭𒑮𒑰𒑱𒑲𒑳𒑴')
    lowercase_a = ''.join(choice(symbols) for _ in range(2))
    lowercase_b = ''.join(choice(symbols) for _ in range(2))
    lowercase_c = ''.join(choice(symbols) for _ in range(2))
    lowercase_d = ''.join(choice(symbols) for _ in range(2))
    lowercase_e = ''.join(choice(symbols) for _ in range(2))
    lowercase_f = ''.join(choice(symbols) for _ in range(2))
    lowercase_g = ''.join(choice(symbols) for _ in range(2))
    lowercase_h = ''.join(choice(symbols) for _ in range(2))
    lowercase_i = ''.join(choice(symbols) for _ in range(2))
    lowercase_j = ''.join(choice(symbols) for _ in range(2))
    lowercase_k = ''.join(choice(symbols) for _ in range(2))
    lowercase_l = ''.join(choice(symbols) for _ in range(2))
    lowercase_m = ''.join(choice(symbols) for _ in range(2))
    lowercase_n = ''.join(choice(symbols) for _ in range(2))
    lowercase_o = ''.join(choice(symbols) for _ in range(2))
    lowercase_p = ''.join(choice(symbols) for _ in range(2))
    lowercase_q = ''.join(choice(symbols) for _ in range(2))
    lowercase_r = ''.join(choice(symbols) for _ in range(2))
    lowercase_s = ''.join(choice(symbols) for _ in range(2))
    lowercase_t = ''.join(choice(symbols) for _ in range(2))
    lowercase_u = ''.join(choice(symbols) for _ in range(2))
    lowercase_v = ''.join(choice(symbols) for _ in range(2))
    lowercase_w = ''.join(choice(symbols) for _ in range(2))
    lowercase_x = ''.join(choice(symbols) for _ in range(2))
    lowercase_y = ''.join(choice(symbols) for _ in range(2))
    lowercase_z = ''.join(choice(symbols) for _ in range(2))
    uppercase_a = ''.join(choice(symbols) for _ in range(2))
    uppercase_b = ''.join(choice(symbols) for _ in range(2))
    uppercase_c = ''.join(choice(symbols) for _ in range(2))
    uppercase_d = ''.join(choice(symbols) for _ in range(2))
    uppercase_e = ''.join(choice(symbols) for _ in range(2))
    uppercase_f = ''.join(choice(symbols) for _ in range(2))
    uppercase_g = ''.join(choice(symbols) for _ in range(2))
    uppercase_h = ''.join(choice(symbols) for _ in range(2))
    uppercase_i = ''.join(choice(symbols) for _ in range(2))
    uppercase_j = ''.join(choice(symbols) for _ in range(2))
    uppercase_k = ''.join(choice(symbols) for _ in range(2))
    uppercase_l = ''.join(choice(symbols) for _ in range(2))
    uppercase_m = ''.join(choice(symbols) for _ in range(2))
    uppercase_n = ''.join(choice(symbols) for _ in range(2))
    uppercase_o = ''.join(choice(symbols) for _ in range(2))
    uppercase_p = ''.join(choice(symbols) for _ in range(2))
    uppercase_q = ''.join(choice(symbols) for _ in range(2))
    uppercase_r = ''.join(choice(symbols) for _ in range(2))
    uppercase_s = ''.join(choice(symbols) for _ in range(2))
    uppercase_t = ''.join(choice(symbols) for _ in range(2))
    uppercase_u = ''.join(choice(symbols) for _ in range(2))
    uppercase_v = ''.join(choice(symbols) for _ in range(2))
    uppercase_w = ''.join(choice(symbols) for _ in range(2))
    uppercase_x = ''.join(choice(symbols) for _ in range(2))
    uppercase_y = ''.join(choice(symbols) for _ in range(2))
    uppercase_z = ''.join(choice(symbols) for _ in range(2))
    digit_0 = ''.join(choice(symbols) for _ in range(2))
    digit_1 = ''.join(choice(symbols) for _ in range(2))
    digit_2 = ''.join(choice(symbols) for _ in range(2))
    digit_3 = ''.join(choice(symbols) for _ in range(2))
    digit_4 = ''.join(choice(symbols) for _ in range(2))
    digit_5 = ''.join(choice(symbols) for _ in range(2))
    digit_6 = ''.join(choice(symbols) for _ in range(2))
    digit_7 = ''.join(choice(symbols) for _ in range(2))
    digit_8 = ''.join(choice(symbols) for _ in range(2))
    digit_9 = ''.join(choice(symbols) for _ in range(2))
    punctuation_1 = ''.join(choice(symbols) for _ in range(2))
    punctuation_2 = ''.join(choice(symbols) for _ in range(2))
    punctuation_3 = ''.join(choice(symbols) for _ in range(2))
    punctuation_4 = ''.join(choice(symbols) for _ in range(2))
    punctuation_5 = ''.join(choice(symbols) for _ in range(2))
    punctuation_6 = ''.join(choice(symbols) for _ in range(2))
    punctuation_7 = ''.join(choice(symbols) for _ in range(2))
    punctuation_8 = ''.join(choice(symbols) for _ in range(2))
    punctuation_9 = ''.join(choice(symbols) for _ in range(2))
    punctuation_10 = ''.join(choice(symbols) for _ in range(2))
    punctuation_11 = ''.join(choice(symbols) for _ in range(2))
    punctuation_12 = ''.join(choice(symbols) for _ in range(2))
    punctuation_13 = ''.join(choice(symbols) for _ in range(2))
    punctuation_14 = ''.join(choice(symbols) for _ in range(2))
    punctuation_15 = ''.join(choice(symbols) for _ in range(2))
    punctuation_16 = ''.join(choice(symbols) for _ in range(2))
    punctuation_17 = ''.join(choice(symbols) for _ in range(2))
    punctuation_18 = ''.join(choice(symbols) for _ in range(2))
    punctuation_19 = ''.join(choice(symbols) for _ in range(2))
    punctuation_20 = ''.join(choice(symbols) for _ in range(2))
    punctuation_21 = ''.join(choice(symbols) for _ in range(2))
    punctuation_22 = ''.join(choice(symbols) for _ in range(2))
    punctuation_23 = ''.join(choice(symbols) for _ in range(2))
    punctuation_24 = ''.join(choice(symbols) for _ in range(2))
    punctuation_25 = ''.join(choice(symbols) for _ in range(2))
    punctuation_26 = ''.join(choice(symbols) for _ in range(2))
    punctuation_27 = ''.join(choice(symbols) for _ in range(2))
    punctuation_28 = ''.join(choice(symbols) for _ in range(2))
    punctuation_29 = ''.join(choice(symbols) for _ in range(2))
    punctuation_30 = ''.join(choice(symbols) for _ in range(2))
    punctuation_31 = ''.join(choice(symbols) for _ in range(2))
    punctuation_32 = ''.join(choice(symbols) for _ in range(2))
    punctuation_33 = ''.join(choice(symbols) for _ in range(2))
    salt_1 = ''.join(choice(symbols) for _ in range(2))
    salt_2 = ''.join(choice(symbols) for _ in range(2))
    salt_3 = ''.join(choice(symbols) for _ in range(2))
    salt_4 = ''.join(choice(symbols) for _ in range(2))
    salt_5 = ''.join(choice(symbols) for _ in range(2))
    salt_6 = ''.join(choice(symbols) for _ in range(2))
    salt_7 = ''.join(choice(symbols) for _ in range(2))
    salt_8 = ''.join(choice(symbols) for _ in range(2))
    salt_9 = ''.join(choice(symbols) for _ in range(2))
    salt_10 = ''.join(choice(symbols) for _ in range(2))
    salt_11 = ''.join(choice(symbols) for _ in range(2))
    salt_12 = ''.join(choice(symbols) for _ in range(2))
    salt_13 = ''.join(choice(symbols) for _ in range(2))
    salt_14 = ''.join(choice(symbols) for _ in range(2))
    salt_15 = ''.join(choice(symbols) for _ in range(2))
    salt_16 = ''.join(choice(symbols) for _ in range(2))
    salt_17 = ''.join(choice(symbols) for _ in range(2))
    salt_18 = ''.join(choice(symbols) for _ in range(2))
    salt_19 = ''.join(choice(symbols) for _ in range(2))
    salt_20 = ''.join(choice(symbols) for _ in range(2))
    salt_21 = ''.join(choice(symbols) for _ in range(2))
    salt_22 = ''.join(choice(symbols) for _ in range(2))
    salt_23 = ''.join(choice(symbols) for _ in range(2))
    salt_24 = ''.join(choice(symbols) for _ in range(2))
    salt_25 = ''.join(choice(symbols) for _ in range(2))
    salt_26 = ''.join(choice(symbols) for _ in range(2))
    salt_27 = ''.join(choice(symbols) for _ in range(2))
    salt_28 = ''.join(choice(symbols) for _ in range(2))
    salt_29 = ''.join(choice(symbols) for _ in range(2))
    salt_30 = ''.join(choice(symbols) for _ in range(2))
    salt_31 = ''.join(choice(symbols) for _ in range(2))
    salt_32 = ''.join(choice(symbols) for _ in range(2))
    salt_33 = ''.join(choice(symbols) for _ in range(2))
    salt_34 = ''.join(choice(symbols) for _ in range(2))
    salt_35 = ''.join(choice(symbols) for _ in range(2))
    salt_36 = ''.join(choice(symbols) for _ in range(2))
    salt_37 = ''.join(choice(symbols) for _ in range(2))
    salt_38 = ''.join(choice(symbols) for _ in range(2))
    salt_39 = ''.join(choice(symbols) for _ in range(2))
    salt_40 = ''.join(choice(symbols) for _ in range(2))
    salt_41 = ''.join(choice(symbols) for _ in range(2))
    salt_42 = ''.join(choice(symbols) for _ in range(2))
    salt_43 = ''.join(choice(symbols) for _ in range(2))
    salt_44 = ''.join(choice(symbols) for _ in range(2))
    salt_45 = ''.join(choice(symbols) for _ in range(2))
    salt_46 = ''.join(choice(symbols) for _ in range(2))
    salt_47 = ''.join(choice(symbols) for _ in range(2))
    salt_48 = ''.join(choice(symbols) for _ in range(2))
    salt_49 = ''.join(choice(symbols) for _ in range(2))
    salt_50 = ''.join(choice(symbols) for _ in range(2))
    salt_51 = ''.join(choice(symbols) for _ in range(2))
    salt_52 = ''.join(choice(symbols) for _ in range(2))
    salt_53 = ''.join(choice(symbols) for _ in range(2))
    salt_54 = ''.join(choice(symbols) for _ in range(2))
    salt_55 = ''.join(choice(symbols) for _ in range(2))
    salt_56 = ''.join(choice(symbols) for _ in range(2))
    salt_57 = ''.join(choice(symbols) for _ in range(2))
    salt_58 = ''.join(choice(symbols) for _ in range(2))
    salt_59 = ''.join(choice(symbols) for _ in range(2))
    salt_60 = ''.join(choice(symbols) for _ in range(2))
    salt_61 = ''.join(choice(symbols) for _ in range(2))
    salt_62 = ''.join(choice(symbols) for _ in range(2))
    salt_63 = ''.join(choice(symbols) for _ in range(2))
    salt_64 = ''.join(choice(symbols) for _ in range(2))
    salt_65 = ''.join(choice(symbols) for _ in range(2))
    salt_66 = ''.join(choice(symbols) for _ in range(2))
    salt_67 = ''.join(choice(symbols) for _ in range(2))
    salt_68 = ''.join(choice(symbols) for _ in range(2))
    salt_69 = ''.join(choice(symbols) for _ in range(2))
    salt_70 = ''.join(choice(symbols) for _ in range(2))
    salt_71 = ''.join(choice(symbols) for _ in range(2))
    salt_72 = ''.join(choice(symbols) for _ in range(2))
    salt_73 = ''.join(choice(symbols) for _ in range(2))
    salt_74 = ''.join(choice(symbols) for _ in range(2))
    salt_75 = ''.join(choice(symbols) for _ in range(2))
    salt_76 = ''.join(choice(symbols) for _ in range(2))
    salt_77 = ''.join(choice(symbols) for _ in range(2))
    salt_78 = ''.join(choice(symbols) for _ in range(2))
    salt_79 = ''.join(choice(symbols) for _ in range(2))
    salt_80 = ''.join(choice(symbols) for _ in range(2))
    salt_81 = ''.join(choice(symbols) for _ in range(2))
    salt_82 = ''.join(choice(symbols) for _ in range(2))
    salt_83 = ''.join(choice(symbols) for _ in range(2))
    salt_84 = ''.join(choice(symbols) for _ in range(2))
    salt_85 = ''.join(choice(symbols) for _ in range(2))
    salt_86 = ''.join(choice(symbols) for _ in range(2))
    salt_87 = ''.join(choice(symbols) for _ in range(2))
    salt_88 = ''.join(choice(symbols) for _ in range(2))
    salt_89 = ''.join(choice(symbols) for _ in range(2))
    salt_90 = ''.join(choice(symbols) for _ in range(2))
    salt_91 = ''.join(choice(symbols) for _ in range(2))
    salt_92 = ''.join(choice(symbols) for _ in range(2))
    salt_93 = ''.join(choice(symbols) for _ in range(2))
    salt_94 = ''.join(choice(symbols) for _ in range(2))
    salt_95 = ''.join(choice(symbols) for _ in range(2))
    salt_96 = ''.join(choice(symbols) for _ in range(2))
    salt_97 = ''.join(choice(symbols) for _ in range(2))
    salt_98 = ''.join(choice(symbols) for _ in range(2))
    salt_99 = ''.join(choice(symbols) for _ in range(2))
    salt_100 = ''.join(choice(symbols) for _ in range(2))
    salt_101 = ''.join(choice(symbols) for _ in range(2))
    salt_102 = ''.join(choice(symbols) for _ in range(2))
    salt_103 = ''.join(choice(symbols) for _ in range(2))
    salt_104 = ''.join(choice(symbols) for _ in range(2))
    salt_105 = ''.join(choice(symbols) for _ in range(2))
    salt_106 = ''.join(choice(symbols) for _ in range(2))
    salt_107 = ''.join(choice(symbols) for _ in range(2))
    salt_108 = ''.join(choice(symbols) for _ in range(2))
    salt_109 = ''.join(choice(symbols) for _ in range(2))
    salt_110 = ''.join(choice(symbols) for _ in range(2))
    salt_111 = ''.join(choice(symbols) for _ in range(2))
    salt_112 = ''.join(choice(symbols) for _ in range(2))
    salt_113 = ''.join(choice(symbols) for _ in range(2))
    salt_114 = ''.join(choice(symbols) for _ in range(2))
    salt_115 = ''.join(choice(symbols) for _ in range(2))
    salt_116 = ''.join(choice(symbols) for _ in range(2))
    salt_117 = ''.join(choice(symbols) for _ in range(2))
    salt_118 = ''.join(choice(symbols) for _ in range(2))
    salt_119 = ''.join(choice(symbols) for _ in range(2))
    salt_120 = ''.join(choice(symbols) for _ in range(2))
    salt_121 = ''.join(choice(symbols) for _ in range(2))
    salt_122 = ''.join(choice(symbols) for _ in range(2))
    salt_123 = ''.join(choice(symbols) for _ in range(2))
    salt_124 = ''.join(choice(symbols) for _ in range(2))
    salt_125 = ''.join(choice(symbols) for _ in range(2))
    salt_126 = ''.join(choice(symbols) for _ in range(2))
    salt_127 = ''.join(choice(symbols) for _ in range(2))
    salt_128 = ''.join(choice(symbols) for _ in range(2))
    salt_129 = ''.join(choice(symbols) for _ in range(2))
    salt_130 = ''.join(choice(symbols) for _ in range(2))
    salt_131 = ''.join(choice(symbols) for _ in range(2))
    salt_132 = ''.join(choice(symbols) for _ in range(2))
    salt_133 = ''.join(choice(symbols) for _ in range(2))
    salt_134 = ''.join(choice(symbols) for _ in range(2))
    salt_135 = ''.join(choice(symbols) for _ in range(2))
    salt_136 = ''.join(choice(symbols) for _ in range(2))
    salt_137 = ''.join(choice(symbols) for _ in range(2))
    salt_138 = ''.join(choice(symbols) for _ in range(2))
    salt_139 = ''.join(choice(symbols) for _ in range(2))
    salt_140 = ''.join(choice(symbols) for _ in range(2))
    salt_141 = ''.join(choice(symbols) for _ in range(2))
    salt_142 = ''.join(choice(symbols) for _ in range(2))
    salt_143 = ''.join(choice(symbols) for _ in range(2))
    salt_144 = ''.join(choice(symbols) for _ in range(2))
    salt_145 = ''.join(choice(symbols) for _ in range(2))
    salt_146 = ''.join(choice(symbols) for _ in range(2))
    salt_147 = ''.join(choice(symbols) for _ in range(2))
    salt_148 = ''.join(choice(symbols) for _ in range(2))
    salt_149 = ''.join(choice(symbols) for _ in range(2))
    salt_150 = ''.join(choice(symbols) for _ in range(2))
    salt_151 = ''.join(choice(symbols) for _ in range(2))
    salt_152 = ''.join(choice(symbols) for _ in range(2))
    salt_153 = ''.join(choice(symbols) for _ in range(2))
    salt_154 = ''.join(choice(symbols) for _ in range(2))
    salt_155 = ''.join(choice(symbols) for _ in range(2))
    salt_156 = ''.join(choice(symbols) for _ in range(2))
    salt_157 = ''.join(choice(symbols) for _ in range(2))
    salt_158 = ''.join(choice(symbols) for _ in range(2))
    salt_159 = ''.join(choice(symbols) for _ in range(2))
    salt_160 = ''.join(choice(symbols) for _ in range(2))
    salt_161 = ''.join(choice(symbols) for _ in range(2))
    salt_162 = ''.join(choice(symbols) for _ in range(2))
    salt_163 = ''.join(choice(symbols) for _ in range(2))
    salt_164 = ''.join(choice(symbols) for _ in range(2))
    salt_165 = ''.join(choice(symbols) for _ in range(2))
    salt_166 = ''.join(choice(symbols) for _ in range(2))
    salt_167 = ''.join(choice(symbols) for _ in range(2))
    salt_168 = ''.join(choice(symbols) for _ in range(2))
    salt_169 = ''.join(choice(symbols) for _ in range(2))
    salt_170 = ''.join(choice(symbols) for _ in range(2))
    salt_171 = ''.join(choice(symbols) for _ in range(2))
    salt_172 = ''.join(choice(symbols) for _ in range(2))
    salt_173 = ''.join(choice(symbols) for _ in range(2))
    salt_174 = ''.join(choice(symbols) for _ in range(2))
    salt_175 = ''.join(choice(symbols) for _ in range(2))
    salt_176 = ''.join(choice(symbols) for _ in range(2))
    salt_177 = ''.join(choice(symbols) for _ in range(2))
    salt_178 = ''.join(choice(symbols) for _ in range(2))
    salt_179 = ''.join(choice(symbols) for _ in range(2))
    salt_180 = ''.join(choice(symbols) for _ in range(2))
    salt_181 = ''.join(choice(symbols) for _ in range(2))
    salt_182 = ''.join(choice(symbols) for _ in range(2))
    salt_183 = ''.join(choice(symbols) for _ in range(2))
    salt_184 = ''.join(choice(symbols) for _ in range(2))
    salt_185 = ''.join(choice(symbols) for _ in range(2))
    salt_186 = ''.join(choice(symbols) for _ in range(2))
    salt_187 = ''.join(choice(symbols) for _ in range(2))
    salt_188 = ''.join(choice(symbols) for _ in range(2))
    salt_189 = ''.join(choice(symbols) for _ in range(2))
    salt_190 = ''.join(choice(symbols) for _ in range(2))
    salt_duplicate_1 = ''.join(choice(symbols) for _ in range(2))
    reverse_string = choice(['0', '1'])
    with open('key.py', 'w', encoding='utf-8')as f:
        f.write("lowercase_a='" + lowercase_a + "';lowercase_b='" + lowercase_b + "';lowercase_c='" + lowercase_c + "';lowercase_d='" + lowercase_d + "';lowercase_e='" + lowercase_e + "';lowercase_f='" + lowercase_f + "';lowercase_g='" + lowercase_g + "';lowercase_h='" + lowercase_h + "';lowercase_i='" + lowercase_i + "';lowercase_j='" + lowercase_j + "';lowercase_k='" + lowercase_k + "';lowercase_l='" + lowercase_l + "';lowercase_m='" + lowercase_m + "';lowercase_n='" + lowercase_n + "';lowercase_o='" + lowercase_o + "';lowercase_p='" + lowercase_p + "';lowercase_q='" + lowercase_q + "';lowercase_r='" + lowercase_r + "';lowercase_s='" + lowercase_s + "';lowercase_t='" + lowercase_t + "';lowercase_u='" + lowercase_u + "';lowercase_v='" + lowercase_v + "';lowercase_w='" + lowercase_w + "';lowercase_x='" + lowercase_x + "';lowercase_y='" + lowercase_y + "';lowercase_z='" + lowercase_z + "';uppercase_a='" + uppercase_a + "';uppercase_b='" + uppercase_b + "';uppercase_c='" + uppercase_c + "';uppercase_d='" + uppercase_d + "';uppercase_e='" + uppercase_e + "';uppercase_f='" + uppercase_f + "';uppercase_g='" + uppercase_g + "';uppercase_h='" + uppercase_h + "';uppercase_i='" + uppercase_i + "';uppercase_j='" + uppercase_j + "';uppercase_k='" + uppercase_k + "';uppercase_l='" + uppercase_l + "';uppercase_m='" + uppercase_m + "';uppercase_n='" + uppercase_n + "';uppercase_o='" + uppercase_o + "';uppercase_p='" + uppercase_p + "';uppercase_q='" + uppercase_q + "';uppercase_r='" + uppercase_r + "';uppercase_s='" + uppercase_s + "';uppercase_t='" + uppercase_t + "';uppercase_u='" + uppercase_u + "';uppercase_v='" + uppercase_v + "';uppercase_w='" + uppercase_w + "';uppercase_x='" + uppercase_x + "';uppercase_y='" + uppercase_y + "';uppercase_z='" + uppercase_z + "';digit_0='" + digit_0 + "';digit_1='" + digit_1 + "';digit_2='" + digit_2 + "';digit_3='" + digit_3 + "';digit_4='" + digit_4 + "';digit_5='" + digit_5 + "';digit_6='" + digit_6 + "';digit_7='" + digit_7 + "';digit_8='" + digit_8 + "';digit_9='" + digit_9 + "';punctuation_1='" + punctuation_1 + "';punctuation_2='" + punctuation_2 + "';punctuation_3='" + punctuation_3 + "';punctuation_4='" + punctuation_4 + "';punctuation_5='" + punctuation_5 + "';punctuation_6='" + punctuation_6 + "';punctuation_7='" + punctuation_7 + "';punctuation_8='" + punctuation_8 + "';punctuation_9='" + punctuation_9 + "';punctuation_10='" + punctuation_10 + "';punctuation_11='" + punctuation_11 + "';punctuation_12='" + punctuation_12 + "';punctuation_13='" + punctuation_13 + "';punctuation_14='" + punctuation_14 + "';punctuation_15='" + punctuation_15 + "';punctuation_16='" + punctuation_16 + "';punctuation_17='" + punctuation_17 + "';punctuation_18='" + punctuation_18 + "';punctuation_19='" + punctuation_19 + "';punctuation_20='" + punctuation_20 + "';punctuation_21='" + punctuation_21 + "';punctuation_22='" + punctuation_22 + "';punctuation_23='" + punctuation_23 + "';punctuation_24='" + punctuation_24 + "';punctuation_25='" + punctuation_25 + "';punctuation_26='" + punctuation_26 + "';punctuation_27='" + punctuation_27 + "';punctuation_28='" + punctuation_28 + "';punctuation_29='" + punctuation_29 + "';punctuation_30='" + punctuation_30 + "';punctuation_31='" + punctuation_31 + "';punctuation_32='" + punctuation_32 + "';punctuation_33='" + punctuation_33 + "';salt_1='" + salt_1 + "';salt_2='" + salt_2 + "';salt_3='" + salt_3 + "';salt_4='" + salt_4 + "';salt_5='" + salt_5 + "';salt_6='" + salt_6 + "';salt_7='" + salt_7 + "';salt_8='" + salt_8 + "';salt_9='" + salt_9 + "';salt_10='" + salt_10 + "';salt_11='" + salt_11 + "';salt_12='" + salt_12 + "';salt_13='" + salt_13 + "';salt_14='" + salt_14 + "';salt_15='" + salt_15 + "';salt_16='" + salt_16 + "';salt_17='" + salt_17 + "';salt_18='" + salt_18 + "';salt_19='" + salt_19 + "';salt_20='" + salt_20 + "';salt_21='" + salt_21 + "';salt_22='" + salt_22 + "';salt_23='" + salt_23 + "';salt_24='" + salt_24 + "';salt_25='" + salt_25 + "';salt_26='" + salt_26 + "';salt_27='" + salt_27 + "';salt_28='" + salt_28 + "';salt_29='" + salt_29 + "';salt_30='" + salt_30 + "';salt_31='" + salt_31 + "';salt_32='" + salt_32 + "';salt_33='" + salt_33 + "';salt_34='" + salt_34 +
                "';salt_35='" + salt_35 + "';salt_36='" + salt_36 + "';salt_37='" + salt_37 + "';salt_38='" + salt_38 + "';salt_39='" + salt_39 + "';salt_40='" + salt_40 + "';salt_41='" + salt_41 + "';salt_42='" + salt_42 + "';salt_43='" + salt_43 + "';salt_44='" + salt_44 + "';salt_45='" + salt_45 + "';salt_46='" + salt_46 + "';salt_47='" + salt_47 + "';salt_48='" + salt_48 + "';salt_49='" + salt_49 + "';salt_50='" + salt_50 + "';salt_51='" + salt_51 + "';salt_52='" + salt_52 + "';salt_53='" + salt_53 + "';salt_54='" + salt_54 + "';salt_55='" + salt_55 + "';salt_56='" + salt_56 + "';salt_57='" + salt_57 + "';salt_58='" + salt_58 + "';salt_59='" + salt_59 + "';salt_60='" + salt_60 + "';salt_61='" + salt_61 + "';salt_62='" + salt_62 + "';salt_63='" + salt_63 + "';salt_64='" + salt_64 + "';salt_65='" + salt_65 + "';salt_66='" + salt_66 + "';salt_67='" + salt_67 + "';salt_68='" + salt_68 + "';salt_69='" + salt_69 + "';salt_70='" + salt_70 + "';salt_71='" + salt_71 + "';salt_72='" + salt_72 + "';salt_73='" + salt_73 + "';salt_74='" + salt_74 + "';salt_75='" + salt_75 + "';salt_76='" + salt_76 + "';salt_77='" + salt_77 + "';salt_78='" + salt_78 + "';salt_79='" + salt_79 + "';salt_80='" + salt_80 + "';salt_81='" + salt_81 + "';salt_82='" + salt_82 + "';salt_83='" + salt_83 + "';salt_84='" + salt_84 + "';salt_85='" + salt_85 + "';salt_86='" + salt_86 + "';salt_87='" + salt_87 + "';salt_88='" + salt_88 + "';salt_89='" + salt_89 + "';salt_90='" + salt_90 + "';salt_91='" + salt_91 + "';salt_92='" + salt_92 + "';salt_93='" + salt_93 + "';salt_94='" + salt_94 + "';salt_95='" + salt_95 + "';salt_96='" + salt_96 + "';salt_97='" + salt_97 + "';salt_98='" + salt_98 + "';salt_99='" + salt_99 + "';salt_100='" + salt_100 + "';salt_101='" + salt_101 + "';salt_102='" + salt_102 + "';salt_103='" + salt_103 + "';salt_104='" + salt_104 + "';salt_105='" + salt_105 + "';salt_106='" + salt_106 + "';salt_107='" + salt_107 + "';salt_108='" + salt_108 + "';salt_109='" + salt_109 + "';salt_110='" + salt_110 + "';salt_111='" + salt_111 + "';salt_112='" + salt_112 + "';salt_113='" + salt_113 + "';salt_114='" + salt_114 + "';salt_115='" + salt_115 + "';salt_116='" + salt_116 + "';salt_117='" + salt_117 + "';salt_118='" + salt_118 + "';salt_119='" + salt_119 + "';salt_120='" + salt_120 + "';salt_121='" + salt_121 + "';salt_122='" + salt_122 + "';salt_123='" + salt_123 + "';salt_124='" + salt_124 + "';salt_125='" + salt_125 + "';salt_126='" + salt_126 + "';salt_127='" + salt_127 + "';salt_128='" + salt_128 + "';salt_129='" + salt_129 + "';salt_130='" + salt_130 + "';salt_131='" + salt_131 + "';salt_132='" + salt_132 + "';salt_133='" + salt_133 + "';salt_134='" + salt_134 + "';salt_135='" + salt_135 + "';salt_136='" + salt_136 + "';salt_137='" + salt_137 + "';salt_138='" + salt_138 + "';salt_139='" + salt_139 + "';salt_140='" + salt_140 + "';salt_141='" + salt_141 + "';salt_142='" + salt_142 + "';salt_143='" + salt_143 + "';salt_144='" + salt_144 + "';salt_145='" + salt_145 + "';salt_146='" + salt_146 + "';salt_147='" + salt_147 + "';salt_148='" + salt_148 + "';salt_149='" + salt_149 + "';salt_150='" + salt_150 + "';salt_151='" + salt_151 + "';salt_152='" + salt_152 + "';salt_153='" + salt_153 + "';salt_154='" + salt_154 + "';salt_155='" + salt_155 + "';salt_156='" + salt_156 + "';salt_157='" + salt_157 + "';salt_158='" + salt_158 + "';salt_159='" + salt_159 + "';salt_160='" + salt_160 + "';salt_161='" + salt_161 + "';salt_162='" + salt_162 + "';salt_163='" + salt_163 + "';salt_164='" + salt_164 + "';salt_165='" + salt_165 + "';salt_166='" + salt_166 + "';salt_167='" + salt_167 + "';salt_168='" + salt_168 + "';salt_169='" + salt_169 + "';salt_170='" + salt_170 + "';salt_171='" + salt_171 + "';salt_172='" + salt_172 + "';salt_173='" + salt_173 + "';salt_174='" + salt_174 + "';salt_175='" + salt_175 + "';salt_176='" + salt_176 + "';salt_177='" + salt_177 + "';salt_178='" + salt_178 + "';salt_179='" + salt_179 + "';salt_180='" + salt_180 + "';salt_181='" + salt_181 + "';salt_182='" + salt_182 + "';salt_183='" + salt_183 + "';salt_184='" + salt_184 + "';salt_185='" + salt_185 + "';salt_186='" + salt_186 + "';salt_187='" + salt_187 + "';salt_188='" + salt_188 + "';salt_189='" + salt_189 + "';salt_190='" + salt_190 + "';salt_duplicate_1='" + salt_duplicate_1 + "';reverse_string='" + reverse_string + "'")
