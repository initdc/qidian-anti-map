// ==UserScript==
// @name         qidian anti map
// @namespace    https://greasyfork.org/zh-CN/scripts/452806-qidian-anti-map
// @version      0.1
// @description  anti map used for qidian
// @author       initdc
// @license      MPL-2.0
// @homepageURL  https://github.com/initdc/qidian-anti-map
// @supportURL   https://github.com/initdc/qidian-anti-map/issues/new
// @match        https://www.81new.cc/355/355246/103241950.html
// @match        https://www.wanben.org/94369319/195266115.html
// @icon         https://www.google.com/s2/favicons?sz=64&domain=www.qidian.com
// @grant        none
// ==/UserScript==

(async function () {
    "use strict";
  
    const map_url =
      "https://raw.githubusercontent.com/initdc/qidian-anti-map/master/map.json";
    let fetchRes = await fetch(map_url);
    let resp = await fetchRes.json();
    //console.log(resp);
  
    const classMap = ["articlecontent", "readerCon"];
    classMap.forEach((c) => {
      const d = document.getElementsByClassName(c)[0];
      let content = "";
      if (d) {
        let inner = d.innerHTML;
        resp.forEach((pair) => {
          content = inner.replace(pair[0], pair[1]);
          inner = content;
        });
        d.innerHTML = content;
      }
    });
  })();
  