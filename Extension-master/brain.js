//IMPORTANT, CONSOLE LOG DOES NOT WORK IN EXTENSION FOR NOW, IDK WHY. DONT RELY ON IT.
//To debug make a div, put the debug inside that div.

btn = document.getElementById("init")
list = document.getElementById("product_list")

btn.addEventListener('click', function() {
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
        var activeTab = tabs[0];
        var pageTitle = activeTab.title;
      
        // Now you can use pageTitle as needed
        btn.innerHTML = pageTitle;
        // Do something with the title, like updating your extension UI
      });
      
    mainFunction();
});

async function mainFunction() {
    try {
        list.innerHTML = "Fetching data..."
        response = await fetch("http://localhost:5000/ping"); // ALWAYYS AWAIT FETCH
        if (response.ok) {
            const responseText = await response.text(); //REMEMBER TO AWAIT THIS, OR DIE
            list.innerHTML = responseText;
        } else {
            list.innerHTML = `Error: ${response.status} - ${response.statusText}`;
        }
    } catch (error) {
        list.innerHTML = `Error: ${response.error}`
    }
}
