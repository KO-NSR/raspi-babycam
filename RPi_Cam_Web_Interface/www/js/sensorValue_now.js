function fetchSensorData() {
    fetch('/html/data/temp.txt')
        .then(response => response.text())
        .then(temp => {
            return fetch('/html/data/humi.txt')
                .then(response => response.text())
                .then(humi => {
                    document.getElementById("temp-value").innerText = "温度：" + temp.trim() + "°C";
                    document.getElementById("humi-value").innerText = "湿度：" + humi.trim() + "%";
                });
        })
        .catch(error => {
            console.error("センサー読み込み失敗：", error);
            document.getElementById("temp-value").innerText = "温度：取得失敗";
            document.getElementById("temp-value").innerText = "湿度：取得失敗";
        });
}

setInterval(fetchSensorData, 5000);
window.onload = fetchSensorData;

