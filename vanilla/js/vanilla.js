function addTitleSeparator() {
    let main = document.getElementById("main-content");
    let firstTitle = main.getElementsByTagName("h1");
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

addTitleSeparator();
convertAdmonitions();