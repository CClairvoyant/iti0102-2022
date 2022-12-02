calories = []
with open("data.txt", "r") as data:
    content = data.read()
content_list = content.split("\n\n")
content_list = list(map(lambda x: x.split("\n"), content_list))
for i in range(len(content_list)):
    content_list[i] = sum(list(map(int, content_list[i])))
print(max(content_list))
content_list.sort(reverse=True)
print(sum(content_list[:3]))
