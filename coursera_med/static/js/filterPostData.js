function createCourse(resp) {
  courses = document.querySelectorAll('.courses__card');
  courses.forEach(courses => {courses.remove()});
  notFind = document.querySelector('.notfindtext');
  const showMore = document.querySelector('.courses__cards__show-more');

  if (showMore) {
    showMore.remove()
  }
  if (notFind) {
    notFind.remove();
  }

  if (resp['courses'].length != 0 ) {
    if (resp['courses'].length > 6) {
      for (index in resp['courses'].slice(0, 6)) {
        fields = resp['courses'][index]['fields'];
  
        course = document.createElement("a");
        course.classList.add("courses__card");
        course.classList.add("show-content");
        course.href = `/courses/${resp['courses'][index]['pk']}`;

        tags = document.createElement("div");
        tags.classList.add("courses__card__tags");
        tag = document.createElement("div");
        tag.classList.add("courses__card__tag");
        tag.innerHTML = fields['specialization']
        tag2 = document.createElement("div");
        tag2.classList.add("courses__card__tag");
        tag2.innerHTML = fields['difficulty']
        tag3 = document.createElement("div");
        tag3.classList.add("courses__card__tag");
        tag3.innerHTML = fields['credit_type']
        tags.appendChild(tag);
        tags.appendChild(tag2);
        tags.appendChild(tag3);
        course.appendChild(tags);
        
        image = document.createElement("div"); 
        image.classList.add('courses__card__image');
        img = document.createElement("img"); 
        img.src = `/media/${fields['image']}`;
        img.alt = "Course image";
        image.appendChild(img);
        course.appendChild(image);

        title = document.createElement('div')
        title.classList.add('courses__card__title')
        title.innerHTML = fields['name']
        course.appendChild(title)

        description = document.createElement('div')
        description.classList.add('courses__card__description')
        description.innerHTML = fields['short_description']
        course.appendChild(description)

        more = document.createElement('div')
        more.classList.add('courses__card__more')
        more.innerHTML = "Подробнее"
        course.appendChild(more)
    
    
        document.querySelector('.courses__cards__wrapper').appendChild(course);
      }
      const showMoreEl = document.createElement('div');
      showMoreEl.classList.add('courses__cards__show-more');
      showMoreEl.classList.add('show-content');
      const showMoreSpan = document.createElement('span');
      showMoreSpan.innerHTML = "Посмотреть больше курсов";
      showMoreEl.appendChild(showMoreSpan);
      document.querySelector('.courses__cards__wrapper').appendChild(showMoreEl);
      const showMore2 = document.querySelector('.courses__cards__show-more');
      showMore2.addEventListener('click', showCard);

      for (index in resp['courses'].slice(6)) {
        console.log(Number(index)+6)
        fields = resp['courses'][Number(index)+6]['fields'];

        course = document.createElement("a");
        course.classList.add("courses__card");
        course.classList.add("hide-content");
        course.href = `/courses/${resp['courses'][Number(index)+6]['pk']}`;

        tags = document.createElement("div");
        tags.classList.add("courses__card__tags");
        tag = document.createElement("div");
        tag.classList.add("courses__card__tag");
        tag.innerHTML = fields['specialization']
        tag2 = document.createElement("div");
        tag2.classList.add("courses__card__tag");
        tag2.innerHTML = fields['difficulty']
        tag3 = document.createElement("div");
        tag3.classList.add("courses__card__tag");
        tag3.innerHTML = fields['credit_type']
        tags.appendChild(tag);
        tags.appendChild(tag2);
        tags.appendChild(tag3);
        course.appendChild(tags);
        
        image = document.createElement("div"); 
        image.classList.add('courses__card__image');
        img = document.createElement("img"); 
        img.src = `/media/${fields['image']}`;
        img.alt = "Course image";
        image.appendChild(img);
        course.appendChild(image);

        title = document.createElement('div')
        title.classList.add('courses__card__title')
        title.innerHTML = fields['name']
        course.appendChild(title)

        description = document.createElement('div')
        description.classList.add('courses__card__description')
        description.innerHTML = fields['short_description']
        course.appendChild(description)

        more = document.createElement('div')
        more.classList.add('courses__card__more')
        more.innerHTML = "Подробнее"
        course.appendChild(more)
    
    
        document.querySelector('.courses__cards__wrapper').appendChild(course);
      }
    } else {
      for (index in resp['courses']) {
        fields = resp['courses'][index]['fields'];

        course = document.createElement("a");
        course.classList.add("courses__card");
        course.href = `/courses/${resp['courses'][index]['pk']}`;

        tags = document.createElement("div");
        tags.classList.add("courses__card__tags");
        tag = document.createElement("div");
        tag.classList.add("courses__card__tag");
        console.log(fields)
        console.log(fields['specialization'])
        tag.innerHTML = fields['specialization']
        tag2 = document.createElement("div");
        tag2.classList.add("courses__card__tag");
        tag2.innerHTML = fields['difficulty']
        tag3 = document.createElement("div");
        tag3.classList.add("courses__card__tag");
        tag3.innerHTML = fields['credit_type']
        tags.appendChild(tag);
        tags.appendChild(tag2);
        tags.appendChild(tag3);
        course.appendChild(tags);
        
        image = document.createElement("div"); 
        image.classList.add('courses__card__image');
        img = document.createElement("img"); 
        img.src = `/media/${fields['image']}`;
        img.alt = "Course image";
        image.appendChild(img);
        course.appendChild(image);

        title = document.createElement('div')
        title.classList.add('courses__card__title')
        title.innerHTML = fields['name']
        course.appendChild(title)

        description = document.createElement('div')
        description.classList.add('courses__card__description')
        description.innerHTML = fields['short_description']
        course.appendChild(description)

        more = document.createElement('div')
        more.classList.add('courses__card__more')
        more.innerHTML = "Подробнее"
        course.appendChild(more)
      
      
        document.querySelector('.courses__cards__wrapper').appendChild(course);
      }
    }
  } else {
    notFind = document.createElement("span");
    notFind.classList.add('notfindtext')
    notFind.innerHTML = "Нет подходящих курсов";
    document.querySelector('.courses__cards__wrapper').appendChild(notFind);
  }
  
}


$('#my-form').on('submit', function(event) {
  event.preventDefault();
  $.ajax({
    url: window.location.pathname,
    type: 'POST',
    data: $(this).serialize(),
    success: function(resp) {
      createCourse(resp);
    }
  });
});


