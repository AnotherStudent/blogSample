from blog import Blogpost, Comment
from time import sleep

print('\n============================================================================')
blogpost = Blogpost('Bill Gates', 'Unix sux!', 'bla bla bla! \nWindows rulez_!')
print(blogpost)
print(blogpost.strComments())
sleep(1)

print('\n============================================================================')
blogpost.addComment(Comment('Linus Torvalds', 'You is stupid! Agrh!!'))
print(blogpost)
print(blogpost.strComments())
sleep(1)

print('\n============================================================================')
blogpost.addComment(Comment('Денис Попов', 'Зато в линуксе не скучные обои!'))
print(blogpost)
print(blogpost.strComments())
