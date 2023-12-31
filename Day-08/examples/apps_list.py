# creating the list of apps using lists and tuples

apps_list = ["frontend", "catalogue", "cart", "shipping"]
print(apps_list)

# length of apps_list
print(len(apps_list))

# adding the new app to apps_list
apps_list.append("dispatch")
print(apps_list)

# inserting the value at particular position
apps_list.insert(2,"user")
print(apps_list)

# removing the app from app_list
apps_list.remove("frontend")
print(apps_list)

# removing the value at particular position
apps_list.pop(2)
print(apps_list)

# concatinating two list
new_apps_list = apps_list + ["payment", "delivered"]
print(new_apps_list)

# accesing the particular app by the index
print(apps_list[0])

# accesing the few apps by apps_list like 2 and 3
print(apps_list[1:3])

# sorting the list in ascending order
sorted_apps_list = apps_list.sort()
print(apps_list)

# sorting the list in descending order
revers_apps_list = apps_list.reverse()
print(apps_list)

# checking if the value is present in list
print("catalogue" in apps_list)
