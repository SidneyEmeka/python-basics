#lists are mutable so we can add remove with indexes

nums = [1,3,2,8,9, 'yeah','can accept. multiple  types']
sizes = ['30','67','67']
all = [nums,sizes]
alls = nums + sizes

age, height,cash = sizes #must have enough vaalues to unpack => it must mmatch the qty
print(height)
sizes.reverse() #diffferent in builts
print(sizes)