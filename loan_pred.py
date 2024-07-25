from pydantic import BaseModel

class LoanPred(BaseModel):
    date_decision: int
    MONTH: float
    WEEK_NUM: float
    actualdpdtolerance_344P: float
    amtinstpaidbefduel24m_4187115A: float
    annuity_780A: float
    annuitynextmonth_57A: float
    applicationcnt_361L: float
    applications30d_658L: float
    applicationscnt_1086L: float
    applicationscnt_464L: float
    applicationscnt_629L: float
    applicationscnt_867L: float
    avgdbddpdlast24m_3658932P: float
    avgdbddpdlast3m_4187120P: float
    avgdbdtollast24m_4525197P: float
    avgdpdtolclosure24_3658938P: float
    avginstallast24m_3658937A: float
    avglnamtstart24m_4525187A: float
    avgmaxdpdlast9m_3716943P: float
    avgoutstandbalancel6m_4187114A: float
    avgpmtlast12m_4525200A: float
    clientscnt12m_3712952L: float
    clientscnt3m_3712950L: float
    clientscnt6m_3712949L: float
    clientscnt_100L: float
    clientscnt_1022L: float
    clientscnt_1071L: float
    clientscnt_1130L: float
    clientscnt_136L: float
    clientscnt_157L: float
    clientscnt_257L: float
    clientscnt_304L: float
    clientscnt_360L: float
    clientscnt_493L: float
    clientscnt_533L: float
    clientscnt_887L: float
    clientscnt_946L: float
    cntincpaycont9m_3716944L: float
    cntpmts24_3658933L: float
    commnoinclast6m_3546845L: float
    credamount_770A: float
    currdebt_22A: float
    currdebtcredtyperange_828A: float
    daysoverduetolerancedd_3976961L: float
    deferredmnthsnum_166L: float
    disbursedcredamount_1113A: float
    downpmt_116A: float
    eir_270L: float
    homephncnt_628L: float
    inittransactionamount_650A: float
    interestrate_311L: float
    interestrategrace_34L: float
    lastapprcredamount_781A: float
    lastdependentsnum_448L: float
    lastotherinc_902A: float
    lastotherlnsexpense_631A: float
    lastrejectcredamount_222A: float
    maininc_215A: float
    mastercontrelectronic_519L: float
    mastercontrexist_109L: float
    maxannuity_159A: float
    maxannuity_4075009A: float
    maxdbddpdlast1m_3658939P: float
    maxdbddpdtollast12m_3658940P: float
    maxdbddpdtollast6m_4187119P: float
    maxdebt4_972A: float
    maxdpdfrom6mto36m_3546853P: float
    maxdpdinstlnum_3546846P: float
    maxdpdlast12m_727P: float
    maxdpdlast24m_143P: float
    maxdpdlast3m_392P: float
    maxdpdlast6m_474P: float
    maxdpdlast9m_1059P: float
    maxdpdtolerance_374P: float
    maxinstallast24m_3658928A: float
    maxlnamtstart6m_4525199A: float
    maxoutstandbalancel12m_4187113A: float
    maxpmtlast3m_4525190A: float
    mindbddpdlast24m_3658935P: float
    mindbdtollast24m_4525191P: float
    mobilephncnt_593L: float
    monthsannuity_845L: float
    numactivecreds_622L: float
    numactivecredschannel_414L: float
    numactiverelcontr_750L: float
    numcontrs3months_479L: float
    numincomingpmts_3546848L: float
    numinstlallpaidearly3d_817L: float
    numinstls_657L: float
    numinstlsallpaid_934L: float
    numinstlswithdpd10_728L: float
    numinstlswithdpd5_4187116L: float
    numinstlswithoutdpd_562L: float
    numinstmatpaidtearly2d_4499204L: float
    numinstpaid_4499208L: float
    numinstpaidearly3d_3546850L: float
    numinstpaidearly3dest_4493216L: float
    numinstpaidearly5d_1087L: float
    numinstpaidearly5dest_4493211L: float
    numinstpaidearly5dobd_4499205L: float
    numinstpaidearly_338L: float
    numinstpaidearlyest_4493214L: float
    numinstpaidlastcontr_4325080L: float
    numinstpaidlate1d_3546852L: float
    numinstregularpaid_973L: float
    numinstregularpaidest_4493210L: float
    numinsttopaygr_769L: float
    numinsttopaygrest_4493213L: float
    numinstunpaidmax_3546851L: float
    numinstunpaidmaxest_4493212L: float
    numnotactivated_1143L: float
    numpmtchanneldd_318L: float
    numrejects9m_859L: float
    pctinstlsallpaidearl3d_427L: float
    pctinstlsallpaidlat10d_839L: float
    pctinstlsallpaidlate1d_3546856L: float
    pctinstlsallpaidlate4d_3546849L: float
    pctinstlsallpaidlate6d_3546844L: float
    pmtnum_254L: float
    posfpd10lastmonth_333P: float
    posfpd30lastmonth_3976960P: float
    posfstqpd30lastmonth_3976962P: float
    price_1097A: float
    sellerplacecnt_915L: float
    sellerplacescnt_216L: float
    sumoutstandtotal_3546847A: float
    sumoutstandtotalest_4493215A: float
    totaldebt_9A: float
    totalsettled_863A: float
    totinstallast1m_4525188A: float
    contractssum_5085716L: float
    days120_123L: float
    days180_256L: float
    days30_165L: float
    days360_512L: float
    days90_310L: float
    firstquarter_103L: float
    for3years_128L: float
    for3years_504L: float
    for3years_584L: float
    formonth_118L: float
    formonth_206L: float
    formonth_535L: float
    forquarter_1017L: float
    forquarter_462L: float
    forquarter_634L: float
    fortoday_1092L: float
    forweek_1077L: float
    forweek_528L: float
    forweek_601L: float
    foryear_618L: float
    foryear_818L: float
    foryear_850L: float
    fourthquarter_440L: float
    numberofqueries_373L: float
    pmtaverage_3A: float
    pmtaverage_4527227A: float
    pmtaverage_4955615A: float
    pmtcount_4527229L: float
    pmtcount_4955617L: float
    pmtcount_693L: float
    pmtscount_423L: float
    pmtssum_45A: float
    riskassesment_940T: float
    secondquarter_766L: float
    thirdquarter_1082L: float
    bankacctype_710L: str | None
    cardtype_51L: str | None
    credtype_322L: str | None
    disbursementtype_67L: str | None
    equalitydataagreement_891L: bool | None
    equalityempfrom_62L: bool | None
    inittransactioncode_186L: str | None
    isbidproduct_1095L: bool | None
    isbidproductrequest_292L: bool | None
    isdebitcard_729L: bool | None
    lastapprcommoditycat_1041M: str | None
    lastapprcommoditytypec_5251766M: str | None
    lastcancelreason_561M: str | None
    lastrejectcommoditycat_161M: str | None
    lastrejectcommodtypec_5251769M: str | None
    lastrejectreason_759M: str | None
    lastrejectreasonclient_4145040M: str | None
    lastst_736L: str | None
    opencred_647L: bool | None
    paytype1st_925L: str | None
    paytype_783L: str | None
    previouscontdistrict_112M: str | None
    twobodfilling_608L: str | None
    typesuite_864L: str | None
    description_5085714M: str | None
    education_1103M: str | None
    education_88M: str | None
    maritalst_385M: str | None
    maritalst_893M: str | None
    requesttype_4525192L: str | None
    riskassesment_302T: str | None
    datefirstoffer_1144D: int
    datelastinstal40dpd_247D: int
    datelastunpaid_3546854D: int
    dtlastpmtallstes_4499206D: int
    firstclxcampaign_1125D: int
    firstdatedue_489D: int
    lastactivateddate_801D: int
    lastapplicationdate_877D: int
    lastapprdate_640D: int
    lastdelinqdate_224D: int
    lastrejectdate_50D: int
    lastrepayingdate_696D: int
    maxdpdinstldate_3546855D: int
    validfrom_1069D: int
    assignmentdate_238D: int
    assignmentdate_4527235D: int
    assignmentdate_4955616D: int
    birthdate_574D: int
    dateofbirth_337D: int
    dateofbirth_342D: int
    responsedate_1012D: int
    responsedate_4527233D: int
    responsedate_4917613D: int
    payvacationpostpone_4187118D: int