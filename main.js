// ==UserScript==
// @name         qidian anti map
// @namespace    https://greasyfork.org/zh-CN/scripts/452806-qidian-anti-map
// @version      0.0.4
// @description  anti map used for qidian
// @author       initdc
// @license      MPL-2.0
// @homepageURL  https://github.com/initdc/qidian-anti-map
// @supportURL   https://github.com/initdc/qidian-anti-map/issues/new
// @match        https://www.lqzw.org/du/67324/25645342.html
// @icon         https://www.google.com/s2/favicons?sz=64&domain=www.qidian.com
// @grant        none
// ==/UserScript==

(async function () {
  "use strict";

  function replaceDOM(d, pairs) {
    if (d) {
      let content = "";
      let inner = d.innerHTML;
      pairs.forEach((pair) => {
        if (pair[0].length > 1) {
          console.log(pair[0], "->", pair[1]);
          content = inner.replace(pair[0], pair[1]);
          inner = content;
        }
      });
      d.innerHTML = content;
    }
  }

  const map_url =
    "https://raw.githubusercontent.com/initdc/qidian-anti-map/master/dist/111.json";
  let fetchRes = await fetch(map_url);
  let resp = await fetchRes.json();
  //console.log(resp);

  const ID_Map = ["txt"];
  const classMap = [];
  
  ID_Map.forEach((id) => {
    const d = document.getElementById(id);
    replaceDOM(d, resp);
  });

  classMap.forEach((c) => {
    const d = document.getElementsByClassName(c)[0];
    replaceDOM(d, resp);
  });
})();
