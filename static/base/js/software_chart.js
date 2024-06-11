var mySoftwareDoughtnutEstadoTicket;
var mySoftwareDoughtnutEstadoAtendimento;
var mySoftwareChartCountTicketResolved;

function goToHSoftwareDiv() {
  try {
    if (
      !document
        .getElementById("softwareDiv")
        .classList.contains("divChartSelected")
    ) {
      document.getElementById("hardwareContent").style = "display: none;";
      document.getElementById("softwareContent").style = "display: flex;";
      document
        .getElementById("hardwareDiv")
        .classList.remove("divChartSelected");
      document.getElementById("softwareDiv").classList.add("divChartSelected");
      fetch("software-estado-ticket-doughnut-chart/")
        .then((response) => response.json())
        .then((data) => {
          renderSoftwareEstadoTicketDoughnutChart(data);
        })
        .catch((error) => console.error("Error:", error));
      fetch("software-estado-atendimento-doughnut-chart/")
        .then((response) => response.json())
        .then((data) => {
          renderSoftwareEstadoAtendimentoDoughnutChart(data);
        })
        .catch((error) => console.error("Error:", error));
      fetch("software-count-ticket-resolved-bar-chart/")
        .then((response) => response.json())
        .then((data) => {
          renderSoftwareCountTicketResolvedChart(data);
        })
        .catch((error) => console.error("Error:", error));
    }
  } catch (error) {
    console.log(error);
    alert("Algo de errado aconteceu! Por favor contacte o suporte.");
  }
}

function renderSoftwareEstadoTicketDoughnutChart(data) {
  try {
    if (mySoftwareDoughtnutEstadoTicket) {
      mySoftwareDoughtnutEstadoTicket.destroy();
    }
    var canvas = document.getElementById("softwareDoughtnutEstadoTicket");
    var ctx = canvas.getContext("2d");
    mySoftwareDoughtnutEstadoTicket = new Chart(ctx, {
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

function renderSoftwareEstadoAtendimentoDoughnutChart(data) {
  try {
    if (mySoftwareDoughtnutEstadoAtendimento) {
      mySoftwareDoughtnutEstadoAtendimento.destroy();
    }
    var canvas = document.getElementById("softwareDoughtnutEstadoAtendimento");
    var ctx = canvas.getContext("2d");
    mySoftwareDoughtnutEstadoAtendimento = new Chart(ctx, {
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

function renderSoftwareCountTicketResolvedChart(data) {
  try {
    if (mySoftwareChartCountTicketResolved) {
      mySoftwareChartCountTicketResolved.destroy();
    }
    var canvas = document.getElementById("softwareCountTicketResolved");
    var ctx = canvas.getContext("2d");
    mySoftwareChartCountTicketResolved = new Chart(ctx, {
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
