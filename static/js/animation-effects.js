function findValidId(unusefulId) {
    if (document.getElementById(unusefulId) && unusefulId <=10) {
        return unusefulId;
    }
    unusefulId++; 
    return findValidId(unusefulId);  
}

let dropdownbuttons = document.querySelectorAll(".btn-dropdown");
for (let i = 0; i < dropdownbuttons.length; i++){
    dropdownbuttons[i].addEventListener("click",() =>{
        if (document.getElementById(i)) {
            document.getElementById(i).classList.toggle("show");
        } else {
            document.getElementById(findValidId(i)).classList.toggle("show");
        }
    });
}

/*
<button id="btn{{reminder.id}}" class="btn-dropdown">
                                            <p>Finished on</p>
                                            <i style="font-size:30px;" class="ri-arrow-down-s-fill"></i>
                                        </button>
*/