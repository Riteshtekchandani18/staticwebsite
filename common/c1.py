class Article:
    author =""
    title=""
    content =""
    like=0

    def __str__(self) -> str:
        return self.title
    def summary (self) -> str:
        return self.content[:20]
    def name (self):
        return self.author
    def count (self):
        return self.like
    
a1 = Article()
a1.author ="john"
a1.title="python is awesome"
a1.content ="some content will be here soon"
a1.like=10

a2 = Article()
a2.author ="alex"
a2.title="java is good"
a2.content ="some content will be here soon"
a2.like=40


a3 = Article()
a3.author ="Lees"
a3.title="Html is good"
a3.content ="some content will be here soon"
a3.like=20

print("our articles are :")
print(a1)
print(a1.summary())
print(a1.name())
print(a1.count())
print(a2)
print(a2.summary())
print(a2.name())
print(a2.count())
print(a3)
print(a3.summary())
print(a3.name())
print(a3.count())