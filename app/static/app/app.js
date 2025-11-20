const cards = document.querySelectorAll(".card");

cards.forEach(card => {
    card.addEventListener("click", function(){
        this.classList.toggle("is-flipped");
        // 同じdivの次の要素をとる
        
    });
});
document.addEventListener('click', function(event){
    console.log('クリックした要素:',event.target);
});
// document.addEventListener('click', function(event){
//     const clickedBackImage = event.target;
//     // クリックされたのが裏面の画像要素か確認
//     if (!clickedBackImage.classList.contains('card-back')){
//         return;  //対象外なら終了
//     }
// })
// // クリックされた要素(裏面の画像要素)
// const clickedBackImage = event.target;
// // 裏面の画像要素を親要素(div class="back")を取得
// const backDiv = clickedBackImage.parentElement;
// // さらに親そうそ(div class="card")を取得
// const cardElement =backDiv.parentElement;
// // 親要素(cardElement)の中から、表面の画像要素(img class="number")を探す
// const frontImageElement = cardElement.querySelector('.card-front');
// // これで、トランプの画像要素が取得できる
// console.log(frontImageElement);