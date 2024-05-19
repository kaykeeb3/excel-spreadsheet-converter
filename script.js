document
  .getElementById("reportForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();
    const jsonData = document.getElementById("jsonData").value.trim();

    fetch("http://localhost:5000/generate-report?type=excel", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: jsonData,
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Erro ao gerar o relatório");
        }
        return response.blob();
      })
      .then((blob) => {
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = "report.xlsx";
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        alert("Relatório gerado com sucesso!");
      })
      .catch((error) => {
        console.error("Error:", error);
        alert("Erro ao gerar o relatório");
      });
  });
