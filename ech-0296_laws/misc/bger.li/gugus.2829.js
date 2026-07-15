if (
    ((function (a, b) {
        function c(a) {
            "loading" === document.readyState
                ? document.addEventListener(
                      "DOMContentLoaded",
                      function () {
                          a();
                      },
                      !1
                  )
                : a();
        }
        function d(a) {
            "complete" === document.readyState
                ? a()
                : window.addEventListener(
                      "load",
                      function () {
                          a();
                      },
                      !1
                  );
        }
        function e(b) {
            if (
                (9 == b.keyCode &&
                    (b.preventDefault(),
                    null === document.getElementById("start")
                        ? document.getElementsByClassName("navbar")[0].classList.contains("showbg")
                            ? l()
                            : k()
                        : document.getElementById("start").focus()),
                13 == b.keyCode && "INPUT" === b.target.tagName)
            ) {
                b.preventDefault();
                let c,
                    d = /^(\d{1,4}[a-z]*)$/i;
                if ("index" === a.module) window.location = "/" + document.getElementById("start").value;
                else if ("sr" === a.module || "zhlex" === a.module || "shlex" === a.module) {
                    c = document.getElementsByName("q")[0].value;
                    let b = c.match(d);
                    null != b && "object" == typeof a.LexCache
                        ? ((b = b[0].toLowerCase()),
                          "object" == typeof a.LexCache[b] || "object" == typeof a.LexCache[a.LexCache.list.indexOf(b)]
                              ? (a.debug && console.log("loading from JS object"), a.lex.cacheLoadArt(b))
                              : (a.debug && console.log("making new request"), a.lex.cacheSaveArt(b, !0)))
                        : (window.location = "/" + c);
                } else if ("LexBoxInput" == b.target.id) {
                    c = document.getElementById("LexBoxInput").value;
                    let b;
                    (b = c.match(d))
                        ? null === document.getElementById("LexBoxData")
                            ? (document.getElementById("LexBoxInput").value = "")
                            : a.decision.loadLexBox(document.getElementById("LexBoxData").dataset.lex, b[0])
                        : (b = c.match(/((?:ZH[-\/]?)?[a-zäöü-]{2,}(?:[-\/]?ZH)?) ?(\d{1,4}[a-zA-Z]*)/i))
                          ? a.decision.loadLexBox(b[1], b[2])
                          : ((b = c.match(/(\d{1,4}[a-zA-Z]*) ?((?:ZH[-\/]?)?[a-zäöü-]{2,}(?:[-\/]?ZH)?)/i)),
                            null === b
                                ? (document.getElementById("LexBoxInput").value = "")
                                : a.decision.loadLexBox(b[2], b[1]));
                } else window.location = "/" + document.getElementsByName("q")[0].value;
                l();
            }
            (37 == b.keyCode || 39 == b.keyCode) &&
                "q" !== document.activeElement.name &&
                "LexBoxInput" !== document.activeElement.id &&
                (("sr" === a.module || "zhlex" === a.module || "shlex" === a.module) &&
                    (37 == b.keyCode && a.lex.cacheLoadArt(a.lexArtPrev),
                    39 == b.keyCode && a.lex.cacheLoadArt(a.lexArtNext)),
                ("bge" === a.module || "aza" === a.module || "zhvgr" === a.module || "markermode" === a.module) &&
                    document.getElementById("LexBox").classList.contains("activeLexBox") &&
                    (37 == b.keyCode &&
                        "none" !== document.getElementById("LexBoxPrev").style.display &&
                        document.getElementById("LexBoxPrev").click(),
                    39 == b.keyCode &&
                        "none" !== document.getElementById("LexBoxNext").style.display &&
                        document.getElementById("LexBoxNext").click())),
                27 == b.keyCode &&
                    ("bge" === a.module || "aza" === a.module || "zhvgr" === a.module || "markermode" === a.module) &&
                    document.getElementById("LexBox").classList.contains("activeLexBox") &&
                    (b.preventDefault(), a.decision.closeLexBox()),
                27 == b.keyCode &&
                    ("sr" === a.module || "zhlex" === a.module || "shlex" === a.module) &&
                    "0px" === document.getElementById("LexIndex").style.right &&
                    (b.preventDefault(), a.lex.hideLexIndex());
        }
        function f() {
            function a(a) {
                if ("object" != typeof a.clipboardData) return;
                a.preventDefault();
                let b = "";
                for (let c = 0; c < window.getSelection().rangeCount; c++)
                    b = b + " " + window.getSelection().getRangeAt(c).toString();
                (b = b.replace(/ +/gm, " ")),
                    (b = b.replace(/\n (?=[A-ZÄÖÜ])/gm, "\n")),
                    (b = b.replace(/\n+/gm, "\n")),
                    (b = b.replace(/\t+/gm, "")),
                    a.clipboardData.setData("text/plain", b.trim());
            }
            document.body.addEventListener("copy", a), document.body.addEventListener("cut", a);
        }
        function g() {
            if (null !== window.location.pathname.match(/\/so$/i)) {
                let b = document.getElementsByClassName("pagebreak");
                for (let a = 0; a < b.length; a++) b[a].style.display = "none";
                let c = document.getElementsByClassName("note");
                for (let a = 0; a < c.length; a++) c[a].style.display = "none";
                a.debug && console.log("speech optimized");
            }
            h();
        }
        function h() {
            window.history.replaceState &&
                a.properURL &&
                window.location.pathname !== "/" + a.properURL &&
                window.history.replaceState(null, document.title, "/" + a.properURL);
        }
        function i(a) {
            let b = [];
            a.split(".").forEach(function (a) {
                0 < b.length
                    ? b.forEach(function (c) {
                          (c[a] = c[a] || {}), b.push(c[a]), b.shift();
                      })
                    : ((window[a] = window[a] || {}), b.push(window[a]));
            });
        }
        function j() {
            let a = document.getElementsByClassName("search")[0];
            a && a.addEventListener("click", k, !1);
            let b = document.getElementsByClassName("navbar")[0],
                c = document.getElementsByName("q")[0];
            c.addEventListener(
                "focus",
                function () {
                    b.classList.add("showbg");
                },
                !1
            ),
                c.addEventListener(
                    "blur",
                    function () {
                        (c.value = ""), b.classList.remove("showbg");
                    },
                    !1
                );
        }
        function k() {
            document.getElementsByName("q")[0].focus();
        }
        function l() {
            (document.getElementsByName("q")[0].value = ""), document.getElementsByName("q")[0].blur();
        }
        function m() {
            (touchstartX = 0), (touchcurX = 0);
        }
        function n(a, b, c) {
            i(b);
            let d = document.createElement("script");
            "noModule" in d
                ? ((d.type = "module"),
                  (d.textContent = 'import * as module from "' + a + '"; window.' + b + " = module;"),
                  c && (d.textContent += " window." + c + "()"))
                : o(a, function (a) {
                      let e = a.responseText,
                          f = "",
                          g = [],
                          h = [];
                      for (; Array.isArray((h = e.match(/export (?:function|var|let|const) ([a-zA-Z_-]+)/))); )
                          g.push(h[1]),
                              (e = e.replace(/export function /, "function ")),
                              (e = e.replace(/export var /, "var ")),
                              (e = e.replace(/export let /, "let ")),
                              (e = e.replace(/export const /, "const "));
                      g.forEach(function (a) {
                          f += "window." + b + "." + a + "=" + a + ";";
                      }),
                          (f += "}());"),
                          c && (f += "window." + c + "();"),
                          (e = "(function() {" + e + f),
                          (d.text = e);
                  }),
                document.head.appendChild(d),
                window.setTimeout(function () {
                    d.parentNode.removeChild(d);
                }, 1e3);
        }
        function o(a, b, c, d) {
            let e = new XMLHttpRequest(),
                f = c ? "POST" : "GET";
            e.open(f, a, !0),
                c && (!d && (d = "application/x-www-form-urlencoded"), e.setRequestHeader("Content-type", d)),
                (e.onreadystatechange = function () {
                    4 !== e.readyState || b(e);
                });
            4 === e.readyState || e.send(c);
        }
        (a.debug = !1),
            (a.loadJS = n),
            (a.sendRequest = o),
            (a.debounce = function (a, b) {
                let c;
                return function () {
                    let d = this,
                        e = arguments;
                    clearTimeout(c),
                        (c = setTimeout(function () {
                            (c = null), a.apply(d, e);
                        }, b));
                };
            }),
            (a.throttle = function (a, b) {
                let c = Date.now();
                return function () {
                    0 > c + b - Date.now() && ((c = Date.now()), a());
                };
            }),
            "index" === a.module
                ? (document.addEventListener("keydown", e, !1),
                  c(function () {
                      window.setTimeout(function () {
                          window.scrollTo(0, 1);
                      }, 0),
                          document.getElementById("start").focus();
                  }))
                : "bge" === a.module || "aza" === a.module || "zhvgr" === a.module || "markermode" === a.module
                  ? (n("/js/decision.2829.min.js", b + ".decision", b + ".decision.init"),
                    document.addEventListener("keydown", e, !1),
                    c(function () {
                        window.setTimeout(function () {
                            window.scrollTo(0, 1);
                        }, 0),
                            window.Hyphenator && Hyphenator.run(),
                            g(),
                            j(),
                            d(function () {
                                window.setTimeout(function () {
                                    document.getElementsByClassName("navbg")[0].classList.add("transitioning"),
                                        document.getElementById("content").classList.add("transitioning");
                                }, 500);
                            });
                    }))
                  : "sr" === a.module || "zhlex" === a.module || "shlex" === a.module
                    ? (n("/js/lex.2829.min.js", b + ".lex", b + ".lex.init"),
                      document.addEventListener("keydown", e, !1),
                      window.addEventListener(
                          "touchstart",
                          function (a) {
                              touchstartX = a.touches[0].pageX;
                          },
                          !1
                      ),
                      window.addEventListener(
                          "touchend",
                          function (b) {
                              (touchcurX = b.changedTouches[0].pageX),
                                  150 <= Math.abs(touchcurX - touchstartX)
                                      ? (touchcurX >= touchstartX
                                            ? (a.lex.cacheLoadArt(a.lexArtPrev),
                                              window.setTimeout(function () {
                                                  window.scrollTo(0, 1);
                                              }, 0))
                                            : (a.lex.cacheLoadArt(a.lexArtNext),
                                              window.setTimeout(function () {
                                                  window.scrollTo(0, 1);
                                              }, 0)),
                                        m())
                                      : m();
                          },
                          !1
                      ),
                      window.addEventListener("touchcancel", m, !1),
                      (a.lexLoading = !1),
                      h(),
                      c(function () {
                          window.setTimeout(function () {
                              window.scrollTo(0, 1);
                          }, 0),
                              window.Hyphenator && Hyphenator.run(),
                              j(),
                              f(),
                              window.setTimeout(function () {
                                  document.getElementsByClassName("navbg")[0].classList.add("transitioning"),
                                      document.getElementById("content").classList.add("transitioning");
                              }, 500);
                      }))
                    : "search" === a.module
                      ? (n("/js/search.2829.min.js", b + ".search", b + ".search.init"),
                        document.addEventListener("keydown", e, !1),
                        c(function () {
                            window.setTimeout(function () {
                                window.scrollTo(0, 1);
                            }, 0),
                                j(),
                                window.setTimeout(function () {
                                    document.getElementsByClassName("navbg")[0].classList.add("transitioning"),
                                        document.getElementById("content").classList.add("transitioning");
                                }, 500);
                        }))
                      : "error" === a.module &&
                        (document.addEventListener("keydown", e, !1),
                        h(),
                        c(function () {
                            window.setTimeout(function () {
                                window.scrollTo(0, 1);
                            }, 0),
                                j(),
                                document.getElementsByName("q")[0].focus(),
                                window.setTimeout(function () {
                                    document.getElementsByClassName("navbg")[0].classList.add("transitioning"),
                                        document.getElementById("content").classList.add("transitioning");
                                }, 500);
                        }));
    })(bgerli, "bgerli"),
    "bger.li" === window.location.hostname)
) {
    var _paq = _paq || [];
    _paq.push(["disableCookies"]),
        _paq.push(["trackPageView"]),
        _paq.push(["enableLinkTracking"]),
        (function () {
            _paq.push(["setTrackerUrl", "//analytics.bger.li/piwik.php"]), _paq.push(["setSiteId", "1"]);
            var a = document,
                b = a.createElement("script"),
                c = a.getElementsByTagName("script")[0];
            (b.type = "text/javascript"),
                (b.async = !0),
                (b.defer = !0),
                (b.src = "//analytics.bger.li/piwik.js"),
                c.parentNode.insertBefore(b, c);
        })();
}
window.setTimeout(deleteAllCookies, 3e3);
function deleteAllCookies() {
    let a = document.cookie.split(";");
    for (let b = 0; b < a.length; b++) {
        let c = a[b],
            d = c.indexOf("="),
            e = -1 < d ? c.substr(0, d) : c;
        document.cookie = e + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT";
    }
}
