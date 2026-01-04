document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".card").forEach((card, index) => {
    card.style.opacity = 0;
    card.style.transform = "translateY(20px)";
    setTimeout(() => {
      card.style.transition = "all 0.5s ease";
      card.style.opacity = 1;
      card.style.transform = "translateY(0)";
    }, 80 * index);
  });

  document.querySelectorAll("form input").forEach((input) =>
    input.addEventListener("keypress", (e) => {
      if (e.key === "Enter") {
        const form = e.target.closest("form");
        if (form) form.submit();
      }
    })
  );

  const searchInput = document.querySelector("[data-todo-search]");
  if (searchInput) {
    searchInput.addEventListener("input", (e) => {
      const value = e.target.value.toLowerCase();
      document.querySelectorAll("[data-todo-item]").forEach((item) => {
        const title = item.getAttribute("data-todo-title") || "";
        const desc = item.getAttribute("data-todo-desc") || "";
        const text = (title + " " + desc).toLowerCase();
        item.style.display = text.includes(value) ? "" : "none";
      });
    });
  }

  document.querySelectorAll("[data-todo-complete]").forEach((checkbox) => {
    checkbox.addEventListener("change", (e) => {
      const item = e.target.closest("[data-todo-item]");
      if (!item) return;
      if (e.target.checked) {
        item.classList.add("completed");
      } else {
        item.classList.remove("completed");
      }
    });
  });
});
