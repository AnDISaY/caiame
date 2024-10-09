const showMore = document.querySelector('.courses__cards__show-more');

function showCard() {
    const showMore = document.querySelector('.courses__cards__show-more');
    var cards = Array.from(document.querySelectorAll('.hide-content'));
    let count = 0;

    for (const card of cards.slice(count, count+6)) {
        card.classList.remove("hide-content");
        card.classList.add("show-content");
    }

    showMore.remove();
    if (cards.slice(count).length > 6) {
        const showMoreEl = document.createElement('div');
        showMoreEl.classList.add('courses__cards__show-more');
        showMoreEl.classList.add('show-content');
        const showMoreSpan = document.createElement('span');
        showMoreSpan.innerHTML = "Посмотреть больше курсов";
        showMoreEl.appendChild(showMoreSpan);
        document.querySelector('.courses__cards__wrapper').appendChild(showMoreEl);
        const showMore2 = document.querySelector('.courses__cards__show-more');
        showMore2.addEventListener('click', showCard);
    }

    count += 6;
}

showMore.addEventListener('click', showCard);