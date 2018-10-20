import json
import Scanner

class Output:
    def __init__(self, format):
        self.formato=format

    def output(self, obj, results=None, openports=None):
        if results is not None:
            self.result = json.loads(results)
        if self.formato=="html":
            self.outHTML(obj)
        elif self.formato == "monitor":
            self.monitor(obj, openports)
        elif self.formato == "multiHTML":
            self.outMultiHTML(obj)
        else:
            self.outText(obj)

    def monitor(self, obj, openports):
        r = self.result
        for port in r['ports']:
            if port not in openports:
                self.outText(obj)
    def outMultiHTML(self, obj, name):
        reportados = []
        head = """
                    <html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"></meta><title>Scan Report</title><style type="text/css" media="all">
                    UL.ulist {padding: 0 10px; line-height:25px; margin-bottom:0px; margin-top:0px;}
                    LI.list {padding: 0 10px; line-height:25px; margin-bottom:0px; margin-top:0px; list-style: disc;}
                    LI.list0 {padding: 0 10px; line-height:25px; margin-bottom:0px; margin-top:0px; list-style: disc; color:#357abd;}
                    LI.list1 {padding: 0 10px; line-height:25px; margin-bottom:0px; margin-top:0px; list-style: disc; color:#4cae4c;}
                    LI.list2 {padding: 0 10px; line-height:25px; margin-bottom:0px; margin-top:0px; list-style: disc; color:#fdc431;}
                    LI.list3 {padding: 0 10px; line-height:25px; margin-bottom:0px; margin-top:0px; list-style: disc; color:#ee9336;}
                    LI.list4 {padding: 0 10px; line-height:25px; margin-bottom:0px; margin-top:0px; list-style: disc; color:#d43f3a;}
                    html, body, div, span, applet, object, iframe, h1, h2, h3, h4, h5, h6, p, blockquote, pre, a, abbr, acronym, address, big, cite, code, del, dfn, em, img, ins, kbd, q, s, samp, small, strike, strong, sub, sup, tt, var, b, u, i, center, dl, dt, dd, ol, ul, li, fieldset, form, label, legend, table, caption, tbody, tfoot, thead, tr, th, td, article, aside, canvas, details, embed, figure, figcaption, footer, header, hgroup, menu, nav, output, ruby, section, summary, time, mark, audio, video {
                        margin: 0;
                        padding: 0;
                        border: 0;
                        font-size: 100%;
                        font: inherit;
                        vertical-align: baseline;
                        -webkit-text-size-adjust: none;
                    }
                    html, body {
                        font-family: helvetica, arial, sans-serif;
                        width: 100%;
                        color: #263645;
                        font-size: 12px;
                        background: #efefef;
                    }
                    a, a:visited, a:active {
                        color: #004a97;
                    }
                    a:hover {
                        color: #00253d;
                    }
                    .container_16 {
                        margin: 0 auto;
                        padding: 0 14px 14px 14px;
                        background: #fff;
                        border-top: #425363 solid 7px;
                        box-shadow: 0 2px 10px rgba(0, 0, 0, .2);
                        margin-bottom: 20px;
                        border-radius: 0 0 5px 5px;
                    }
                    #reportContent {
                        width: 100%;
                    }
                    h1.classtitle {
                        padding: 15px 0 10px 0;
                        border-bottom: 1px dotted #ccc;
                        margin: 0 0 15px 0;
                    }
                    h2.classtitle {
                        color: #00a5b5;
                        font-weight: normal;
                        font-size: 22px;
                        margin: 0;
                        ping: 0;
                    }
                    h2.date {
                        font-size: 14px;
                        color: #768591;
                        margin: 0;
                        padding: 0;
                        font-weight: normal;
                    }
                    .reportinfo {
                        display: block;
                        width: 100%;
                        font-size: 16px;
                        padding: 0 0 15px 0;
                        margin: 0 0 5px 0;
                        font-weight: normal;
                        border-bottom: 1px dotted #ccc;
                    }
                    .reportpadding {
                        padding: 15px 0 0 0 !important;
                    }
                    .classtoc {
                        display: block;
                        font-size: 18px;
                        color: #777779;
                        padding: 15px 0;
                        margin: 15px 0 0 0;
                    }
                    h1.classchapter {
                        background: #425363;
                        color: #fff;
                        font-weight: bold;
                        font-size: 16px;
                        padding: 6px 10px;
                        margin: 10px 0 0 0;
                        border-radius: 4px 4px 0 0;
                    }
                    h2.classsection {
                        display: block;
                        background: #425363;
                        color: #fff;
                        font-weight: bold;
                        font-size: 14px;
                        padding: 6px 10px;
                        margin: 30px 0 0 0;
                        border-radius: 4px 4px 0 0;
                    }
                    h2.classh1 {
                        display: block;
                        background: #efefef;
                        font-weight: bold;
                        font-size: 13px;
                        padding: 6px 10px;
                    }
                    .classtext {
                        font-size: 13px;
                        line-height: 18px;
                    }
                    div#reportContent div span.classtext {
                        padding: 6px 10px;
                        display: inline-block;
                    }
                    h2.classsubsection {
                        background: #768591;
                        color: #fff;
                        font-weight: bold;
                        font-size: 13px;
                        padding: 6px 10px;
                    }
                    .classheader h1 {
                        color: #fff;
                        font-weight: bold;
                        font-size: 15px;
                        padding: 0 10px;
                        text-align: center;
                    }
                    .reportinfo b {
                        font-weight: bold;
                    }
                    h3.classtitle {
                        color: #69737b;
                        font-size: 16px;
                        padding: 0 10px;
                    }
                    .classsection_sub tr, td {
                        color: #053958;
                        font-size: 13px;
                        padding: 0 10px;
                    }
                    td {
                        padding: 6px 10px;
                    }
                    h2.classsection, h2.classsection0, h2.classsection1, h2.classsection2, h2.classsection3, h2.classsection4 {
                        background: #053958;
                        color: #fff;
                        font-weight: bold;
                        font-size: 13px;
                        padding: 6px 10px;
                        margin-bottom: 0px;
                        margin-top: 10px;
                    }
                    .classcell4, h2.classsection4 {
                        background-color: #d43f3a;
                    }
                    .classcell3, h2.classsection3 {
                        background-color: #ee9336;
                    }
                    .classcell2, h2.classsection2 {
                        background-color: #fdc431;
                    }
                    .classcell1, h2.classsection1 {
                        background-color: #4cae4c;
                    }
                    .classcell0, h2.classsection0 {
                        background-color: #357abd;
                    }
                    #copyright {
                        display: block;
                        width: 100%;
                        text-align: center;
                        font-size: 12px;
                        color: #A9A8A9;
                        padding: 6px 0 20px 0;
                    }
                    #copyright a, #copyright a:visited, #copyright a:active {
                        color: #A9A8A9;
                    }
                    div.icon {
                        display: none;
                    }
                    .nopadding {
                        padding: 0 !important;
                    }
                    body.email h2.classh1 {
                        display: block;
                        margin: 20px 0 0 0;
                        background: #425363;
                        color: #fff;
                        font-weight: bold;
                        font-size: 14px;
                        padding: 6px 10px;
                        border-radius: 4px 4px 0 0;
                    }
                    body.email div#reportContent div span.classtext {
                        padding: 0;
                        display: inline;
                    }
                    body.email h2.tips {
                        background: #004a97 !important;
                    }
                    body.email h2.errors {
                        background: #c00 !important;
                    }
                    body.email h2.classsection {
                        display: none;
                    }
                    .classtoc1 a {
                        font-size: 16px;
                    }
                    .classtoc2 a {
                        font-size: 13px;
                        padding: 0 20px;
                    }
                    xmp {
                        display: block;
                        white-space: pre-wrap;
                        font-family: monospace;
                    }
                    h2.classh2 {
                        background: #f8f8f8;
                        font-weight: bold;
                        font-size: 13px;
                        padding: 6px 10px;
                    }
                    .classpre {
                        display: block;
                        font-size: 13px;
                        font-family: Courier New, Courier, monospace;
                        padding: 10px;
                        color: #000;
                    }
                    .classh1_grey h2 {
                        background: #eaeaea;
                        color:#053958;
                        font-size: 13px;
                        padding: 0 10px;
                        margin-top:0px;
                        margin-bottom:2px;
                    }
                    @media only screen and (max-device-width: 480px) {
                    html, body {
                        display: block;
                        min-width: 480px;
                        background: #fff;
                    }
                    table {
                        table-layout: auto !important;
                    }
                    table td {
                        word-wrap: break-word;
                    }
                    table.container_16 {
                        width: 100%;
                        padding: 0 4% 20px 4%;
                        background: #fff;
                        border-top: #425363 solid 7px;
                        box-shadow: none !important;
                        margin-bottom: 20px;
                        border-radius: 0;
                    }
                    #copyright {
                        display: block;
                        width: 90%;
                        text-align: center;
                        font-size: 10px;
                        color: #A9A8A9;
                        padding: 5px 0 20px 0;
                        border-top: 1px dotted #ccc;
                        margin: 0 auto;
                        line-height: 16px
                    }
                    .classtitle img {
                        display: block;
                        margin: 0 auto;
                    }
                    }
                    </style><script type="text/javascript">
                    function toggle(divId) {
                        var divObj = document.getElementById(divId);
                        if (divObj) {
                            var displayType = divObj.style.display;
                        if (displayType == "" || displayType == "block") {
                            divObj.style.display = "none";
                        } else {
                            divObj.style.display = "block";
                            }
                        }
                    }
                    function ceall(flag) {
                        var divs = document.getElementsByTagName("div");
                        var i = 0;
                        for (i = 0; i < divs.length; i++) {
                            if (divs[i].getAttribute("id") != null && divs[i].getAttribute("id").match('btag-')) {
                                if (flag == 0) {
                                    divs[i].style.display = "none";
                                } else {
                                    divs[i].style.display = "block";
                                    }
                            }
                        }
                    }
                    </script></head>
                """
        body = """<body class="">"""
        for host in obj.hosts:
            r=json.loads(host)
            ip=r["ip_str"]
            isp = r["isp"]
            org = r["org"]
            asn = r["asn"]
            country = r["country_name"]
            os = r["os"]
            ports = r["ports"]
            if ip not in reportados:
                reportados.append(ip)
                # Anadir datos a la cabecera
                body = body + """
                        <table cellpadding="0" cellspacing="0" border="0" width="100%">
                        <tbody>
                        <tr>
                        <td align="center" valign="top" class"nopadding" style="vertical-align: top">
                        <table cellpadding="0" cellspacing="0" border="0" width="80%" bgcolor="#FFFFFF" class="container_16">
                        <tbody>
                        <tr><td>
                        <table xmlns="" width="100%">
                            <tr>
                                <td width="20%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> Start time: </span></td>
                                <td width="80%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> {0} </span></td>
                            </tr>
                            <tr>
                                <td width="20%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> End time: </span></td>
                                <td width="80%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> {1} </span></td>
                            </tr>
                        </table>
                        <h2 xmlns="" class="classh1 " style="vertical-align: middle;">Host Information</h2>
                        <table xmlns="" width="100%">
                            <tr>
                                <td width="20%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> IP: </span></td>
                                <td width="80%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> {2} </span></td>
                            </tr>
                            <tr>
                                <td width="20%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> OS: </span></td>
                                <td width="80%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> {3} </span></td>
                            </tr>
                            <tr>
                                <td width="20%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> ASN: </span></td>
                                <td width="80%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> {4} </span></td>
                            </tr>
                            <tr>
                                <td width="20%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> ISP: </span></td>
                                <td width="80%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> {5} </span></td>
                            </tr>
                            <tr>
                                <td width="20%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> Country Name: </span></td>
                                <td width="80%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> {6} </span></td>
                            </tr>
                            <tr>
                                <td width="20%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> Org: </span></td>
                                <td width="80%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> {7} </span></td>
                            </tr>
                            <tr>
                                <td width="20%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> Number of open ports: </span></td>
                                <td width="80%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> {8} </span></td>
                            </tr></table>
                        """.format(obj.startTime, obj.endTime, ip, os, asn, isp, country, org, len(ports))
                # Anadimos la cabecera de los resultados
                body = body + """
                            <h2 xmlns="" class="classh1 " style="vertical-align: middle;">Results Details </h2>
                            <div id="reportContent">
                        """
                # Por puerto
                for port in r["data"]:
                    body = body + """
                                <span xmlns class="classh1_grey"><h2><span class="classection_sub">
                                <table width="100%">
                                <tbody>
                                <tr width="100%" onclick="toggle('host{1}puerto{0}')" onmouseover="this.style.cursor='pointer'" title="Collapse/Expand" style="cursor: pointer;">
                                <td width="5%" height="50%">
                                <table style="table-layaout: fxed;" width="30px" height="15px">
                                <tbody>
                                <tr width="100%">
                                <td width="100%" class="classcell0"></td></tr></tbody></table></td>
                                <td align="left" width="85%">Puerto: {0}</td>
                                <td align="rigth" width="10%">[-/+]</td></tr></tbody></table></span></h2></span>
                                """.format(port["port"], ip)
                    body = body + """<div xmlns id="host{1}puerto{0}" style="display: none;">""".format(port["port"], ip)
                    for datos in port.items():

                        if datos[0] in ["hash", "location", "timestamp", "asn", "ip", "org", "isp", "ip_str", "os", "_shodan",
                                        "port", "opts"]:
                            pass
                        else:
                            body = body + """
                                        <h2 class="classh1 " style="vertical-align: middle;">{0}</h2>
                                        <span class="classtext" style="color: #263645; font-weight: normal;"><xmp>{1}</xmp></span>
                                        """.format(datos[0].capitalize(), datos[1])
                    body = body + """</div>"""
                s=Scanner.Scan("Nmap")
                reportescan=s.scan(ip, "default")
                body = body + """
                    <span xmlns class="classh1_grey"><h2><span class="classection_sub">
                    <table width="100%">
                    <tbody>
                    <tr width="100%" onclick="toggle('host{1}{0}')" onmouseover="this.style.cursor='pointer'" title="Collapse/Expand" style="cursor: pointer;">
                    <td width="5%" height="50%">
                    <table style="table-layaout: fxed;" width="30px" height="15px">
                    <tbody>
                    <tr width="100%">
                    <td width="100%" class="classcell4"></td></tr></tbody></table></td>
                    <td align="left" width="85%">{0}</td>
                    <td align="rigth" width="10%">[-/+]</td></tr></tbody></table></span></h2></span>
                    """.format("Scan", ip)
                body = body + """<div xmlns id="host{1}{0}" style="display: none;">""".format("Scan", ip)
                body = body + """
                    <h2 class="classh1 " style="vertical-align: middle;">{0}</h2>
                    <span class="classtext" style="color: #263645; font-weight: normal;"><xmp>{1}</xmp></span></div>
                    """.format("Scan Nmap", reportescan)

                body = body + """</div></td></tr></tbody></table></td>"""
        body = body + """</tr></tbody></table></html>"""
        file = open('{0}.html'.format(name.replace("/", "-")), 'w')
        file.write(head + body)

    def outText(self, obj):
        r = self.result
        ip = r["ip_str"]
        isp = r["isp"]
        org = r["org"]
        asn = r["asn"]
        country = r["country_name"]
        os = r["os"]
        ports = r["ports"]
        print "Host basic Info:"
        print "Start time: {0}".format(obj.startTime)
        print "End time: {0}".format(obj.endTime)
        print "---IP: {0}".format(ip)
        print "---ISP: {0}".format(isp)
        print "---ORG: {0}".format(org)
        print "---ASN: {0}".format(asn)
        print "---Country: {0}".format(country)
        print "---OS: {0}".format(os)
        print "---Number open ports: {0}".format(len(ports))
        for port in r["data"]:
            print "---------------------------"
            print "Puerto: {0}".format(port["port"])
            for datos in port.items():
                if datos[0] in ["hash", "location", "timestamp", "asn", "ip", "org", "isp", "ip_str", "os", "_shodan",
                                "port", "opts"]:
                    pass
                else:
                    print "{0}: {1}".format(datos[0].capitalize(), datos[1])

    def outHTML(self, obj):
        head = """
            <html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"></meta><title>Scan Report</title><style type="text/css" media="all">
            UL.ulist {padding: 0 10px; line-height:25px; margin-bottom:0px; margin-top:0px;}
            LI.list {padding: 0 10px; line-height:25px; margin-bottom:0px; margin-top:0px; list-style: disc;}
            LI.list0 {padding: 0 10px; line-height:25px; margin-bottom:0px; margin-top:0px; list-style: disc; color:#357abd;}
            LI.list1 {padding: 0 10px; line-height:25px; margin-bottom:0px; margin-top:0px; list-style: disc; color:#4cae4c;}
            LI.list2 {padding: 0 10px; line-height:25px; margin-bottom:0px; margin-top:0px; list-style: disc; color:#fdc431;}
            LI.list3 {padding: 0 10px; line-height:25px; margin-bottom:0px; margin-top:0px; list-style: disc; color:#ee9336;}
            LI.list4 {padding: 0 10px; line-height:25px; margin-bottom:0px; margin-top:0px; list-style: disc; color:#d43f3a;}
            html, body, div, span, applet, object, iframe, h1, h2, h3, h4, h5, h6, p, blockquote, pre, a, abbr, acronym, address, big, cite, code, del, dfn, em, img, ins, kbd, q, s, samp, small, strike, strong, sub, sup, tt, var, b, u, i, center, dl, dt, dd, ol, ul, li, fieldset, form, label, legend, table, caption, tbody, tfoot, thead, tr, th, td, article, aside, canvas, details, embed, figure, figcaption, footer, header, hgroup, menu, nav, output, ruby, section, summary, time, mark, audio, video {
                margin: 0;
                padding: 0;
                border: 0;
                font-size: 100%;
                font: inherit;
                vertical-align: baseline;
                -webkit-text-size-adjust: none;
            }
            html, body {
                font-family: helvetica, arial, sans-serif;
                width: 100%;
                color: #263645;
                font-size: 12px;
                background: #efefef;
            }
            a, a:visited, a:active {
                color: #004a97;
            }
            a:hover {
                color: #00253d;
            }
            .container_16 {
                margin: 0 auto;
                padding: 0 14px 14px 14px;
                background: #fff;
                border-top: #425363 solid 7px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, .2);
                margin-bottom: 20px;
                border-radius: 0 0 5px 5px;
            }
            #reportContent {
                width: 100%;
            }
            h1.classtitle {
                padding: 15px 0 10px 0;
                border-bottom: 1px dotted #ccc;
                margin: 0 0 15px 0;
            }
            h2.classtitle {
                color: #00a5b5;
                font-weight: normal;
                font-size: 22px;
                margin: 0;
                ping: 0;
            }
            h2.date {
                font-size: 14px;
                color: #768591;
                margin: 0;
                padding: 0;
                font-weight: normal;
            }
            .reportinfo {
                display: block;
                width: 100%;
                font-size: 16px;
                padding: 0 0 15px 0;
                margin: 0 0 5px 0;
                font-weight: normal;
                border-bottom: 1px dotted #ccc;
            }
            .reportpadding {
                padding: 15px 0 0 0 !important;
            }
            .classtoc {
                display: block;
                font-size: 18px;
                color: #777779;
                padding: 15px 0;
                margin: 15px 0 0 0;
            }
            h1.classchapter {
                background: #425363;
                color: #fff;
                font-weight: bold;
                font-size: 16px;
                padding: 6px 10px;
                margin: 10px 0 0 0;
                border-radius: 4px 4px 0 0;
            }
            h2.classsection {
                display: block;
                background: #425363;
                color: #fff;
                font-weight: bold;
                font-size: 14px;
                padding: 6px 10px;
                margin: 30px 0 0 0;
                border-radius: 4px 4px 0 0;
            }
            h2.classh1 {
                display: block;
                background: #efefef;
                font-weight: bold;
                font-size: 13px;
                padding: 6px 10px;
            }
            .classtext {
                font-size: 13px;
                line-height: 18px;
            }
            div#reportContent div span.classtext {
                padding: 6px 10px;
                display: inline-block;
            }
            h2.classsubsection {
                background: #768591;
                color: #fff;
                font-weight: bold;
                font-size: 13px;
                padding: 6px 10px;
            }
            .classheader h1 {
                color: #fff;
                font-weight: bold;
                font-size: 15px;
                padding: 0 10px;
                text-align: center;
            }
            .reportinfo b {
                font-weight: bold;
            }
            h3.classtitle {
                color: #69737b;
                font-size: 16px;
                padding: 0 10px;
            }
            .classsection_sub tr, td {
                color: #053958;
                font-size: 13px;
                padding: 0 10px;
            }
            td {
                padding: 6px 10px;
            }
            h2.classsection, h2.classsection0, h2.classsection1, h2.classsection2, h2.classsection3, h2.classsection4 {
                background: #053958;
                color: #fff;
                font-weight: bold;
                font-size: 13px;
                padding: 6px 10px;
                margin-bottom: 0px;
                margin-top: 10px;
            }
            .classcell4, h2.classsection4 {
                background-color: #d43f3a;
            }
            .classcell3, h2.classsection3 {
                background-color: #ee9336;
            }
            .classcell2, h2.classsection2 {
                background-color: #fdc431;
            }
            .classcell1, h2.classsection1 {
                background-color: #4cae4c;
            }
            .classcell0, h2.classsection0 {
                background-color: #357abd;
            }
            #copyright {
                display: block;
                width: 100%;
                text-align: center;
                font-size: 12px;
                color: #A9A8A9;
                padding: 6px 0 20px 0;
            }
            #copyright a, #copyright a:visited, #copyright a:active {
                color: #A9A8A9;
            }
            div.icon {
                display: none;
            }
            .nopadding {
                padding: 0 !important;
            }
            body.email h2.classh1 {
                display: block;
                margin: 20px 0 0 0;
                background: #425363;
                color: #fff;
                font-weight: bold;
                font-size: 14px;
                padding: 6px 10px;
                border-radius: 4px 4px 0 0;
            }
            body.email div#reportContent div span.classtext {
                padding: 0;
                display: inline;
            }
            body.email h2.tips {
                background: #004a97 !important;
            }
            body.email h2.errors {
                background: #c00 !important;
            }
            body.email h2.classsection {
                display: none;
            }
            .classtoc1 a {
                font-size: 16px;
            }
            .classtoc2 a {
                font-size: 13px;
                padding: 0 20px;
            }
            xmp {
                display: block;
                white-space: pre-wrap;
                font-family: monospace;
            }
            h2.classh2 {
                background: #f8f8f8;
                font-weight: bold;
                font-size: 13px;
                padding: 6px 10px;
            }
            .classpre {
                display: block;
                font-size: 13px;
                font-family: Courier New, Courier, monospace;
                padding: 10px;
                color: #000;
            }
            .classh1_grey h2 {
                background: #eaeaea;
                color:#053958;
                font-size: 13px;
                padding: 0 10px;
                margin-top:0px;
                margin-bottom:2px;
            }
            @media only screen and (max-device-width: 480px) {
            html, body {
                display: block;
                min-width: 480px;
                background: #fff;
            }
            table {
                table-layout: auto !important;
            }
            table td {
                word-wrap: break-word;
            }
            table.container_16 {
                width: 100%;
                padding: 0 4% 20px 4%;
                background: #fff;
                border-top: #425363 solid 7px;
                box-shadow: none !important;
                margin-bottom: 20px;
                border-radius: 0;
            }
            #copyright {
                display: block;
                width: 90%;
                text-align: center;
                font-size: 10px;
                color: #A9A8A9;
                padding: 5px 0 20px 0;
                border-top: 1px dotted #ccc;
                margin: 0 auto;
                line-height: 16px
            }
            .classtitle img {
                display: block;
                margin: 0 auto;
            }
            }
            </style><script type="text/javascript">
            function toggle(divId) {
                var divObj = document.getElementById(divId);
                if (divObj) {
                    var displayType = divObj.style.display;
                if (displayType == "" || displayType == "block") {
                    divObj.style.display = "none";
                } else {
                    divObj.style.display = "block";
                    }
                }
            }
            function ceall(flag) {
                var divs = document.getElementsByTagName("div");
                var i = 0;
                for (i = 0; i < divs.length; i++) {
                    if (divs[i].getAttribute("id") != null && divs[i].getAttribute("id").match('btag-')) {
                        if (flag == 0) {
                            divs[i].style.display = "none";
                        } else {
                            divs[i].style.display = "block";
                            }
                    }
                }
            }
            </script></head>
        """
        body = """<body class="">"""
        r = self.result
        ip = r["ip_str"]
        isp = r["isp"]
        org = r["org"]
        asn = r["asn"]
        country = r["country_name"]
        os = r["os"]
        ports = r["ports"]
        # Anadir datos a la cabecera
        body = body + """
        <table cellpadding="0" cellspacing="0" border="0" width="100%">
        <tbody>
        <tr>
        <td align="center" valign="top" class"nopadding" style="vertical-align: top">
        <table cellpadding="0" cellspacing="0" border="0" width="80%" bgcolor="#FFFFFF" class="container_16">
        <tbody>
        <tr><td>
        <table xmlns="" width="100%">
            <tr>
                <td width="20%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> Start time: </span></td>
                <td width="80%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> {0} </span></td>
            </tr>
            <tr>
                <td width="20%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> End time: </span></td>
                <td width="80%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> {1} </span></td>
            </tr>
        </table>
        <h2 xmlns="" class="classh1 " style="vertical-align: middle;">Host Information</h2>
        <table xmlns="" width="100%">
            <tr>
                <td width="20%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> IP: </span></td>
                <td width="80%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> {2} </span></td>
            </tr>
            <tr>
                <td width="20%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> OS: </span></td>
                <td width="80%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> {3} </span></td>
            </tr>
            <tr>
                <td width="20%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> ASN: </span></td>
                <td width="80%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> {4} </span></td>
            </tr>
            <tr>
                <td width="20%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> ISP: </span></td>
                <td width="80%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> {5} </span></td>
            </tr>
            <tr>
                <td width="20%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> Country Name: </span></td>
                <td width="80%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> {6} </span></td>
            </tr>
            <tr>
                <td width="20%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> Org: </span></td>
                <td width="80%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> {7} </span></td>
            </tr>
            <tr>
                <td width="20%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> Number of open ports: </span></td>
                <td width="80%" valign="top" class="classcell"><span class="classtext" style="color: #263645; font-weight: normal;"> {8} </span></td>
            </tr></table>
        """.format(obj.startTime, obj.endTime, ip, os, asn, isp, country, org, len(ports))
        #Anadimos la cabecera de los resultados
        body = body + """
            <h2 xmlns="" class="classh1 " style="vertical-align: middle;">Results Details</h2>
            <div id="reportContent">
        """
        #Por puerto
        for port in r["data"]:
            body = body + """
                <span xmlns class="classh1_grey"><h2><span class="classection_sub">
                <table width="100%">
                <tbody>
                <tr width="100%" onclick="toggle('puerto{0}')" onmouseover="this.style.cursor='pointer'" title="Collapse/Expand" style="cursor: pointer;">
                <td width="5%" height="50%">
                <table style="table-layaout: fxed;" width="30px" height="15px">
                <tbody>
                <tr width="100%">
                <td width="100%" class="classcell0"></td></tr></tbody></table></td>
                <td align="left" width="85%">Puerto: {0}</td>
                <td align="rigth" width="10%">[-/+]</td></tr></tbody></table></span></h2></span>
                """.format(port["port"])
            body = body + """<div xmlns id="puerto{0}" style="display: none;">""".format(port["port"])
            for datos in port.items():

                if datos[0] in ["hash", "location", "timestamp", "asn", "ip", "org", "isp", "ip_str", "os", "_shodan",
                                "port", "opts"]:
                    pass
                else:
                        body = body + """
                        <h2 class="classh1 " style="vertical-align: middle;">{0}</h2>
                        <span class="classtext" style="color: #263645; font-weight: normal;"><xmp>{1}</xmp></span>
                        """.format(datos[0].capitalize(), datos[1])
            body = body + """</div>"""
        s = Scanner.Scan("Nmap")
        reportescan = s.scan(ip, "default")
        body = body + """
            <span xmlns class="classh1_grey"><h2><span class="classection_sub">
            <table width="100%">
            <tbody>
            <tr width="100%" onclick="toggle('host{1}{0}')" onmouseover="this.style.cursor='pointer'" title="Collapse/Expand" style="cursor: pointer;">
            <td width="5%" height="50%">
            <table style="table-layaout: fxed;" width="30px" height="15px">
            <tbody>
            <tr width="100%">
            <td width="100%" class="classcell4"></td></tr></tbody></table></td>
            <td align="left" width="85%">{0}</td>
            <td align="rigth" width="10%">[-/+]</td></tr></tbody></table></span></h2></span>
            """.format("Scan", ip)
        body = body + """<div xmlns id="host{1}{0}" style="display: none;">""".format("Scan", ip)
        body = body + """
            <h2 class="classh1 " style="vertical-align: middle;">{0}</h2>
            <span class="classtext" style="color: #263645; font-weight: normal;"><xmp>{1}</xmp></span></div>
            """.format("Scan Nmap", reportescan)
        body = body + """</div></td></tr></tbody></table></td></tr></tbody></table></html>"""
        file=open('Host{0}.html'.format(ip), 'w')
        file.write(head + body)
