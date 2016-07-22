import os
import re
import urllib
import datetime

# List of airport codes so we don't have to include the file or query wikipedia to check
airportList = ['KAAA','KAAF','KAAO','KAAS','KAAT','KABE','KABI','KABQ','KABR','KABY','KACB','KACJ','KACK','KACP','KACQ','KACT','KACV','KACY','KACZ','KADC','KADG','KADH','KADM','KADS','KADT','KADU','KADW','KAEG','KAEJ','KAEL','KAEX','KAFF','KAFJ','KAFK','KAFN','KAFO','KAFP','KAFW','KAGC','KAGO','KAGR','KAGS','KAGZ','KAHC','KAHH','KAHN','KAHQ','KAIA','KAIB','KAID','KAIG','KAIK','KAIO','KAIT','KAIV','KAIY','KAIZ','KAJG','KAJO','KAJR','KAJZ','KAKH','KAKO','KAKQ','KAKR','KALB','KALI','KALK','KALM','KALN','KALO','KALS','KALW','KALX','KAMA','KAMG','KAMN','KAMT','KAMW','KANB','KAND','KANE','KANJ','KANK','KANP','KANQ','KANW','KANY','KAOC','KAOH','KAOO','KAOV','KAPA','KAPC','KAPF','KAPG','KAPH','KAPN','KAPT','KAPV','KAQO','KAQP','KAQR','KAQW','KARA','KARB','KARG','KARM','KARR','KART','KARV','KARW','KASD','KASE','KASG','KASH','KASJ','KASL','KASN','KAST','KASW','KASX','KASY','KATA','KATL','KATS','KATW','KATY','KAUG','KAUH','KAUM','KAUN','KAUO','KAUS','KAUW','KAVC','KAVK','KAVL','KAVO','KAVP','KAVQ','KAVX','KAWG','KAWM','KAWO','KAXA','KAXH','KAXN','KAXQ','KAXS','KAXV','KAXX','KAYS','KAYX','KAZC','KAZE','KAZO','KAZU','KBAB','KBAC','KBAD','KBAF','KBAK','KBAM','KBAN','KBAX','KBAZ','KBBB','KBBD','KBBG','KBBP','KBBW','KBCB','KBCE','KBCK','KBCT','KBDE','KBDG','KBDJ','KBDH','KBDL','KBDN','KBDQ','KBDR','KBDU','KBEC','KBED','KBEH','KBFA','KBFD','KBFE','KBFF','KBFI','KBFK','KBFL','KBFM','KBFR','KBFW','KBGD','KBGE','KBGF','KBGM','KBGR','KBHB','KBHC','KBHK','KBHM','KBID','KBIE','KBIF','KBIH','KBIL','KBIS','KBIV','KBIX','KBJC','KBJI','KBJJ','KBJN','KBKD','KBKE','KBKF','KBKL','KBKN','KBKS','KBKT','KBKV','KBKW','KBKX','KBLF','KBLH','KBLI','KBLM','KBLU','KBLV','KBMC','KBMG','KBMI','KBML','KBMQ','KBMT','KBNA','KBNG','KBNL','KBNO','KBNW','KBOI','KBOK','KBOS','KBOW','KBPG','KBPI','KBPK','KBPP','KBPT','KBQK','KBQR','KBRD','KBRL','KBRO','KBRY','KBST','KBTA','KBTF','KBTL','KBTM','KBTN','KBTP','KBTR','KBTV','KBTY','KBUB','KBUF','KBUM','KBUR','KBUU','KBUY','KBVI','KBVN','KBVO','KBVS','KBVU','KBVX','KBVY','KBWC','KBWD','KBWG','KBWI','KBWP','KBXA','KBXG','KBXK','KBXM','KBYG','KBYH','KBYI','KBYS','KBYY','KBZN','KCAD','KCAE','KCAG','KCAK','KCAO','KCAR','KCAV','KCBE','KCBF','KCBG','KCBK','KCBM','KCCA','KCCB','KCCO','KCCR','KCCY','KCDA','KCDC','KCDD','KCDH','KCDI','KCDK','KCDN','KCDR','KCDS','KCDW','KCEA','KCEC','KCEF','KCEK','KCEU','KCEV','KCEW','KCEY','KCEZ','KCFD','KCFE','KCFJ','KCFS','KCFT','KCFV','KCGC','KCGE','KCGF','KCGI','KCGS','KCGZ','KCHA','KCHD','KCHK','KCHN','KCHO','KCHQ','KCHS','KCHT','KCHU','KCIC','KCID','KCII','KCIN','KCIR','KCIU','KCJJ','KCJR','KCKA','KCKB','KCKC','KCKF','KCKI','KCKM','KCKN','KCKP','KCKV','KCLE','KCLI','KCLK','KCLL','KCLM','KCLR','KCLS','KCLT','KCLW','KCMA','KCMH','KCMI','KCMR','KCMX','KCMY','KCNC','KCNH','KCNK','KCNM','KCNO','KCNP','KCNU','KCNW','KCNY','KCOD','KCOE','KCOF','KCOI','KCOM','KCON','KCOQ','KCOS','KCOT','KCOU','KCPC','KCPK','KCPM','KCPR','KCPS','KCPT','KCPU','KCQA','KCQB','KCQC','KCQF','KCQM','KCQW','KCQX','KCRE','KCRG','KCRO','KCRP','KCRQ','KCRS','KCRT','KCRW','KCRX','KCRZ','KCSB','KCSG','KCSM','KCSQ','KCSV','KCTB','KCTJ','KCTK','KCTY','KCTZ','KCUB','KCUH','KCUL','KCUT','KCVG','KCVH','KCVK','KCVN','KCVO','KCVS','KCVX','KCWA','KCWC','KCWF','KCWI','KCWS','KCWV','KCXE','KCXL','KCXO','KCXP','KCXU','KCXW','KCXY','KCYO','KCYS','KCYW','KCZD','KCZG','KCZK','KCZL','KCZT','KDAA','KDAB','KDAF','KDAG','KDAL','KDAN','KDAW','KDAY','KDBN','KDBQ','KDCA','KDCU','KDCY','KDDC','KDDH','KDEC','KDED','KDEH','KDEN','KDEQ','KDET','KDEW','KDFI','KDFW','KDGL','KDGW','KDHN','KDHT','KDIK','KDIJ','KDKB','KDKK','KDKR','KDKX','KDLC','KDLF','KDLH','KDLL','KDLN','KDLO','KDLS','KDLZ','KDMA','KDMN','KDMO','KDMW','KDNL','KDNN','KDNS','KDNV','KDOV','KDPA','KDPG','KDPL','KDQH','KDRA','KDRI','KDRO','KDRT','KDRU','KDSM','KDSV','KDTA','KDTG','KDTL','KDTN','KDTO','KDTS','KDTW','KDUA','KDUC','KDUG','KDUH','KDUJ','KDUX','KDVK','KDVL','KDVN','KDVO','KDVP','KDVT','KDWH','KDWU','KDXE','KDXR','KDXX','KDXZ','KDYA','KDYB','KDYL','KDYR','KDYS','KDYT','KDZJ','KEAG','KEAN','KEAR','KEAT','KEAU','KEBG','KEBS','KECG','KECS','KECU','KEDC','KEDE','KEDG','KEDJ','KEDN','KEDU','KEDW','KEED','KEEN','KEEO','KEET','KEFC','KEFD','KEFK','KEFT','KEFW','KEGE','KEGI','KEGQ','KEGT','KEGV','KEHA','KEHO','KEHR','KEIK','KEIW','KEKA','KEKM','KEKN','KEKO','KEKQ','KEKX','KEKY','KELA','KELD','KELK','KELM','KELN','KELO','KELP','KELY','KELZ','KEMM','KEMP','KEMT','KEMV','KEND','KENL','KENV','KENW','KEOE','KEOK','KEOP','KEOS','KEPG','KEPH','KEPM','KEQA','KEQY','KERI','KERR','KERV','KERY','KESC','KESF','KESN','KEST','KESW','KETB','KETC','KETN','KEUF','KEUG','KEUL','KEVB','KEVM','KEVU','KEVV','KEVW','KEVY','KEWB','KEWK','KEWN','KEWR','KEXX','KEYE','KEYF','KEYQ','KEYW','KEZF','KEZI','KEZM','KEZS','KEZZ','KFAF','KFAM','KFAR','KFAT','KFAY','KFBG','KFBL','KFBR','KFBY','KFCA','KFCH','KFCI','KFCM','KFCS','KFCT','KFCY','KFDK','KFDR','KFDW','KFDY','KFEP','KFES','KFET','KFFA','KFFC','KFFL','KFFM','KFFO','KFFT','KFFZ','KFGX','KFHB','KFHR','KFHU','KFIG','KFIT','KFKA','KFKL','KFKN','KFKR','KFKS','KFLD','KFLG','KFLL','KFLO','KFLP','KFLV','KFLX','KFLY','KFME','KFMH','KFMM','KFMN','KFMY','KFMZ','KFNB','KFNL','KFNT','KFOA','KFOD','KFOE','KFOK','KFOM','KFOT','KFOZ','KFPK','KFPR','KFQD','KFRG','KFRH','KFRI','KFRM','KFRR','KFSD','KFSE','KFSI','KFSK','KFSM','KFSO','KFST','KFSU','KFSW','KFTG','KFTK','KFTT','KFTW','KFTY','KFUL','KFVE','KFVX','KFWA','KFWC','KFWN','KFWQ','KFWS','KFXE','KFXY','KFYE','KFYJ','KFYM','KFYV','KFZG','KFZI','KFZY','KGAB','KGAD','KGAF','KGAG','KGAI','KGBD','KGBN','KGBR','KGCC','KGCD','KGCK','KGCM','KGCN','KGDJ','KGDM','KGDP','KGDV','KGDY','KGED','KGEG','KGEU','KGEV','KGEY','KGFA','KGFK','KGFL','KGGE','KGGF','KGGG','KGGI','KGGW','KGHG','KGHM','KGIC','KGIF','KGJT','KGKJ','KGKT','KGKY','KGLD','KGLH','KGLS','KGLW','KGMJ','KGMU','KGNB','KGNC','KGNF','KGNG','KGNI','KGNT','KGNV','KGOK','KGON','KGOO','KGOV','KGPI','KGPT','KGRB','KGRD','KGRF','KGRI','KGRK','KGRN','KGRR','KGSB','KGSO','KGSP','KGSW','KGTB','KGTE','KGTF','KGTG','KGTR','KGTU','KGUC','KGUP','KGUS','KGUY','KGVE','KGVT','KGVQ','KGWB','KGWO','KGWR','KGWS','KGWW','KGXA','KGXY','KGYB','KGYH','KGYI','KGYR','KGYY','KGZH','KGZL','KHAB','KHAF','KHAE','KHAI','KHAO','KHAR','KHBC','KHBG','KHBI','KHBR','KHBZ','KHCD','KHDE','KHDN','KHDO','KHEE','KHEF','KHEG','KHEI','KHEQ','KHEY','KHEZ','KHFD','KHFF','KHGR','KHHF','KHHR','KHHW','KHIE','KHIF','KHII','KHIO','KHJH','KHJO','KHKA','KHKS','KHKY','KHLC','KHLG','KHLN','KHLX','KHLR','KHMN','KHMS','KHMT','KHMZ','KHND','KHNZ','KHOB','KHOE','KHON','KHOP','KHOT','KHOU','KHPN','KHQG','KHQM','KHQU','KHQZ','KHRI','KHRJ','KHRL','KHRO','KHRU','KHRX','KHSA','KHSE','KHSI','KHSP','KHSR','KHST','KHSV','KHTH','KHTO','KHTS','KHUA','KHUF','KHUL','KHUM','KHUT','KHVC','KHVE','KHVN','KHVR','KHVS','KHWD','KHWO','KHWQ','KHWV','KHWY','KHXD','KHXF','KHYA','KHYI','KHYR','KHYS','KHYW','KHYX','KHZE','KHZL','KIAB','KIAD','KIAG','KIAH','KIBM','KICR','KICT','KIDA','KIDI','KIDL','KIDP','KIEN','KIFP','KIGM','KIGX','KIIB','KIIY','KIJD','KIJX','KIKW','KILE','KILG','KILM','KILN','KIML','KIMM','KIMS','KIND','KINJ','KINK','KINS','KINT','KINW','KIOW','KIPJ','KIPL','KIPT','KISM','KISN','KISO','KISP','KISW','KITH','KITR','KIWA','KIWI','KIXD','KIYK','KIZA','KIZG','KJAC','KJAN','KJAX','KJBR','KJCT','KJDN','KJEF','KJFK','KJFX','KJER','KJGG','KJHN','KJHW','KJKA','KJMS','KJNX','KJQF','KJRA','KJRB','KJST','KJSV','KJVW','KJWG','KJWN','KJYO','KJYR','KJZI','KJZP','KKIC','KKLS','KKNB','KLAA','KLAF','KLAL','KLAM','KLAN','KLAR','KLAS','KLAW','KLAX','KLBB','KLBE','KLBF','KLBL','KLBR','KLBT','KLCG','KLCK','KLCH','KLCI','KLCQ','KLDJ','KLDM','KLEB','KLEE','KLEM','KLEW','KLEX','KLFI','KLFK','KLFT','KLGA','KLGB','KLGD','KLGF','KLGU','KLHB','KLHM','KLHQ','KLHV','KLHX','KLHZ','KLIC','KLIT','KLKP','KLKR','KLKV','KLKU','KLLJ','KLLQ','KLLU','KLMO','KLMS','KLMT','KLNC','KLNA','KLND','KLNK','KLNN','KLNP','KLNS','KLOL','KLOU','KLOR','KLOZ','KLPC','KLPR','KLQK','KLQR','KLRD','KLRF','KLRG','KLRU','KLSB','KLSE','KLSF','KLSK','KLSN','KLSV','KLTS','KLTY','KLUF','KLUG','KLUL','KLVK','KLVL','KLVM','KLVN','KLVS','KLWB','KLWC','KLWL','KLWM','KLWS','KLWT','KLWV','KLXL','KLXN','KLXT','KLXV','KLYH','KLYO','KLZU','KLZZ','KMAC','KMAE','KMAF','KMAI','KMAL','KMAN','KMAO','KMAW','KMBG','KMBO','KMBS','KMBT','KMCB','KMCC','KMCE','KMCF','KMCI','KMCK','KMCN','KMCO','KMCW','KMCZ','KMDD','KMDQ','KMDS','KMDT','KMDW','KMDZ','KMEB','KMEI','KMEJ','KMEM','KMER','KMEV','KMFE','KMFI','KMFR','KMFV','KMGE','KMGG','KMGJ','KMGM','KMGW','KMGY','KMHE','KMHK','KMHL','KMHN','KMHR','KMHS','KMHT','KMHV','KMIA','KMIB','KMIC','KMIO','KMIT','KMIV','KMJX','KMKO','KMKA','KMKE','KMKJ','KMKL','KMKT','KMKY','KMLB','KMLC','KMLD','KMLE','KMLF','KMLI','KMLS','KMLT','KMLU','KMMH','KMMI','KMMK','KMMS','KMMT','KMMU','KMMV','KMNI','KMNZ','KMOB','KMOD','KMOR','KMOT','KMPE','KMPI','KMPJ','KMPO','KMPR','KMPV','KMQI','KMQJ','KMQS','KMQY','KMRB','KMRF','KMRH','KMRN','KMRY','KMSL','KMSO','KMSN','KMSP','KMSS','KMSV','KMSY','KMTC','KMTH','KMTJ','KMTN','KMTP','KMTV','KMTW','KMUO','KMUT','KMUU','KMVC','KMVI','KMVL','KMVM','KMVY','KMWH','KMWK','KMWL','KMXA','KMXF','KMXO','KMYF','KMYL','KMYR','KMYV','KMYZ','KMZJ','KNAB','KNBC','KNBJ','KNCA','KNDY','KNEL','KNEN','KNEW','KNFE','KNFD','KNFG','KNFJ','KNFL','KNFW','KNGP','KNGS','KNGU','KNGZ','KNHL','KNHK','KNHZ','KNID','KNIP','KNJK','KNJM','KNJW','KNKL','KNKT','KNKX','KNLC','KNMM','KNOW','KNPA','KNPI','KNQA','KNQB','KNQX','KNRA','KNRB','KNRN','KNRQ','KNRS','KNSI','KNTD','KNTK','KNTU','KNUC','KNUI','KNUN','KNUQ','KNUW','KNVI','KNWL','KNYG','KNYL','KNXF','KNXP','KNXX','KNZJ','KNZY','KOAJ','KOAK','KOAR','KOBE','KOBI','KOCF','KOCH','KOCW','KODO','KODX','KOEL','KOFF','KOFK','KOFP','KOGA','KOGB','KOGD','KOGS','KOIC','KOIN','KOJA','KOJC','KOKB','KOKC','KOKK','KOKM','KOKS','KOKV','KOLD','KOLE','KOLF','KOLM','KOLS','KOLU','KOLV','KOLZ','KOMA','KOMH','KOMK','KOMN','KONA','KONL','KONO','KONP','KONT','KONX','KOPF','KOPL','KOQN','KOQU','KORB','KORD','KORE','KORF','KORG','KORH','KORL','KORS','KOSH','KOSU','KOSX','KOTH','KOTM','KOUN','KOVE','KOVS','KOWB','KOWD','KOWI','KOWK','KOXB','KOXC','KOXD','KOXR','KOYM','KOZA','KOZR','KPAE','KPAM','KPAN','KPAO','KPBF','KPBG','KPBI','KPBX','KPCM','KPCU','KPCZ','KPDC','KPDK','KPDT','KPDX','KPEO','KPEQ','KPFC','KPFN','KPGA','KPGD','KPGR','KPGV','KPHF','KPHG','KPHH','KPHK','KPHL','KPHP','KPHT','KPHX','KPIA','KPIB','KPIE','KPIH','KPIR','KPIT','KPKB','KPKV','KPLB','KPLK','KPLR','KPLU','KPMB','KPMD','KPMV','KPMZ','KPNA','KPNC','KPNE','KPNM','KPNN','KPNS','KPOB','KPOC','KPOU','KPOY','KPPF','KPQI','KPQL','KPRB','KPRC','KPRN','KPRX','KPSB','KPSC','KPSF','KPSK','KPSM','KPSO','KPSP','KPTB','KPTD','KPTN','KPTS','KPTT','KPTV','KPTW','KPUB','KPUC','KPUJ','KPUW','KPVB','KPVC','KPVD','KPVE','KPVF','KPVG','KPVJ','KPVU','KPVW','KPWA','KPWD','KPWK','KPWM','KPWT','KPXE','KPYG','KPYM','KPYP','KPYX','KQA7','KQAD','KQAE','KQAJ','KQAQ','KQAX','KQAY','KQCO','KQCT','KQCU','KQD9','KQDM','KQEZ','KQGV','KQGX','KQIR','KQIU','KQL5','KQMA','KQMG','KQMH','KQNC','KQNN','KQNS','KQNT','KQNY','KQOS','KQPC','KQPD','KQRY','KQSA','KQSE','KQSL','KQSM','KQSR','KQTA','KQTI','KQTO','KQTU','KQTX','KQTZ','KQVO','KQWM','KQXJ','KQXN','KQYB','KRAC','KRAL','KRAP','KRAW','KRBD','KRBE','KRBG','KRBL','KRBM','KRBW','KRCA','KRCE','KRCM','KRCT','KRDD','KRDG','KRDM','KRDR','KRDU','KRED','KREO','KREI','KRGK','KRHP','KRHV','KRIC','KRID','KRIF','KRIL','KRIR','KRIU','KRIV','KRIW','KRJD','KRKR','KRKD','KRKS','KRLD','KRME','KRMN','KRND','KRNM','KRNO','KRNT','KRNV','KROA','KROC','KROG','KROW','KRPB','KRPD','KRPH','KRPX','KRQE','KRRT','KRSL','KRST','KRSW','KRTN','KRTS','KRUE','KRUG','KRUQ','KRUT','KRVL','KRVS','KRWI','KRWL','KRWV','KRXE','KRYN','KRYV','KRYW','KRYY','KRZL','KRZN','KRZT','KRZZ','KSAA','KSAC','KSAD','KSAF','KSAN','KSAS','KSAT','KSAV','KSAW','KSAZ','KSBA','KSBD','KSBM','KSBN','KSBP','KSBS','KSBX','KSBY','KSCB','KSCD','KSCH','KSCK','KSCR','KSDC','KSDF','KSDL','KSDM','KSDY','KSEA','KSEE','KSEF','KSEG','KSEM','KSEP','KSEZ','KSFB','KSFD','KSFF','KSFM','KSFO','KSFQ','KSFZ','KSGF','KSGJ','KSGT','KSGU','KSHD','KSHN','KSHR','KSHV','KSIF','KSIK','KSIY','KSJC','KSJN','KSJT','KSKA','KSKF','KSKI','KSKX','KSLB','KSLC','KSLE','KSLG','KSLI','KSLK','KSLN','KSLR','KSMD','KSME','KSMF','KSMN','KSMO','KSMQ','KSMS','KSMX','KSNA','KSNC','KSNK','KSNL','KSNS','KSNT','KSNY','KSOA','KSOP','KSOW','KSPA','KSPB','KSPD','KSPF','KSPG','KSPS','KSPW','KSPX','KSQL','KSRC','KSRQ','KSRR','KSSC','KSSF','KSSN','KSSQ','KSTC','KSTF','KSTK','KSTL','KSTP','KSTS','KSUA','KSUN','KSUS','KSUT','KSUU','KSUW','KSUX','KSUZ','KSVC','KSVE','KSVH','KSWF','KSWI','KSWO','KSWT','KSWW','KSXL','KSXT','KSXU','KSYF','KSYI','KSYL','KSYN','KSYR','KSZL','KSZP','KSZT','KTAD','KTAN','KTBX','KTCC','KTCL','KTCM','KTCS','KTCY','KTDF','KTDO','KTEB','KTEL','KTEX','KTGI','KTHM','KTHP','KTHV','KTIK','KTIW','KTIX','KTKI','KTKO','KTLH','KTLR','KTMB','KTME','KTMK','KTNP','KTNT','KTNU','KTNX','KTOA','KTOI','KTOL','KTOP','KTOR','KTPA','KTPF','KTPH','KTPL','KTQE','KTQH','KTQK','KTRI','KTRK','KTRM','KTRX','KTSP','KTTA','KTTD','KTTF','KTTN','KTUL','KTUP','KTUS','KTVC','KTVL','KTVR','KTVY','KTWF','KTWT','KTXK','KTYL','KTYQ','KTYR','KTYS','KTZR','KTZT','KUAO','KUBE','KUBS','KUCA','KUCP','KUDD','KUDG','KUES','KUGN','KUIL','KUIN','KUKF','KUKI','KUKL','KUKT','KULS','KUMP','KUNI','KUNU','KUNV','KUOS','KUOX','KUTS','KUUU','KUVA','KUZA','KVAY','KVBG','KVBT','KVBW','KVCB','KVCT','KVCV','KVDF','KVEL','KVER','KVES','KVGT','KVIH','KVIS','KVJI','KVKS','KVKX','KVLD','KVLL','KVMR','KVNC','KVNY','KVPS','KVPZ','KVQQ','KVRB','KVSF','KVTA','KVTN','KVUJ','KVUO','KVVS','KVYS','KWAL','KWAY','KWBW','KWDG','KWHP','KWJF','KWLD','KWLW','KWMC','KWRB','KWRI','KWRL','KWST','KWVI','KWVL','KWWD','KWWR','KWYS','KXBP','KXFL','KXMR','KXNA','KXNO','KXTA','KXVG','KYIP','KYKM','KYKN','KYNG','KZEF','KZER','KZPH','KZUN','KZZV']

def get_climate_data(station, year, print_start_year, print_end_year):
  '''Takes a station and year, downloads the monthly data for that station and saves to a csv file in ./data. Will check first to see if the file already exists. Uses print_start_year and print_end_year for file naming'''
  filename = './data/historicalMonthlyMeans_' + station + '_' + print_start_year + '-' + print_end_year + '.csv'

  if not os.path.exists(filename):
    with open(filename, 'w') as myfile:
      myfile.write('year,month,station,temp \n')
  
  month_number = 1
  while month_number < 13:
    url = 'http://www.wunderground.com/history/airport/' + station + '/' + str(year) +'/' +str(month_number) + '/25' + '/MonthlyHistory.html' # chose 25 for the day because it appears in every month
    tempURL = urllib.urlopen(url).read() # scrapes the html from the URL
    tempMatch = re.search('Mean Temperature\D+\d\d\D+(\d\d)', tempURL)
    if tempMatch:
      temp = tempMatch.group(1)
      with open(filename, 'a') as myfile:
        myfile.write(str(year) + ',' + str(month_number) + ',' + station + ',' + temp + '\n') # note that this will just append...won't overwrite existing file!
    month_number +=1
    

station = raw_input("Please enter a 4-letter station ID: ")
station = station.upper() # wunderground isn't picky, but still.
while station not in airportList:
  station = raw_input("\nID not found. Not sure of the station ID? Visit\n http://www.wunderground.com/history/ and enter your zip code. \n\nPlease enter a 4-letter station ID: ")
  station = station.upper()

start_year = raw_input("Please enter a 4-digit starting year: ")
while len(str(start_year)) != 4:
  start_year = raw_input("That wasn't 4 digits. Please try again: ")
while int(start_year) < 1948:
  start_year = raw_input("Data are only available from 1948 - present. Please try again: ")

end_year = raw_input("Please enter a 4-digit ending year: ")
while len(str(end_year)) != 4:
  end_year = raw_input("That wasn't 4 digits. Please try again: ")

now = datetime.datetime.now()
while int(end_year) > now.year:
  end_year = raw_input("Data are only available from 1948 - present. Please try again: ")
  
start_year = int(start_year)
end_year = int(end_year)

# get the original start and end values for file naming purposes
print_start_year = str(start_year)
print_end_year = str(end_year)

# Download the data, unless the end year is before the start year. If the end year is before the start year, print an error.
if end_year < start_year:
  print "ERROR: The end year you entered was before the start year. The end year must be greater than or equal to the start year."
else:
  while start_year <= end_year:
    get_climate_data(station, start_year, print_start_year, print_end_year)
    start_year +=1
