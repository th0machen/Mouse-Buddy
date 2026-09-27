const status = document.getElementById("status");
const duration = document.getElementById("duration");


document.getElementById("startBtn").addEventListener("click", async () => {

    try {

        const selectedDuration = Number(
            duration.value
        );


        const response = await fetch(
            "http://localhost:5000/start",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    duration: selectedDuration
                })
            }
        );


        const data = await response.json();

        console.log(data);

        status.textContent = "Running";


    } catch (error) {

        console.error(error);

        status.textContent = "Controller Offline";
    }

});


document.getElementById("stopBtn").addEventListener("click", async () => {

    try {

        const response = await fetch(
            "http://localhost:5000/stop",
            {
                method: "POST"
            }
        );


        const data = await response.json();

        console.log(data);

        status.textContent = "Stopped";


    } catch (error) {

        console.error(error);

        status.textContent = "Controller Offline";
    }

});