async function update(){
    const res = await fetch("/api/gps");
    const data = await res.json();

    document.getElementById("fix").textContent = data.fix ? "YES" : "NO FIX";
    document.getElementById("lat").textContent = data.lat ?? "--";
    document.getElementById("lon").textContent = data.lon ?? "--";
    document.getElementById("alt").textContent = data.alt ?? "--";
    document.getElementById("sats").textContent = data.sats;
    document.getElementById("hdop").textContent = data.hdop ?? "--";
}

update();
setInterval(update, 1000);