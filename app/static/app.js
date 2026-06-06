const form = document.getElementById("record-form");
if (form) {
  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    const payload = Object.fromEntries(new FormData(form).entries());
    const response = await fetch("/api/records", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    const message = document.getElementById("message");
    message.textContent = response.ok ? "已提交" : "提交失败";
    if (response.ok) {
      form.reset();
    }
  });
}
