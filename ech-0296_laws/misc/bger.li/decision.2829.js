var ns = bgerli,
    nsn = "bgerli";
export function init() {
    document.addEventListener("click", decisionClickHandler, !1),
        initCitToggler(),
        regLexLinkHandlers(),
        navInitMarkerMode(),
        navInitLexBox();
}
function navInitMarkerMode() {
    let a = document.getElementsByClassName("markermode")[0];
    a &&
        a.addEventListener(
            "click",
            function () {
                a.classList.add("loading"), ns.loadJS("/js/markermode.2829.min.js", nsn + ".mm", nsn + ".mm.loadUI");
            },
            !1
        );
}
function navInitLexBox() {
    let a = document.getElementsByClassName("lexbox")[0];
    a &&
        a.addEventListener(
            "click",
            function () {
                toggleLexBox();
            },
            !1
        );
}
function decisionClickHandler(a) {
    ("undefined" != typeof a &&
        ("" === document.getElementById("LexBox").innerHTML ||
            a.target.classList.contains("lexbox") ||
            "P" === a.target.tagName ||
            "A" === a.target.tagName ||
            "H1" === a.target.tagName ||
            "SPAN" === a.target.tagName ||
            "INPUT" === a.target.tagName ||
            "STRONG" === a.target.tagName ||
            "B" === a.target.tagName)) ||
        closeLexBox();
}
function initCitToggler() {
    let a = document.getElementById("cittoggle");
    a &&
        (a.onclick = function (a) {
            a.preventDefault();
            let b = document.getElementsByClassName("citinfo");
            if ("block" === b[0].style.display) for (let a = 0; a < b.length; a++) b[a].style.display = "none";
            else for (let a = 0; a < b.length; a++) b[a].style.display = "block";
        });
}
export function toggleLexBox() {
    let a = document.getElementById("content"),
        b = document.getElementById("LexBox"),
        c = document.getElementById("LexBoxInput");
    a.classList.contains("activeLexBox")
        ? isFullyOnScreen(b)
            ? closeLexBox(!1)
            : isPartiallyOnScreen(b) && b.clientHeight > window.innerHeight
              ? closeLexBox(!1)
              : (offsetLexBox(),
                null !== c &&
                    window.setTimeout(function () {
                        c.focus();
                    }, 750))
        : "" === b.innerHTML
          ? loadLexBox(null, null)
          : (offsetLexBox(), showLexBox(), null !== c && c.focus());
}
function showLexBox() {
    document.getElementById("content").classList.add("activeLexBox"),
        document.getElementById("LexBox").classList.add("activeLexBox");
}
export function closeLexBox(a) {
    document.getElementById("content").classList.remove("activeLexBox"),
        document.getElementById("LexBox").classList.remove("activeLexBox"),
        "undefined" == typeof a && (a = !0),
        a && (document.getElementById("LexBox").innerHTML = ""),
        (window.loaded_art = "");
}
export function loadLexBox(a, b) {
    if ((offsetLexBox(), a + b !== window.loaded_art))
        if (
            ((window.loaded_art = a + b),
            (document.getElementById("LexBox").innerHTML = '<img class="loader" src="/css/loader.gif">'),
            showLexBox(),
            null === a && null === b)
        )
            (document.getElementById("LexBox").innerHTML =
                '<a id="LexBoxClose" href="."></a><a id="LexBoxSearch" href="."></a><input id="LexBoxInput" type="text" autocomplete="off" style="width: 260px">"'),
                window.setTimeout(function () {
                    registerMainLexBoxButtons(), document.getElementById("LexBoxInput").focus();
                }, 200);
        else {
            let c;
            (c =
                0 === a.toUpperCase().indexOf("ZH") ||
                -1 !== a.toUpperCase().indexOf("/ZH") ||
                -1 !== a.toUpperCase().indexOf("ZH/")
                    ? "/modules/zhlex.php?LexBox=1&lex=" + a.replace(/[-\/]?ZH[-\/]?/i, "") + "&art=" + b
                    : 0 === a.toUpperCase().indexOf("SH")
                      ? "/modules/shlex.php?LexBox=1&lex=" + a.replace(/[-\/]?SH[-\/]?/i, "") + "&art=" + b
                      : "/modules/sr.php?LexBox=1&lex=" + a + "&art=" + b),
                ns.sendRequest(c, loadLexBoxResponseHandler);
        }
}
function loadLexBoxResponseHandler(a) {
    if (
        ((document.getElementById("LexBox").innerHTML = a.responseText),
        window.Hyphenator && hyphntLexBox(),
        null !== document.getElementById("LexBoxData"))
    ) {
        let a = document.getElementById("LexBoxData").dataset.part,
            b = document.getElementById("LexBoxData").dataset.nart;
        "" === a && (document.getElementById("LexBoxPrev").style.display = "none"),
            "" === b && (document.getElementById("LexBoxNext").style.display = "none"),
            "" !== a &&
                (document.getElementById("LexBoxPrev").onclick = function (b) {
                    b.preventDefault(), loadLexBox(document.getElementById("LexBoxData").dataset.lex, a);
                }),
            "" !== b &&
                (document.getElementById("LexBoxNext").onclick = function (a) {
                    a.preventDefault(), loadLexBox(document.getElementById("LexBoxData").dataset.lex, b);
                });
    }
    registerMainLexBoxButtons();
}
function offsetLexBox() {
    let a = window.pageYOffset ? window.pageYOffset : document.documentElement.scrollTop;
    return (document.getElementById("LexBox").style.top = a + "px"), a;
}
function isFullyOnScreen(a) {
    let b = a.getBoundingClientRect();
    return 0 <= b.top && b.bottom <= window.innerHeight;
}
function isPartiallyOnScreen(a) {
    let b = a.getBoundingClientRect();
    return (
        (0 <= b.top && b.top < window.innerHeight) ||
        (0 <= b.bottom && b.bottom < window.innerHeight) ||
        (a.clientHeight > window.innerHeight && 0 > b.top && b.bottom > window.innerHeight)
    );
}
function registerMainLexBoxButtons() {
    (document.getElementById("LexBoxSearch").onclick = function (a) {
        a.preventDefault();
        (document.getElementById("LexBoxContent").innerHTML =
            '<input id="LexBoxInput" type="text" autocomplete="off">'),
            document.getElementById("LexBoxContent").children[0].focus();
    }),
        (document.getElementById("LexBoxClose").onclick = function (a) {
            a.preventDefault(), closeLexBox();
        });
}
function regLexLinkHandlers() {
    let a = document.getElementsByClassName("LexLink");
    for (let b = 0; b < a.length; b++) a[b].onclick = lexLinkClickHandler;
}
function lexLinkClickHandler(a) {
    if ((a.preventDefault(), 960 <= window.innerWidth || 960 <= document.documentElement.clientWidth)) {
        let a = this.href.match(/([%\w-]{2,})_(\d{1,4}[a-zA-Z]*)/);
        loadLexBox(decodeURI(a[1]), a[2]);
    } else window.location.href = this.href;
}
function hyphntLexBox() {
    Hyphenator.config({
        selectorfunction: function () {
            return document.getElementsByName("LexBox");
        },
        onhyphenationdonecallback: function () {
            (document.getElementById("LexBox").style.display = "block"),
                (document.getElementById("LexBox").style.opacity = 1);
        },
    }),
        Hyphenator.run();
}
