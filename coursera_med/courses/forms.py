from django import forms

from .models import language_choices, duration_choices, Course, Module, Lecture, UserCourse


# class CourseForm(forms.Form):
#     name = forms.CharField(max_length=200)
#     description = forms.Textarea()
#     image = forms.ImageField()
#     language = forms.CharField(widget=forms.Select(choices=language_choices))
#     duration = forms.CharField(widget=forms.Select(choices=duration_choices))
#     start_date = forms.DateTimeField()
#     finish_date = forms.DateTimeField()


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'short_description', 'image', 'language', 'duration', ]


class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['course', 'name', 'description', 'sequence_number', ]


class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['name', 'text', 'type', 'video', 'module', 'duration', ]


class UserCourseForm(forms.ModelForm):
    class Meta:
        model = UserCourse
        fields = ['course', 'user', 'status', ]





# class FilterSelect(forms.Select):
#     def __init__(self, *args, **kwargs):
#         self.src = kwargs.pop('src', {})
#         super().__init__(*args, **kwargs)

#     def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
#         options = super(FilterSelect, self).create_option(name, value, label, selected, index, subindex=None, attrs=None)
#         print('bebebe')
#         print(options)
#         for k, v in self.src.items():
#             options['attrs'][k] = v[options['value']]
#         return options


class CourseFilterForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['specialization', 'difficulty', 'credit_type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':"courses__form__select"})


        # src = kwargs.pop('src', {})
        # choices = kwargs.pop('choices', ())
        # super().__init__(*args, **kwargs)
        # print('bebebe')
        # FilterSelect(attrs={'class': 'courses__form__select'}, src=src, choices=choices)
        # self.fields['specialization'].widget = FilterSelect(attrs={'class': 'courses__form__select'}, src=src, choices=choices)


# class CourseFilterForm(forms.Form):
#     specialization_choice = [
#         ('cardiology', 'Кардиология'),
#         ('neurology', 'Неврология'),
#         ('orthopedics', 'Ортопедия'),
#     ]

#     difficulty_choice = [
#         ('beginner', 'Начальный'),
#         ('intermediate', 'Средний'),
#         ('advanced', 'Продвинутый'),
#     ]

#     credit_type_choice = [
#         ('cme', 'CME'),
#         ('ce', 'CE'),
#         ('other', 'Другое'),
#     ]
#     specialization = forms.ChoiceField(label="specialization", choices=(specialization_choice), widget=forms.Select(attrs={'class':'selector'}))