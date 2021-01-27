from mdeditor.fields import MDTextFormField  # 追加


class ArticleForm(forms.Form):
    title = forms.CharField()
    content = MDTextFormField()  # 変更