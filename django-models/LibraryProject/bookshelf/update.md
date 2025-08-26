
## 3. update.md

```markdown
```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
# Output: Nineteen Eighty-Four
