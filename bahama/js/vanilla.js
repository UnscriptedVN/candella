/* vanilla.js
 * Utilities for conversions from PyMarkdown to Vanilla
 * (C) 2021 Marquis Kurt.
 * 
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at https://mozilla.org/MPL/2.0/.
 */

function getAllExternalLinks() {
    let main = document.getElementById("main-content");
    for (const link of main.getElementsByTagName("a")) {
        if (link.href.search(window.location.hostname) === -1) {
            link.classList.add("p-link--external")
        }
    }
}

function getLabels() {
    let main = document.getElementById("main-content");
    main.innerHTML = main.innerHTML
        .replace(/\{label:deprecated\}/g, "<span class=\"p-label--deprecated\">Deprecated</span>")
        .replace(/\{label:new\}/g, "<span class=\"p-label--new\">New</span>")
        .replace(/\{label:updated\}/g, "<span class=\"p-label--updated\">Updated</span>");
}

function addTitleSeparator() {
    let main = document.getElementById("main-content");
    let firstTitle = main.getElementsByTagName("h1");
    if (firstTitle.length < 1) return;
    firstTitle[0].after(document.createElement("hr"));
}

function convertAdmonitions() {
    let admonitions = document.getElementsByClassName("admonition");
    for (const admonition of admonitions) {
        if (admonition.classList.contains("danger") || admonition.classList.contains("critical")) {
            admonition.classList.add("p-notification--negative");
        }
        else if (admonition.classList.contains("warning") || admonition.classList.contains("attention")) {
            admonition.classList.add("p-notification--caution");
        }
        else if (admonition.classList.contains("important") || admonition.classList.contains("note") || admonition.classList.contains("tip")) {
            admonition.classList.add("p-notification--information");
        }
        else {
            admonition.classList.add("p-notification");
        }

        let newElement = document.createElement("p");
        newElement.classList.add("p-notification__response");
        newElement.setAttribute("role", "status");
            
        let response = document.createElement("span");
        response.classList.add("p-notification__status");
        response.innerText = admonition.children[0].innerText;
        
        newElement.appendChild(response);
        newElement.appendChild(admonition.children[1]);

        admonition.appendChild(newElement);
        admonition.removeChild(admonition.children[0]);
    }
}

getAllExternalLinks();
getLabels();
addTitleSeparator();
convertAdmonitions();
