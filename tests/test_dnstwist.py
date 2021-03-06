"""Test of the basics of dnstwist."""
import dnstwister.dnstwist.dnstwist as dnstwist


def test_unicode_fuzzing():
    """Test can fuzz and generate unicode."""
    unicode_domain = 'xn--domain.com'.decode('idna')

    fuzzer = dnstwist.fuzz_domain(unicode_domain)
    fuzzer.fuzz()

    assert sorted([d['domain-name'] for d in fuzzer.domains]) == [
        u'www-\u3bd9\u3bdc\u3bd9\u3bdf.com',
        u'www\u3bd9\u3bdc\u3bd9\u3bdf.com',
        u'ww\u3bd9\u3bdc\u3bd9\u3bdf.com',
        u'\u3bd9-\u3bdc\u3bd9\u3bdf.com',
        u'\u3bd9.\u3bdc\u3bd9\u3bdf.com',
        u'\u3bd9\u3bd9\u3bdc\u3bd9\u3bdf.com',
        u'\u3bd9\u3bd9\u3bdc\u3bdf.com',
        u'\u3bd9\u3bd9\u3bdf.com',
        u'\u3bd9\u3bdc-\u3bd9\u3bdf.com',
        u'\u3bd9\u3bdc.\u3bd9\u3bdf.com',
        u'\u3bd9\u3bdc\u3bd9-\u3bdf.com',
        u'\u3bd9\u3bdc\u3bd9.com',
        u'\u3bd9\u3bdc\u3bd9.\u3bdf.com',
        u'\u3bd9\u3bdc\u3bd9\u3bd9\u3bdf.com',
        u'\u3bd9\u3bdc\u3bd9\u3bdf.com',
        u'\u3bd9\u3bdc\u3bd9\u3bdfa.com',
        u'\u3bd9\u3bdc\u3bd9\u3bdfb.com',
        u'\u3bd9\u3bdc\u3bd9\u3bdfc.com',
        u'\u3bd9\u3bdc\u3bd9\u3bdfcom.com',
        u'\u3bd9\u3bdc\u3bd9\u3bdfd.com',
        u'\u3bd9\u3bdc\u3bd9\u3bdfe.com',
        u'\u3bd9\u3bdc\u3bd9\u3bdff.com',
        u'\u3bd9\u3bdc\u3bd9\u3bdfg.com',
        u'\u3bd9\u3bdc\u3bd9\u3bdfh.com',
        u'\u3bd9\u3bdc\u3bd9\u3bdfi.com',
        u'\u3bd9\u3bdc\u3bd9\u3bdfj.com',
        u'\u3bd9\u3bdc\u3bd9\u3bdfk.com',
        u'\u3bd9\u3bdc\u3bd9\u3bdfl.com',
        u'\u3bd9\u3bdc\u3bd9\u3bdfm.com',
        u'\u3bd9\u3bdc\u3bd9\u3bdfn.com',
        u'\u3bd9\u3bdc\u3bd9\u3bdfo.com',
        u'\u3bd9\u3bdc\u3bd9\u3bdfp.com',
        u'\u3bd9\u3bdc\u3bd9\u3bdfq.com',
        u'\u3bd9\u3bdc\u3bd9\u3bdfr.com',
        u'\u3bd9\u3bdc\u3bd9\u3bdfs.com',
        u'\u3bd9\u3bdc\u3bd9\u3bdft.com',
        u'\u3bd9\u3bdc\u3bd9\u3bdfu.com',
        u'\u3bd9\u3bdc\u3bd9\u3bdfv.com',
        u'\u3bd9\u3bdc\u3bd9\u3bdfw.com',
        u'\u3bd9\u3bdc\u3bd9\u3bdfx.com',
        u'\u3bd9\u3bdc\u3bd9\u3bdfy.com',
        u'\u3bd9\u3bdc\u3bd9\u3bdfz.com',
        u'\u3bd9\u3bdc\u3bd9\u3bdf\u3bdf.com',
        u'\u3bd9\u3bdc\u3bdc\u3bd9\u3bdf.com',
        u'\u3bd9\u3bdc\u3bdf.com',
        u'\u3bd9\u3bdc\u3bdf\u3bd9.com',
        u'\u3bdc\u3bd9\u3bd9\u3bdf.com',
        u'\u3bdc\u3bd9\u3bdf.com',
    ]


def test_top_level_domains_db_is_loaded():
    """The TLD database should be loaded."""
    assert dnstwist.DB_TLD


def test_basic_fuzz():
    """Test of the fuzzer.

    This'll be high-maintenance, but will help track changes over time.
    """
    fuzzer = dnstwist.fuzz_domain('www.example.com')
    fuzzer.fuzz()

    assert sorted([d['domain-name'] for d in fuzzer.domains]) == [
        '2ww.example.com',
        '3ww.example.com',
        '7ww.example.com',
        'aww.example.com',
        'eww.example.com',
        'gww.example.com',
        'qww.example.com',
        'sww.example.com',
        'uww.example.com',
        'vvvvvv.example.com',
        'vvvvw.example.com',
        'vvww.example.com',
        'vww.example.com',
        'w-ww.example.com',
        'w.example.com',
        'w.ww.example.com',
        'w2w.example.com',
        'w2ww.example.com',
        'w3w.example.com',
        'w3ww.example.com',
        'w7w.example.com',
        'waw.example.com',
        'waww.example.com',
        'wew.example.com',
        'weww.example.com',
        'wgw.example.com',
        'wqw.example.com',
        'wqww.example.com',
        'wsw.example.com',
        'wsww.example.com',
        'wuw.example.com',
        'wvvvv.example.com',
        'wvvw.example.com',
        'wvw.example.com',
        'ww-w.example.com',
        'ww.example.com',
        'ww.w.example.com',
        'ww.wexample.com',
        'ww2.example.com',
        'ww2w.example.com',
        'ww3.example.com',
        'ww3w.example.com',
        'ww7.example.com',
        'wwa.example.com',
        'wwaw.example.com',
        'wwe.example.com',
        'wwew.example.com',
        'wwg.example.com',
        'wwq.example.com',
        'wwqw.example.com',
        'wws.example.com',
        'wwsw.example.com',
        'wwu.example.com',
        'wwv.example.com',
        'wwvv.example.com',
        'www.3example.com',
        'www.3xample.com',
        'www.4example.com',
        'www.4xample.com',
        'www.axample.com',
        'www.dexample.com',
        'www.dxample.com',
        'www.e-xample.com',
        'www.e.xample.com',
        'www.e3xample.com',
        'www.e4xample.com',
        'www.e8ample.com',
        'www.eample.com',
        'www.eaxmple.com',
        'www.ecample.com',
        'www.ecxample.com',
        'www.edample.com',
        'www.edxample.com',
        'www.eexample.com',
        'www.ehample.com',
        'www.epample.com',
        'www.erxample.com',
        'www.esample.com',
        'www.esxample.com',
        'www.ewxample.com',
        'www.ex-ample.com',
        'www.ex.ample.com',
        'www.ex1ample.com',
        'www.ex1mple.com',
        'www.ex2ample.com',
        'www.ex2mple.com',
        'www.exa-mple.com',
        'www.exa-ple.com',
        'www.exa.mple.com',
        'www.exa1mple.com',
        'www.exa2mple.com',
        'www.exaample.com',
        'www.exaeple.com',
        'www.exaiple.com',
        'www.exajmple.com',
        'www.exajple.com',
        'www.exakmple.com',
        'www.exakple.com',
        'www.exalmple.com',
        'www.exalple.com',
        'www.exam-ple.com',
        'www.exam.ple.com',
        'www.exam0le.com',
        'www.exam0ple.com',
        'www.examjple.com',
        'www.examkple.com',
        'www.examle.com',
        'www.examlle.com',
        'www.examlpe.com',
        'www.examlple.com',
        'www.exammle.com',
        'www.exammple.com',
        'www.examnple.com',
        'www.examole.com',
        'www.examople.com',
        'www.examp-le.com',
        'www.examp.le.com',
        'www.examp0le.com',
        'www.examp1e.com',
        'www.exampde.com',
        'www.exampe.com',
        'www.exampel.com',
        'www.examphe.com',
        'www.exampie.com',
        'www.exampke.com',
        'www.exampkle.com',
        'www.exampl-e.com',
        'www.exampl.com',
        'www.exampl.e.com',
        'www.exampl3.com',
        'www.exampl4.com',
        'www.exampla.com',
        'www.exampld.com',
        'www.example.com',
        'www.examplea.com',
        'www.exampleb.com',
        'www.examplec.com',
        'www.examplecom.com',
        'www.exampled.com',
        'www.examplee.com',
        'www.examplef.com',
        'www.exampleg.com',
        'www.exampleh.com',
        'www.examplei.com',
        'www.examplej.com',
        'www.examplek.com',
        'www.examplel.com',
        'www.examplem.com',
        'www.examplen.com',
        'www.exampleo.com',
        'www.examplep.com',
        'www.exampleq.com',
        'www.exampler.com',
        'www.examples.com',
        'www.examplet.com',
        'www.exampleu.com',
        'www.examplev.com',
        'www.examplew.com',
        'www.examplex.com',
        'www.exampley.com',
        'www.examplez.com',
        'www.examplg.com',
        'www.exampli.com',
        'www.examplke.com',
        'www.examplle.com',
        'www.examplm.com',
        'www.examplme.com',
        'www.examplo.com',
        'www.examploe.com',
        'www.examplpe.com',
        'www.examplr.com',
        'www.exampls.com',
        'www.examplu.com',
        'www.examplw.com',
        'www.examplz.com',
        u'www.exampl\xe9.com',
        u'www.exampl\xea.com',
        u'www.exampl\xeb.com',
        u'www.exampl\u0113.com',
        u'www.exampl\u0115.com',
        u'www.exampl\u0117.com',
        u'www.exampl\u0119.com',
        u'www.exampl\u011b.com',
        u'www.exampl\u03f5.com',
        u'www.exampl\u0435.com',
        u'www.exampl\u0454.com',
        u'www.exampl\u04bd.com',
        u'www.exampl\u1eb9.com',
        'www.exampme.com',
        'www.exampmle.com',
        'www.exampne.com',
        'www.exampoe.com',
        'www.exampole.com',
        'www.examppe.com',
        'www.exampple.com',
        u'www.examp\u0142e.com',
        u'www.examp\u026be.com',
        'www.examqle.com',
        'www.examrle.com',
        'www.examtle.com',
        'www.examxle.com',
        u'www.exam\xdele.com',
        u'www.exam\u01bfle.com',
        u'www.exam\u03c1le.com',
        u'www.exam\u03f7le.com',
        u'www.exam\u0440le.com',
        'www.exanmple.com',
        'www.exannple.com',
        'www.exanple.com',
        'www.exaople.com',
        'www.exaple.com',
        'www.exapmle.com',
        'www.exapmple.com',
        'www.exapple.com',
        'www.exaqmple.com',
        'www.exarnple.com',
        'www.exarrple.com',
        'www.exasmple.com',
        'www.exawmple.com',
        'www.exaymple.com',
        'www.exazmple.com',
        u'www.exa\u0271ple.com',
        u'www.exa\u043cple.com',
        u'www.exa\u1d0dple.com',
        u'www.exa\u1e43ple.com',
        'www.excample.com',
        'www.excmple.com',
        'www.exdample.com',
        'www.exemple.com',
        'www.eximple.com',
        'www.exmaple.com',
        'www.exmple.com',
        'www.exomple.com',
        'www.exqample.com',
        'www.exqmple.com',
        'www.exsample.com',
        'www.exsmple.com',
        'www.exumple.com',
        'www.exwample.com',
        'www.exwmple.com',
        'www.exxample.com',
        'www.exyample.com',
        'www.exymple.com',
        'www.exzample.com',
        'www.exzmple.com',
        u'www.ex\xe0mple.com',
        u'www.ex\xe1mple.com',
        u'www.ex\xe2mple.com',
        u'www.ex\xe3mple.com',
        u'www.ex\xe4mple.com',
        u'www.ex\xe5mple.com',
        u'www.ex\u0103mple.com',
        u'www.ex\u01cemple.com',
        u'www.ex\u0227mple.com',
        u'www.ex\u0251mple.com',
        u'www.ex\u0307ample.com',
        u'www.ex\u0430mple.com',
        u'www.ex\u04d3mple.com',
        u'www.ex\u1ea1mple.com',
        'www.eyample.com',
        'www.eyxample.com',
        'www.ezample.com',
        'www.ezxample.com',
        u'www.e\u0445ample.com',
        u'www.e\u04b3ample.com',
        'www.gxample.com',
        'www.ixample.com',
        'www.mxample.com',
        'www.oxample.com',
        'www.rexample.com',
        'www.rxample.com',
        'www.sexample.com',
        'www.sxample.com',
        'www.uxample.com',
        'www.wexample.com',
        'www.wxample.com',
        'www.xample.com',
        'www.xeample.com',
        'www.zexample.com',
        'www.zxample.com',
        u'www.\xe9xample.com',
        u'www.\xe9xampl\xe9.com',
        u'www.\xeaxample.com',
        u'www.\xeaxampl\xea.com',
        u'www.\xebxample.com',
        u'www.\xebxampl\xeb.com',
        u'www.\u0113xample.com',
        u'www.\u0113xampl\u0113.com',
        u'www.\u0115xample.com',
        u'www.\u0115xampl\u0115.com',
        u'www.\u0117xample.com',
        u'www.\u0117xampl\u0117.com',
        u'www.\u0119xample.com',
        u'www.\u0119xampl\u0119.com',
        u'www.\u011bxample.com',
        u'www.\u011bxampl\u011b.com',
        u'www.\u03f5xample.com',
        u'www.\u03f5xampl\u03f5.com',
        u'www.\u0435xample.com',
        u'www.\u0435xampl\u0435.com',
        u'www.\u0454xample.com',
        u'www.\u0454xampl\u0454.com',
        u'www.\u04bdxample.com',
        u'www.\u04bdxampl\u04bd.com',
        u'www.\u1eb9xample.com',
        u'www.\u1eb9xampl\u1eb9.com',
        'www2.example.com',
        'www3.example.com',
        'wwwa.example.com',
        'wwwe.example.com',
        'wwwe.xample.com',
        'wwwexample.com',
        'wwwnexample.com',
        'wwwq.example.com',
        'wwws.example.com',
        'wwww.example.com',
        'wwwx.example.com',
        'wwx.example.com',
        'wwxw.example.com',
        u'ww\u0461.example.com',
        u'ww\u051d.example.com',
        u'ww\u0561.example.com',
        'wxw.example.com',
        'wxww.example.com',
        u'w\u0461w.example.com',
        u'w\u0461\u0461.example.com',
        u'w\u051dw.example.com',
        u'w\u051d\u051d.example.com',
        u'w\u0561w.example.com',
        u'w\u0561\u0561.example.com',
        'xww.example.com',
        u'\u0461ww.example.com',
        u'\u0461\u0461w.example.com',
        u'\u0461\u0461\u0461.example.com',
        u'\u051dww.example.com',
        u'\u051d\u051dw.example.com',
        u'\u051d\u051d\u051d.example.com',
        u'\u0561ww.example.com',
        u'\u0561\u0561w.example.com',
        u'\u0561\u0561\u0561.example.com'
    ]

    assert fuzzer.domains == [
        {'domain-name': 'www.example.com', 'fuzzer': 'Original*'},
        {'domain-name': 'www.examplea.com', 'fuzzer': 'Addition'},
        {'domain-name': 'www.exampleb.com', 'fuzzer': 'Addition'},
        {'domain-name': 'www.examplec.com', 'fuzzer': 'Addition'},
        {'domain-name': 'www.exampled.com', 'fuzzer': 'Addition'},
        {'domain-name': 'www.examplee.com', 'fuzzer': 'Addition'},
        {'domain-name': 'www.examplef.com', 'fuzzer': 'Addition'},
        {'domain-name': 'www.exampleg.com', 'fuzzer': 'Addition'},
        {'domain-name': 'www.exampleh.com', 'fuzzer': 'Addition'},
        {'domain-name': 'www.examplei.com', 'fuzzer': 'Addition'},
        {'domain-name': 'www.examplej.com', 'fuzzer': 'Addition'},
        {'domain-name': 'www.examplek.com', 'fuzzer': 'Addition'},
        {'domain-name': 'www.examplel.com', 'fuzzer': 'Addition'},
        {'domain-name': 'www.examplem.com', 'fuzzer': 'Addition'},
        {'domain-name': 'www.examplen.com', 'fuzzer': 'Addition'},
        {'domain-name': 'www.exampleo.com', 'fuzzer': 'Addition'},
        {'domain-name': 'www.examplep.com', 'fuzzer': 'Addition'},
        {'domain-name': 'www.exampleq.com', 'fuzzer': 'Addition'},
        {'domain-name': 'www.exampler.com', 'fuzzer': 'Addition'},
        {'domain-name': 'www.examples.com', 'fuzzer': 'Addition'},
        {'domain-name': 'www.examplet.com', 'fuzzer': 'Addition'},
        {'domain-name': 'www.exampleu.com', 'fuzzer': 'Addition'},
        {'domain-name': 'www.examplev.com', 'fuzzer': 'Addition'},
        {'domain-name': 'www.examplew.com', 'fuzzer': 'Addition'},
        {'domain-name': 'www.examplex.com', 'fuzzer': 'Addition'},
        {'domain-name': 'www.exampley.com', 'fuzzer': 'Addition'},
        {'domain-name': 'www.examplez.com', 'fuzzer': 'Addition'},
        {'domain-name': 'vww.example.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'uww.example.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'sww.example.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'gww.example.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': '7ww.example.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'wvw.example.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'wuw.example.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'wsw.example.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'wgw.example.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'w7w.example.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'wwv.example.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'wwu.example.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'wws.example.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'wwg.example.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'ww7.example.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'wwwnexample.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'www.dxample.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'www.gxample.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'www.axample.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'www.mxample.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'www.uxample.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'www.eyample.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'www.ezample.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'www.epample.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'www.ehample.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'www.e8ample.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'www.excmple.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'www.exemple.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'www.eximple.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'www.exqmple.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'www.exalple.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'www.exaople.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'www.exaiple.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'www.exaeple.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'www.exa-ple.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'www.examqle.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'www.examrle.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'www.examtle.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'www.examxle.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'www.exam0le.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'www.exampme.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'www.exampne.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'www.examphe.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'www.exampde.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'www.exampld.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'www.examplg.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'www.exampla.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'www.examplm.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': 'www.examplu.com', 'fuzzer': 'Bitsquatting'},
        {'domain-name': u'www.\u0454xampl\u0454.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.ex\u0430mple.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.ex\u0307ample.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': 'vvvvw.example.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.exa\u043cple.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.exa\u0271ple.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.exampl\xeb.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.exampl\xea.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.exampl\xe9.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'\u0461ww.example.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.exam\u01bfle.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.ex\xe5mple.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': 'www.exanple.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.\u0454xample.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.\u0113xample.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.\u0119xampl\u0119.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.\u0117xampl\u0117.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.\u011bxample.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'ww\u051d.example.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'w\u0461w.example.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'\u0461\u0461\u0461.example.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.\xe9xampl\xe9.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': 'www.exampie.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.exampl\u1eb9.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.exampl\u04bd.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'w\u051d\u051d.example.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.\u04bdxampl\u04bd.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': 'vvww.example.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'ww\u0461.example.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'w\u0461\u0461.example.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.ex\u0103mple.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': 'wvvvv.example.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.ex\xe2mple.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.exampl\u0454.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.ex\xe3mple.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': 'wwvv.example.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.\u04bdxample.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': 'www.exannple.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'\u051d\u051d\u051d.example.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.ex\xe0mple.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.\u03f5xample.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'\u051d\u051dw.example.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.\xe9xample.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.exam\u0440le.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': 'www.exarrple.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.exam\xdele.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.examp\u026be.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.exampl\u0435.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.\u0435xampl\u0435.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.exa\u1d0dple.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.\xebxample.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.\u03f5xampl\u03f5.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.\xeaxampl\xea.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.e\u04b3ample.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.exam\u03f7le.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'w\u051dw.example.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'\u0561ww.example.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.ex\xe1mple.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.\u0117xample.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.exampl\u0115.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.\u011bxampl\u011b.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.exampl\u03f5.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': 'www.exarnple.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.ex\u01cemple.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.\u0119xample.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.\u0113xampl\u0113.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.exam\u03c1le.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'w\u0561w.example.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'\u0561\u0561\u0561.example.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.ex\u04d3mple.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'\u0561\u0561w.example.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.\u0115xample.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.\u1eb9xampl\u1eb9.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'ww\u0561.example.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.e\u0445ample.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': 'vvvvvv.example.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': 'wvvw.example.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.\xeaxample.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.\xebxampl\xeb.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.ex\u0251mple.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.examp\u0142e.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.\u0115xampl\u0115.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.exa\u1e43ple.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'w\u0561\u0561.example.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'\u051dww.example.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.exampl\u011b.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.exampl\u0119.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.exampl\u0113.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.exampl\u0117.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'\u0461\u0461w.example.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.\u1eb9xample.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.ex\u0227mple.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.ex\u1ea1mple.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.ex\xe4mple.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': 'www.examp1e.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': u'www.\u0435xample.com', 'fuzzer': 'Homoglyph'},
        {'domain-name': 'w-ww.example.com', 'fuzzer': 'Hyphenation'},
        {'domain-name': 'ww-w.example.com', 'fuzzer': 'Hyphenation'},
        {'domain-name': 'www.e-xample.com', 'fuzzer': 'Hyphenation'},
        {'domain-name': 'www.ex-ample.com', 'fuzzer': 'Hyphenation'},
        {'domain-name': 'www.exa-mple.com', 'fuzzer': 'Hyphenation'},
        {'domain-name': 'www.exam-ple.com', 'fuzzer': 'Hyphenation'},
        {'domain-name': 'www.examp-le.com', 'fuzzer': 'Hyphenation'},
        {'domain-name': 'www.exampl-e.com', 'fuzzer': 'Hyphenation'},
        {'domain-name': 'www.exampple.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.ezxample.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.examlple.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.exampole.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.exa2mple.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'wsww.example.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.edxample.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.exyample.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'wxww.example.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.exazmple.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.exanmple.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.examplle.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.ex1ample.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.exasmple.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'wwwa.example.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.e4xample.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'wwsw.example.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.zexample.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.exam0ple.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.exapmple.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.exakmple.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.exammple.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www3.example.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.examploe.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.e3xample.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.exwample.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'wwew.example.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.excample.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.ewxample.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.examplme.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.exzample.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.exawmple.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'waww.example.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.dexample.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'wwxw.example.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.exdample.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.sexample.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'ww2w.example.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.exampkle.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'wwaw.example.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.examjple.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.eyxample.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'wqww.example.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.exalmple.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.wexample.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'w3ww.example.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'w2ww.example.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.exaymple.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.examnple.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.exampmle.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'wwwe.example.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.ecxample.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'ww3w.example.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www2.example.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.exsample.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'weww.example.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'wwwx.example.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'wwws.example.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.rexample.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.examp0le.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.4example.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.examople.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.esxample.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.exaqmple.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.exqample.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'wwqw.example.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.examplke.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.exa1mple.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.ex2ample.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.exajmple.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.examkple.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.examplpe.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.3example.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.erxample.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'wwwq.example.com', 'fuzzer': 'Insertion'},
        {'domain-name': 'www.exaple.com', 'fuzzer': 'Omission'},
        {'domain-name': 'www.eample.com', 'fuzzer': 'Omission'},
        {'domain-name': 'www.examle.com', 'fuzzer': 'Omission'},
        {'domain-name': 'www.exampl.com', 'fuzzer': 'Omission'},
        {'domain-name': 'wwwexample.com', 'fuzzer': 'Omission'},
        {'domain-name': 'w.example.com', 'fuzzer': 'Omission'},
        {'domain-name': 'www.xample.com', 'fuzzer': 'Omission'},
        {'domain-name': 'www.exampe.com', 'fuzzer': 'Omission'},
        {'domain-name': 'www.exmple.com', 'fuzzer': 'Omission'},
        {'domain-name': 'ww.example.com', 'fuzzer': 'Omission'},
        {'domain-name': 'www.exaample.com', 'fuzzer': 'Repetition'},
        {'domain-name': 'www.eexample.com', 'fuzzer': 'Repetition'},
        {'domain-name': 'www.exxample.com', 'fuzzer': 'Repetition'},
        {'domain-name': 'wwww.example.com', 'fuzzer': 'Repetition'},
        {'domain-name': 'www.exsmple.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'www.rxample.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'eww.example.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'www.ecample.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'www.exakple.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'wwa.example.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'www.ex2mple.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'www.wxample.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'www.4xample.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'wxw.example.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'www.sxample.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'ww2.example.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'www.exymple.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'aww.example.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'www.zxample.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'wew.example.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'wwx.example.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'www.exajple.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'www.examplz.com', 'fuzzer': 'Replacement'},
        {'domain-name': '2ww.example.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'www.exampls.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'w2w.example.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'www.examplw.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'wwe.example.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'www.examole.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'ww3.example.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'www.examlle.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'www.exampl3.com', 'fuzzer': 'Replacement'},
        {'domain-name': '3ww.example.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'www.exzmple.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'www.esample.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'waw.example.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'www.examplr.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'www.3xample.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'www.examppe.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'xww.example.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'www.edample.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'www.exampke.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'www.exampoe.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'wqw.example.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'www.exwmple.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'www.exapple.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'qww.example.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'w3w.example.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'www.exammle.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'wwq.example.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'www.ex1mple.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'www.exampl4.com', 'fuzzer': 'Replacement'},
        {'domain-name': 'w.ww.example.com', 'fuzzer': 'Subdomain'},
        {'domain-name': 'ww.w.example.com', 'fuzzer': 'Subdomain'},
        {'domain-name': 'www.e.xample.com', 'fuzzer': 'Subdomain'},
        {'domain-name': 'www.ex.ample.com', 'fuzzer': 'Subdomain'},
        {'domain-name': 'www.exa.mple.com', 'fuzzer': 'Subdomain'},
        {'domain-name': 'www.exam.ple.com', 'fuzzer': 'Subdomain'},
        {'domain-name': 'www.examp.le.com', 'fuzzer': 'Subdomain'},
        {'domain-name': 'www.exampl.e.com', 'fuzzer': 'Subdomain'},
        {'domain-name': 'ww.wexample.com', 'fuzzer': 'Transposition'},
        {'domain-name': 'wwwe.xample.com', 'fuzzer': 'Transposition'},
        {'domain-name': 'www.xeample.com', 'fuzzer': 'Transposition'},
        {'domain-name': 'www.eaxmple.com', 'fuzzer': 'Transposition'},
        {'domain-name': 'www.exmaple.com', 'fuzzer': 'Transposition'},
        {'domain-name': 'www.exapmle.com', 'fuzzer': 'Transposition'},
        {'domain-name': 'www.examlpe.com', 'fuzzer': 'Transposition'},
        {'domain-name': 'www.exampel.com', 'fuzzer': 'Transposition'},
        {'domain-name': 'www.exampli.com', 'fuzzer': 'Vowel swap'},
        {'domain-name': 'www.examplo.com', 'fuzzer': 'Vowel swap'},
        {'domain-name': 'www.oxample.com', 'fuzzer': 'Vowel swap'},
        {'domain-name': 'www.ixample.com', 'fuzzer': 'Vowel swap'},
        {'domain-name': 'www.exomple.com', 'fuzzer': 'Vowel swap'},
        {'domain-name': 'www.exumple.com', 'fuzzer': 'Vowel swap'},
        {'domain-name': 'www.examplecom.com', 'fuzzer': 'Various'}
    ]
