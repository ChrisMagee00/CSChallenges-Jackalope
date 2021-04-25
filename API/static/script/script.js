function navControl() {
    //When the button is clicked, check if the sidebar is currently open or closed
    //If open, close it by setting width and padding to 0
    if (document.getElementById("mySidebar").style.width == "250px") {
        document.getElementById("mySidebar").style.width = "0";
        document.getElementById("main").style.marginLeft = "0";
        document.getElementById("navopener").innerHTML = "☰ Open Sidebar";
    }
    //else, open it by setting the sidebar width and main div padding
    else {
        document.getElementById("mySidebar").style.width = "250px";
        document.getElementById("main").style.marginLeft = "250px";
        document.getElementById("navopener").innerHTML = "☰ Close Sidebar";
    }
}