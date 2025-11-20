const cards = document.querySelectorAll(".card");

cards.forEach(card => {
    card.addEventListener("click", function(e){
        this.classList.toggle("is-flipped");
        // 同じdivの次の要素をとる
        // クリックされた要素（img.backなど)
        const clicked = e.target;
        // このカードを取得
        const cardInner = clicked.closest(".card-inner");
        // 同じカード内のfrontとbackを取得
        const frontImg = cardInner.querySelector(".front");
        console.log("front:", frontImg.src);
    });
});

