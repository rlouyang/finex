# IWZ after PEY
# IFSM after MDD
# BSJN after WYDE
# HHYX after TYTE
# ITLT after SBND
# HJPX after CID
# EMSA after RTLA
# LEMF after EMBH
# PUTX after MOM
# HDRW after TAO
# MUAC after IBMH
# HACW after SPUN
# FGHY after GURI
# CFT after CLY
# ITEQ after BDAT
# LBDC after HDLV
# RTLA after MATL
# SPYD after QUS
# EZR after EUDV
# BITE after IPD
# HAHA after KSA
# CNHX after SDEM
# BSCP after LDRI
# ASHX after SDEM
# EMSD after AZIA
# XINA after KFYP
# ROLA after GDXX
# EMLB after HEGJ
# HDEE after KLEM
etf_dict = {'agricultural': ['DBA','RJA','JO','JJG','CORN','SGG','JJA','WEAT','NIB','COW','FUD','BAL','UAG','CHOC','SOYB','GRU','CAFE','UBC','CANE','JJS','CTNN','USAG','AGF','WEET','SGAR','TAGS','DIRT','LSTK','GRWN'], 'all': ['VTI','USMV','IWV','SCHB','SCHD','ITOT','PKW','PDP','QUAL','MTUM','IYY','FPX','MOAT','TILT','QDF','ONEQ','PEY','VUSE','CSD','RYJ','TTFS','VTHR','BFOR','SIZE','FNDB','QDEF','GURU','PWC','NFO','FAB','KNOW','FAD','TUTT','QDYN','DWAQ','FVL','EUSA','IPO','WMW','MMTM','NASH','QINC','TUSA','HECO','RWV','HUSE','TOFR','VLU','ACTX','CNTR','RORO'], 'alternative': ['TAN','PBW','GEX','ICLN','PZD','QCLN','PBD','NLR','FAN','PUW','KWT','YLCO'], 'asia': ['EWY','EWT','VPL','AAXJ','EPP','EWA','EWS','IPAC','GMF','FHK','DBKO','ENZL','AXJL','DVYA','FPA','AUSE','JHDG','ADRA','DXKW','PAF','DBAP','FTW','QAUS','QTWN','AXJV','HKOR','KROO','FKO','DBAU','OASI','QKOR','OAPH','HEWY','HAUD','SCIX','FAUS'], 'building': ['ITB','XHB','PKB','HOMX','FLM'], 'california': ['CMF','PWZ','CXA'], 'china': ['FXI','EWH','MCHI','GXC','ASHR','FNI','PGJ','KWEB','HAO','PEK','CNXT','ASHS','YAO','ECNS','CN','CXSE','FCA','KBA','AFTY','CHNA','KFYP'], 'commodities': ['DBC','DJP','GSG','USCI','RJI','GCC','FTGC','GSC','DJCI','UCI','GSP','BCM','PDBC','GRN','SBV','CSCB','CSCR'], 'commodity': ['GDX','GUNR','IGE','GDXJ','MOO','GNR','XME','WOOD','CUT','URA','SIL','SGDM','PICK','HAP','SLX','GRES','RING','LIT','REMX','CRBQ','PAGG','GLDX','VEGI','SGDJ','COPX','PSAU','GNAT','CU','CROP','SLVP','SOIL','PLTM','SILJ','JUNR'], 'communications': ['VOX','IYZ','IXP','IST','XTL','FONE'], 'consumer_discretionary': ['XLY','FXD','VCR','IYC','XRT','FDIS','RXI','PEZ','PEJ','RTH','RCD','PBS','PSCD','CHIQ','INCO','CARZ','BJK','PMR','IPD'], 'consumer_staples': ['XLP','FXG','VDC','IYK','ECON','KXI','RHS','PSL','PBJ','FSTA','IPS','PSCC','BRAQ'], 'corporate': ['LQD','VCSH','CSJ','CIU','VCIT','SCPB','FLOT','VCLT','BSCH','ITR','CLY','BSCI','BSCG','BSCJ','BSCK','BSCF','CORP','MINC','LWC','BSCL','BSCM','PICB','IBND','IBCC','IGHG','FLTB','RAVI','IBDB','FLTR','IBDC','QLTA','SLQD','IBDA','IBDD','IBCD','BSCO','IBDH','BSCN','IBCE','IBDF','IBCB','PFIG','FCOR','FLRT','CBND','IBDJ','LQDH','SKOR','CLYH','CRDT','LDRI','IGIH'], 'currency': ['UUP','FXE','USDU','FXC','FXA','FXF','FXY','DBV','CYB','FXB','CEW','UDN','FXS','CNY','EUFX','BZF','FORX','ICN','FXCH','CCX','FXSG','AYT','ERO','GBB','ICI','JEM','JYN','INR','PGD'], 'diversified': ['MDIV','AOR','AOA','AOM','WBII','WBIH','IYLD','AOK','GAL','GYLD','INKM','YYY','TUTI','GAA','GMOM','MLTI','DVHI','FDIV','MATH','SCTO','YDIV','PERM','GTAA','EFFE','GIVE','GCE','DBIZ','HIPS'], 'emerging_markets_bonds': ['EMB','PCY','EMLC','LEMB','VWOB','ELD','DSUM','EMCB','EBND','KCNY','CHNB','CEMB','CBON','EMCD','EMAG','EMIH','PFEM','FEMB','EMBH'], 'emerging_markets_equities': ['VWO','EEM','IEMG','INDA','EEMV','RSX','EPI','DEM','SCHE','DGS','INDY','FM','PIN','VNM','EZA','TUR','EWX','AIA','PXH','FNDE','EDIV','EIDO','EWM','INP','EPHE','THD','ERUS','HEEM','GMM','TLTE','SCIF','BKF','PIE','EPOL','GEM','BBRC','EELV','DVYE','DBEM','FEM','ADRE','EMFM','BIK','IDX','EEB','EEMS','QEMM','AFK','SMIN','QAT','GUR','FRN','RSXJ','EGPT','JPEM','GAF','DGRE','FEMS','EMDD','UAE','RBL','GULF','NGE','SCIN','HILO','PLND','ASEA','EMCG','ROAM','MES','EMQQ','EWEM','EDOG','BICK','IDXJ','PAK','EMCR','KSA','QEM','EMFT','QDEM','SDEM','EMBB','AZIA','KLEM','KEMP','XSOE','XCEM','EEHB'], 'energy': ['XLE','VDE','XOP','OIH','IYE','IXC','IEO','IEZ','FENY','FXN','FCG','XES','RYE','PXI','PXE','KOL','PXJ','FRAK','PSCE','FILL','ENY','IPW','CRAK','IOIL','CHIE'], 'europe': ['HEDJ','VGK','EZU','EWG','FEZ','DBEU','IEV','EWU','HEZU','EWP','HEWG','EWI','EWL','DFE','FEEU','IEUR','FEP','EWQ','EWD','DXGE','GREK','FEU','EUSC','FKU','FGM','FSZ','FDD','FXEU','EWN','EIRL','EWK','DBGR','HEWI','NORW','EWO','HEWP','IEUS','DBEZ','GXF','EDEN','HFXE','PGAL','DXPS','SMEZ','EUMV','ENOR','EWGS','EFNL','HGEU','ADRU','EUDG','EWUS','DAX','FEUZ','QDEU','HFEZ','STXX','HEWU','HEWL','DBUK','EUDV','OEUR','OEUH','QGBR','HDEZ','SBEU','SCID','QESP'], 'financials': ['XLF','VFH','KBE','KRE','IYF','FXO','IYG','KIE','KBWB','IAT','PSP','EUFN','IAI','KBWD','FNCL','IXG','RYF','PSCF','QABA','IAK','KCE','KBWP','BIZD','BDCS','CHIX','KBWR','PFI','RWW','KBWI','JHMF','PEX','KBWC','IPF','XLFS','BRAF'], 'foreign_large': ['EFA','VEA','DBEF','IEFA','SCHF','EFAV','IDV','HEFA','EFV','EWC','EFG','PID','DWX','PXF','FNDF','DWM','TLTD','IHDG','DOL','IDLV','DTH','DOO','PIZ','FDT','EIS','DGT','ADRD','IEIL','IPKW','HFXI','FYLD','CIZ','RODM','HGI','IDHQ','IVAL','FWDI','FCFI','FCAN','QCAN','INTF','KLDW','QEFA','HDEF','IDHB','HDWM','HEWC','CIL','CID'], 'foreign_small': ['SCZ','VSS','DLS','GWX','SCHC','FNDC','DIM','PDN','MDD','IEIS','HSCZ','CNDA','FDTS','ISCF','HDLS'], 'global_equities': ['VEU','ACWI','VT','VXUS','ACWX','ACWV','IXUS','IOO','FIGY','SDIV','GWL','CWI','IFV','VIDI','NFRA','IQDF','FGD','TOK','URTH','IDOG','DEW','LOWC','IQDE','DNL','WDIV','GVAL','DBAW','LVL','ISRA','JPGE','JETS','ACIM','IQDY','EPRO','RTR','VEGA','AADR','EFAD','MOTI','HDAW','EQLT','DXUS','CCXE','DIVI','ROGS','QWLD','QXUS','QDXU','BCHP','SPUN','HAWX','ACWF','RGRO','IPOS','FPXI','GURI'], 'global_real': ['RWX','VNQI','RWO','IFGL','WPS','GQRE','DRW','GRI','FFR','IFEU','REET','TAO','DBRE','EMRE'], 'government': ['SHY','IEF','TLT','IEI','GOVT','SCHO','VGSH','AGZ','TLH','SCHR','VGIT','EDV','ITE','VGLT','TLO','PLW','FTSD','ZROZ','TUZ','SST','TIPX','TENZ','TFLO','FIVZ','DLBL','DTYL','DFVL','SIPE','DTUL','STPP','USFR'], 'health': ['XLV','IBB','VHT','FXH','FBT','XBI','IYH','PJP','IXJ','IHE','IHF','FHLC','XPH','IHI','BBH','RYH','PBE','PPH','PSCH','PTH','XHS','SBIO','IRY','XHE','BBC','BBP','JHMH','JHMT','ARKG','CNCR'], 'hedge': ['QAI','WDTI','ALFA','MNA','RLY','HDG','DIVY','ALTS','CPI','QMN','MCRO','FMF','DRVN','HHFR','HHDG','FUTS','MRGR','QEH','CSMA','RRF','VAMO','QED','QLS'], 'high': ['HYG','JNK','BKLN','SJNK','HYS','SHYG','SRLN','BSJG','PHB','BSJH','HYLS','BSJI','BSJF','FTSL','SNLN','HYEM','HYLD','BSJJ','HYXU','IHY','GHYG','HYHG','BSJK','EMHY','QLTB','HYGH','ANGL','CJNK','PGHY','YPRO','IJNK','BSJL','BSJM','HYZD','HYND','QLTC','HYIH','WYDE','THHY','TYTE'], 'industrials': ['XLI','VIS','IYJ','ITA','FXR','PPA','EXI','XAR','FIDU','RGI','PRN','PSCI','AIRR','IPN','EVX','ARKQ','CHII'], 'inflation': ['TIP','TDTT','VTIP','STPZ','SCHP','WIP','IPE','STIP','TDTF','LTPZ','ILB','TIPZ','ITIP','GTIP'], 'international': ['BWX','IGOV','BWZ','ISHG','AUNZ','ALD','GGOV'], 'inverse_bonds': ['TBF','TMV','PST','SJB','DTYS','TYO','TBX','DLBS','JGBD','TAPR','JGBS','TYBS','DTUS','RISE','FLAT','DFVS','SAGG','IGS','TYNS'], 'inverse_commodities': ['DNO','DGZ','SZO','DDP','BOS'], 'inverse_equities': ['SH','RWM','DOG','EUM','PSQ','HDGE','CHAD','JDST','EFZ','LABD','SEF','MYY','SBB','DDG','YXI','ZBIO','MLPS','DRIP','CLAW','PILS','HAKD','WDRW','GDJS','HBZ','TOTS','GDXS','SBM','KRS'], 'inverse_volatility': ['XIV','SVXY','ZIV','IVOP','XXV','VXDN'], 'japan': ['EWJ','DXJ','DBJP','HEWJ','DFJ','SCJ','DXJS','ITF','FJP','JSC','NKY','DXJR','JPMV','JPP','HGJP','HFXJ','DXJF','QJPN','JPN','DXJH','DXJT','DXJC','SCIJ','JDG'], 'large_cap_blend': ['SPY','IVV','VOO','IWB','RSP','VV','SPLV','SCHX','OEF','FV','FEX','MGC','JKD','SPHQ','VONE','XLG','TRND','DSI','CSM','RWL','KLD','PBP','EQAL','EQL','CFO','XRLV','GSLC','IWL','SPHB','EWRI','HSPX','ELR','EQWL','FWDD','LGLV','CAPE','WIL','JPUS','IBLN','VALX','CFA','QYLD','VSPY','SPGH','FMK','JHML','JHMC','DHVW','SPYB','BWV','IQLT','IMTM','QVM','QUS','SPXV','SPXN','SPXE','SPXT','SYE','SCIU','ZLRG','USSD','USWD','ERW','EEH','QGTA','SLOW','UK'], 'large_cap_growth': ['QQQ','IWF','VUG','IVW','SCHG','RPG','MGK','IUSG','JKE','FTC','VOOG','SPYG','QQEW','IWY','VONG','PWB','QQXT','FBG','PXLG','WBIE','QQQE','CFGE','RPX','SYG','RWG','CAPX','SLDR'], 'large_cap_value': ['IWD','VIG','VTV','DVY','SDY','DIA','VYM','IVE','PRF','HDV','DLN','SCHV','FVD','SDOG','FTA','MGV','PWV','DTN','DHS','NOBL','FNDX','FDL','RPV','IUSV','VLUE','DGRW','CVY','SPHD','DTD','VONV','VOOV','PFM','DIV','JKF','DGRO','SPYV','DVP','DEF','SYLD','IWX','EPS','WBIG','WBIL','WBIF','FTCS','DIVC','CDC','IELG','EXT','RDIV','QVAL','EZY','PXLV','DOD','RDVY','OUSA','ROUS','SBUS','VLML','FTHI','GVT','LRGF','VLLV','FTLB','CDL','SYV'], 'latin': ['EWZ','EWW','ILF','ECH','EPU','BRF','GXG','BRZU','EWZS','GML','ARGT','ICOL','EEML','DBMX','FLN','BRAZ','DBBR','AND','HEWW','QMEX','FBZ'], 'leveraged_bonds': ['TBT','TTT','UST','TMF','UBT','SBND','BUNT','LBND','TYD','SYTL','JGBT','IGU','TBZ','UJB','TPS'], 'leveraged_commodities': ['UWTI','UCO','UGAZ','AGQ','DWTI','SCO','USLV','DGP','GLL','UGL','DZZ','ZSL','DGAZ','DTO','BOIL','UGLD','DSLV','DGLD','KOLD','UCD','DAG','CMD','BOM','DEE','BDD','DYY'], 'leveraged_currency': ['EUO','YCS','DRR','CROC','ULE','YCL','URR'], 'leveraged_equities': ['SSO','SDS','FAS','TQQQ','QLD','UPRO','FBGX','TNA','UYG','BIB','FLGE','SPXU','SPXL','NUGT','ERX','TZA','SQQQ','QID','SPXS','CURE','DUST','FAZ','DDM','MLPL','BDCL','DXD','RUSL','TECL','EDC','UDOW','TWM','UWM','YINN','CEFL','SDOW','RXL','LABU','DIG','ROM','SOXL','MVV','BIS','EDZ','YANG','JNUG','INDL','URTY','CHAU','SRTY','ERY','EEV','RETL','MIDU','FXP','UYM','SKF','GASL','EPV','UBIO','DVYL','DUG','RUSS','UMDD','SOXS','DZK','SPLX','UPV','BZQ','UCC','XPP','USD','HDLV','LMLP','HOML','UPW','EFO','UGE','SDYL','SAA','EET','UXI','SMN','MLPV','TECS','EZJ','SMHD','EWV','JPNL','FINU','GUSH','LBJ','DPK','KRU','MIDZ','SPUU','MZZ','REW','EFU','SIJ','SMDD','LTL','FINZ','UMX','SDD','SDP','RXD','UBR','DPST','HAKK','PILL','SSG','NAIL','HBU','SCC','SOP','MATL','HEGE','UOP','GDJJ','HEGJ','UXJ','SZK','LLDM','LLSP','LLSC','JPX','SMK','LLEM','GDXX','TLL'], 'leveraged_multi': ['DVHL'], 'leveraged_real': ['MORL','URE','DRN','REK','SRS','LRET','RWXL','DRV'], 'leveraged_volatility': ['UVXY','TVIX','TVIZ'], 'long': ['HVPW','RALS','FTLS','CSLS','HTUS','LALT','FLAG','BTAL','AGLS','LSC','JGBB','DIVA','RINF','MOM','CHEP','SIZ'], 'materials': ['XLB','VAW','IYM','MXI','FXZ','FMAT','PYZ','RTM','PSCM','IRV','CHIM'], 'metals': ['DBB','JJC','RJZ','JJM','JJN','UBM','LEDD','CPER','JJU','JJT','CUPM','FOIL','NINI','LD','HEVY'], 'mid_cap_blend': ['IJH','MDY','IWR','VO','VXF','SCHM','FNX','JKG','IVOO','RWK','CZA','EWRM','XMLV','EQWM','REGL','JHMM','MDLL'], 'mid_cap_growth': ['IWP','IJK','VOT','RFG','IVOG','MDYG','JKH','WBIA','FNY','PXMG'], 'mid_cap_value': ['IWS','VOE','IJJ','DON','EZM','JKI','MDYV','WBIC','IVOV','RFV','WBIB','WBID','FNK','PXMV','VLSM','SMDV'], 'mlps': ['AMLP','AMJ','MLPI','EMLP','MLPN','IMLP','AMU','ATMP','MLPA','YMLP','MLPC','MLPX','MLPO','ZMLP','MLPY','OSMS','YMLI','MLPG','YGRO','AMZA','FMLP','ENFR','MLPW','MLPJ'], 'money': ['MINT','SHV','BIL','NEAR','GSY','PVI','ULST'], 'mortgage': ['MBB','VMBS','CMBS','MBG','GNMA','MBSD','LMBS','COBO'], 'national': ['MUB','SHM','HYD','TFI','ITM','SUB','PZA','BAB','HYMB','SMB','MUNI','IBMF','IBME','SHYD','MLN','IBMH','VTEB','IBMI','SMMU','XMPT','BABS','MEAR','RVNU','PRB','GMMB'], 'new': ['NYF','PZT','INY'], 'oil': ['USO','OIL','UNG','DBO','DBE','BNO','UGA','USL','RJN','UNL','OLO','GAZ','OLEM','UHN','UBN','ONG','FUE','JJE','DCNG'], 'precious': ['GLD','IAU','SLV','SGOL','PPLT','SIVR','PALL','DGL','GLTR','DBP','OUNZ','PTM','DBS','WITE','GYEN','GEUR','UBG','PGM','USV','JJP','BLNG','GLDI','SLVO'], 'preferred': ['PFF','PGX','CWB','PGF','FPE','VRP','PSK','PFXF','SPFF','IPFF'], 'real': ['VNQ','IYR','ICF','RWR','SCHH','REM','REZ','FRI','KBWY','MORT','ROOF','FTY','PSR','FREL','WREI','SRET','EWRE'], 'small_cap_blend': ['IWM','IJR','VB','SCHA','PRFZ','IWC','FYX','VTWO','DWAS','SLY','RWJ','VIOO','JKJ','XSLV','TWOK','FDM','EWRS','SMLV','DGRS','CSF','PZI','WMCR','EQWS','CSA','SMLL','ZSML','GURX'], 'small_cap_growth': ['IWO','VBK','IJT','SLYG','RZG','VTWG','JKK','VIOG','FYC','RSCO','FFTY','PXSG'], 'small_cap_value': ['IWN','VBR','IJS','DES','FNDA','SLYV','EES','JKL','RZV','VIOV','VTWV','PXSV','FYT','IESM','CSB','SMLF'], 'target': ['TDV', 'TDN'], 'technology': ['XLK','VGT','FDN','IYW','HACK','IGV','IGM','IXN','RYT','FXL','XT','SKYY','TDIV','MTK','SOXX','FTEC','PSCT','QTEC','SMH','PNQI','PTF','XSD','IGN','PSJ','ROBO','CIBR','SOCL','FCOM','PSI','CQQQ','XSW','PXQ','QQQC','ARKW','IPK','ARKK','IPAY','BDAT'], 'total': ['AGG','BND','BSV','BIV','BNDX','BOND','GVI','SCHZ','BLV','TOTL','LAG','PCEF','RIGS','ISTB','IUSB','VBND','FLRN','GBF','NFLT','FTSM','ILTB','FBND','INC','HOLD','AGZD','FWDB','AGND','BYLD','GMTB','AGGY','UBND'], 'transportation': ['IYT','XTN','SEA'], 'utilities': ['XLU','VPU','IGF','IDU','FXU','JXI','FUTY','GHII','RYU','GII','EMIF','INXX','IPU','PXR','PUI','TOLZ','DBU','PSCU','GRID','BRXX','DBIF','UTES'], 'volatility': ['VXX','VIXY','VXZ','VIXM','XVIX','VIIX','CVOL','VIIZ','VXUP'], 'volatility_hedged': ['PHDG','VQT','SPXH','TRSK','XVZ','VQTS','VIXH'], 'water': ['PHO','CGW','PIO','FIW']}

categories = {'agricultural': 'Agricultural Commodities', 'all': 'All Cap Equities', 'alternative': 'Alternative Energy Equities', 'asia': 'Asia Pacific Equities', 'building': 'Building & Construction ', 'california': 'California Munis', 'china': 'China Equities', 'commodities': 'Commodities', 'commodity': 'Commodity Producers Equities', 'communications': 'Communications Equities', 'consumer_discretionary': 'Consumer Discretionary Equities', 'consumer_staples': 'Consumer Staples Equities', 'corporate': 'Corporate Bonds', 'currency': 'Currency', 'diversified': 'Diversified Portfolio', 'emerging_markets_bonds': 'Emerging Markets Bonds', 'emerging_markets_equities': 'Emerging Markets Equities', 'energy': 'Energy Equities', 'europe': 'Europe Equities', 'financials': 'Financials Equities', 'foreign_large': 'Foreign Large Cap Equities', 'foreign_small': 'Foreign Small & Mid Cap Equities', 'global_equities': 'Global Equities', 'global_real': 'Global Real Estate', 'government': 'Government Bonds', 'health': 'Health & Biotech Equities', 'hedge': 'Hedge Fund', 'high': 'High Yield Bonds', 'industrials': 'Industrials Equities', 'inflation': 'Inflation-Protected Bonds', 'international': 'International Government Bonds', 'inverse_bonds': 'Inverse Bonds', 'inverse_commodities': 'Inverse Commodities', 'inverse_equities': 'Inverse Equities', 'inverse_volatility': 'Inverse Volatility', 'japan': 'Japan Equities', 'large_cap_blend': 'Large Cap Blend Equities', 'large_cap_growth': 'Large Cap Growth Equities', 'large_cap_value': 'Large Cap Value Equities', 'latin': 'Latin America Equities', 'leveraged_bonds': 'Leveraged Bonds', 'leveraged_commodities': 'Leveraged Commodities', 'leveraged_currency': 'Leveraged Currency', 'leveraged_equities': 'Leveraged Equities', 'leveraged_multi': 'Leveraged Multi-Asset', 'leveraged_real': 'Leveraged Real Estate', 'leveraged_volatility': 'Leveraged Volatility', 'long': 'Long-Short', 'materials': 'Materials', 'metals': 'Metals', 'mid_cap_blend': 'Mid Cap Blend Equities', 'mid_cap_growth': 'Mid Cap Growth Equities', 'mid_cap_value': 'Mid Cap Value Equities', 'mlps': 'MLPs', 'money': 'Money Market', 'mortgage': 'Mortgage Backed Securities', 'national': 'National Munis', 'new': 'New York Munis', 'oil': 'Oil & Gas', 'precious': 'Precious Metals', 'preferred': 'Preferred Stock/Convertible Bonds', 'real': 'Real Estate', 'small_cap_blend': 'Small Cap Blend Equities', 'small_cap_growth': 'Small Cap Growth Equities', 'small_cap_value': 'Small Cap Value Equities', 'target': 'Target Retirement Date', 'technology': 'Technology Equities', 'total': 'Total Bond Market', 'transportation': 'Transportation Equities', 'utilities': 'Utilities Equities', 'volatility': 'Volatility', 'volatility_hedged': 'Volatility Hedged Equity', 'water': 'Water Equities'}