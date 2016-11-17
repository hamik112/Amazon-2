var ue_mbl = ue_csm.ue.exec(function(f, a) {
    function k(e) {
        b = e || {};
        a.AMZNPerformance = b;
        b.transition = b.transition || {};
        b.timing = b.timing || {}; ! a.webclient || "function" !== typeof webclient.getRealClickTime || a.cordova && a.cordova.platformId && "ios" == cordova.platformId || (b.tags instanceof Array && (e = -1 != b.tags.indexOf("usesAppStartTime") || b.transition.type ? !b.transition.type && -1 < b.tags.indexOf("usesAppStartTime") ? "warm-start": void 0 : "view-transition", e && (b.transition.type = e)), "reload" === d._nt && f.ue_orct || "intrapage-transition" === d._nt ? a.performance && performance.timing && performance.timing.navigationStart ? b.timing.transitionStart = a.performance.timing.navigationStart: delete b.timing.transitionStart: "undefined" === typeof d._nt && a.performance && performance.timing && performance.timing.navigationStart && a.history && "function" === typeof a.History && "object" === typeof a.history && history.length && 1 != history.length && (b.timing.transitionStart = a.performance.timing.navigationStart));
        e = b.transition;
        var c;
        c = d._nt ? d._nt: void 0;
        e.subType = c;
        a.ue && a.ue.tag && a.ue.tag("has-AMZNPerformance");
        d.isl && a.uex && uex("at", "csm-timing");
        l()
    }
    function m(b) {
        a.ue && a.ue.count && a.ue.count("csm-cordova-plugin-failed", 1)
    }
    function l() {
        try {
            P.register("AMZNPerformance",
            function() {
                return b
            })
        } catch(a) {}
    }
    function g() {
        if (!b) return "";
        ue_mbl.cnt = null;
        var a = b.transition,
        c;
        c = b.timing.transitionStart;
        c = "undefined" !== typeof c && "undefined" !== typeof h ? c - h: void 0;
        a = ["mts", c, "mtt", a.type, "mtst", a.subType, "mtlt", a.launchType];
        c = "";
        for (var d = 0; d < a.length; d += 2) {
            var f = a[d],
            g = a[d + 1];
            "undefined" !== typeof g && (c += "&" + f + "=" + g)
        }
        return c
    }
    function n(a, c) {
        b && (h = c, b.timing.transitionStart = a, b.transition.type = "view-transition", b.transition.subType = "ajax-transition", b.transition.launchType = "normal", ue_mbl.cnt = g)
    }
    var d = f.ue || {},
    h = f.ue_t0,
    b;
    if (a.P && a.P.when && a.P.register) return a.P.when("CSMPlugin").execute(function(a) {
        a.buildAMZNPerformance && a.buildAMZNPerformance({
            successCallback: k,
            failCallback: m
        })
    }),
    {
        cnt: g,
        ajax: n
    }
},
"mobile-timing")(ue_csm, window);

(function(d) {
    d._uess = function() {
        var a = "";
        screen && screen.width && screen.height && (a += "&sw=" + screen.width + "&sh=" + screen.height);
        var b = function(a) {
            var b = document.documentElement["client" + a];
            return "CSS1Compat" === document.compatMode && b || document.body["client" + a] || b
        },
        c = b("Width"),
        b = b("Height");
        c && b && (a += "&vw=" + c + "&vh=" + b);
        return a
    }
})(ue_csm);

(function(a) {
    var b = document.ue_backdetect;
    b && b.ue_back && a.ue && (a.ue.bfini = b.ue_back.value);
    a.uet && a.uet("be");
    a.onLdEnd && (window.addEventListener ? window.addEventListener("load", a.onLdEnd, !1) : window.attachEvent && window.attachEvent("onload", a.onLdEnd));
    a.ueh && a.ueh(0, window, "load", a.onLd, 1);
    a.ue && a.ue.tag && (a.ue_furl && a.ue_furl.split ? (b = a.ue_furl.split(".")) && b[0] && a.ue.tag(b[0]) : a.ue.tag("nofls"))
})(ue_csm);

(function(g, h) {
    function d(a, d) {
        var b = {};
        if (!e || !f) try {
            var c = h.sessionStorage;
            c ? a && ("undefined" !== typeof d ? c.setItem(a, d) : b.val = c.getItem(a)) : f = 1
        } catch(g) {
            e = 1
        }
        e && (b.e = 1);
        return b
    }
    var b = g.ue || {},
    a = "",
    f, e, c, a = d("csmtid");
    f ? a = "NA": a.e ? a = "ET": (a = a.val, a || (a = b.oid || "NI", d("csmtid", a)), c = d(b.oid), c.e || (c.val = c.val || 0, d(b.oid, c.val + 1)), b.ssw = d);
    b.tabid = a
})(ue_csm, window);

(function(b, c) {
    var a = c.images;
    a && a.length && b.ue.count("totalImages", a.length)
})(ue_csm, document);

ue_csm.ue._rtn = 1; (function(e, f) {
    function h(a) {
        a = a.split("?")[0] || a;
        a = a.replace("http://", "").replace("https://", "").replace("resource://", "").replace("res://", "").replace("undefined://", "").replace("chrome://", "").replace(/\*/g, "").replace(/!/g, "").replace(/~/g, "");
        var b = a.split("/");
        a = a.substr(a.lastIndexOf("/") + 1);
        b.splice( - 1);
        b = b.map(function(a) {
            c[a] || (c[a] = (k++).toString(36));
            return c[a]
        });
        b.push(a);
        return b.join("!")
    }
    function l() {
        return f.getEntriesByType("resource").filter(function(a) {
            return d._rre(a) < d._ld
        }).sort(function(a, b) {
            return a.responseEnd - b.responseEnd
        }).splice(0, m).map(function(a) {
            var b = [],
            c;
            for (c in a) g[c] && a[c] && b.push(g[c] + Math.max(a[c] | 0, -1).toString(36));
            b.push("i" + a.initiatorType); (1 == d._rtn && d._afjs > n || 2 == d._rtn) && b.push("n" + h(a.name));
            return b.join("_")
        }).join("*")
    }
    function p() {
        var a = "pm",
        b;
        for (b in c) c.hasOwnProperty(b) && (a += "*" + c[b] + "_" + b);
        return a
    }
    function q() {
        d.log({
            k: "rtiming",
            value: l() + "~" + p()
        },
        "csm")
    }
    if (f && f.getEntriesByType && Array.prototype.map && Array.prototype.filter && e.ue && e.ue.log) {
        var g = {
            connectStart: "c",
            connectEnd: "C",
            domainLookupStart: "d",
            domainLookupEnd: "D",
            duration: "z",
            fetchStart: "f",
            redirectStart: "r",
            redirectEnd: "R",
            requestStart: "q",
            responseStart: "s",
            responseEnd: "S",
            startTime: "a"
        },
        d = e.ue,
        c = {},
        k = 1,
        n = 20,
        m = 200;
        d && d._rre && (d._art = function() {
            d._ld && window.setTimeout(q, 0)
        })
    }
})(ue_csm || {},
window.performance);

(function(c, d) {
    var b = c.ue,
    a = d.navigator;
    b && b.tag && a && (a = a.connection || a.mozConnection || a.webkitConnection) && a.type && b.tag("netInfo:" + a.type)
})(ue_csm, window);

(function(c, d) {
    function g(a, b) {
        for (var c = [], d = 0; d < a.length; d++) {
            var f = a[d],
            e = b.encode(f);
            if (f[h]) {
                var k = b.metaSep,
                f = f[h],
                l = b.metaPairSep,
                g = [],
                m = void 0;
                for (m in f) f.hasOwnProperty(m) && g.push(m + "=" + f[m]);
                f = g.join(l);
                e += k + f
            }
            c.push(e)
        }
        return c.join(b.resourceSep)
    }
    function n(a) {
        var b = a[h] = a[h] || {};
        b[t] || (b[t] = c.ue_mid);
        b[u] || (b[u] = c.ue_sid);
        b[k] || (b[k] = c.ue_id);
        b.csm = 1;
        a = "//" + c.ue_furl + "/1/" + a[v] + "/1/OP/" + a[w] + "/" + a[x] + "/" + g([a], y);
        if (p) try {
            p.call(d[q], a)
        } catch(e) {
            c.ue.sbf = 1,
            (new Image).src = a
        } else(new Image).src = a
    }
    function r() {
        l && l.isStub && l.replay(function(a, b, c) {
            a = a[0];
            b = a[h] = a[h] || {};
            b[k] = b[k] || c;
            n(a)
        });
        e.impression = n;
        l = null
    }
    if (! (1 < c.ueinit)) {
        var h = "metadata",
        x = "impressionType",
        v = "foresterChannel",
        w = "programGroup",
        t = "marketplaceId",
        u = "session",
        k = "requestId",
        q = "navigator",
        e = c.ue || {},
        p = d[q] && d[q].sendBeacon,
        s = function(a, b, c, d) {
            return {
                encode: d,
                resourceSep: a,
                metaSep: b,
                metaPairSep: c
            }
        },
        y = s("", "?", "&",
        function(a) {
            return g(a.impressionData, z)
        }),
        z = s("/", ":", ",",
        function(a) {
            return a.featureName + ":" + g(a.resources, A)
        }),
        A = s(",", "@", "|",
        function(a) {
            return a.id
        }),
        l = e.impression; (e.impression || n)({
            programGroup: "csm",
            impressionType: "action",
            impressionData: [{
                featureName: "csm-features",
                resources: [{
                    id: "impression-tracking"
                }]
            }],
            foresterChannel: "action-impressions"
        });
        p ? r() : (e.attach("load", r), e.attach("beforeunload", r));
        d.P && d.P.register && d.P.register("impression-client",
        function() {})
    }
})(ue_csm, window);

var ue_pty = "AuthenticationPortal";

var ue_spty = "RegistrationApplication";
