function changeToTableView() {
  try {
    if (!document.getElementById("tableIcon").classList.add("iconSelected")) {
      document.getElementById("table").style = "display: inline-table;";
      document.getElementById("chart").style = "display: none;";
      document.getElementById("tableIcon").classList.add("iconSelected");
      document.getElementById("chartIcon").classList.remove("iconSelected");
    }
  } catch (error) {
    console.log(error);
    alert("Algo de errado aconteceu! Por favor contacte o suporte.");
  }
}

function changeToChartView() {
  try {
    if (
      !document.getElementById("chartIcon").classList.contains("iconSelected")
    ) {
      window.stop();
      fetch("hardware-estado-ticket-doughnut-chart/")
        .then((response) => response.json())
        .then((data) => {
          renderHardwareEstadoTicketDoughnutChart(data);
        })
        .catch((error) => console.error("Error:", error));
      fetch("hardware-estado-atendimento-doughnut-chart/")
        .then((response) => response.json())
        .then((data) => {
          renderHardwareEstadoAtendimentoDoughnutChart(data);
        })
        .catch((error) => console.error("Error:", error));
      fetch("hardware-count-ticket-resolved-bar-chart/")
        .then((response) => response.json())
        .then((data) => {
          renderHardwareCountTicketResolvedChart(data);
        })
        .catch((error) => console.error("Error:", error));
      document.getElementById("table").style = "display: none;";
      document.getElementById("chart").style = "display: initial;";
      document.getElementById("tableIcon").classList.remove("iconSelected");
      document.getElementById("chartIcon").classList.add("iconSelected");
    }
  } catch (error) {
    console.log(error);
    alert("Algo de errado aconteceu! Por favor contacte o suporte.");
  }
}

document.getElementById("tipoTicket").addEventListener("change", function () {
  try {
    var tipo = this.value;
    if (tipo === "software") {
      document.getElementById("softwareFields").style.display = "block";
      document.getElementById("hardwareFields").style.display = "none";
    } else if (tipo === "hardware") {
      document.getElementById("softwareFields").style.display = "none";
      document.getElementById("hardwareFields").style.display = "block";
    }
  } catch (error) {
    console.log(error);
    alert("Algo de errado aconteceu! Por favor contacte o suporte.");
  }
});

function downloadTicketCsv() {
  try {
    let hardwareUrl = "/download/hardware/";
    const hardwareAnchor = document.createElement("a");
    hardwareAnchor.href = hardwareUrl;
    hardwareAnchor.download = "hardware_tickets.csv";
    document.body.appendChild(hardwareAnchor);
    hardwareAnchor.click();
    document.body.removeChild(hardwareAnchor);

    let softwareUrl = "/download/software/";
    const softwareAnchor = document.createElement("a");
    softwareAnchor.href = softwareUrl;
    softwareAnchor.download = "software_tickets.csv";
    document.body.appendChild(softwareAnchor);
    softwareAnchor.click();
    document.body.removeChild(softwareAnchor);
  } catch (error) {
    console.log(error);
    alert("Algo de errado aconteceu! Por favor contacte o suporte.");
  }
}
