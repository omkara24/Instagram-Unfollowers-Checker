document.addEventListener("DOMContentLoaded", () => {

    const searchInput = document.getElementById("searchInput");

    if (searchInput) {

        searchInput.addEventListener("keyup", () => {

            const searchText =
                searchInput.value.toLowerCase();

            const cards =
                document.querySelectorAll(".user-card");

            cards.forEach(card => {

                const username =
                    card.querySelector(".username")
                        .textContent
                        .toLowerCase();

                if (
                    username.includes(searchText)
                ) {
                    card.style.display = "";
                }
                else {
                    card.style.display = "none";
                }

            });

        });

    }

});