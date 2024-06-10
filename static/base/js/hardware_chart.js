var myHardwareDoughtnutEstadoTicket;
var myHardwareDoughtnutEstadoAtendimento;
var myHardwareChartCountTicketResolved;

function goToHardwareDiv() {
  if (
    !document
      .getElementById("hardwareDiv")
      .classList.contains("divChartSelected")
  ) {
    window.stop();
    document.getElementById("softwareContent").style = "display: none;";
    document.getElementById("hardwareContent").style = "display: flex;";
    document.getElementById("softwareDiv").classList.remove("divChartSelected");
    document.getElementById("hardwareDiv").classList.add("divChartSelected");
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
  }
}
function renderHardwareEstadoTicketDoughnutChart(data) {
  try {
    if (myHardwareDoughtnutEstadoTicket) {
      myHardwareDoughtnutEstadoTicket.destroy();
    }
    var canvas = document.getElementById("hardwareDoughtnutEstadoTicket");
    var ctx = canvas.getContext("2d");
    myHardwareDoughtnutEstadoTicket = new Chart(ctx, {
      type: "doughnut",
      data: {
        labels: data.labels,
        datasets: [
          {
            data: data.data,
            backgroundColor: [
              "rgba(255, 165, 0, 0.5)",
              "rgba(54, 162, 235, 0.5)",
              "rgba(255, 0, 0, 0.7)",
            ],
            borderColor: [
              "rgba(255, 165, 0, 1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 0, 0, 1)",
            ],
            borderWidth: 1,
          },
        ],
      },
      options: {
        responsive: true,
        legend: {
          display: true,
          position: "bottom",
        },
      },
    });
  } catch (error) {
    console.log(error);
    alert("Algo de errado aconteceu! Por favor contacte o suporte.");
  }
}
function renderHardwareEstadoAtendimentoDoughnutChart(data) {
  try {
    if (myHardwareDoughtnutEstadoAtendimento) {
      myHardwareDoughtnutEstadoAtendimento.destroy();
    }
    var canvas = document.getElementById("hardwareDoughtnutEstadoAtendimento");
    var ctx = canvas.getContext("2d");
    myHardwareDoughtnutEstadoAtendimento = new Chart(ctx, {
      type: "doughnut",
      data: {
        labels: data.labels,
        datasets: [
          {
            data: data.data,
            backgroundColor: [
              "rgba(255, 0, 0, 0.7)",
              "rgba(255, 165, 0, 0.5)",
              "rgba(54, 162, 235, 0.5)",
            ],
            borderColor: [
              "rgba(255, 165, 0, 1)",
              "rgba(255, 165, 0, 1)",
              "rgba(54, 162, 235, 1)",
            ],
            borderWidth: 1,
          },
        ],
      },
      options: {
        responsive: true,
        legend: {
          display: true,
          position: "bottom",
        },
      },
    });
  } catch (error) {
    console.log(error);
    alert("Algo de errado aconteceu! Por favor contacte o suporte.");
  }
}
function renderHardwareCountTicketResolvedChart(data) {
  try {
    if (myHardwareChartCountTicketResolved) {
      myHardwareChartCountTicketResolved.destroy();
    }
    var canvas = document.getElementById("hardwareCountTicketResolved");
    var ctx = canvas.getContext("2d");
    myHardwareChartCountTicketResolved = new Chart(ctx, {
      type: "bar",
      data: {
        labels: data.labels,
        datasets: [
          {
            label: "Tickets resolvidos",
            data: data.data,
            backgroundColor: ["rgba(216, 118, 213, 0.6)"],
            borderColor: ["rgba(216, 118, 213, 1)"],
            borderWidth: 1,
          },
        ],
      },
      options: {
        responsive: true,
        scales: {
          x: {
            position: "bottom",
          },
          y: {
            beginAtZero: true,
            ticks: {
              stepSize: 1,
            },
          },
        },
        legend: {
          display: true,
          position: "bottom",
        },
      },
    });
  } catch (error) {
    console.log(error);
    alert("Algo de errado aconteceu! Por favor contacte o suporte.");
  }
}
