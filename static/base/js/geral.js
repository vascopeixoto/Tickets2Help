function editar_modal(ticketId, tipo) {
  $.ajax({
    url: "/editdetailsticket/" + tipo + "/" + ticketId + "/",
    success: function (data) {},
    error: function (xhr, status, error) {
      console.error("Error:", error);
    },
  });
}
function changeToTableView() {
  if (!document.getElementById("tableIcon").classList.add("iconSelected")) {
    document.getElementById("table").style = "display: inline-table;";
    document.getElementById("chart").style = "display: none;";
    document.getElementById("tableIcon").classList.add("iconSelected");
    document.getElementById("chartIcon").classList.remove("iconSelected");
  }
}
function changeToChartView() {
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
}
document.getElementById("tipoTicket").addEventListener("change", function () {
  var tipo = this.value;
  if (tipo === "software") {
    document.getElementById("softwareFields").style.display = "block";
    document.getElementById("hardwareFields").style.display = "none";
  } else if (tipo === "hardware") {
    document.getElementById("softwareFields").style.display = "none";
    document.getElementById("hardwareFields").style.display = "block";
  }
});
